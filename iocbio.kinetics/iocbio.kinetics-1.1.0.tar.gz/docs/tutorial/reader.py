import numpy, hashlib

from iocbio.kinetics.io.data import Data, Carrier
from .experiment import ExperimentTutorial

IocbioKineticsModule = ["reader"]

def reader(txt):
    lines = txt.splitlines()
    if not lines[0].startswith("# Header info"):
        return None, None, None
    data = {}
    li = 1
    while lines[li].startswith("# "):
        # split into maximally 2 elements, key and value
        # the first 2 chars are '# ' and we skip them
        processed = lines[li][2:].split(":", 1)
        if len(processed) != 2:
            break
        # store key,value pair after removing whitespaces
        data[ processed[0].strip() ] = processed[1].strip()
        # move to the next line
        li += 1

    events = {}
    x = []
    y = []
    while li < len(lines):
        # split into maximally 3 elements, key, value, and event
        processed = lines[li].split("\t", 2)
        if len(processed) < 2:
            # maybe a trailing line in the end of experiment
            break
        time = float(processed[0])
        sl = float(processed[1])
        x.append(time)
        y.append(sl)
        if len(processed)==3:
            e = processed[2].strip()
            if len(e) >= 1:
                # storing event as a dictionary
                events[time] = processed[2]
        # move to the next line
        li += 1
    data['events'] = events
    return data, numpy.array(x), numpy.array(y)
            

def create_data(database, experiment_id=None, args=None):
    from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric

    filename=getattr(args, "file_name", None)
    fulltxt=None
    if experiment_id is not None:
        fulltxt = ExperimentTutorial.get_fulltxt(database, experiment_id)

    if filename is not None:
        fulltxt = open(filename, 'r').read()

    # check if we can load anything
    if fulltxt is None: return None

    d, x, y = reader(fulltxt)
    # check if data was imported
    if d is None: return None

    # calculate experiment id if needed
    if experiment_id is None:
        expid = "tutorial sarcomere length - " + hashlib.sha256(fulltxt.encode('utf-8')).hexdigest()
    else:
        expid = experiment_id

    # add filename to the data object
    d["this_file"] = filename

    # store data in expected format
    dd = { 'sarcomere_length': { 'x': x,
                                 'y': Carrier('Sarcomere length', 'um', y) } }
        
    data = Data( expid,
                 # any type of configuration used in the analysis further
                 config=d,
                 # specific type of experiment, may mention hardware
                 type="Tutorial experiment Sarcomere Shortening",
                 # more generic type of experiment
                 type_generic = "Sarcomere shortening",
                 # datetime string
                 time = d["Date"] + " " + d["Time"],
                 # name of experiment
                 name = d["Experiment name"],
                 # x-axis data
                 xname = "Time", xunit = "seconds",
                 xlim = (x[0], x[-1]),
                 # measured data
                 data = dd )

    # check if we have data in the database. If not, store it
    if not ExperimentGeneric.has_record(database, data.experiment_id):
        # set database into read/write mode as we import the data
        database.set_read_only(False)
        # store the data
        ExperimentTutorial.store(database, data, fulltxt)

    return data
