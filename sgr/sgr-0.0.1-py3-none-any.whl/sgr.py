import imp
import logging
import pkgutil
import abc

# https://github.com/aws/sagemaker-containers

class SageMakerRegistry(object):
  class __metaclass__(type):
    def __init__(cls, name, base, attrs):
      if not hasattr(cls, 'registered'):
          cls.registered = []
      else:
          cls.registered.append(cls)
  @classmethod
  def load(cls, *paths):
    paths = list(paths)
    cls.registered = []
    for _, name, _ in pkgutil.iter_modules(paths):
      fid, pathname, desc = imp.find_module(name, paths)
      try:
        imp.load_module(name, fid, pathname, desc)
      except Exception as e:
        logging.warning(f"could not load plugin module '{pathname}': {e.message}")
      finally:
        if fid:
          fid.close()
    @abc.abstractmethod
    def train(self, **kwargs):
      raise NotImplementedError

    @abc.abstractmethod
    def serve(self, **kwargs):
      raise NotImplementedError