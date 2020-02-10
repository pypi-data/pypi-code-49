import os
from os.path import exists
import logging
from intervaltree import intervaltree
logger = logging.getLogger(__file__)

# Define a Data Object


class Data:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '<'+self.name+'> '+str(self.__dict__)


# Arg Max in a Dic
def argmaxdic(dic):
    mx = {'v': 0, 'i': 0}
    for d in dic:
        tmp = dic[d]
        if(mx['v'] < tmp):
            mx['v'] = tmp
            mx['i'] = d
    return mx['i']


class MyTask:
    params={}
    def applyParams(self, params):
        self.params = params
        for p in params:
            self.__dict__[p]=params[p]
        return True

    def reset(self):
        pass

    def __str__(self):
        return '<'+self.__class__.__name__+'> '+str(self.__dict__)

    def shortname(self):
        return self.__class__.__name__

    def save(self, file):
        import pickle
        file = file+'.pkl'
        with open(file, 'wb') as f:
            pickle.dump([self], f)

    def load(self, file):
        pass

# Defining Interval Tree from Activities.


def makeIntervalTree(acts):
    tree = IntervalTree()

    for act in acts:
        start = act['StartTime'].value
        end = act['EndTime'].value
        if(start == end):
            start = start-1
        tree[start:end] = act
    return tree


def makeNonOverlapIntervalTree(acts):
    tree = makeIntervalTree(acts)
    tree.split_overlaps()
    tree.merge_equals(data_reducer=lambda x, y: y)
    return tree

# Find overlap between 2 event in Minutes


def findOverlap(a, b):
    return ((min(a['EndTime'], b['EndTime'])-max(a['StartTime'], b['StartTime'])).value)/pd.to_timedelta('60s').value


# Buffer data type for stacking stream
class Buffer:
    def __init__(self, input, minsize, maxsize):
        self.data = input
        self.times = input.time.values
        self.datavalues = input.values
        self.minsize = minsize
        self.maxsize = maxsize
        self.start_index = 0

    def removeTop(self, idx):
        self.start_index = idx

    def getEventsInRange(self, starttime, endtime):
        sindex = self.searchTime(starttime, -1)
        eindex = self.searchTime(endtime, +1)
        if(sindex is None):
            return None
        if(eindex is None):
            return None
        return self.data.iloc[sindex:eindex+1]

    def searchTime(self, time, operator=0):
        times = self.times
        n = len(times)
        L = self.start_index
        R = n

        if operator == 1:
            while L < R:
                m = int((L + R) / 2)

                if times[m] <= time:
                    L = m + 1
                else:
                    R = m
            return L-1 if L > self.start_index else None
        else:
            while L < R:
                m = int((L + R) / 2)

                if times[m] < time:
                    L = m + 1
                else:
                    R = m
            return L if L < n else None


print('Utils loaded successfully!!')


def instantiate(method):
    m = method['method']()
    m.applyParams(method['params'])


def saveState(vars, file):
    import pickle

    file = 'save_data/'+file+'/'
    if not (os.path.exists(file)):
        os.makedirs(file)
    with open(file+'data.pkl', 'wb') as f:
        pickle.dump(vars, f)


def loadState(file):
    import pickle
    file = 'save_data/'+file+'/'
    with open(file+'data.pkl', 'rb') as f:
        return pickle.load(f)


def saveFunctions(func, file):
    file = 'save_data/'+file+'/'
    if not (os.path.exists(file)):
        os.makedirs(file)
    for k in func.__dict__:
        obj = func.__dict__[k]

        if isinstance(obj, MyTask):
            tmpfunc = obj.func
            obj.func = ''
            obj.save(file+'_'+k+'_'+type(obj).__module__+'_')
            obj.func = tmpfunc


def loadall(file):
    import pickle
    data = loadState(file)
    file = 'save_data/'+file+'/'
    func = Data('Saved Functions')
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(file) if isfile(join(file, f))]
    for f in onlyfiles:
        x = f.split('_')
        if('data.pkl'in f):
            continue

        if('.pkl' in f):
            with open(file+f, 'rb') as fl:
                func.__dict__[x[1]] = pickle.load(fl)
        elif('pyact.h5' in f):
            from classifier.PyActLearnClassifier import PAL_NN
            classifier = PAL_NN()
            classifier.load(file+f)
            func.__dict__[x[1]] = classifier
        elif('.h5' in f):
            from classifier.KerasClassifier import KerasClassifier
            classifier = KerasClassifier()
            classifier.load(file+f)
            func.__dict__[x[1]] = classifier
        else:
            logger.error('unsupported'+f)

    return [data, func]


def configurelogger(file, dir):
    from datetime import datetime
    # Default parameters
    log_filename = os.path.basename(__file__).split('.')[0] + \
        '-%s.log' % datetime.now().strftime('%y%m%d_%H-%M-%S')
    # Setup output directory
    output_dir = dir
    if output_dir is not None:
        output_dir = os.path.abspath(os.path.expanduser(output_dir))
        if os.path.exists(output_dir):
            # Found output_dir, check if it is a directory
            if not os.path.isdir(output_dir):
                exit(
                    'Output directory %s is found, but not a directory. Abort.' % output_dir)
        else:
            # Create directory
            os.makedirs(output_dir)
    else:
        output_dir = '.'
    log_filename = os.path.join(output_dir, log_filename)
    # Setup Logging as early as possible
    import sys
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] %(name)s:%(levelname)s:%(message)s',
                        handlers=[logging.FileHandler(log_filename),
                                  logging.StreamHandler(sys.stdout)])
    logging.getLogger().setLevel(logging.DEBUG)
