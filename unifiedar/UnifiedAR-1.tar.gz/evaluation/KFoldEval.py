from evaluation.evaluation_abstract import Evaluation
from general.utils import Data
from sklearn.model_selection import KFold
import logging
logger = logging.getLogger(__file__)

class KFoldEval(Evaluation):
    def __init__(self, fold):
        self.fold=fold
    def precompute(self, dataset):
        pass

    def evaluate(self, dataset, strategy):
        ttmaker = self.makeFoldTrainTest(
            dataset.sensor_events, dataset.activity_events, self.fold)
        models = {}
        for f, (Train, Test) in enumerate(ttmaker):
            logger.debug('=========Fold %d ============', f)
            acts=[a for a in dataset.activities_map]
            strategy.train(dataset, Train, acts)
            models[f] = strategy.test(Test)

        return models

    def makeFoldTrainTest(self, sensor_events, activity_events, fold):
        sdate = sensor_events.time.apply(lambda x: x.date())
        adate = activity_events.StartTime.apply(lambda x: x.date())
        days = adate.unique()
        kf = KFold(n_splits=fold)
        kf.get_n_splits(days)

        for j, (train_index, test_index) in enumerate(kf.split(days)):
            Train0 = Data('train_fold_'+str(j))
            Train0.s_events = sensor_events.loc[sdate.isin(days[train_index])]
            Train0.a_events = activity_events.loc[adate.isin(
                days[train_index])]
            Train0.s_event_list=Train0.s_events.values
            Test0 = Data('test_fold_'+str(j))
            Test0.s_events = sensor_events.loc[sdate.isin(days[test_index])]
            Test0.a_events = activity_events.loc[adate.isin(days[test_index])]
            Test0.s_event_list=Test0.s_events.values

            yield Train0, Test0
