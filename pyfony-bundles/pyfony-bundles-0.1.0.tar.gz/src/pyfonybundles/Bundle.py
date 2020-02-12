from typing import List
from box import Box
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerInterface import ContainerInterface
from injecta.definition.Definition import Definition

class Bundle:

    def getConfigFiles(self):
        return ['config.yaml']

    def getCompilerPasses(self) -> List[CompilerPassInterface]:
        return []

    def modifyRawConfig(self, rawConfig: dict) -> dict:
        return rawConfig

    def modifyServices(self, definitions: List[Definition]):
        return definitions

    def modifyParameters(self, parameters: Box) -> Box:
        return parameters

    def boot(self, container: ContainerInterface):
        pass
