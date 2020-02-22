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

def findall(path, fileExt='all'):
    """
    Get all files in a given path recursively.
    
    Arguments:
        path (str)
    
    Keyword Arguments:
        fileExt (str), default='all'
            'exe', 'jpg', etc.
    
    Returns:
        list
    """
    result = []
    if fileExt == 'all':
        for root, _, files in os.walk(path):
            for i in files:
                result.append(root.replace('\\','/') + '/' + i)
    else:
        for root, _, files in os.walk(path):
            for i in files:
                if i.lower().endswith(tuple(fileExt.split(' '))):
                    result.append(root.replace('\\','/') + '/' + i)
    return result
