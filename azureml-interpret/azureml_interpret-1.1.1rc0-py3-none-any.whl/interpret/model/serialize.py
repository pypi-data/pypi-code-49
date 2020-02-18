# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines serialization API for models interfacing with interpretability SDK."""

import os
import logging
try:
    from azureml._logging import ChainedIdentity
except ImportError:
    from interpret_community.common.chained_identity import ChainedIdentity
from azureml.interpret.common.constants import LoggingNamespace, Serialization
from azureml.interpret.common.exceptions import SerializationException, MissingPackageException, \
    UnsupportedModelException

KERAS_MODEL_FILE = 'KERAS_MODEL_FILE'


def _is_keras_model(model):
    try:
        import tensorflow as tf
    except:
        tf = None
    return str(type(model)).endswith("keras.engine.sequential.Sequential'>") or \
        str(type(model)).endswith("keras.models.Sequential'>") or \
        str(type(model)).endswith("keras.engine.training.Model'>") or \
        (tf is not None and isinstance(model, tf.keras.Model))


class KerasSerializer(ChainedIdentity):
    """Serialize non-picklable keras models.

    Base class for serializing non-picklable models.
    """

    def __init__(self, **kwargs):
        """Serialize non-picklable keras models.

        Base class for serializing non-picklable models.
        """
        super(KerasSerializer, self).__init__(**kwargs)
        self._logger.debug('Initializing KerasSerializer')

    def save(self, model):
        """Influence how the model is saved.

        :return state: The state to be pickled.
        :rtype state: dict
        """
        if not _is_keras_model(model):
            raise UnsupportedModelException("Model not supported, must be a tf.keras.Model, "
                                            "keras.engine.sequential.Sequential, keras.models.Sequential, "
                                            "or keras.engine.training.Model")
        # Save the keras model to string
        import tempfile
        temp_filename = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
        model.save(temp_filename)
        with open(temp_filename, "rb") as temp_file:
            read_model = temp_file.read()
        os.remove(temp_filename)
        return {KERAS_MODEL_FILE: read_model}

    def load(self, state):
        """Influence how the model is loaded.

        :param state: The unpickled state to be loaded.
        :type state: dict
        :return model: The loaded model.
        :rtype model: tf.keras.Model
        """
        read_model = state[KERAS_MODEL_FILE]
        if isinstance(read_model, bytes):
            try:
                import tensorflow as tf
            except:
                err = "Tensorflow model cannot be loaded in environment without tensorflow package installed"
                raise MissingPackageException(err)
            # Load the keras model to string
            import tempfile
            temp_filename = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
            with open(temp_filename, "wb") as temp_file:
                temp_file.write(read_model)
            read_model = tf.keras.models.load_model(temp_file.name)
            os.remove(temp_filename)
        else:
            raise SerializationException("Failed to deserialize model, unexpected serialization format")
        return read_model

    def __getstate__(self):
        """Influence how KerasSerializer is pickled.

        Removes logger which is not serializable.

        :return state: The state to be pickled, with logger removed.
        :rtype state: dict
        """
        odict = self.__dict__.copy()
        del odict[Serialization.LOGGER]
        return odict

    def __setstate__(self, dict):
        """Influence how KerasSerializer is unpickled.

        Re-adds logger which is not serializable.

        :param dict: A dictionary of deserialized state.
        :type dict: dict
        """
        self.__dict__.update(dict)
        parent = logging.getLogger(LoggingNamespace.AZUREML)
        self._logger = parent.getChild(self._identity)
