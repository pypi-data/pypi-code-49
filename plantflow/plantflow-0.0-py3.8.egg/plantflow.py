import random
import simpy
from math import inf
import statistics
import time
import sys


class Tank(simpy.Container):
    """
    For storing liquid materials
    """
    def __init__(self, env, name, capacity=1e3, init=0, *args, **kwargs):
        super().__init__(env, init=init, capacity=capacity, *args, **kwargs)
        self.env = env
        self.name = name
        self.data = [(self._env.now, self.level)]
        
    def put(self, *args, **kwargs):
        self.data.append((self._env.now, self.level))
        return super().put(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        self.data.append((self._env.now, self.level))
        return super().get(*args, **kwargs)


class Truck(simpy.Resource):
    """
    For moving stuff around
    """
    def __init__(self, env, name, capacity=1e3, init=0, *args, **kwargs):
        super().__init__(env, init=init, capacity=capacity, *args, **kwargs)
        self.env = env
        self.name = name
        self.data = [(self._env.now, self.level)]
        
    def put(self, *args, **kwargs):
        self.data.append((self._env.now, self.level))
        return super().put(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        self.data.append((self._env.now, self.level))
        return super().get(*args, **kwargs)

    
class UnitOperation(object):
    """
    Represents single or multiple UnitOps as long as operations
    are meant for one consistent batch/flow item (batch item does
    not interact with other objects during operation)
    
    Parameters
    ---------------
    
    Returns
    ---------------
    """
    
    def __init__(self, env, name, operating_times, 
                 discharge_header=False, batch_size=1,
                 route_in=None, route_out=None, route_out_type='priority',
                 route_out_di=None, schedule=None, dump_blocked_discharge=True):
        self.env = env
        self.name = name
        self.process = env.process(self.main())
        self.batch_size = batch_size
        self.broken = False
        self.blocked = False
        self.batches_completed = 0
        self.waiting = 0
        self.backed_discharge = 0
        self.blocked_time = 0
        self.schedule = schedule
        self.dist_di = operating_times
        self.discharge_header = discharge_header
        self.route_out = route_out        
        self.route_in = route_in
        self.route_out_type = route_out_type
        self.route_out_di = route_out_di
        self.dump_blocked_discharge = dump_blocked_discharge
        self.data = []

        if self.discharge_header:
            self.operating_times = list(operating_times.keys())[:-1]
            self.discharge_times = list(operating_times.keys())[-1]
        else:
            self.operating_times = list(operating_times.keys())

    def main(self):   
        while True:      
            if self.schedule:
                scheduling = self.env.process(self.envoke_schedule(self.env))
                yield scheduling
            if self.route_in: # find available source material
                charging = self.env.process(self.charge(self.env))
                yield charging
            working = self.env.process(self.operate(self.env))
            yield working
            if self.route_out:
                discharging = self.env.process(self.discharge(self.env))
                yield discharging
            self.batches_completed += 1   
            
    def envoke_schedule(self, env):
        for i in range(0, max(self.schedule['Days Operating'].values())):
            if not i in self.schedule['Days Operating'].values():
                if env.now == i*24*60:
                    yield env.timeout(24*60)
            elif max(self.schedule['Days Operating'].values())*24*60 <= env.now:
                yield env.timeout(24*60)
                    
    def charge(self, env):
        while True:
            available_tanks = [i for i, x in enumerate([i.level >= self.batch_size 
                                                        for i in self.route_in]) if x]
            if available_tanks:
                yield self.route_in[available_tanks[random.randint(0,
                                    len(available_tanks)-1)]].get(self.batch_size)
                break
            else:     
                start_waiting = self.env.now
                yield self.env.timeout(10) # wait 10 mins
                self.waiting += self.env.now - start_waiting
                
    def operate(self, env):
        for step in self.operating_times: # parallel processes
            if type(self.dist_di[step]) != float:
                population = list(self.dist_di[step])
                k = 1
                time = random.sample(population,k)[0]        
            else: 
                time = abs(random.gauss(self.dist_di[step], .25*self.dist_di[step]))
            yield self.env.timeout(time)
            
    def discharge(self, env):   
        if self.discharge_header: # if discharge shares header
            discharge_request = self.discharge_header.request()
            start_waiting = self.env.now                
            population = list(self.dist_di[self.discharge_times])
            k = 1
            time = random.sample(population,k)[0]
            yield discharge_request
            self.waiting += self.env.now - start_waiting
            yield self.env.timeout(time)

        if self.route_out_type == 'percent':
            index = random.randint(0,pd.DataFrame(self.route_out_di).shape[0]-1)
            for i, x in enumerate(self.route_out_di):
                successful = False
                while not successful:
                    quantity = self.route_out_di[x][index] / 100
                    if quantity > 0:
                        matching_tanks = [self.route_out[a] for a, b in enumerate([x in k.name for k
                                                                                   in self.route_out]) if b]
                        available_tanks = [l for l, m in enumerate([l.capacity - 
                                                                    l.level >= self.batch_size 
                                                                    for l in matching_tanks]) if m]
                        if available_tanks:
                            self.blocked = False
                            yield matching_tanks[available_tanks[random.randint(0,
                                        len(available_tanks)-1)]].put(self.batch_size * quantity)
                            successful = True
                        else:
                            if self.dump_blocked_discharge:
                                self.blocked = True
                                self.backed_discharge += self.batch_size * quantity
                                self.monitor_blockage(self.env, x, self.batch_size * quantity)
                                self.blocked = False
                                successful = True
                            else:
                                #wait
                                self.blocked = True
                                start_waiting = self.env.now
                                yield self.env.timeout(10) # wait 10 mins
                                self.blocked_time += self.env.now - start_waiting
                                continue
                    else:
                        successful = True

        if self.route_out_type == 'priority':
            successful = False
            while not successful:
                available_tanks = [i for i, x in enumerate([i.capacity - 
                                                            i.level >= self.batch_size 
                                                            for i in self.route_out]) if x]
                if available_tanks:
                    self.blocked = False
                    yield self.route_out[available_tanks[random.randint(0,
                                        len(available_tanks)-1)]].put(self.batch_size)
                    successful = True
                else:
                    if self.dump_blocked_discharge:
                        self.blocked = True
                        self.backed_discharge += self.batch_size
                        self.monitor_blockage(self.env, x, self.batch_size)
                        self.blocked = False
                        successful = True
                    else:
                        #wait
                        self.blocked = True
                        start_waiting = self.env.now
                        yield self.env.timeout(10) # wait 10 mins
                        self.blocked_time += self.env.now - start_waiting
                        continue

        if self.discharge_header: # release discharge header
            self.discharge_header.release(discharge_request)

            
    def monitor_blockage(self, env, path, amt):
        """
        This is our monitoring callback
        """
        item = (
            self.name,
            path,
            self.env.now, # the current simulation time
            amt
            )
        self.data.append(item)

        
class Benchmark:
    """
    benchmark method used by the unittests
    """
    @staticmethod
    def run(function):
        timings = []
        stdout = sys.stdout
        for i in range(5):
            sys.stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            print("{} {:3.2f} {:3.2f}".format(
                1 + i, mean,
                statistics.stdev(timings, mean) if i > 1 else 0))
