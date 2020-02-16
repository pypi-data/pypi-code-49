import pulumi
from pulumi import log
import sys
import os
from pulumi_aws import lambda_, iam
from .utils import format_resource_name, filebase64sha256
import glob
from .zip_package import ZipPackage
from .pip_requirements import PipRequirements

class LambdaPackaging(pulumi.ComponentResource):
    def __init__(self,
                 name,
                 requirements_path='requirements.txt',
                 runtime='python3.6',
                 layer=False,
                 dockerize=False,
                 include=["**"],
                 no_deploy=[],
                 exclude=[],
                 opts=None):
        """
        :name: name of the resource
        :requirements_path: relative path of requirements.txt
        :runtime: python runtime
        :layer: use lambda layer
        :dockerize: dockerize python requirements
        :no_deploy: list of requirements to prevent from packaging
        :include: list of dirs, files to include while packaging
        :exclude: list of dirs, files to exclude while packaging
        """
        super().__init__('nuage:aws:LambdaPackage ', name, None, opts)
        self.requirements_path = requirements_path
        self.runtime = runtime
        self.layer = layer
        self.dockerize = dockerize
        self.no_deploy = no_deploy
        self.include = include
        self.exclude = exclude
        self.project_root =  os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
        pulumi.log.info(self.project_root)

        # install requirements through pip
        pip = PipRequirements('requirements.txt', '.plp/')

        pip.install_requirements()
        # zip package
        packaged_asset = ZipPackage(self.project_root, 'lambda.zip', pip.target_install_path, self.include, self.exclude)
        packaged_asset.zip_package()

        
    

        
