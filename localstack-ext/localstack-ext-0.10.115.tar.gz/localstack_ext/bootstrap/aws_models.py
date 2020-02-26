from localstack.utils.aws import aws_models
tXmjL=super
tXmjn=None
tXmjs=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  tXmjL(LambdaLayer,self).__init__(arn)
  self.cwd=tXmjn
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,tXmjs,env=tXmjn):
  tXmjL(RDSDatabase,self).__init__(tXmjs,env=env)
 def name(self):
  return self.tXmjs.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
