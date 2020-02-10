from general.utils import MyTask
import numpy as np

def featureExtraction(feat,datasetdscr,s_event_list,windows,istrain):
    method=feat
    
    if(istrain):
        method.precompute(datasetdscr,windows)
    fw=method.featureExtract2(s_event_list,windows[0])

    if(len(fw.shape)==1):
        result=np.zeros((len(windows),fw.shape[0]))
    else:
        result=np.zeros((len(windows),fw.shape[0],fw.shape[1]))
    result[0]=fw
    for i in range(1,len(windows)):
        w=windows[i]
        result[i]=method.featureExtract2(s_event_list,w)

    #result  =   np.array(result)
    
    return result

class FeatureExtraction(MyTask):
    def precompute(self,datasetdscr,windows):
        self.datasetdscr=datasetdscr
        pass
    def featureExtract(self,window):
        pass
