from localstack.utils.aws import aws_models
WEuRr=super
WEuRh=None
WEuRO=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  WEuRr(LambdaLayer,self).__init__(arn)
  self.cwd=WEuRh
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,WEuRO,env=WEuRh):
  WEuRr(RDSDatabase,self).__init__(WEuRO,env=env)
 def name(self):
  return self.WEuRO.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
