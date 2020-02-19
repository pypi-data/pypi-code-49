
import json
import time
import glob
import numpy as np
import matplotlib.pyplot as plt
import os
import time

from pathlib import Path
#print()


def rand_str(n=16):
    return ''.join(list(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'),size=n)))

def get_json_file():
    return get_time_str()+'.json'

def get_msg_file():
    return get_time_str()+'.log'

def get_time_str():
    tm = time.localtime()
    return '{:4}-{:02}-{:02}-{:02}-{:02}-{:02}'.format(tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min,tm.tm_sec)

def get_time_str2():
    tm = time.localtime()
    return '{:4}-{:02}-{:02} {:02}:{:02}:{:02}'.format(tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min,tm.tm_sec)


def get_time_from_str(time_str):
    t = [int(s) for s in time_str.split('-')]
    return (t[0]-2000)*365*24*60*60+t[1]*30*24*60*60+t[2]*24*60*60+t[3]*60*60+t[4]*60+t[5]

def plot_stat(stat,with_loss=True):
    plt.plot(stat[:,0].astype('int32'),stat[:,1])
    plt.plot(stat[:,0].astype('int32'),stat[:,2])
    if with_loss:
        plt.plot(stat[:,0].astype('int32'),stat[:,3])
        plt.plot(stat[:,0].astype('int32'),stat[:,4])

class PerfLogger():
    def __init__(self, prefix = None):
        if prefix is None:
            self.prefix = rand_str(8)
        else:
            self.prefix = prefix
        
        #self.get_logger_name()
            
        self.root = os.path.join(Path.home(),'.perf_logger/')
        
        self.log_path = os.path.join(self.root,self.prefix)
        if os.path.exists(self.log_path):
            self.history_files = glob.glob(self.log_path+'/*.json')
            self.history_msg_files = glob.glob(self.log_path+'/*.log')
            print('log history exists in '+self.log_path)
            
        else:            
            os.makedirs(self.log_path,exist_ok=True)
        
        
        self.current_log_file = os.path.join(self.log_path,get_json_file())
        self.msg_file = os.path.join(self.log_path,get_msg_file())      
        
        self.current_pf_js = []
    def log(self,epoch, train_acc, val_acc,train_loss=0,val_loss=0):
        js = [{'train_acc':train_acc,'val_acc':val_acc,'train_loss':train_loss,'val_loss':val_loss,'epoch':epoch}]
        self.current_pf_js += js
        with open(self.current_log_file,'wt') as fp:
            json.dump(self.current_pf_js,fp)      
    def log_str(self,msg):
        header = get_time_str2()        
        try:
            with open(self.msg_file,'at') as fp:
                fp.write(header+'\t'+msg+'\n')
        except:
            raise(Exception('error in writing msg to log file '+self.msg_file))
            
        
        
    
        
    def get_history_log(self):
        js = []
        names = []
        for f in self.history_files:
            with open(f,'rt') as fp:
                js.append(json.load(fp))
            names.append(f.split('/')[-1][:-5])
        return js,names
        
    def show_history_log(self,with_loss=True):
        all_js,names = self.get_history_log()
        leg = []
        if with_loss:
            leg0 = ['train_acc','val_acc','train_loss','val_loss']
        else:
            leg0 = ['train_acc','val_acc']
        for name,js in zip(names,all_js):
            stat = np.array([(d['epoch'],d['train_acc'],d['val_acc'],d['train_loss'],d['val_loss']) \
                             for d in js])
            plot_stat(stat,with_loss)            
            leg += [name+':'+l for l in leg0 ]            
            plt.legend(leg)
        print(leg)
        plt.show()
        
    def list_all_files(self,):
        print('index\tmsg-files')
        print('-'*16)
        for i, f in enumerate(self.history_msg_files):
            print(i,'\t',f)
        print('\n\n')
        print('index\tlog-files')
        print('-'*16)
        
        
        for i, f in enumerate(self.history_files):
            print(i,'\t',f)
        
            
    
    def get_last_log(self):
        last_t = 0   
        last_f = None
        for f in self.history_files:
            name = f.split('/')[-1][:-5]
            t = get_time_from_str(name)
            if t > last_t:
                last_t =t
                last_f = f
        if last_f is None:
            return None
        with open(last_f,'rt') as fp:
            js = json.load(fp)
        return js
           
    def show_last_log(self,with_loss=True):
        js = self.get_last_log()
        if js is None:
            print('no last log existed')
            return 
        stat = np.array([(d['epoch'],d['train_acc'],d['val_acc'],d['train_loss'],d['val_loss']) \
                         for d in js])
        plot_stat(stat,with_loss = with_loss)
        
        plt.legend(['train_acc','val_acc','train_loss','val_loss'])
            
    
    def get_last_log(self):
        last_t = 0   
        last_f = None
        for f in self.history_files:
            name = f.split('/')[-1][:-5]
            t = get_time_from_str(name)
            if t > last_t:
                last_t =t
                last_f = f
        if last_f is None:
            return None
        with open(last_f,'rt') as fp:
            js = json.load(fp)
        return js
           
    def show_last_log(self,with_loss):
        js = self.get_last_log()
        if js is None:
            print('no last log existed')
            return 
        stat = np.array([(d['epoch'],d['train_acc'],d['val_acc'],d['train_loss'],d['val_loss']) \
                         for d in js])
        plot_stat(stat,with_loss)

        plt.legend(['train_acc','val_acc','train_loss','val_loss'])      
        
    def compare_last_log(self,with_loss=True):
        js = self.get_last_log()
        if js is None:
            print('no last log existed')
            return 
        stat = np.array([(d['epoch'],d['train_acc'],d['val_acc'],d['train_loss'],d['val_loss']) \
                         for d in js])
        plt.figure()
        plot_stat(stat,with_loss)
        
        leg = ['last:train_acc','last:val_acc','last:train_loss','last:val_loss']
        if not with_loss:
            leg = leg[:-2]
        
        js = self.current_pf_js
        
        stat = np.array([(d['epoch'],d['train_acc'],d['val_acc'],d['train_loss'],d['val_loss']) \
                         for d in js])
        
        plot_stat(stat,with_loss)
        leg += ['curr:train_acc','curr:val_acc','curr:train_loss','curr:val_loss']
        if not with_loss:
            leg = leg[:-2]
        plt.legend(leg)  
        
        plt.show()
    def compare_log(self,log_idx,with_loss=True):
        try:
            log_file = self.history_files[log_idx]
            with open(log_file,'rt') as fp:
                js = json.load(fp)
        except:
            raise(Exception('error in loading log file with index:{}'.format(log_idx)))
     
        stat = np.array([(d['epoch'],d['train_acc'],d['val_acc'],d['train_loss'],d['val_loss']) \
                         for d in js])
        plt.figure()
        plot_stat(stat,with_loss)
        
        leg = ['last:train_acc','last:val_acc','last:train_loss','last:val_loss']
        if not with_loss:
            leg = leg[:-2]
        
        js = self.current_pf_js
        if len(js)!=0:
           
            stat = np.array([(d['epoch'],d['train_acc'],d['val_acc'],d['train_loss'],d['val_loss']) \
                             for d in js])
            plot_stat(stat,with_loss)
            leg += ['curr:train_acc','curr:val_acc','curr:train_loss','curr:val_loss']
            if not with_loss:
                leg = leg[:-2]
        plt.legend(leg)  
        
        plt.show()
        
  
        
        
    def show_current_log(self,with_loss=True):
        js = self.current_pf_js        
        stat = np.array([(d['epoch'],d['train_acc'],d['val_acc'],d['train_loss'],d['val_loss']) \
                         for d in js])        
        plot_stat(stat,with_loss)
        leg = ['curr:train_acc','curr:val_acc','curr:train_loss','curr:val_loss']    
        if not with_loss:
            leg = leg[:2]
        plt.legend(leg)      
        plt.show()
        
#logger = PerfLogger(prefix='vox1_speaker_with_noise_enhan')    
#logger.compare_log(2,with_loss=False)
