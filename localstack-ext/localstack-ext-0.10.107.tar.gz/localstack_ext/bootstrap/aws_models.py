from localstack.utils.aws import aws_models
JWkPD=super
JWkPN=None
JWkPg=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  JWkPD(LambdaLayer,self).__init__(arn)
  self.cwd=JWkPN
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,JWkPg,env=JWkPN):
  JWkPD(RDSDatabase,self).__init__(JWkPg,env=env)
 def name(self):
  return self.JWkPg.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
