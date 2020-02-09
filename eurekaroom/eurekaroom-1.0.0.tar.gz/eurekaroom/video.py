#!/usr/bin/env python3

# Tested with Python 3.7.4, tkinter/Tk 8.6.9 on macOS 10.13.6 only.
__version__ = '19.07.29'  # mrJean1 at Gmail dot com

import logging
logger = logging.getLogger(__name__)

# Imports
from omxplayer.player import OMXPlayer
from os.path import expanduser, isfile
from time import sleep

#----------------------------------------------------------------------
class Player():
    """
    The window that deals with videos.
    """

    #----------------------------------------------------------------------
    def __init__(self, video, title=None, rotation=0.0, portrait=False):
        """
        Constructor for the Player class

        Parameters:
            video (str): The path leading to the video
            title (str): A name for the video frame.
            portrait (bool): Set to True adjust the vlc playback 
        
        TODO:
            rotation (float): The amount the video should be rotated
        """
        
        self.video = expanduser(video)
        self.rotation = rotation
        
        # Videp player arguments
        #args = []
        #args.append('--no-xlib')
        #args.append('--quiet')
        #if portrait:
        #    args.append('--monitor-par=16:9')
        ##if rotation > 0.0:
        ##    args.append("--rotate-angle={}".format(rotation))
        ##    args.append('--video-filter=rotate')
        #print("=========== Video args: {}".format(args))

        self.player = OMXPlayer(self.video)#, dbus_name='org.mpris.MediaPlayer2.omxplayer1')
        logger.info("OMXPlayer Started")
        sleep(2.5)
        self.player.pause()

    #----------------------------------------------------------------------   
    def destroy(self):
        """
        Closes, the Video player
        """

        #* Shutdown the Player
        logger.info("Quite OMXPlayer")
        self.player.quit()
        
    #----------------------------------------------------------------------
    def Play(self):

        #* Ensures that a valid video file is specified
        if isfile(self.video):

            #* Play Video
            self.player.play()
            logger.info("Playing OMXPlayer")