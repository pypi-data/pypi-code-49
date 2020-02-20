from json import JSONEncoder
from acronyms.acronym import Acronym

class AcronymJSONEncoder(JSONEncoder):
    def default(self, object): # pylint: disable=E0202
        if isinstance(object, Acronym):
            return {
                "shortform" : object.shortform,
                "longform" : object.longform }
        else:
            return JSONEncoder.default(self, object)
