# Author: Craig Hickman
# Contact: craig.hickman@ukaea.uk

# Doc String
'''A package for creating interactive command line prompts from any given class'''

from PyInquirer import prompt
from pprint import pprint
import inspect
from inspect import signature
import json

class ObjTerm:
    """ An interactive prompt to call methods of any given object.
    
    Use `start()` to bring up the promp
    """

    # A dictionary of function names and their associated callable, of the object passed into the ObjTerm constructor
    __methodMap = dict()
    
    # Keep track of the number of args for a callableMethod
    __methodSigMap= dict()
    
    # A javascript object used by the PyInquirer prompt
    __exeMethodQuestions =  {
            'type': 'list',
            'name': 'methodName',
            'message': 'Choose a callableMethod to execute',
            'choices': [
            ]
        }
    
    __m_kill = False
    
    def __init__(self, object):
        """ An interactive prompt to call methods of any given object.
        
        `Use start() to bring up the prompt`
        
        @param self: auto captured reference to self
        @param object: The object to create a interactive terminal for
        """
        # Create a local copy of the object. Because this is python, its actually a refference so this is okay
        self.__m_object = object   
        
        # Create a list of methods that the object provides
        attrs = (getattr(self.__m_object, name) for name in dir(self.__m_object))
        allMethods = filter(inspect.ismethod, attrs)
        
        # Ignore the ctor and dtor #todo turn this into a filter
        # and build the MethodMap
        for callableMethod in allMethods:
            if(callableMethod.__name__ != '__init__') and (callableMethod.__name__ != '__del__'):
                self.__methodMap[callableMethod.__name__] = callableMethod
                sig = signature(callableMethod)
                self.__methodSigMap[callableMethod.__name__] = sig
        
        self.__methodMap['Exit'] = self.__kill
        exitSig = signature(self.__kill)
        self.__methodSigMap['Exit'] = exitSig
        
        # build the json object used by the PyInquirer prompt
        for methodNameKey in self.__methodMap:
            self.__exeMethodQuestions['choices'].append(methodNameKey)
    
    def markDisabled(self, functionName):
        """ Mark the `functioName` function as disabled"""
        methodNameMap = {'name' : functionName,
                        'disabled' : 'Unavailable at this time'}
        try:
            self.__exeMethodQuestions['choices'].remove(functionName)    
            self.__exeMethodQuestions['choices'].append(methodNameMap)
        except Exception as e:
            print(str(e) + " : No function named " + functionName)

    #ToDo the impl of this
    def markEnabled(self, functionName):
        """ Mark the `functioName` function as disabled"""
        methodNameMap = {'name' : functionName,
                        'disabled' : 'Unavailable at this time'}
        try:
            self.__exeMethodQuestions['choices'].remove(methodNameMap)    
            self.__exeMethodQuestions['choices'].append(functionName)
        except TypeError as e:
            print(str(e) + " : i.e Method is allready enabled")
        except ValueError as e:
            print(str(e) + " : i.e no function named " + functionName + ", or " + functionName + " is allready enabled")
            
    def __kill(self):
        """ internal function pointed to by the prompt `Exit` command
        """
        self.__m_kill = True
    
    def start(self):
        """ Begins the terminal. Blocks the thread of execution untill `Exit` is called from the terminal,
        or `ctrl-c` is detected
        """
        
        try:
            while(self.__m_kill == False):
                self.__prompt()
        except KeyboardInterrupt:
            print('Goodbye!')
    
    def __prompt(self):
        """ Internal function used to prompt the user for an input, and use the result to call a function
        """
        
        answers = prompt(self.__exeMethodQuestions)
        exe = self.__methodMap[answers['methodName']]
        sig = self.__methodSigMap[answers['methodName']]
        
        # If no parameters, just execute
        if (len(sig.parameters)) == 0:
            exe()
            return 0
        
        paramNames = [ v for v in sig.parameters.keys() ]
        
        #If paramters, create sub prompt
        paramQuestions = []
        for x in range(len(sig.parameters)):
            
            paramQuestionsInner = {
                'type': 'input',
                'name': 'param' + str(x),
                'message': 'Enter parameter ' + str(paramNames[x])
            }
            paramQuestions.append(paramQuestionsInner)

        answers = prompt(paramQuestions)
        
        # Execute with args
        list_values = [ v for v in answers.values() ]
        # Split list into positional args
        exe(*list_values)
        return 0