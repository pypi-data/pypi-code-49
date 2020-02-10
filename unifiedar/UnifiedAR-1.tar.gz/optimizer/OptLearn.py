from memory_profiler import profile
from constants import no_memory_limit
from general.utils import MyTask
import skopt
import logging
logger = logging.getLogger(__file__)
import numpy as np
class OptLearn(MyTask):
    no_memory_limit=False
    def __init__(self,functions,callback):
        self.shortrunname=functions.shortrunname
        self.functions=functions
        self.callback=callback
    
    # @profile
    def run(self):
        shortrunname=self.shortrunname
        func  =self.functions
        
        logger.debug('%s %s', shortrunname,'start')
        
        
        func.segmentor.reset()
        func.featureExtractor.reset()
        params=ParamMaker([func.segmentor,func.featureExtractor,func.classifier])
        x0,bounds=params.convertToArray()

        result={}
        
        def qfunc(param): 
            segparams=params.getParams(param,0)
            feaparams=params.getParams(param,1)
            claparams=params.getParams(param,2)
            if not func.featureExtractor.applyParams(feaparams):
                return 100000
            if not func.segmentor.applyParams(segparams):
                return 100000
            if not func.classifier.applyParams(claparams):
                return 100000
            logger.debug('%s',func.segmentor.params)
            logger.debug('%s segparam: %s feaparam: %s claparam: %s', shortrunname,segparams,feaparams,claparams)
            q=self.callback(func)
            # if no_memory_limit:
            #     result['last']=result['history'][str(param)]={'q':q}
            
            return -q if ~np.isnan(q) else 100000
        
        if len(x0)>0:
            optq=skopt.forest_minimize(qfunc,bounds,n_jobs=8,n_calls=30)
            optq={'x':optq['x'],'q':optq['fun']}
        else:
            optq={'x':x0, 'q':qfunc(x0)};
        logger.debug('%s %s', shortrunname,optq)
        
        result['optq']=optq
        result['segparams']=params.getParams(optq['x'],0)
        result['feaparams']=params.getParams(optq['x'],1)
        result['claparams']=params.getParams(optq['x'],2)

        

        self.result=result
        return result



class ParamMaker:
    def __init__(self,items):
        self.items=items
        self._fixItems()

    def convertToArray(self):
        #seg.params.length
        x0=[]
        bounds=[]

        for item in self.items:
            logger.debug('%s',item)
            if(item.findopt):
                for p in item.defparams:
                    bounds.append([p['min'],p['max']])
                    x0.append(p['init'])
        return x0,bounds

    def getParams(self,X,i):
        items=self.items
        x0=[];
        
        if not items[i].findopt:
            for p in items[i].defparams:
                x0.append(p['init'])
            return self.convertArray2ParamsDic(x0,items[i].defparams)
        fi=0
        for j in range(i):
            if(items[j].findopt):
                fi=fi+len(items[j].defparams)
            
        return self.convertArray2ParamsDic(X[fi:fi+len(items[i].defparams)],items[i].defparams)
    
    def convertArray2ParamsDic(self,array,params):
        paramDic={}
        for i,p in enumerate(params):
                paramDic[p['var']]=array[i]
        return paramDic

    def _fixItems(self):
        for item in self.items:
            for p in item.defparams:
                if 'var' in p: continue
                for n in p:
                    if n == 'min' or n == 'max' or n == 'init':
                        continue
                    p['var']=n
                    p['init']=p[n]
                    break
