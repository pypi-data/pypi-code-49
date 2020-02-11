import requests
import os
import json
import uuid
import time
from enum import Enum
from oauthlib.oauth2 import LegacyApplicationClient, InvalidGrantError
from requests_oauthlib import OAuth2Session
import atexit
import numbers
import pkg_resources
import outdated

from openlab import credentials, login, piController, logger
from openlab import results, setpoints

class http_client(object):
    sim = None
    max_results_attempts = 20
    max_init_attempts=100
    """
    A utility class for using the openLab RESTfull API
    """ 
    def __init__(self, proxies = {}, **kwargs):
        print("Initializing http client...")

        #create and validate the oauth client
        self.client= login.create_token(**kwargs) # returns an oauth session
        self.credentials = login.get_credentials(**kwargs) #FIXME
        self.url = self.credentials['url']

        # FIXME change to alive endpoint
        self.check_login_worked()
        self.version_check()
        
        # see if there there is another server url that the web client has decided would be better to use
        if 'EndpointUrl' in self.whoami().keys():
            self.url = self.whoami()['EndpointUrl']

        #TODO: Call to version endpoint

    def version_check(self):
        try:
            version = pkg_resources.get_distribution("openlab").version
            is_outdated, latest_version = outdated.check_outdated('openlab', version)
            if is_outdated:
                print("Your openlab version {} is outdated. Consider upgrading to {}".format(version, latest_version))
        except:
            # Don't want version check to crash/affect client
            print("Could not verify openlab is current")
            
        return

    def check_login_worked(self):
        #first, we check for invalid grant errors
        try:
            r=self.client.get(self.url+"/users/whoami") #random method to call web api, so that we can check the response code
            if r.status_code != 200:
                print("Call to whoami failed with HTTP Code: {}. Attempting to create new token".format(r.status_code))
                self.client = login.create_token()
            else:
                print("Login Succesfull")

        except InvalidGrantError:
            print("Invalid Grant Exception Thrown. Attempting to create new token")
            self.client = login.create_token()
        return 

    def get_custom_endpoint(self, endpoint_url):
        """Call a custom endpoint url.
        Current endpoint urls can be found at live.openlab.app/swagger"""
        r = self.client.get(self.url + endpoint_url)
        return r.json()

    def labels(self):
        r=self.client.get(self.url+"/labels/")
        return self.standard_response(r, 200) 

    def labels_by_id(self, config_id):
        r=self.client.get(self.url+"/configurations/" + str(config_id) + "/labels")
        return self.standard_response(r, 200)     

    @staticmethod
    def standard_response(response, success_status_code, success_msg=None):
        if response.status_code == success_status_code:
            if success_msg is not None:
                print(success_msg)

            return response.json()
        else:
            raise Exception("Error getting response from web_client:\n {} \n {}".format(response, response.text))
            
    def whoami(self):
        """
        Returns information about the current user
        """
        r=self.client.get(self.url+"/users/whoami")
        return self.standard_response(r, 200)

    def alive(self):
        """
        Pings the API and returns True if alive
        """
        r=self.client.get(self.url+"/alive")
        return True if r.status_code == 204 else False

    def version(self):
        """
        The API version
        """
        r=self.client.get(self.url+"/version")
        return self.standard_response(r, 200)

    def user_limits(self, **kwargs):
        """Returns the user limits"""
        query = dict()
        if 'licenseId' in kwargs.keys():
            query['licenseId'] = kwargs.get("licenseId")
            r = self.client.get(self.url + "/users/limits?", params = query)
        elif 'license_id' in self.credentials.keys():
            query['licenseId'] = self.credentials['license_id']
            r = self.client.get(self.url + "/users/limits?", params = query)
        else:
            print("No license given. Defaulting to personal license")
            r = self.client.get(self.url + "/users/limits")
        return self.standard_response(r,200)

    def simulations(self):
        """
        Returns all simulations of the current user
        """        
        r=self.client.get(self.url+"/simulations")
        return self.standard_response(r, 200)

    def check_if_simulation_exists(self,sim_id):
        simulations = self.simulations()
        sim_exists = False
        for simulation in simulations:
            if simulation['SimulationID'] == sim_id:
                sim_exists = True
        if not sim_exists:
            raise Exception("Simulation {} does not exist".format(sim_id))

    def set_setpoints(self, sim_id, step, setpoints, shouldComplete=False):
        """
        Sends setpoints to a given simulation
        """
        data= self.format_set_point_data(step, setpoints, shouldComplete)
        r=self.client.post(self.url+"/simulations/"+sim_id+"/setpoints", json= data)
        if r.status_code == 404:
            self.check_if_simulation_exists(sim_id)

        return self.standard_response(r, 200)
    
    def all_setpoints(self,sim_id):
        """
        Returns all the set points of a simulation
        """
        #timestep = self.last_timestep(sim_id)
        r=self.client.get(self.url+"/simulations/"+ sim_id+ "/setpoints")
        
        if r.status_code == 404:
            self.check_if_simulation_exists(sim_id)
        
        return self.standard_response(r, 200)

    def last_setpoint(self, sim_id):
        """
        Returns the last set points of a simulation
        """
        #timestep = self.last_timestep(sim_id)
        r=self.client.get(self.url+"/simulations/"+ sim_id+ "/setpoints/last")

        if r.status_code == 404:
            self.check_if_simulation_exists(sim_id)
        
        return self.standard_response(r, 200)

    def last_timestep(self, sim_id):
        """
        Returns the last timestep of a simulation
        """
        r=self.client.get(self.url+"/simulations/"+ sim_id+ "/timestep")

        if r.status_code == 404:
            self.check_if_simulation_exists(sim_id)

        return self.standard_response(r, 200)
    
    def get_simulation_status(self,sim_id):
        r = self.client.get(self.url+"/simulations/"+sim_id+"/status")

        if r.status_code == 404:
            self.check_if_simulation_exists(sim_id)

        return self.standard_response(r, 200)

    def get_simulation_results(self, sim_id, from_step, to_step, filter_depth, tags: list, validate_tags= True):
        """
        Gets the simuation results of a given simulation for a given time interval.
        Setting filter_depth = True filers out the depth based results profiles for all but the last setpoints
        Returns a dictonary of dictonaries e.g. results[timeStep]["tag"]
        """
        query=dict()
        query["timestepfrom"]= str(from_step)
        if to_step is not from_step:
            query["timestepto"]=str(to_step)
        for tag in tags:
            if validate_tags and tag not in results.valid_results:
                raise Exception("""
                '{}' is not a valid OpenLab result tag. Check spelling and capitilization.
                If you think this is a mistake, pass in validate=False to the get_simulation_results method""".format(tag))
            query[tag]="true"
        query["filterDepth"]=str(filter_depth)
        
        r=self.client.get(self.url+"/simulations/"+ str(sim_id)+ "/results?", params= query)
        res = r.json()

        #convert the json to a dictionary of the requested results tags
        result=dict()
        result = self.collect_timebased_results(None, res, tags) # Timestep is deprecated and not used
        return result

    def configurations(self):
        """
        Returns all configurations of the current user
        """
        r=self.client.get(self.url+"/configurations") #r is of class response
        return self.standard_response(r, 200)

    def create_configuration(self, name, data):
        """
        Creates a configuration with the given data and name
        To see example of data structure format, see the configuration_data() method
        """
        config_id= str(uuid.uuid4())
        body = {'ConfigurationID':config_id, 'Data':data, 'Name':name}
        r=self.client.post(self.url+"/configurations", json = body)
        return self.standard_response(r, 201)

    def update_configuration(self, name, data):
        """
        Updates a configuration with the given data and name
        To see example of data structure format, see the configuration_data() method
        """
        config_id=self.configuration_id(name)
        body={'Data':data, 'Name':name}
        r=self.client.put(self.url+"/configurations/"+config_id, json=body)
        return self.standard_response(r, 200)
    
    def check_if_configuration_id_exists(self,config_id):
        configurations = self.configurations()
        config_exists = False
        for configuration in configurations:
            if configuration['ConfigurationID'] == config_id:
                config_exists = True
        if not config_exists:
            raise Exception("Configuration {} does not exist".format(config_id))

    def check_if_configuration_name_exists(self,config_name):
        configurations = self.configurations()
        config_exists = False
        for configuration in configurations:
            if configuration['Name'] == config_name:
                config_exists = True
        if not config_exists:
            raise Exception("Configuration {} does not exist".format(config_name))

    def configuration_info(self, config_id):
        """
        Returns all configuration info and data of the given configuration
        """
        r=self.client.get(self.url+"/configurations/"+ config_id)

        if r.status_code == 404:
            self.check_if_configuration_id_exists(config_id)

        return self.standard_response(r, 200)

    def configuration_id(self, name):
        """
        Returns configuration id with a given name
        """
        r=self.client.get(self.url+"/configurations/"+ name)

        if r.status_code == 404:
            self.check_if_configuration_name_exists(name)

        return self.standard_response(r, 200)

    def configuration_data(self, config_id):
        """Returns a dictionary of configuration data such as Trajectory, Architecture, Fluids etc..."""
        config = self.configuration_info(config_id)
        return config['Data']

    def configuration_simulations(self, config_id):
        """
        Returns all the simulations for a given configuration ID
        """
        r = self.client.get(self.url+"/configurations/"+str(config_id)+"/simulations")

        if r.status_code == 404:
            self.check_if_configuration_id_exists(config_id)

        return self.standard_response(r, 200)

    def delete_simulation(self, simulationID):
        """
        Deletes a given simulation
        Prompt will be given to confirm
        """
        answer = input("Are you sure you want to delete Simulation {}\t(y/n)".format(simulationID))
        if answer == "y":
            self.client.delete(self.url+"/simulations/"+simulationID)
            print("Simulation {} was deleted".format(simulationID))
        else:
            return

    def simulation_by_id(self, sim_id):
        """
        Returns simulation with a given id
        **Note you must use the id, not the name, as multiple simulations can have the same name
        """
        if type(sim_id) is not str:
            return print("Error. Sim-id must be a string")

        r=self.client.get(self.url+"/simulations/"+ sim_id)

        if r.status_code == 404:
            self.check_if_simulation_exists(sim_id)
            
        return self.standard_response(r, 200)
    
    def create_simulation(self, config_name, sim_name, initial_bit_depth, **kwargs):
        """
        Creates a simulation
        **kwargs influx_type and TimeStep
        Run by calling step() method
        Returns a Simulation Class
        """
        kwargs.setdefault('influx_type', {})
        kwargs.setdefault('TimeStep', 1)
        
        influx_type = kwargs.get('influx_type')
        if not isinstance(influx_type, dict):
            raise TypeError("influx_type has be a dictionary")

        #create a sim_id
        sim_id= str(uuid.uuid4())
        config_id = self.configuration_id(config_name)
        
        #check initial bit depth is valid
        max_depth = self.max_configuration_depth(config_id)
        if initial_bit_depth > max_depth:
            raise Exception("Initial bit depth of {} can not be greater than configurations maximum openhole depth of {}".format(
                initial_bit_depth,max_depth))

        #check if max simulation capacity already reached
        user_limits = self.user_limits(**kwargs)

        license_id = self.credentials['license_id']
        if license_id is not None:
            kwargs['license_id'] = license_id

        print("User limits: {}".format(user_limits))
        if type(user_limits) is dict and "MaxConcurrentSimulations" in user_limits.keys():
            simulation_capacity = user_limits['MaxConcurrentSimulations']
            active_simulations = set()
            simulations = self.simulations()
            for sim in simulations:
                status = sim['Status']
                if status == "Running" or status == "Created":
                    active_simulations.add(sim['SimulationID'])
            if len(active_simulations) >= simulation_capacity:
                raise Exception(
                    """Max conccurent simulation capacity of {} reached.\n
                    Please stop/complete one of the running simulations to continue: \n
                    {} \n
                    Or visit https://openlab.app to upgrade your account and get more conccurent simulation capacity.
                    """.format(simulation_capacity, active_simulations))

        # format the data to send web_client
        simulation= self.format_simulation_meta_data(self, sim_id, config_id, sim_name,initial_bit_depth, **kwargs)
        #print("simulation: ", simulation)
        r=self.client.post(self.url+"/simulations", json = simulation)
        self.standard_response(r, 200)

        # get the simulation id that the web_client created
        simulation_id = r.json()["SimulationID"]
        
        for x in range(self.max_init_attempts):
             r=self.client.get(self.url+"/simulations/"+str(simulation_id)+"/status")          
             if r.json()["Status"] == "Running":
                 print("Simulation Initialized")
                 #create a simulation class and return it to the caller
                 return Simulation(config_id, simulation_id, self)
             else: 
                 time.sleep(0.2)
                 x = x + 1        
        raise Exception("Failed to start simulation " + sim_name + "\nMax attempts reached") 

    def simulation_timestep(self, sim_id):
        r = self.client.get(self.url+"/simulations/"+sim_id+"/timestep")
        
        if r.status_code == 404:
            self.check_if_simulation_exists(sim_id)

        return self.standard_response(r, 200)

    def max_configuration_depth(self,config_id):
        """
        Returns the maximum openhole depth of a configuration in meters
        """
        depth = self.configuration_info(config_id)['Data']['Architecture']['OpenHole']['DepthInterval']['MaxX']
        return depth
          
    def end_simulation(self, sim_id, timeStep = None):
        body = [] # json must be list?
        setpoints = {}
        # Don't break old scripts that don't pass in step
        if timeStep is None:
            timeStep = self.simulation_timestep(sim_id) + 1
            setpoints['Timestep'] = timeStep
        elif timeStep > 0:
            setpoints['Timestep'] = timeStep
            setpoints['Data'] = {} # blank setpoints
            setpoints['ShouldComplete'] = True
        else:
            setpoints['Timestep'] = 0

        setpoints['ShouldComplete'] = True

        body.append(setpoints)

        success_msg = "{} was completed".format(sim_id)

        r=self.client.post(self.url+"/simulations/"+sim_id+"/setpoints", json= body)
        return self.standard_response(r, 200, success_msg)

    @staticmethod
    def format_configuration_meta_data(id,name,description,data):
        return { 'ConfigurationID': id, 'Data': data, 'Description': description, 'Name': name}

    @staticmethod
    def format_simulation_meta_data(self, sim_id, config_id, name, initial_bit_depth, **kwargs):
        kwargs.setdefault('influx_type', {})
        kwargs.setdefault('TimeStep',1)
        
        simulation_model = {}

        ## TODO Add check for key in kwargs.keys(): check if valid kwarg
        model_configuration = {}

        influx_type = kwargs.get('influx_type')
        step_duration = kwargs.get('TimeStep')

        if 'licenseId' in kwargs.keys():
            simulation_model['licenseId'] = kwargs.get("licenseId")
        elif 'license_id' in self.credentials.keys():
            simulation_model['licenseId'] = self.credentials['license_id']
        
        print("influx_type: ", influx_type)
        # do some influx type validations if it was passed in
        if influx_type != {}:
            if "Id" not in influx_type.keys():
                raise Exception("Influx Id key was not entered")

            #check if influx id is one of the client's supported influx types
            if influx_type['Id'] in influx_types:
                print("{} mode selected".format(influx_type['Id']))
                for k in influx_type.keys():
                    #append model configuration with influx dict
                    model_configuration[k] = influx_type[k]
            else:
                raise Exception("Invalid influx type '{}' entered. Available influx types are {}".format(
                    influx_type['Id'],influx_types))
        else:
            print("No influx mode selected. Defaulting to 'no influx and loss'")
            model_configuration['Id'] = "NoInfluxLoss"
            model_configuration['ManualReservoirMode'] = False
            model_configuration['UseReservoirModel'] = False

        if step_duration > 1:
            raise Exception("Step Duration must less than or equal to 1")
        elif step_duration <= 0:
            raise Exception("Step Duration must be greater than 0")
        elif step_duration != 1:
            print("Using Transient Mechanical Model with time step: ", step_duration)
            model_configuration['UseTransientMechanicalModel'] = True
            model_configuration['StepDuration'] = step_duration
        else:
            print("Using non-transient model")

        #print("Model Configuration: ", model_configuration)
        simulation_model['Name'] = name
        simulation_model['SimulationID'] = sim_id
        simulation_model['ConfigurationID'] = config_id
        simulation_model['Status'] =  "Created"
        simulation_model['InitialValues'] = {"BitDepth":initial_bit_depth}
        simulation_model['ModelConfiguration'] = model_configuration


        return  simulation_model

    @staticmethod
    def collect_timebased_results(timestep, data, tags: list):
        """
        Collects the given tags from the result set
        Timestep is deprecated and not used
        """
        result= { tag: dict() for tag in tags }
        for v in data:
            tag, step, value = v['t'], v['s'], v['v']
            
            if isinstance(value[0]['d'], numbers.Number):
                # Depth based
                result[tag][step] = value #dump all the depths/value pairs into the result
            else:
                # Time based
                result[tag][step] = value[0]['v'] #drop the NaN depth
        return result

    @staticmethod
    def format_set_point_data(timestep, setpoints: dict, shouldComplete = False):
        return [{"TimeStep":timestep, "Data": setpoints, "ShouldComplete":shouldComplete}]

influx_types = ["ManualInflux", "ManualLoss", "GeoPressureGradient"]

default_manual_influx = {"ComplexReservoirKickOffTime": 30,
            "Id" : "ManualInflux",
            "ManualInfluxLossMd": 2500,
            "ManualInfluxLossMassRate" : 0.83333333,
            "ManualInfluxLossTotalMass": 100,
            "ManualReservoirMode" : True,
            "UseReservoirModel" : True}

default_manual_loss = {"ComplexReservoirKickOffTime": 30,
            "Id" : "ManualLoss",
            "ManualInfluxLossMd": 2500,
            "ManualInfluxLossMassRate" : -1.66666667,
            "ManualInfluxLossTotalMass": 1000,
            "ManualReservoirMode" : True,
            "UseReservoirModel" : True}
            
# technically not default because there are no variable inputs, but want to keep it consistent with the other names
default_geopressure_gradient = {"Id": "GeoPressureGradient", 
            "ManualReservoirMode" : False,
            "UseReservoirModel": True}

#simulation iterable class
class IterSimulation(type):
    def __iter__(cls):
        return iter(cls._registry)

class Simulation(http_client,metaclass=IterSimulation):
    """
    A Simulation class for the OpenLab http_client
    """
    #Things needed to make the simulations iterable
    __metaclass__ = IterSimulation
    _registry = []

    client = None

    def  __init__(self, config_id, sim_id, client):
        self.config_id = config_id
        self.http_client = client
        self.sim_id = sim_id
        self.setpoints = setpoints.Setpoints()
        self.results = results.Results()
        try:
            self.max_timeStep = client.user_limits()['MaxTimeStep']
        except: self.max_timeStep = None

        self.end_simulation_on_exiting = True
        self.has_been_stopped = False
        self.filter_depth_based_results = True #setting true will only get the depth based results for the most recent setpoint
        self.ModelConfiguration = {}
        self._registry.append(self) #add the simulation to the iterable registry 
        self.connecting_previously = False
        self.currently_connecting = False
        self.timeStep = 0
    
    def __iter__(self):
        return iter(self)

    def get_conf_id(self):
        """
        Returns the configuration id of the simulation instance
        """
        return self.config_id

    def get_sim_id(self):
        """
        Returns the simulation id for the simulation instance
        """
        return self.sim_id

    def whoamiFromSimulation(self):
        return self
    
    def get_status(self):
        """
        Returns the status of the simulation instance 
        """
        return http_client.get_simulation_status(self.http_client,self.sim_id)['Status']

    def last_setpoints(self):
        """
        Returns the last setpoints for the simulation instance
        """
        return http_client.last_setpoint(self.http_client, self.sim_id)

    def current_step(self):
        """
        Returns the current step for the simulation instance
        """
        return http_client.simulation_timestep(self.http_client, self.sim_id)
    
    def current_setpoints(self):
        """
        Returns the simulations instances current setpoints that will be sent to web client when the step method is called
        """
        #empty dictionary for setpoints
        toSet = dict()
        #toSet["TimeStep"] = self.timeStep
        if self.setpoints.ChokeOpening is not None:
            toSet["ChokeOpening"] = self.setpoints.ChokeOpening
        if self.setpoints.TopOfStringVelocity is not None:
            toSet["TopOfStringVelocity"] = self.setpoints.TopOfStringVelocity
        if self.setpoints.FlowRateIn is not None:
            toSet["FlowRateIn"] = self.setpoints.FlowRateIn
        if self.setpoints.SurfaceRPM is not None:
            toSet["SurfaceRPM"] = self.setpoints.SurfaceRPM
        if self.setpoints.ChokePumpFlowRateIn is not None:
            toSet["ChokePumpFlowRateIn"] = self.setpoints.ChokePumpFlowRateIn
        if self.setpoints.DesiredROP is not None:
            toSet["DesiredROP"] = self.setpoints.DesiredROP
        if self.setpoints.BOPChokeOpening is not None:
            toSet["BopChokeOpening"] = self.setpoints.BOPChokeOpening
        if self.setpoints.MainPitActive is not None:
            toSet["MainPitActive"] = self.setpoints.MainPitActive
        if self.setpoints.MainPitReturn is not None:
            toSet["MainPitReturn"] = self.setpoints.MainPitReturn
        if self.setpoints.ControlActivePit is not None:
            toSet["ControlActivePit"] = self.setpoints.ControlActivePit
        if self.setpoints.ControlActivePitDensity is not None:
            toSet["ControlActivePitDensity"] = self.setpoints.ControlActivePitDensity
        if self.setpoints.ControlActivePitTemperature is not None:
            toSet["ControlActivePitTemperature"] = self.setpoints.ControlActivePitTemperature
        return toSet

    def auto_step(self,steps: int, tags = None):
        start_step = self.current_step() + 1
        end_step = start_step + steps
        for i in range(start_step, end_step):
            self.step(i)
            if tags is not None:
                self.get_results(i, tags)

    def step(self,timeStep):
        """
        Steps the simulation one step forward
        """ 
        # verify the time step is correct
        if timeStep != self.timeStep + 1:
            raise Exception(f"Trying to set a set a setpoint ({timeStep}) not at the immediate next timestep ({self.timeStep+1}).")
            
        if timeStep == self.max_timeStep:
            print("Max simulation time of {} steps reached. Vist https://openlab.app to upgrade your account and get more time".format(self.max_timeStep))
            self.stop()

        #get the client to post the setpoints to the web_client
        http_client.set_setpoints(self.http_client,self.sim_id, timeStep, self.current_setpoints(), False)

        # Get results to ensure it was taken (Connection gets automatically requested)
        res = self.get_results(timeStep, [])
        try:
            actual_ts = list(res['Connection'].keys())[-1] # A result looks like => {'tag': {ts : value}}

            if timeStep != actual_ts:
                raise Exception(f"Timesteps don't match. Requested => {timeStep} | Returned => {actual_ts}")

        except TypeError:
            print(f"Failed getting results at {timeStep}. Timesteps may not match anymore")

        self.timeStep = timeStep
        
                
    def get_results(self,timeStep,tags: list):
        """
        Gets the results for the given timestep
        Pass in openlab.results.all_results() for all available results
        """
        res = None
        if timeStep >= 1:
            if "Connection" not in tags:
                tags.append("Connection")
        

            attempts = 0
            #loop until we get data or reach the max amount of attempts
            while(True):
                #get the http_client to request simulation results
                res = http_client.get_simulation_results(self.http_client, self.sim_id,timeStep, timeStep, self.filter_depth_based_results, tags)

                if res.get("Connection"):
                    #break out of while loop once there are results
                    break

                elif attempts >= self.max_results_attempts:
                    # Increase wait time. Something is taking a long time
                    time.sleep(1)
                
                else:
                    attempts = attempts + 1
                    
                    if attempts == self.max_results_attempts:
                        print("Something is taking a long time...")

                    time.sleep(0.02)
            
            try:
                connection = res.get("Connection")
                if connection:
                    if connection.get(timeStep) == 1:
                        #check if it just started connecting
                        if self.connecting_previously == False:
                            print("Connecting new pipe")
                        
                        self.connecting_previously = True
                        self.currently_connecting = True

                    elif self.currently_connecting == True:
                        #this will only trigger when res[timeStep]['Connection'] == 0 and flag hasn't been reset
                        print("Done Connecting Pipe")
                        self.currently_connecting = False

                ##assign each result from the client to its respected result dictionary in simulation class
                for tag in tags:
                    if tag in res.keys():
                        try:
                            getattr(self.results, tag)[timeStep] = res[tag][timeStep]
                        except TypeError:
                            print("Type Error. Time step: {}; Tag: {}".format(timeStep, tag))
                        except AttributeError:
                            print("Tag '{}' is not a recognized OpenLab result tag".format(tag))

            except AttributeError:
                print(f"Attribute Error. Results were not properly assigned for timestep {timeStep}")

        return res
    
    def stop(self):
        """
        Complete the simulation instance
        """
        print("Ending simulation {}".format(self.sim_id))
        next_timestep = self.current_step() + 1
        http_client.end_simulation(self.http_client, self.sim_id, next_timestep)
        self.has_been_stopped = True

    @property
    def end_simulation_on_exiting(self):
        return self._end_simulation_on_exiting
    @end_simulation_on_exiting.setter
    def end_simulation_on_exiting(self, value):
        self._end_simulation_on_exiting = value

def stop_running_simulations():
    """
    Exit code that ends all running simulations
    """
    number_of_sims = len(Simulation._registry)
    if number_of_sims > 0:
        print("Exiting Code...")
        print("{} simulations were created".format(number_of_sims))
        try:
            #loop through all the client simulations
            for simulation in Simulation:
                status = simulation.get_status()
                sim_id = simulation.sim_id

                #stop the simulation if it is running, initializing, or created
                active = status == "Running" or status == "Initializing" or status == "Created"
                already_ended = simulation.has_been_stopped
                
                if active and not already_ended:
                    print("Simulation {} is still {}".format(sim_id, status))
                    if simulation.end_simulation_on_exiting == True:
                        simulation.stop()
                    else:
                        print("Sim {} was not ended because end_simulation_on_exiting was set to false".format(sim_id))
        except:
            raise Exception("Could not iterate simulations")

#register the functions to run at exit
atexit.register(stop_running_simulations)
