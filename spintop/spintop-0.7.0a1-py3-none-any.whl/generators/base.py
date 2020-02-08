import importlib

from abc import ABC, abstractmethod

from spintop.models import SpintopTestRecordCollection

class Generator(ABC):
    def __init__(self, transform_pipeline=None):
        self.transform_pipeline = transform_pipeline
        
    def __call__(self, *args, **kwargs):
        generated = self.generate(*args, **kwargs)
        if self.transform_pipeline:
            return self.transform_pipeline.transform(generated)
        else:
            return generated
    
    @abstractmethod
    def generate(self, *args, **kwargs):
        raise NotImplementedError()
    
class GeneratorFromModule(Generator):
    def __init__(self, module):
        super(GeneratorFromModule, self).__init__()
        self.module = module
        
    @classmethod
    def from_module_name(cls, module_name):
        return cls(
            importlib.import_module(module_name)
        )
        
    def generate(self, *args, **kwargs):
        """Override."""
        return self.module.generate(*args, **kwargs)

def generator_from_module_or_module_name(module_or_module_name):
    if isinstance(module_or_module_name, str):
        generator_obj = importlib.import_module(module_or_module_name)
    else:
        generator_obj = module_or_module_name
    return GeneratorFromModule(generator_obj)