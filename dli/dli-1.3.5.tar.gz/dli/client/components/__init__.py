import types
from functools import wraps

from dli.client.aspects import extract_metadata, LoggingAspect, AnalyticsAspect


class ComponentsAspectWrapper(type):
    """
    This decorates all functions in a Component with a logging function.
    """
    __aspects = [LoggingAspect(), AnalyticsAspect()]

    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, types.FunctionType):
                attrs[attr_name] = cls._wrap_call_with_aspects(attr_value)

        return super(ComponentsAspectWrapper, cls).__new__(cls, name, bases, attrs)

    @classmethod
    def _wrap_call_with_aspects(cls, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                metadata = extract_metadata(self, self, func, args, kwargs)
            except Exception as e:
                if getattr(self, 'logger', None):
                    self.logger.exception(
                        'Error while reading function metadata.', e
                    )
                return func(self, *args, **kwargs)

            try:
                cls._invoke_pre_call_aspects(self, metadata)
                result = func(self, *args, **kwargs)
                cls._invoke_post_call_aspects(self, metadata)
                return result
            except Exception as e:
                cls._invoke_after_exception_aspects(self, metadata, e)
                raise e

        return wrapper

    @classmethod
    def _invoke_pre_call_aspects(cls, wrapped_object, metadata):
        for aspect in cls.__aspects:
            aspect.invoke_pre_call_aspects(wrapped_object, metadata)

    @classmethod
    def _invoke_post_call_aspects(cls, wrapped_object, metadata):
        for aspect in cls.__aspects:
            aspect.invoke_post_call_aspects(wrapped_object, metadata)

    @classmethod
    def _invoke_after_exception_aspects(cls, wrapped_object, metadata, exception):
        for aspect in cls.__aspects:
            aspect.invoke_after_exception_aspects(wrapped_object, metadata, exception)


class SirenComponent(metaclass=ComponentsAspectWrapper):

    def __init__(self, client=None):
        self.client = client
