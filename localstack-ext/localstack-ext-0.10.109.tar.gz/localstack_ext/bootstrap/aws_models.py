from localstack.utils.aws import aws_models
hKulR=super
hKulb=None
hKulV=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  hKulR(LambdaLayer,self).__init__(arn)
  self.cwd=hKulb
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,hKulV,env=hKulb):
  hKulR(RDSDatabase,self).__init__(hKulV,env=env)
 def name(self):
  return self.hKulV.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
