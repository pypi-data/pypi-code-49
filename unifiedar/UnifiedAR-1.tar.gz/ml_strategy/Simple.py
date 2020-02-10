
import logging

from sklearn.metrics import confusion_matrix

from feature_extraction.feature_abstract import featureExtraction
from general.utils import Data, MyTask
from metric.CMbasedMetric import CMbasedMetric
from metric.event_confusion_matrix import event_confusion_matrix
from metric.EventBasedMetric import EventBasedMetric
import ml_strategy.abstract
from optimizer.BruteForce import method_param_selector
from optimizer.OptLearn import OptLearn, ParamMaker
from segmentation.segmentation_abstract import prepare_segment,prepare_segment2
logger = logging.getLogger(__file__)

class SimpleStrategy(ml_strategy.abstract.MLStrategy):
    def train(self, datasetdscr, data, acts):
        self.datasetdscr=datasetdscr
        self.acts=acts
        self.traindata=self.justifySet(self.acts,data)
        bestOpt=method_param_selector(self.learning)
        self.functions=bestOpt.functions
        



    
    def learning(self,func):
        func.acts=self.acts
        logger.debug('Starting learning .... %s' % (func.shortrunname))
        Tdata=func.preprocessor.process(self.datasetdscr, self.traindata)
        logger.debug('Preprocessing Finished %s' % (func.preprocessor.shortname()))
        Sdata=prepare_segment2(func,Tdata,self.datasetdscr)
        logger.debug('Segmentation Finished %d segment created %s' % (len(Sdata.set_window), func.segmentor.shortname()))
        Sdata.set=featureExtraction(func.featureExtractor,self.datasetdscr,Sdata.s_event_list,Sdata.set_window,True)
        logger.debug('FeatureExtraction Finished shape %s , %s' % (str(Sdata.set.shape), func.featureExtractor.shortname()))

        func.classifier.createmodel(Sdata.set[0].shape,len(self.acts))
        logger.debug('Classifier model created  %s' % (func.classifier.shortname()))
        func.classifier.train(Sdata.set, Sdata.label) 
        logger.debug('Classifier model trained  %s' % (func.classifier.shortname()))

        logger.info("Evaluating....")
        predicted   =func.classifier.predict(Sdata.set)
        pred_events =func.combiner.combine(Sdata.s_event_list,Sdata.set_window,predicted)
        logger.debug('events merged  %s' % (func.combiner.shortname()))
        #eventeval=EventBasedMetric(Sdata.a_events,pred_events,self.acts)
        event_cm    =event_confusion_matrix(Sdata.a_events,pred_events,self.acts)
        quality     =CMbasedMetric(event_cm,'macro')
        logger.debug('Evalution quality is %s'%quality)
        return quality['f1']
        
        
    def test(self, data):
        func=self.functions
        data=self.justifySet(self.acts,data)
        func.acts=self.acts

        Tdata=func.preprocessor.process(self.datasetdscr, data)
        Sdata=prepare_segment2(func,Tdata,self.datasetdscr)
        Sdata.set=featureExtraction(func.featureExtractor,None,Sdata.s_event_list,Sdata.set_window,False)
        result=Data('TestResult')
        result.shortrunname=func.shortrunname
        result.Sdata=Sdata
        result.predicted=func.classifier.predict(Sdata.set)
        result.params={}
        for f in func.__dict__:
            obj = func.__dict__[f]
            if isinstance(obj, MyTask):
                result.params[f]=obj.params
        
        result.predicted_classes=func.classifier.predict_classes(Sdata.set)    

        pred_events=self.functions.combiner.combine(Sdata.s_event_list,Sdata.set_window,result.predicted)
        
        result.pred_events=pred_events
        result.real_events=data.a_events

        result.event_cm    =event_confusion_matrix(data.a_events,pred_events,self.acts)
        result.quality     =CMbasedMetric(result.event_cm,'macro')
        

        return result
