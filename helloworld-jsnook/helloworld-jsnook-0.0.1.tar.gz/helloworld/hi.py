"""Hello world program"""
class Main(object):
    """Class that returns string output"""
    def __init__(self, message='Hello, world!'):
        self.__message = message
    
    def __str__(self):
        return self.__message
print(Main())
