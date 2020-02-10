
import numpy as np
import pandas as pd
from intervaltree.intervaltree import IntervalTree
from general.utils import Data

def event_confusion_matrix(r_activities,p_activities,labels):
    cm=np.zeros((len(labels),len(labels)))
    # begin=real0.StartTime.min()
    # end=real0.EndTime.max()
    predicted=[p for i,p in p_activities.iterrows()]
    real=[p for i,p in r_activities.iterrows()]

    #   predicted.append({'StartTime':begin,'EndTime':end,'Activity':0})
    #   real.append({'StartTime':begin,'EndTime':end,'Activity':0})
    events=merge_split_overlap_IntervalTree(predicted,real)
    #predictedtree=makeIntervalTree(labels)

    
    for eobj in events:
        e=eobj.data
        pact=e.P.Activity if not(e.P is None) else 0
        ract=e.R.Activity if not(e.R is None) else 0
        cm[ract][pact]+=max((eobj.end-eobj.begin)/pd.to_timedelta('60s').value,0.01)
            
    #for p in predicted:
    #  for q in realtree[p['StartTime'].value:p['EndTime'].value]:
    #      timeconfusion_matrix[p['Activity']][q.data['Activity']]+=findOverlap(p,q.data);
            
    return cm









def merge_split_overlap_IntervalTree(p_acts,r_acts):
    tree=IntervalTree()

    for act in p_acts:
        start=act['StartTime'].value;
        end=act['EndTime'].value;
        if(start==end):
            start=start-1
        #tree[start:end]={'P':{'Activitiy':act.Activity,'Type':'P','Data':act}]
        d=Data('P-act')
        d.P=act
        d.R=None
        tree[start:end]=d #{'P':act,'PActivitiy':act.Activity}
        
    for act in r_acts:
        start=act['StartTime'].value;
        end=act['EndTime'].value;
        if(start==end):
            start=start-1
        #tree[start:end]=[{'Activitiy':act.Activity,'Type':'R','Data':act}]
        d=Data('P-act')
        d.P=None
        d.R=act
        tree[start:end]=d #{'R':act,'RActivitiy':act.Activity}

    tree.split_overlaps()
    def data_reducer(x,y):
        res=x
        if not(y.P is None):
            if (res.P is None) or y.P['EndTime']<res.P['EndTime']:
                res.P=y.P
        if not(y.R is None):
            if (res.R is None) or y.R['EndTime']<res.R['EndTime']:
                res.R=y.R
        return res
    
    tree.merge_equals(data_reducer=data_reducer)
            
    return tree