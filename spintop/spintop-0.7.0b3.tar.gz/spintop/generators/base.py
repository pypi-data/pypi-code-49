import importlib

from abc import ABC, abstractmethod

from spintop.models import SpintopTestRecordCollection
from spintop.transforms import Transformer

class Generator(Transformer):
    """Transformers natively support a generator behaviour through the __call__ function."""
    
class GeneratorFromModule(Generator):
    def __init__(self, module):
        super(GeneratorFromModule, self).__init__()
        self.module = module
        
    @classmethod
    def from_module_name(cls, module_name):
        return cls(
            importlib.import_module(module_name)
        )
        
    def __call__(self, *args, **kwargs):
        """Override."""
        return self.module.generate(*args, **kwargs)

def generator_from_module_or_module_name(module_or_module_name):
    if isinstance(module_or_module_name, str):
        generator_obj = importlib.import_module(module_or_module_name)
    else:
        generator_obj = module_or_module_name
    return GeneratorFromModule(generator_obj)