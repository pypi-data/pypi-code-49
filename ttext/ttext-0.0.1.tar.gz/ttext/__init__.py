# encoding=utf-8

from ttext.autolink import Autolink
from ttext.extractor import Extractor
from ttext.highlighter import HitHighlighter
from ttext.validation import Validation
from ttext.unicode import force_unicode

class TwitterText(object):
    def __init__(self, text):
        self.text = force_unicode(text) # this will get modified by some functions
        self.original_text = self.text # this never changes; use it as a fallback or for comparison
        self.has_been_linked = False
        self.tweet_length = None # gets changed by validation method
        self.tweet_is_valid = None # gets changed by validation method
        self.validation_error = None # gets changed by validation method
        
    def __unicode__(self):
        return self.text
        
    def __repr__(self):
        return self.__unicode__()
    
    @property
    def autolink(self):
        return Autolink(self.text, parent = self)
        
    @property
    def extractor(self):
        return Extractor(self.text)
        
    @property
    def highlighter(self):
        return HitHighlighter(self.text, parent = self)
        
    @property
    def validation(self):
        return Validation(self.text, parent = self)