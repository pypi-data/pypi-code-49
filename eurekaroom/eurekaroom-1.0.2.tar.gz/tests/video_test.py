import unittest
import tkinter as Tk
from eurekaroom import Player


#######################################################################
class PlayerTest(unittest.TestCase):

    #----------------------------------------------------------------------
    def test_video_frame_creation(self):
        """
        Tests the video.Player class  assignment to an identifier.
        """

        player = Player(parent=Tk.Tk(), video=".media/Videos/Planet_Success.mp4")

        self.assertIsInstance(player, Player, msg="Instance of class")

    #----------------------------------------------------------------------
    def test_video_is_playing(self):
        
        player = Player(parent=Tk.Tk(), video=".media/Videos/Planet_Success.mp4")
        Not_Playing = player.IsPlaying()
        player.Play()

        self.assertNotEqual(player.IsPlaying, Not_Playing)
        
    #----------------------------------------------------------------------
    def test_non_video_dosnt_play(self):
       
       player = Player(parent=Tk.Tk(), video=".media/Videos/Non_Existent.mp4")
       Not_Playing = player.IsPlaying()
       player.Play()

       self.assertIs(player.IsPlaying(), Not_Playing)

    #----------------------------------------------------------------------
    def test_player_closed(self):
        """
        Test to make sure the Tk Frame that contained the vlc player closes
        """
        player = Player(parent=Tk.Tk(), video=".media/Videos/Planet_Success.mp4")
        player.closePlayer()
        self.assertFalse(isinstance(player.videopanel, Tk.Frame) )

#######################################################################

if __name__ == "__main__":
    unittest.main()