from localstack.utils.aws import aws_models
SXdYD=super
SXdYT=None
SXdYa=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  SXdYD(LambdaLayer,self).__init__(arn)
  self.cwd=SXdYT
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,SXdYa,env=SXdYT):
  SXdYD(RDSDatabase,self).__init__(SXdYa,env=env)
 def name(self):
  return self.SXdYa.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
