 
class ClassMaker:
    '''A helper class for building a MetaClass.
    Programaticly add functions, variables, and lines to the initilaiser,
    and then get an instance of the class with makeClass().
    The initialser of the resulting class must be called manually with __init__()'''
    
    __classInitFunctionList = []
    
    def __init__(self):
        '''The initialiser sets the default class name of the class to be built as \'UnNamedClass\''''
        self.__attr = {}
        self.__name = "UnNamedClass"
  
    def setClassName(self, name):
        '''Set the classname of the class that will be created'''
        self.__name = name
    
    def addFunctionToInitialiser(self, callable):
        '''Add a function that will be called during the initialiser of the class that will be built'''
        self.__classInitFunctionList.append(callable)
    
    def __classInit(self):
        '''A private function used by the class to be builts initialiser'''
        for f in self.__classInitFunctionList:
            f()
    
    def addFunction(self, functionName, callable):
        '''Add a function to the class to be built'''
        self.__attr[functionName] = lambda : callable()
        
    def addFunction_1arg(self, functionName, callable):
        '''Add a function to the class to be built'''
        self.__attr[functionName] = lambda arg : callable(arg)
        
    def addFunction_2arg(self, functionName, callable):
        '''Add a function to the class to be built'''
        self.__attr[functionName] = lambda arg1, arg2 : callable(arg1, arg2)
  
    def addVariable(self, variableName, defaultValue):
        '''Add a variable to the class to be built'''
        self.__attr[variableName] = defaultValue

    def makeClass(self):
        '''Make the class. Only call this once the functions and variables have been added.'''
        self.addFunction('__init__', self.__classInit)
        Meta = type(self.__name, (), self.__attr)
        return Meta
    
if __name__ == "__main__":
    
    maker = ClassMaker()
    maker.setClassName('Foo')
    maker.addFunction('bar', lambda : print("Hello World!"))
    maker.addFunction_1arg('echo', lambda arg : print(arg))
    maker.addFunction_2arg("sum", lambda arg1, arg2 : print(arg1 + arg2))
    maker.addFunction('ret42', lambda : 42)
    maker.addVariable('baz', 5)
    
    maker.addFunctionToInitialiser(lambda : print("Initialising"))
    maker.addFunctionToInitialiser(lambda : print("!"))

    foo = maker.makeClass()
    foo.__init__()
    foo.bar()
    foo.echo(7)
    foo.sum(9,1)
    print(foo.ret42())
    print(foo.baz)