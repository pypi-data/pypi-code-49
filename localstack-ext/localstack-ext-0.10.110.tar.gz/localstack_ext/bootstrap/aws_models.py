from localstack.utils.aws import aws_models
yaWlx=super
yaWlD=None
yaWlp=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  yaWlx(LambdaLayer,self).__init__(arn)
  self.cwd=yaWlD
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,yaWlp,env=yaWlD):
  yaWlx(RDSDatabase,self).__init__(yaWlp,env=env)
 def name(self):
  return self.yaWlp.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
