"""
Unpublished work.
Copyright (c) 2018 by Teradata Corporation. All rights reserved.
TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

Primary Owner: karthik.thelukuntla@teradata.com
Secondary Owner:

This file is for providing user configurable options.
"""
from teradataml.common.exceptions import TeradataMlException
from teradataml.common.messages import Messages
from teradataml.common.messagecodes import MessageCodes


class _ConfigureSuper(object):

    def __init__(self):
        pass

    def _SetKeyValue(self, name, value):
        super().__setattr__(name, value)

    def _GetValue(self, name):
        return super().__getattribute__(name)


def _create_property(name):
    storage_name = '_' + name

    @property
    def prop(self):
        return self._GetValue(storage_name)

    @prop.setter
    def prop(self, value):
        self._SetKeyValue(storage_name, value)

    return prop


class _Configure(_ConfigureSuper):
    """
    Options to configure database related values.
    """

    default_varchar_size = _create_property('default_varchar_size')
    column_casesensitive_handler = _create_property('column_casesensitive_handler')
    vantage_version = _create_property('vantage_version')

    def __init__(self, default_varchar_size=1024, column_casesensitive_handler = False, vantage_version="vantage1.1"):
        """
        PARAMETERS:
            default_varchar_size:
                It is required to mention size of varchar datatype in Teradata Vantage, the default size is 1024.
                User can configure this parameter using options.
                Types: int
                Example:
                    teradataml.options.configure.default_varchar_size = 512

            column_casesensitive_handler:
                Sets the value of the option "column_casesensitive_handler" to True or False.
                One should set this to True, when ML Engine connector property is CASE-SENSITIVE, else
                set to False, which is CASE-INSENSITIVE.
                Types: bool
                Example:
                    # When ML Engine connector property is CASE-SENSITIVE, set this parameter to True.
                    teradataml.options.configure.column_casesensitive_handler = True
        """
        super().__init__()
        super().__setattr__('default_varchar_size', default_varchar_size)
        super().__setattr__('column_casesensitive_handler', column_casesensitive_handler)
        super().__setattr__('vantage_version', vantage_version)

        # internal configurations
        # These configurations are internal and should not be
        # exported to the user's namespace.
        super().__setattr__('_validate_metaexpression', False)

    def __setattr__(self, name, value):
        if hasattr(self, name):
            if name == 'default_varchar_size':
                if not isinstance(value, int):
                    raise TeradataMlException(Messages.get_message(MessageCodes.UNSUPPORTED_DATATYPE, name,
                                                                   'int'),
                                              MessageCodes.UNSUPPORTED_DATATYPE)
                if value <= 0:
                    raise TeradataMlException(Messages.get_message(MessageCodes.TDMLDF_POSITIVE_INT, name, "greater than"),
                                              MessageCodes.TDMLDF_POSITIVE_INT)
            elif name == 'column_casesensitive_handler' or name == '_validate_metaexpression':
                if not isinstance(value, bool):
                    raise TeradataMlException(Messages.get_message(MessageCodes.UNSUPPORTED_DATATYPE, name,
                                                                   'bool'),
                                              MessageCodes.UNSUPPORTED_DATATYPE)
            elif name == 'vantage_version':
                if not isinstance(value, str):
                    raise TeradataMlException(Messages.get_message(MessageCodes.UNSUPPORTED_DATATYPE, name,
                                                                   'str'),
                                              MessageCodes.UNSUPPORTED_DATATYPE)
                valid_versions = ['vantage1.0', 'vantage1.1']
                value = value.lower()
                if value not in valid_versions:
                    raise TeradataMlException(Messages.get_message(MessageCodes.INVALID_ARG_VALUE,
                                                                   value,
                                                                   name,
                                                                   "a value in {}".format(valid_versions)),
                                              MessageCodes.INVALID_ARG_VALUE)

            super().__setattr__(name, value)
        else:
            raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, name))


configure = _Configure()
