import tkinter as Tk
import os
import sys
import logging
logger = logging.getLogger(__name__)
from .video import Player
from eurekaroom import config

# For Image display
from PIL import Image, ImageTk, ImageOps
from os.path import expanduser
from time import sleep


NODE_STATUS_QUICK = 0
NODE_STATUS_NORMAL = 1
NODE_STATUS_DETAILED = 2
NODE_STATUS = {
    'QUICK': NODE_STATUS_QUICK,
    'NORMAL': NODE_STATUS_NORMAL,
    'DETAILED': NODE_STATUS_DETAILED,
}


class EurekaNode():
    """
    A class that ties all the room resources and nodes together and provides access through the API
    """

    name = None
    display = None
    audio = None
    rotation = 0
    player = None
    window=None
    portrait = False

    ####################
    ## Initialization ##
    ####################

    #----------------------------------------------------------------------
    def __init__(self, name, rotation=0):

        self.name = name
        self.rotation = rotation

    #----------------------------------------------------------------------
    def initDisplay(self, orientation=0):
        """
        Initializes the display window for visuals. Create the Parent class
        """

        ####TODO: initialize the video with accounting for 'orientation' value
        ####?: 'orientation' value should be passed to playVideo()

        # Set local disply so that remote execution does not confuse the target DISPLAY
        if not 'DISPLAY' in os.environ:
            os.environ['DISPLAY'] = ':0.0'
        logging.debug("os.environ['DISPLAY']={}".format(os.environ['DISPLAY']))

        # Create the TK-Player window root 
        try:
            self.display = Tk.Tk()
        except Exception as err:
            ####TODO: add better exception handling of display initialization failure
            logging.error(err)
            sys.exit(1)
        
        self.display.configure(bg="black")
        self.display.attributes("-fullscreen", True)

        self.window = Tk.Label(self.display)
        self.window.configure(bg="black")
        self.window.pack(fill=Tk.BOTH, expand=1)

        if self.window.winfo_width() < self.window.winfo_height():
            self.portrait = True
        
        self.display.mainloop()

    ###########
    ## Image ##
    ###########

    #----------------------------------------------------------------------
    def createPhotoImage(self, displayWindow, imagepath):
        """
        Transform photo

        Paramaters:
            displayWindow (Tk widget)
            imagepath (str)
        
        Return:
            A resized image.
        """

        load = Image.open(imagepath)
        
        screenWidth = int(displayWindow.winfo_width())
        screenHeight = int(displayWindow.winfo_height())
        
        # resize and display the part of the picture that spans the width and the middle 1/3 of the screens height (Used for rotated displays)
        if (screenWidth < screenHeight):
            load = ImageOps.fit(load,(screenWidth, int(screenHeight/3) ), Image.ANTIALIAS)
            logger.debug("Image set to display in Portrait Mode.")
        else:
            load = ImageOps.fit(load,(screenWidth, screenHeight), Image.ANTIALIAS)
            logger.debug("Image set to display in Landscape Mode.")
        
        return load

    #----------------------------------------------------------------------
    def updateWallpaper(self, imagepath):
        """
        This function sets the wallpaper on the device 

        Paramiter:
            imagepath (str): The path to an image
        """

        imagepath = expanduser(imagepath)
        load = self.createPhotoImage(self.window, imagepath)
        photo = ImageTk.PhotoImage(load)
        self.window.config(image=photo)
        self.window.image=photo

    #----------------------------------------------------------------------
    def playImage(self, imagepath, time):
        """
        This function displays an image to the default screen on the device it is running on
        
        Paramiter:
            imagepath (str): The path to an image
        """
        
        self.ClosePlayer()

        self.player = Tk.Label(self.window)
        self.player.configure(bg='black')
        self.player.pack(fill=Tk.BOTH, expand=1)

        imagepath = expanduser(imagepath)
        load = self.createPhotoImage(self.player, imagepath)
        
        photo = ImageTk.PhotoImage(load)
        self.player.config(image=photo)
        self.player.image=photo

        sleep(int(time))
        self.player.destroy()

    ###########
    ## Video ##
    ###########

    #----------------------------------------------------------------------
    def ClosePlayer(self):
        """
        Emidiatly remove video/picture from the screen
        """
        if self.player:
            self.player.destroy()

    #----------------------------------------------------------------------
    def playVideo(self, videopath):
        """
        Set and play a video

        Parameters:
            videopath (string): The video to be played
        """

        self.ClosePlayer()

        self.player = Player(video=videopath, rotation=self.rotation, portrait=self.portrait)
        self.player.Play()

    ###########
    ## Audio ##
    ###########

    #----------------------------------------------------------------------
    def initAudio(self):
        """
        Initializes the audio output stream
        """
        ####TODO: add audio initialization code
        pass

    #----------------------------------------------------------------------
    def playAudio(self, audiopath):
        """
        This function plays an audio file on the device it is running on
        """
        ####TODO: check that the image ixists and is accessible
        pass
    
    ###########
    ## Misc. ##
    ###########
    
    #----------------------------------------------------------------------
    def end_callback(self, event):
        print('End of media stream (event %s)' % event.type)
        logging.debug("End of media stream (event {})".format(event.type))
        sys.exit(0)

    #----------------------------------------------------------------------
    def destroyDisplay(self):
        """
        Closes the main application window.
        """
        self.window.destroy()
        self.display.destroy()

    #----------------------------------------------------------------------
    def reset(self):
        """
        Resets the hardware and variable state of this device (not to be considerd a reboot, however)
        """
        pass

    ################
    ## Get Func's ##
    ################

    #----------------------------------------------------------------------
    def getTkStatus(self):
        """
        Gets the status of the main application window.
        """

        return self.display.wm_state()

    #----------------------------------------------------------------------
    def getstatus(self, level=NODE_STATUS_NORMAL):
        """
        The Function to get the status of a node

        Parameters:
            level (custom):
                NODE_STATUS_QUICK 
                NODE_STATUS_NORMAL 
                NODE_STATUS_DETAILED 

        Returns:
            A status of the running 'node' based on the detail 'level' requested
        """
        if level==NODE_STATUS_QUICK:
            status = True
        elif level==NODE_STATUS_NORMAL:
            status = {
                'state': 'running',
                'description':'running with no errors'
            }
        else:
            #### TODO: add complete dynamic status response for the detailed request
            status = {
                'state': 'running',
                'description':'running with no errors',
                'name': self.name,
                # etc...
            }

        return status

    #----------------------------------------------------------------------
    def getMedia(self, type="All"):
        """
        This function returns the media listed in the config.ini

        Paramaters:
            type (str): ("All", "Video", "Audio", "Image")
        
        Returns:
            A Dictionary containing the requested media names.
        """

        if type == "All":
            media = dict(config.parser.items('video'))
            media.update(config.parser.items('image'))
        elif type == "Video":
            media = dict(config.parser.items('video'))
        elif type == "Image":
            media = dict(config.parser.items('image'))
        
        return media

    #----------------------------------------------------------------------
    def getMediaPath(self, type='', id=''):
        """
        This Functions provides the full path to a media file

        Paramater:
            type (str) : The type of media: image, video, audio
            id (str) : The name of the file

        Return:
            The full path including the file name.
        """

        try:
            media = dict(config.parser.items(section=type))[id]
            logger.info("`media` set to {}".format(media))
        except Exception as err:
            logger.warning('"{}", "{}" not found, "{}"'.format(type, id, err))
            media = id

        return media

####################################################################
