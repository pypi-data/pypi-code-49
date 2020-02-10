from general.utils import MyTask
from intervaltree.intervaltree import IntervalTree
class AbstractActivityFetcher(MyTask):
    def precompute(self,dataset):
        self.a_events_tree=IntervalTree()
        for i,act in dataset.a_events.iterrows():
            self.a_events_tree[act.StartTime.value:act.EndTime.value]=act  
        pass
    def getActivity(self,dataset,window):
        pass