import unittest
from eurekaroom import app


#######################################################################
class RouteTest(unittest.TestCase):

    ############################
    ### Run before each test ###
    ############################

    #----------------------------------------------------------------------
    def setUp(self):

        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        #    os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    def destroydisplay(self):
        self.app.open('/DestroyDisplay/', follow_redirects=True)

    #############
    ### Tests ###
    #############

    #----------------------------------------------------------------------
    def test_index_route(self):
        """
        Tests the / flask route.
        """

        indexResponse = self.app.open('/', follow_redirects=True)

        self.assertEqual(indexResponse.status_code, 200, msg="Index Route failed")

    #----------------------------------------------------------------------
    #def test_CreateNode(self):
    #    indexResponse = self.app.get('/CreateNode/', follow_redirects=True)
    #    self.destroydisplay()
    #    self.assertEqual(indexResponse.status_code, 200, msg="Node Created")

    #----------------------------------------------------------------------
    def test_404(self):
        """
        Test for in-valid route handling.
        """

        indexResponse = self.app.get('/blablabla', follow_redirects=True)

        self.assertEqual(indexResponse.status_code, 404, msg="Invalid route")

    #----------------------------------------------------------------------
    def test_invalid_image(self):
        """
        Test the route that displays images making sure that a non valid image is not played
        """
        from time import sleep
        self.app.open('/CreateNode/', follow_redirects=True)
        sleep(1)
        imageName = "doesNotExit.jpg"

        indexResponse = self.app.get('/DisplayPicture/{}/5'.format(imageName))
        #self.destroydisplay()
        self.assertEqual(indexResponse.status_code, 303, msg="Invalid image request.")

    #----------------------------------------------------------------------
    def test_image_display(self):
        """
        Test the route that displays images
        """

        from time import sleep
        self.app.open('/CreateNode/', follow_redirects=True)
        sleep(1)
        imageName = "meadow.jpg"     

        indexResponse = self.app.get('/DisplayPicture/{}/5'.format(imageName))

        #self.destroydisplay()
        self.assertEqual(indexResponse.status_code, 302, msg="Image request failed.")
        
#######################################################################

if __name__ == "__main__":
    unittest.main()