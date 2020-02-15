from .lambdaexceptions import *
import json
import logging, traceback

logger = logging.getLogger("pspring-aws")

class LambdaHandler():

    def __init__(self,*args,**kargs):
        self.type = kargs.get("type","proxy")
        self.corsHeaders = kargs.get("corsheaders")

    def __call__(self,classObj):
        handlerOrig = classObj.handler
        constructorOrig = classObj.__init__
        def constructor(*args,**kargs):
            selfObj = args[0]
            selfObj.logattrs = {}
            constructorOrig(*args,**kargs)

        def logtemplate(selfObj,logObj):
            logdict=dict()
            if type(logObj) == type(""):
                logdict.update(selfObj.logattrs)
                logdict.update({
                    "message" : logObj
                })
                return logdict
            else:
                logdict.update(selfObj.logattrs)
                logdict.update(logObj)
                return logdict

        def debug(selfObj,logObj):
            logger.debug(selfObj.logtemplate(logObj))
        def info(selfObj,logObj):
            logger.info(selfObj.logtemplate(logObj))
        def error(selfObj,logObj):
            logger.error(selfObj.logtemplate(logObj))
        def warn(selfObj,logObj):
            logger.warn(selfObj.logtemplate(logObj))

        def addToLogger(selfObj,fieldName,fieldValue):
            selfObj.logattrs.update({
                fieldName : fieldValue
            })

        def handler(*args,**kargs):
            finalresponse = None
            try:
                selfObj = args[0]
                event = args[1]
                context = args[2]
                econtext = event.get('requestContext',{})
                requestId = str(econtext.get('requestId',{}))
                traceId = event.get("headers",{}).get("X-Amzn-Trace-Id")
                cfId = event.get("headers",{}).get("X-Amz-Cf-Id")
                selfObj.addToLogger("requestId",requestId)

                if hasattr(context,"aws_request_id"):
                    selfObj.addToLogger("awsRequestId",context.aws_request_id)

                if traceId != None:
                    selfObj.addToLogger("X-Amzn-Trace-Id",traceId)

                if cfId != None:
                    selfObj.addToLogger("X-Amz-Cf-Id",cfId)

                if str(econtext.get('requestId')) == "COLD_START_WARMER":
                    selfObj.debug("Received cold start request")
                    return {
                        "statusCode" : "200",
                        "body" : json.dumps("{}")
                    }

                response = handlerOrig(*args,**kargs)
                finalresponse = {
                    "statusCode" : "200"
                }
                finalresponse.update(response)
                
                return finalresponse

            except LambdaException as le:
                 finalresponse = le.getResponse()
            except Exception as e:
                logger.error(traceback.format_exc()+str(e))
                if hasattr(e,"statusCode") and hasattr(e,"response"):
                    finalresponse =  LambdaException(str(e),e.statusCode,e.response).getResponse()
                else:
                    finalresponse =  LambdaException(str(e)).getResponse()

            if(self.corsHeaders != None and type(self.corsHeaders) == type({})):
                headers = finalresponse.get("headers",{})
                headers.update(self.corsHeaders)
                finalresponse.update({"headers" : headers})
            return finalresponse

        classObj.handler = handler
        classObj.__init__ = constructor
        classObj.addToLogger = addToLogger
        classObj.debug = debug
        classObj.info = info
        classObj.warn = warn
        classObj.error = error
        classObj.logtemplate = logtemplate
        return classObj
