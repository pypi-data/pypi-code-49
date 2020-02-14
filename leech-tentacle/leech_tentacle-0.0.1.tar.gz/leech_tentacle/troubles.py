class TentacleException(Exception):
    """ super class for exceptions specific to the tentacle.

    """
    @property
    def message(self):
        raise NotImplementedError()


class MalformedConfigException(TentacleException):
    """ exceptions to handle ExtractionConfig and SourceConfig data that does not conform to standard.

    """
    def __init__(self, malformed_component, config_data, malformation_type):
        self._malformed_component = malformed_component
        self._config_data = config_data
        self._malformation_type = malformation_type

    @property
    def message(self):
        return f'could not generate {self._malformed_component} from {self._config_data}, {self._malformation_type}'


class UnknownObjectException(TentacleException):
    """ exceptions to handle requests for objects or configurations that do not exist in the tentacle.

    """
    def __init__(self, object_type: str, object_value: str):
        self._object_type = object_type
        self._object_value = object_value

    @property
    def message(self):
        return f'{self._object_type} {self._object_value} is not registered with the tentacle'


class UnknownExtractionTypeException(UnknownObjectException):
    """ raised when an unregistered ExtractionType is invoked.

    """
    def __init__(self, extraction_type: str):
        super(UnknownExtractionTypeException, self).__init__('ExtractionType', extraction_type)


class UnknownExtractorException(UnknownObjectException):
    """ raised when an extraction is attempted with an unknown Extractor class.

    """
    def __init__(self, extractor_class: str):
        super(UnknownExtractorException, self).__init__('Extractor', extractor_class)


class UnknownProcessorException(UnknownObjectException):
    """ raised when an extraction is attempted with an unknown Processor class.

    """
    def __init__(self, processor_class: str):
        super(UnknownProcessorException, self).__init__('Processor', processor_class)


class UnknownIdSourceException(UnknownObjectException):
    """ raised when an extraction is attempted for an unknown IdSource.

    """
    def __init__(self, id_source: str):
        super(UnknownIdSourceException, self).__init__('IdSource', id_source)
