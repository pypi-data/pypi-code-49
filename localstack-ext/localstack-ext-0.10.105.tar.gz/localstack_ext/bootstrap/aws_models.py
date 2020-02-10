from localstack.utils.aws import aws_models
pLXNG=super
pLXNy=None
pLXNt=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  pLXNG(LambdaLayer,self).__init__(arn)
  self.cwd=pLXNy
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,pLXNt,env=pLXNy):
  pLXNG(RDSDatabase,self).__init__(pLXNt,env=env)
 def name(self):
  return self.pLXNt.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
