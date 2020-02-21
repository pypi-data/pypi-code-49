import re

mock_response = '{"Response":"No Response Set"}'
mock_path = ''
mock_method = ''
mock_request = ''

def mock_call(method,path,request):
    """
    Handles local testing, not intended to be called directly.
    """
    global mock_method 
    mock_method = method
    global mock_path
    mock_path = path
    pat = re.compile('"number":"([0-9]+)"')
    matches = pat.findall(request)
    if matches.count('4000100011112224') != len(matches):
        raise Exception('Please only use test card 4000100011112224 with the mockhandler')
    global mock_request
    mock_request = request
    global mock_response
    return mock_response
    