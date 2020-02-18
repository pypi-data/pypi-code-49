import builtins
import os
from abc import ABC
from copy import deepcopy
from enum import Enum
from logging import getLogger
from typing import *

import pkg_resources
from dataclasses import fields, dataclass, Field, field, replace
from dataclasses_json import DataClassJsonMixin
from dataclasses_json.core import Json
from pyhocon import ConfigTree, ConfigFactory, ConfigException

from functional import Option
from ._classes import Path, RelPath, extract_generic, extract_optional
from ._decorations import *
from ._decorations import _FIELD_CONSTRUCTOR_POST_INIT, _FIELD_CONSTRUCTOR_ARGUMENT_TYPE
from .settings import Settings
from .util import get_field, dump_config, wraps_class

logger = getLogger('dataclasses-config')
A = TypeVar('A')

@dataclass(frozen=Settings.frozen)
class ConfigInvalidError(ConfigException):
    """
    Base exception class used inside this package.
    """
    
    cls: Type['Config']
    """ A `dataclasses_config.Config` which caused an exception. """
    
    config: ConfigTree
    """ A `pyhocon.ConfigTree` which caused an exception. """
    
    @property
    def dump(self) -> str:
        """ A config string representation. """
        return dump_config(self.config)
    
    @property
    def message(self) -> str:
        """ An exception message. """
        return f"Config for class {self.cls.__name__!r} is invalid. {self.dump}"
    
    def __post_init__(self):
        super(ConfigException, self).__init__(self.message)
    
    def __hash__(self):
        return hash(self.message)

@dataclass(frozen=Settings.frozen)
class ConfigMissingKeyError(ConfigInvalidError):
    """
    This exception is raised when the config key is requested but missing.
    This exception **is not** a successor of `KeyError`
    due to the way `KeyError`s are represented.
    """
    
    key: str
    """ A config key which caused an exception. """
    
    @property
    def message(self) -> str:
        return f"Config for class {self.cls.__name__!r} does not contain a required field {self.key!r}. {self.dump}"
    
    def __hash__(self):
        return hash(self.message)

_hidden_field = lambda default: field(default=default, init=False, repr=False, compare=False)

T = TypeVar('T')
@dataclass
class FieldExtension(Generic[T]):
    """
    A helper class for dataclass field manipulations.
    Contains the original `dataclasses.Field` object,
    its positional index and type information.
    """
    
    base: Field
    """ An original `dataclasses.Field` object. """
    positional_index: int
    """ Positional index of the field in class (for getting/setting inside `*args`). """
    
    is_optional: bool = field(init=False)
    is_generic: bool = field(init=False)
    tp: Type[T] = field(init=False)
    """
    The unwrapped type.
    It has removed generics (i.e., `MyClass[int]` becomes `MyClass`),
    as well as removed optional (i.e., `Optional[MyClass]` becomes `MyClass`).
    """
    
    def __post_init__(self):
        tp = self.base.type
        self.is_optional, tp = extract_optional(tp)        
        self.is_generic, tp, _ = extract_generic(tp)
        self.tp = tp
    
    @classmethod
    def from_class(cls, class_or_instance, filter: Union[Callable[['FieldExtension[T]'], bool], Type[T], None] = None) -> Iterator['FieldExtension[T]']:
        """
        Extracts the `dataclasses_config.FieldExtension`s from the given class.
        Returns an iterator.
        Ignores non-init fields.
        
        Args:
            class_or_instance: A DataClass type or DataClass instance.
             
            filter: Any of the following:
                
                - `None` *(default)*
                Nothing is filtered.
                
                - `Callable` with the signature:
                `dataclasses_config.FieldExtension => bool`
                This case, this function applies as a filter.
        
        """
        
        fields_seq = builtins.filter(lambda f: f.init, fields(class_or_instance))
        seq = (FieldExtension(f, i) for i, f in enumerate(fields_seq))
        
        if (filter is None):
            return seq
        
        elif (isinstance(filter, type)):
            _base = filter
            filter = lambda f: isinstance(f.tp, type) and issubclass(f.tp, _base)
        elif (callable(filter)):
            pass
        else:
            raise TypeError(f"Invalid type of filter argument: {filter!r} ({type(filter)!r}). Expected: type, callable or None")
        
        return builtins.filter(filter, seq)
del T

@dataclass(frozen=Settings.frozen)
class Config(DataClassJsonMixin, ABC):
    """
    A base class for the configuration.
    Could be automatically parsed from dict, json string and `pyhocon.ConfigTree`.
    
    Automatically processes the nested classes.
    Automatically post-processes classes marked with the `dataclasses_config.deserialize_with()` decorator.
    """
    
    _config: ConfigTree = _hidden_field(None)
    _config_kwargs: Dict[str, Any] = _hidden_field(None)
    
    @classmethod
    def from_config(cls: Type[A], config: ConfigTree, **kwargs) -> A:
        """
        Class-method.
        Parses the given `pyhocon.ConfigTree` and returns the new instance of this class.
        """
        
        res = cls.from_dict(config, config_kwargs=kwargs)
        object.__setattr__(res, '_config', config)
        object.__setattr__(res, '_config_kwargs', kwargs)
        return res
    
    @classmethod
    def from_dict(cls: Type[A], kvs: Json, *, config_kwargs: Dict[str, Any] = None, **kwargs) -> A:
        """
        Class-method.
        Parses the given parsed JSON-object and returns the new instance of this class.
        
        Args:
            kvs: `Dict[str, Any]`
            config_kwargs: Optional. `Dict[str, Any]`. Internal.
                `config_kwargs` are passed directly to the `dataclasses_config.Config.from_config()` calls
                while parsing the nested `Config`s.
            **kwargs: Extra options from the original `dataclasses_json.DataClassJsonMixin.from_dict()`.
        
        Raises:
            ConfigMissingKeyError: Raised when the config key is required but missing.
        
        """
        
        if (config_kwargs is None):
            config_kwargs = dict()
        
        kvs = deepcopy(kvs)
        for f in FieldExtension.from_class(cls):
            if (isinstance(f.tp, type)):
                if (issubclass(f.tp, Config)):
                    tree = ConfigTree(kvs.get(f.base.name, dict()))
                    kvs[f.base.name] = f.tp.from_config(tree, **config_kwargs)
                
                elif (issubclass(f.tp, Enum)):
                    value = kvs.get(f.base.name, None)
                    if (value is None):
                        continue
                    
                    updated = None
                    if (isinstance(value, str)):
                        try:
                            # noinspection PyUnresolvedReferences
                            updated = f.tp[value]
                        except ValueError:
                            pass
                    
                    if (updated is None):
                        updated = f.tp(value)
                    
                    kvs[f.base.name] = updated
        
        try:
            return super().from_dict(kvs, **kwargs)
        except KeyError as e:
            # noinspection PyArgumentList
            raise ConfigMissingKeyError(cls, kvs, e.args[0])
    
    def __post_init__(self):
        for f in FieldExtension.from_class(self, lambda f: hasattr(f.tp, _FIELD_CONSTRUCTOR_ARGUMENT_TYPE)):
            v = getattr(self, f.base.name)
            
            if (f.is_optional and v is None):
                continue
            
            # ToDo: Check ConstructorDataType
            cdt: ConstructorDataType = getattr(f.tp, _FIELD_CONSTRUCTOR_ARGUMENT_TYPE)
            post: PostInitFunctionType = getattr(f.tp, _FIELD_CONSTRUCTOR_POST_INIT)
            
            v = f.tp(v)
            if (post is not None):
                x = post(v, f.base.type)
                if (x is not None):
                    v = x
            
            object.__setattr__(self, f.base.name, v)
    
    def replace(self, **changes):
        """
        Return a new object replacing specified fields with new values.
        
        This is especially useful for frozen classes.
        
        Example:
            ```python
            @dataclass(frozen=Settings.frozen)
            class C(Config):
                x: int
                y: int
            
            c = C(1, 2)
            c1 = c.replace(x=3)
            assert c1.x == 3 and c1.y == 2
            ```
        """
        
        return replace(self, **changes)
    
    D = TypeVar('D', bound=dict)
    def asdict(self, *, dict_factory: Type[D] = dict) -> D:
        """
        Return the fields of a dataclass instance as a new dictionary mapping
        field names to field values.
        
        Args:
            dict_factory: `Type[dict]`.
                If given, `dict_factory` will be used instead of built-in dict.
                The function applies recursively to field values that are
                dataclass instances. This will also look into built-in containers:
                tuples, lists, and dicts.
                
                Default: `dict`
        
        Example:
            ```python
            @dataclass(frozen=Settings.frozen)
            class C(Config):
                x: int
                y: int
            
            c = C(1, 2)
            assert c.asdict() == { 'x': 1, 'y': 2 }
            ```
        """
        
        return dict_factory(self._asdict_iter())
    
    def _asdict_iter(self) -> Iterator[Tuple[str, Any]]:
        for f in FieldExtension.from_class(self, filter=lambda f: f.base.init):
            yield f.base.name, getattr(self, f.base.name)

    del D

T = TypeVar('T', bound=Config)
def main_config \
(
    *args,
    resources_directory: str = 'resources/',
    default_config_name: str = 'application.conf',
    reference_config_name: str = 'reference.conf',
    env_variable_name: Optional[str] = 'PYTHON_APPLICATION_CONFIG_PATH',
    root_config_path: str = None,
    module: str = None,
    log_config: bool = True,
) -> Callable[[Type[T]], Type[T]]:
    """
    Decorates the given `dataclasses_config.MainConfig` class with the default overrides.
    Multiple `dataclasses_config.main_config` directives override each other,
    and only the last is used.
    
    Args:
        *args: 
        resources_directory: `str`.
            Defines where to look for the config files.
            This applies for both current directory lookup and module resources directory lookup.
            
            *Default: `resources/`*
        
        default_config_name: `str` 
            Defines the default application config filename.
            It is searched in current directory and prioritized over the reference config
            when loading configuration via `dataclasses_config.MainConfig.default()`.
            
            *Default: `application.conf`*
        
        reference_config_name: `str`
            Defines the default reference config filename.
            It is searched in both current directory and resources directory
            when loading configuration via `dataclasses_config.MainConfig.default()`.
            Reference config values are fallback for values missing in the application config.
            
            *Default: `reference.conf`*
        
        env_variable_name: `Optional[str]`
            Defines the environment variable name to be used for searching default configuration.
            Could be set to None if this config could not be loaded via the environment variable.
            
            *Default: `PYTHON_APPLICATION_CONFIG_PATH`*
             
        root_config_path: Optional. `str`
            Defines the offset from the config root when loading the default and/or reference values.
            Ignored when calling `dataclasses_config.Config.from_config`
            
            By default, the root is used.
        
        module: Optional. `str`
            The module name resources are loaded from.
            (Reference config is loaded from the resources directory -- see above.)
            
            By default, the module from this class is used (which is get by `cls.__module__`).
        
        log_config: `bool`.
            If `True` (default), the config is logged to the `'dataclasses-config'` log
            with the INFO logging level.
    
    """
    
    def decorator(cls: Type[T]) -> Type[T]:
        @wraps_class(cls)
        @dataclass(frozen=Settings.frozen)
        class wrapper(dataclass(frozen=Settings.frozen)(cls)):
            _resources_directory: str = _hidden_field(default=resources_directory)
            _default_config_name: str = _hidden_field(default=default_config_name)
            _reference_config_name: str = _hidden_field(default=reference_config_name)
            _env_variable_name: str = _hidden_field(default=env_variable_name)
            _root_config_path: str = _hidden_field(default=root_config_path)
            _module: str = _hidden_field(default=module)
            _log: bool = _hidden_field(default=log_config)
        
        return wrapper
    
    if (args):
        return decorator(*args)
    else:
        return decorator

@main_config
class MainConfig(Config, ABC):
    """
    A `dataclasses_config.Config` extension which should be used
    for an application and/or module root config.
    
    This class **always** tries to load the reference config,
    whether the default config is loaded or the specific one.
    
    This reference config is then looked in current directory
    and module resources directory as a fallback.
    When loaded, it is merged with the loaded application config,
    with the application config's values prioritized.
    
    This works very similarly to the Scala's [lightbend/config](https://github.com/lightbend/config)
    
    ## See Also:
    1. Lightbend Config: https://github.com/lightbend/config
    2. Its Standard Behaviour: https://github.com/lightbend/config#standard-behavior
    """
    
    @classmethod
    def _get_module(cls) -> str:
        module: Optional[str] = get_field(cls, '_module').default
        if (module is None):
            module: str = cls.__module__
        
        return module
    
    @classmethod
    def _get_default_config_name(cls) -> str:
        return get_field(cls, '_default_config_name').default
    
    @classmethod
    def _get_reference_config_name(cls) -> str:
        return get_field(cls, '_reference_config_name').default
    
    @classmethod
    def _get_resources_directory(cls) -> str:
        return get_field(cls, '_resources_directory').default
    
    @classmethod
    def _get_env_variable_name(cls) -> Optional[str]:
        return get_field(cls, '_env_variable_name').default
    
    @classmethod
    def _get_log(cls) -> bool:
        return get_field(cls, '_log').default
    
    @classmethod
    def _get_root_config_path(cls) -> Optional[str]:
        return get_field(cls, '_root_config_path').default
    
    @classmethod
    def default(cls: Type[A]) -> A:
        """
        Tries to load the default config and merge reference config into it.
        
        If the `PYTHON_APPLICATION_CONFIG_PATH` environment variable exists and non-empty,
        then this would try to load config from this variable.
        Path might be relative and absolute.
        Raises an exception if config is missing.
        
        If such variable does not exist (or has empty value),
        then the default application config is searched.
        Search includes only resources directory in current working directory.
        Does not raise an exception if nothing is found.
        
        See `dataclasses_config.main_config()` for more information.
        
        Returns:
            `MainConfig`
        """
        
        default_config_name: str = cls._get_default_config_name()
        resources_directory: str = cls._get_resources_directory()
        
        env_var_name = cls._get_env_variable_name()
        application_conf_path = None
        if (env_var_name is not None):
            application_conf_path = os.environ.get(env_var_name, None)        
        if (application_conf_path):
            ignore_missing = False
        else:
            application_conf_path = os.path.join(resources_directory, default_config_name)
            ignore_missing = True
        
        return cls.load_config(application_conf_path, ignore_missing=ignore_missing)
    
    @classmethod
    def load_config(cls: Type[A], path: str, *, ignore_missing: bool = False) -> A:
        """
        Loads the given application config and merges the reference config into it.
        Applies root config offset if any.
        
        Args:
            path: `str`.
                A path to load config from.
                Path might be relative and absolute.
            
            ignore_missing: `bool`.
                Defines whether to raise an exception if config could not be loaded (`False`, default) or not (`True`).
        
        Returns:
            `MainConfig`
        """
        
        root_config_path: Optional[str] = cls._get_root_config_path()
        
        # application.conf
        # It is environment-dependent
        try:
            application_conf: ConfigTree = ConfigFactory.parse_file(path)
        except FileNotFoundError:
            if (ignore_missing):
                application_conf = ConfigTree()
            else:
                raise
        
        if (root_config_path is not None):
            application_conf = application_conf.get_config(root_config_path, ConfigTree())
        
        return cls.from_config(application_conf)
    
    @classmethod
    def reference_config(cls) -> ConfigTree:
        """
        Returns the `pyhocon.ConfigTree` representing the content of reference config.
        Reference config is searched in resources directories at
        current working directory (first) and module directory (next).
        Returns empty config if nothing found.
        Applies root config offset if any.
        
        Returns:
            `pyhocon.ConfigTree`
        """
        
        reference_config_name: str = cls._get_reference_config_name()
        module: str = cls._get_module()
        resources_directory: str = cls._get_resources_directory()
        root_config_path: Optional[str] = cls._get_root_config_path()
        
        # reference.conf
        # It is built inside package resources
        try:
            expected = os.path.join(resources_directory, reference_config_name)
            reference_conf_path: str = pkg_resources.resource_filename(module, expected)
            if (not os.path.isfile(reference_conf_path)):
                reference_conf_path = expected
            reference_conf: ConfigTree = ConfigFactory.parse_file(reference_conf_path)
        except FileNotFoundError:
            reference_conf = ConfigTree()
        else:
            del reference_conf_path, expected
        
        if (root_config_path is not None):
            reference_conf = reference_conf.get_config(root_config_path, ConfigTree())
        
        return reference_conf
    
    @classmethod
    def from_config(cls: Type[A], config: ConfigTree, **kwargs) -> A:
        """
        Same as the super-class' `dataclasses_config.Config.from_config()`,
        but merges the reference config.
        
        Optionally logs the config if such option was provided in
        `dataclasses_config.main_config()` parameters.
        """
        
        log: bool = cls._get_log()
        
        reference_conf = cls.reference_config()
        # The resulting config is the result of merging of reference config and application config
        conf = ConfigTree.merge_configs(reference_conf, config, copy_trees=True)
        
        if (log):
            logger.info(dump_config(conf))
        return super().from_config(conf, **kwargs)

@dataclass(frozen=Settings.frozen)
class ConfigWithRoot(Config, ABC):
    """
    Extension to the `dataclasses_config.Config` which
    allows `dataclasses_config.RelPath` post-processing.
    """
    
    root: Optional[Path]
    """ Optional. `str`. Current root directory which is used for `dataclasses_config.RelPath` instances. """
    
    def with_root(self: A, root: Optional[Path] = None, *, default_path: str = '.', **kwargs) -> A:
        """
        Creates a copy of this class, with all instances of
        `dataclasses_config.RelPath` transformed to their absolute path form.
        (But still remain instances of `dataclasses_config.RelPath`)
        
        Overrides `root` field in the resulting instance.
        Should work fine with the frozen dataclasses (potentially).
        
        The first available root is applied:
        1. `root` argument.
        2. `root` field.
        3. `default_path` argument.
        
        Args:
            root: `str`.
                A first-priority root to apply.
            
            default_path: `str`.
                A fallback root to apply.
                
                *Default: `.`*
            
            **kwargs: 
                Format arguments for `dataclasses_config.RelPath.apply()`
        
        Returns:
        
        """
        
        root: Path = (Option(root) or Option(self.root)).get_or_else(Path(default_path))
        
        kvs = dict()
        for f in FieldExtension.from_class(self, RelPath):
            v = getattr(self, f.base.name)
            if (isinstance(v, RelPath)):
                kvs[f.base.name] = v.apply(root, **kwargs)
        
        kvs.setdefault('root', root)
        return replace(self, **kvs)

del A

__all__ = \
[
    'main_config',
    
    'Config',
    'ConfigInvalidError',
    'ConfigMissingKeyError',
    'ConfigWithRoot',
    'FieldExtension',
    'MainConfig',
]
