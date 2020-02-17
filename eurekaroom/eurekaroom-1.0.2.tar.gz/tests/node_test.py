import unittest
from eurekaroom import init_mynode

from threading import Thread
from time import sleep


#######################################################################
class NodeTest(unittest.TestCase):

    node =None
    ############################
    ### Run before each test ###
    ############################

    #----------------------------------------------------------------------
    def setUp(self):
        init_mynode("TestNode")

    def init_tkinter(self):
        
        from eurekaroom import mynode
        self.node =  Thread(target= mynode.initDisplay )
        self.node.start()
        

        sleep(1)
    
    def close_tkinter(self):
        from eurekaroom import mynode
        mynode.destroyDisplay()
        self.node._delete()
    #############
    ### Tests ###
    #############

    def test_mynode_import(self):
        from eurekaroom import mynode
        self.assertIsNotNone(mynode)
    
    #def test_mynode_tkinter(self):
    #    
    #    self.init_tkinter()
    #    from eurekaroom import mynode
    #    #mynode.initDisplay()
    #    status = mynode.getTkStatus()
    #    self.close_tkinter()
    #    self.assertIsNotNone(status)
    #    
    #
   # def test_get_media_path(self):
   #     from eurekaroom import mynode
   #     media = 'meadow.jpg'
   #     mediaPath = mynode.getMediaPath(type='image', id=media)
   #     self.assertNotEqual(mediaPath, media)
#
   # def test_set_background(self):
   #     from eurekaroom import mynode
   #     media = 'meadow.jpg'
   #     mediaPath = mynode.getMediaPath(type='image', id=media)
   #     self.init_tkinter()
   #     try:
   #         mynode.updateWallpaper(mediaPath)
   #     except Exception as err:
   #         print(err)
   #     self.assertIsNotNone(mynode.getTkStatus())
   #     self.close_tkinter()

if __name__ == "__main__":
    unittest.main()