import mimetypes
from os import path

from framework.httpexceptions import HttpNotFoundException

class StaticHandler():
    """StaticHandler handles request to static files and serves these files.
    """
    
    def __init__(self, folder, fallback_file = None):
        """Create new StaticHandler, point it to the base folder to search files in
        """
        self._folder = folder
        self._fallback_file = fallback_file
        
        # If the path doesn't end with an "/" add one.
        if not self._folder.endswith("/"):
            self._folder += "/"
    
    def handle(self, state):
        """Handles a request to a static file. Serves the file
        """
        (request, response, session) = state.unfold()
        
        try:
            # Try to open the file in binary mode
            if self._fallback_file and not path.isfile(self._folder + request.path_info):
                full_path = self._folder + self._fallback_file
            else:
                full_path = self._folder + request.path_info

            file = open(full_path, 'rb')
            
            # Try to guess the content type
            response.content_type = mimetypes.guess_type(full_path)[0]

            # Set a default content type if no guess was found
            if not response.content_type:
                response.content_type = "application/octet-stream"
            
            # We write binary data so return no charset
            response.charset = None
            
            # Read the contents of the file to the body of the response
            response.body = file.read()
        except:
            raise HttpNotFoundException()
        else:
            file.close()
                
        return state