from localstack.utils.aws import aws_models
dGOfK=super
dGOfF=None
dGOfU=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  dGOfK(LambdaLayer,self).__init__(arn)
  self.cwd=dGOfF
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,dGOfU,env=dGOfF):
  dGOfK(RDSDatabase,self).__init__(dGOfU,env=env)
 def name(self):
  return self.dGOfU.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
