from localstack.utils.aws import aws_models
ysNWo=super
ysNWE=None
ysNWr=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  ysNWo(LambdaLayer,self).__init__(arn)
  self.cwd=ysNWE
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,ysNWr,env=ysNWE):
  ysNWo(RDSDatabase,self).__init__(ysNWr,env=env)
 def name(self):
  return self.ysNWr.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
