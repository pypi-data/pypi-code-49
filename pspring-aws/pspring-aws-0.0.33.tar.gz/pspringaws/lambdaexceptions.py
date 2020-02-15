import json

class LambdaException(Exception):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code = "500"
        self.msg = "Internal Server Error : "+str(self)
        self.payload = None
        if len(args) > 1:
            self.code = args[1]
        if len(args) > 0:
            self.msg = args[0]
        if len(args) > 2:
            self.payload = args[2]

        self.errorCode = kargs.get("errorCode")

    def getResponse(self):

        if self.payload != None:
            return {
                "statusCode": self.code,
                "body": self.payload
            }
        return {
            "statusCode": self.code,
            "body": json.dumps({
                "message" : self.msg,
                "code" : self.errorCode
            })
        }

class NotFoundException(LambdaException):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code="404"

class UnAuthorizedException(LambdaException):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code="401"

class Forbidden(LambdaException):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code="403"

class InternalServerException(LambdaException):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code="500"

class CreatedException(LambdaException):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code="201"

class MethodNotAllowed(LambdaException):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code="405"

class BadRequest(LambdaException):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code="400"

class UnSupportedMediaType(LambdaException):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code="415"

class RedirectException(LambdaException):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.code="301"
