# encoding: utf-8

from tempfile import NamedTemporaryFile
import os


class LaunchEditorException(Exception):     pass
class SystemException(Exception):           pass


def getEditor():

    editor = os.environ.get('EDITOR')

    if editor == None:

        raise LaunchEditorException('$EDITOR undefined')

    return editor


def system(cmd):
    
    r = os.system(cmd)
    
    if r != 0:
            
        raise SystemException('Editor failed with status {}'.format(r))


def launchEditor(**tmpFileArgs):
    '''
    @param **tmpFileArgs: extra args to NamedTemporaryFile(), e.g.
    
        prefix='pm-msg-', suffix='.txt',
         
    '''
    
    temp = NamedTemporaryFile(delete=False, dir='.', **tmpFileArgs)
    temp.close()

    try:
        
        system('{} {}'.format(getEditor(), temp.name))
        
        # Now that the editor has finished, let's reopen the file
        temp = open(temp.name)
        
        msg = temp.read()
        temp.close()
        
        return msg
    
    finally:

        # Deleting
        os.remove(temp.name)


