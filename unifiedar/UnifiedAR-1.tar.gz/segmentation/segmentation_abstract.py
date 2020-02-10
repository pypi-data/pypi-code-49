from general.utils import Data, MyTask
import numpy as np
from general.utils import Buffer
import logging 
# Define segmentation
def segment(dtype,datasetdscr, segment_method):
    buffer = Buffer(dtype.s_events, 0, 0)
    w_history = []
    segment_method.reset()
    segment_method.precompute(datasetdscr,dtype.s_events,dtype.a_events,dtype.acts)
    while(1):
        window = segment_method.segment(w_history, buffer)
        if window is None:
            return
        w_history.append(window)
        yield window


class Segmentation(MyTask):
    def precompute(self,datasetdscr, s_events, a_events, acts):
        pass

    def segment(self, w_history, buffer):
        pass


def prepare_segment(func,dtype,datasetdscr):
    segmentor = func.segmentor
    
    
    func.activityFetcher.precompute(dtype)

    procdata = Data(segmentor.__str__())
    procdata.generator = segment(dtype,datasetdscr, segmentor)
    procdata.set = []
    procdata.label = []
    procdata.set_window = []
    procdata.acts = func.acts
    procdata.s_events = dtype.s_events
    procdata.a_events = dtype.a_events
    
    i = 0
    for x in procdata.generator:
        if i % 10000 == 0:
            logger.debug(segmentor.shortname(), i)
        i += 1
        procdata.set_window.append(x)
        procdata.label.append(
            func.activityFetcher.getActivity(dtype, x['window']))
    del procdata.generator
    procdata.label = np.array(procdata.label)

    return procdata


def prepare_segment2(func,dtype,datasetdscr):
    segmentor = func.segmentor
    
    
    func.activityFetcher.precompute(dtype)

    procdata = Data(segmentor.__str__())
    procdata.generator  = segment2(dtype,datasetdscr, segmentor)
    procdata.set        = []
    procdata.label      = []
    procdata.set_window = []
    procdata.acts       = func.acts
    procdata.s_events   = dtype.s_events
    procdata.s_event_list= dtype.s_event_list
    procdata.a_events   = dtype.a_events
    
    i = 0
    for x in procdata.generator:
        if i % 10000 == 0:
            print(segmentor.shortname(), i)
        i += 1
        procdata.set_window.append(x)
        procdata.label.append(func.activityFetcher.getActivity2(dtype.s_event_list, x))
    del procdata.generator
    procdata.label = np.array(procdata.label)

    return procdata

# Define segmentation
def segment2(dtype,datasetdscr, segment_method):
    buffer = Buffer(dtype.s_events, 0, 0)
    w_history = []
    segment_method.reset()
    segment_method.precompute(datasetdscr,dtype.s_events,dtype.a_events,dtype.acts)
    while(1):
        window = segment_method.segment2(w_history, buffer)
        if window is None:
            return
        w_history.append(window)
        yield window
