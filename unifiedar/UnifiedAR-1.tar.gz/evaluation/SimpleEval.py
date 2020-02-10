import pandas as pd

from evaluation.evaluation_abstract import Evaluation
from general.utils import Data
from general.utils import saveState
from general.utils import saveFunctions

class SimpleEval(Evaluation):
    
    def evaluate(self, dataset, strategy):
        Train, Test = self.makeTrainTest(
            dataset.sensor_events, dataset.activity_events)
        acts=[a for a in dataset.activities_map]
        strategy.train(dataset, Train, acts)
        testres = strategy.test(Test)
        
        return [testres]

    def makeTrainTest(self, sensor_events, activity_events):
        dataset_split = min(activity_events.StartTime) + \
            ((max(activity_events.EndTime)-min(activity_events.StartTime))*4/5)
        dataset_split = pd.to_datetime(dataset_split.date())  # day
        Train = Data('train')
        Test = Data('test')
        Train.s_events = sensor_events[sensor_events.time < dataset_split]
        Train.a_events = activity_events[activity_events.EndTime < dataset_split]
        Train.s_event_list=Train.s_events.values
        
        Test.s_events = sensor_events[sensor_events.time >= dataset_split]
        Test.a_events = activity_events[activity_events.EndTime >= dataset_split]
        Test.s_event_list=Test.s_events.values
        return Train, Test
