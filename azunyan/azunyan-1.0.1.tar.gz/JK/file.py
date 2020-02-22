import os



def find(path, itemType='all'):
    """
    List folders, files or both in a given path.
    
    Arguments:
        path (str)
    
    Keyword Arguments:
        itemType (str), default='all'
            'all', 'folder', 'file'
    
    Returns:
        list
    """
    result = []
    if itemType == 'all':
        for itemName in os.listdir(path):
            itemPath = path + '/' + itemName
            result.append(itemPath)
    elif itemType == 'folder':
        for itemName in os.listdir(path):
            itemPath = path + '/' + itemName
            if os.path.isdir(itemPath):
                result.append(itemPath)
    elif itemType == 'file':
        for itemName in os.listdir(path):
            itemPath = path + '/' + itemName
            if os.path.isfile(itemPath):
                result.append(itemPath)
    return result

def findall(path, fileExts=[]):
    """
    Get all files in a given path recursively.
    
    Arguments:
        path (str)
    
    Keyword Arguments:
        fileExts (list), default=[]
            ['exe', 'jpg']
            [] matches all files
    
    Returns:
        list
    """
    result = []
    if fileExts == []:
        for root, _, files in os.walk(path):
            for i in files:
                result.append(root.replace('\\','/') + '/' + i)
    else:
        for root, _, files in os.walk(path):
            for i in files:
                if os.path.splitext(i.lower())[-1][1:] in fileExts:
                    result.append(root.replace('\\','/') + '/' + i)
    return result
