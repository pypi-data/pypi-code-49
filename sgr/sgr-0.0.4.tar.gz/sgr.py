import imp
import logging
import pkgutil
import inspect
import abc
import sys

from pathlib import Path
from importlib import import_module, util, machinery

# https://github.com/aws/sagemaker-containers

class SageMakerModelRegistry(object):
  @abc.abstractmethod
  def train(self, **kwargs):
    raise NotImplementedError

  @abc.abstractmethod
  def serve(self, **kwargs):
    raise NotImplementedError

def import_classes(modname, base_class=SageMakerModelRegistry().__class__):
    module = import_module(modname)
    for member_name, obj in inspect.getmembers(module):
      if inspect.isclass(obj) and base_class in obj.__bases__:
          # TODO test if the obj implements the interface
          # Keep in mind that this only instantiates the ensemble_wrapper,
          # but not the real target classifier
          return obj()
    raise RuntimeError("Unable to find classes extends {base_class} in {modname} on PYTHONPATH")

