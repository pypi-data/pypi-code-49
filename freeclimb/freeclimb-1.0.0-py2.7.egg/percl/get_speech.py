import json
from openapi_client.percl.grammar_type import GrammarType

class GetSpeech(object):
    openapi_types = {
        'action_url': 'str',
        'grammar_type': 'str',
        'grammar_file': 'str',
        'grammar_rule': 'str',
        'play_beep': 'bool',
        'no_input_timeout_ms': 'int',
        'recognition_timeout_ms': 'int',
        'confidence_threshold': 'float',
        'n_best_list_length': 'int',
        'sensitivity_level': 'float',
        'speech_complete_timeout_ms': 'int',
        'speech_incomplete_timeout_ms': 'int',
        'prompts': 'string'
    }

    attribute_map = {
        'action_url': 'action_url',
        'grammar_type': 'grammar_type',
        'grammar_file': 'grammar_file',
        'grammar_rule': 'grammar_rule',
        'play_beep': 'play_beep',
        'no_input_timeout_ms': 'no_input_timeout_ms',
        'recognition_timeout_ms': 'recognition_timeout_ms',
        'confidence_threshold': 'confidence_threshold',
        'n_best_list_length': 'n_best_list_length',
        'sensitivity_level': 'sensitivity_level',
        'speech_complete_timeout_ms': 'speech_complete_timeout_ms',
        'speech_incomplete_timeout_ms': 'speech_incomplete_timeout_ms',
        'prompts': 'prompts'
    }

    def __init__(self, action_url, grammar_file):
        self._action_url = action_url
        self._grammar_file = grammar_file
        grammar_type_instance = GrammarType('')
        self._grammar_type = grammar_type_instance.URL
        self._grammar_rule = None
        self._play_beep = None
        self._no_input_timeout_ms = None
        self._recognition_timeout_ms = None
        self._confidence_threshold = None
        self._n_best_list_length = None
        self._sensitivity_level = None
        self._speech_complete_timeout_ms = None
        self._speech_incomplete_timeout_ms = None
        self._prompts = None

    @property
    def action_url(self):
        return self._action_url

    @property
    def grammar_type(self):
        return self._grammar_type

    @property
    def grammar_file(self):
        return self._grammar_file

    @property
    def grammar_rule(self):
        return self._grammar_rule

    @property
    def play_beep(self):
        return self._play_beep
    
    @property
    def no_input_timeout_ms(self):
        return self._no_input_timeout_ms

    @property
    def recognition_timeout_ms(self):
        return self._recognition_timeout_ms
 
    @property
    def confidence_threshold(self):
        return self._confidence_threshold

    @property
    def n_best_list_length(self):
        return self._n_best_list_length

    @property
    def sensitivity_level(self):
        return self._sensitivity_level

    @property
    def speech_complete_timeout_ms(self):
        return self._speech_complete_timeout_ms

    @property
    def speech_incomplete_timeout_ms(self):
        return self._speech_incomplete_timeout_ms

    @property
    def prompts(self):
        return self._prompts

    @action_url.setter
    def action_url(self, action_url):
        self._action_url = action_url

    @grammar_type.setter
    def grammar_type(self, grammar_type):
        grammar_type_instance = GrammarType('')
        try:
            grammar_type_code = getattr(grammar_type_instance, grammar_type.upper())
            self._grammar_type = grammar_type_code
        except AttributeError:
            raise ValueError("grammer_type must be set to one of the following values: 'URL' or 'BUILTIN'. Default is 'URL'. A value of 'URL' indicates the grammarFile attribute specifies a URL that points to the grammar file. A value of 'BUILTIN' indicates the grammarFile attribute specifies the name of one of the platform built-in grammar files.")

    @grammar_file.setter
    def grammar_file(self, grammar_file):
        self._grammar_file = grammar_file

    @grammar_rule.setter
    def grammar_rule(self, grammar_rule):
        self._grammar_rule = grammar_rule

    @play_beep.setter
    def play_beep(self, play_beep):
        self._play_beep = play_beep

    @no_input_timeout_ms.setter
    def no_input_timeout_ms(self, no_input_timeout_ms):
        self._no_input_timeout_ms = no_input_timeout_ms

    @recognition_timeout_ms.setter
    def recognition_timeout_ms(self, recognition_timeout_ms):
        self._recognition_timeout_ms = recognition_timeout_ms

    @confidence_threshold.setter
    def confidence_threshold(self, confidence_threshold):
        self._confidence_threshold = confidence_threshold

    @n_best_list_length.setter
    def n_best_list_length(self, n_best_list_length):
        self._n_best_list_length = n_best_list_length

    @sensitivity_level.setter
    def sensitivity_level(self, sensitivity_level):
        self._sensitivity_level = sensitivity_level

    @speech_complete_timeout_ms.setter
    def speech_complete_timeout_ms(self, speech_complete_timeout_ms):
        self._speech_complete_timeout_ms = speech_complete_timeout_ms
    
    @speech_incomplete_timeout_ms.setter
    def speech_incomplete_timeout_ms(self, speech_incomplete_timeout_ms):
        self._speech_incomplete_timeout_ms = speech_incomplete_timeout_ms

    @prompts.setter
    def prompts(self, prompts):
        self._prompts = prompts
        
    def to_dict(self):
        as_dict = {
            self.__class__.__name__ : {
                'action_url': self._action_url,
                'grammar_type': self._grammar_type,
                'grammar_file': self._grammar_file,
                'grammar_rule': self._grammar_rule,
                'play_beep': self._play_beep,
                'no_input_timeout_ms': self._no_input_timeout_ms,
                'recognition_timeout_ms': self._recognition_timeout_ms,
                'confidence_threshold': self._confidence_threshold,
                'n_best_list_length': self._n_best_list_length,
                'sensitivity_level': self._sensitivity_level,
                'speech_complete_timeout_ms': self._speech_complete_timeout_ms,
                'speech_incomplete_timeout_ms': self._speech_incomplete_timeout_ms,
                'prompts': self._prompts
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
