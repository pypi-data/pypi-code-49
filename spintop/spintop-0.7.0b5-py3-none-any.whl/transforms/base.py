import warnings
import types

class TransformError(Exception): pass

class Transformer(object):
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()
    
    def generate(self, *args, **kwargs):
        for value in self(*args, **kwargs):
            yield value
    
    def append(self, *transforms):
        return join_transforms(self, *transforms)

    def __add__(self, transform):
        return self.join_with(transform)

    def __radd__(self, other):
        return other.join_with(self)
    
    def __rshift__(self, other):
        return self + other
        
    def __rrshift__(self, other):
        return other + self
    
    def join_with(self, other):
        return join_transforms(self, other)

class FunctionTransformer(Transformer):
    def __init__(self, fn):
        self.fn = fn
        
    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)

class TransformBuilder():
    def __init__(self, *transforms, _first_step=None):
        self.first_step = _first_step
        self.append(*transforms)
            
    @property
    def last_step(self):
        last_step = self.first_step
        while last_step is not None and last_step.next_step:
            last_step = last_step.next_step
        return last_step
            
    def append(self, *transforms):
        if len(transforms) == 1 and isinstance(transforms[0], TransformStep):
            first_next_step = transforms[0]
        else:
            first_next_step = None
            for transform in reversed(transforms):
                first_next_step = TransformStep(transform, next_step=first_next_step)
        
        if self.first_step:
            self.last_step.set_next(first_next_step)
        else:
            self.first_step = first_next_step
        
    def prepend(self, transform):
        if self.first_step is not None:
            # Not first step
            self.first_step = self.first_step.prepend(transform)
        else:
            # First step
            self.first_step = TransformStep(transform)
            
    def __call__(self, *args, **kwargs):
        return self.first_step(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(self.first_step, name)
    
    def split(self, branches=2):
        return tuple(self.copy() for _ in range(branches))
        
    def copy(self):
        return TransformBuilder(_first_step=self.first_step.copy())
    
    def join_with(self, other):
        new_self = self.copy()
        new_self.append(other)
        return new_self

    def __repr__(self):
        return repr(self.first_step)

class TransformStep(Transformer):
    def __init__(self, transform_fn, next_step=None):
        if isinstance(transform_fn, TransformStep):
            raise TransformError("The transform function cannot be an instance of TransformStep.")
        self._transform_fn = transform_fn
        self._next_step = next_step
    
    @property
    def next_step(self):
        return self._next_step
    
    @property
    def transform_fn(self):
        return self._transform_fn
    
    def __call__(self, *args, **kwargs):
        """ The first transform step can be called with as many arguments as desired. However, subsequent steps
        will receive only one argument: the result of the previous transform.
        """
        generator = self.generate(*args, **kwargs)
        result = list(generator)

        if len(result) != 1:
            raise Exception(
                "Transform did not return exactly one (!={}) value. "
                "If this is a generator and you wish to iterate the "
                "yield values, use the 'generate' method instead of "
                "__call__.".format(len(result)))
        else:
            return result[0]

    def generate(self, *args, **kwargs):
        obj = self.transform_fn(*args, **kwargs)
        
        if obj is None:
            raise TransformError("Transformer fn {} returned None".format(self.transform_fn))

        if isinstance(obj, types.GeneratorType):
            for subobj in obj:
                yield from self._call_next_step(subobj)
        else:
            yield from self._call_next_step(obj)

    def _call_next_step(self, obj):
        if self.next_step:
            yield from self.next_step.generate(obj)
        else:
            yield obj
        
    def set_next(self, next_step):
        if self.next_step:
            raise TransformError('Next step already defined ! This would break the transform pipeline.')
        self._next_step = next_step
        
    def prepend(self, transform):
        if isinstance(transform, TransformStep):
            previous_step = transform.copy(next_step=self)
        else:
            previous_step = self.__class__(transform, next_step=self)
        return previous_step
    
    def copy(self, next_step=None):
        next_step = next_step
        if next_step is None and self.next_step:
            next_step = self.next_step.copy()
        return self.__class__(self.transform_fn, next_step=next_step)
    
    def __repr__(self):
        return "TransformStep(fn={}), next=\n{}".format(self.transform_fn, repr(self.next_step))
    
class EmptyTransformer(Transformer):
    def __call__(self, arg):
        return arg
    
def join_transforms(*transforms):
    return TransformBuilder(*transforms)

def transformer(fn):
    return FunctionTransformer(fn)