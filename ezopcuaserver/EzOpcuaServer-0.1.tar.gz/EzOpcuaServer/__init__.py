from opcua import Server, ua
from signalslot import Signal

class EzOpcuaServer:
    def __init__(self):
        self.__server = Server()
    
    def setEndpoint(self, endpoint):
        self.__server.set_endpoint(endpoint)
        
    def registerNamespace(self, uri):
        self.idx = self.__server.register_namespace(uri)
    
    def addObject(self, path):
        
        parts = path.split('/')
        
        if len(parts) == 1:
            self.__server.get_objects_node().add_object(self.idx, parts)
        else: 
            objectName = parts.pop() #last in list

            objects = self.__server.get_objects_node()
            
            lastNode = objects
            for part in parts:
                #check if folder allready exists
                try:
                    #print("looking for " + str(self.idx) + ":" + part)
                    lastNode = lastNode.get_child(str(self.idx) + ":" + part)
                except:
                    #if not, make that folder
                    #print(part + " not found, making folder")
                    lastNode = lastNode.add_folder(self.idx, part)
            
            #add the object 
            lastNode.add_object(self.idx, objectName)
    
    signals = {}
    
    def addMethod(self, path):
        
        parts = path.split('/')
        
        if len(parts) == 1:
            signal = Signal()
            self.signals[path] = signal
            self.__server.get_objects_node().add_method(self.idx, parts, lambda x: signal.emit())
            return signal
            
        else: 
            objectName = parts.pop() #last in list

            objects = self.__server.get_objects_node()
            
            #build path
            lastNode = objects
            for part in parts:
                #check if folder allready exists
                try:
                    #print("looking for " + str(self.idx) + ":" + part)
                    lastNode = lastNode.get_child(str(self.idx) + ":" + part)
                except:
                    #if not, make that folder
                    #print(part + " not found, making folder")
                    lastNode = lastNode.add_folder(self.idx, part)
            
            #add method
            signal = Signal()
            self.signals[path] = signal
            
            lastNode.add_method(self.idx, objectName, lambda x: signal.emit())
            return signal
    
    def setAvailability(self, path, availability):
        parts = path.split('/')
        objects = self.__server.get_objects_node()
            
        #get path
        lastNode = objects
        for part in parts:
            try:
                lastNode = lastNode.get_child(str(self.idx) + ":" + part)
            except:
                print("Error " + path + " does not exist")
        
        lastNode.set_attribute(ua.AttributeIds.Executable, ua.DataValue(availability))

    def getAvailability(self, path):
        parts = path.split('/')
        objects = self.__server.get_objects_node()
            
        #get path
        lastNode = objects
        for part in parts:
            try:
                lastNode = lastNode.get_child(str(self.idx) + ":" + part)
            except:
                print("Error " + path + " does not exist")
        
        return lastNode.get_attribute(ua.AttributeIds.Executable)
        
    def setUserAvailability(self, path, availability):
        parts = path.split('/')
        objects = self.__server.get_objects_node()
            
        #get path
        lastNode = objects
        for part in parts:
            try:
                lastNode = lastNode.get_child(str(self.idx) + ":" + part)
            except:
                print("Error " + path + " does not exist")
        
        lastNode.set_attribute(ua.AttributeIds.UserExecutable, ua.DataValue(availability))
    
    
    def getUserAvailability(self, path):
        parts = path.split('/')
        objects = self.__server.get_objects_node()
            
        #get path
        lastNode = objects
        for part in parts:
            try:
                lastNode = lastNode.get_child(str(self.idx) + ":" + part)
            except:
                print("Error " + path + " does not exist")
        
        return lastNode.get_attribute(ua.AttributeIds.UserExecutable)
            
    def start(self):
        self.__server.start()