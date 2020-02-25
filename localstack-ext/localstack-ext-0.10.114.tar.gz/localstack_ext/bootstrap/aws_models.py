from localstack.utils.aws import aws_models
tFvhA=super
tFvhu=None
tFvhN=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  tFvhA(LambdaLayer,self).__init__(arn)
  self.cwd=tFvhu
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,tFvhN,env=tFvhu):
  tFvhA(RDSDatabase,self).__init__(tFvhN,env=env)
 def name(self):
  return self.tFvhN.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
