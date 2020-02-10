from json import loads, dumps
from openhtf.plugs.user_input import UserInput

class FormUserInput(UserInput):
    def prompt(self, message, form_schema, *args, **kwargs):
        response = super(FormUserInput, self).prompt(message=self.pack_message(message, form_schema), *args, **kwargs)
        if response:
            response = self.unpack_response(response)
        return response
        
    def pack_message(self, message, form_schema):
        return dumps({
            'message': message,
            'form_schema': form_schema
        })
        
    def unpack_response(self, response):
        return loads(response)