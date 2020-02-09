import logging
logger = logging.getLogger(__name__)

from flask import Flask, render_template, flash, redirect, url_for
from threading import Thread
from eurekaroom import EurekaNode

myapp = Flask(__name__)
myapp.config['SECRET_KEY'] = 'you-will-never-guess'

mynode = None
def init_node(NodeName):
    global mynode
    mynode = EurekaNode(NodeName)
    
#----------------------------------------------------------------------
# Create a default route
@myapp.route('/')
@myapp.route('/index/')
def index():
    """
    Display Main/Index page
    """

    try:
        isWindowRunning = mynode.getTkStatus()
    except:
        isWindowRunning = False

    images = mynode.getMedia("Image")
    videos = mynode.getMedia("Video")
    return render_template('index.html', title="Eurekaroom", name=mynode.name, image=images, video =videos, node=isWindowRunning)

@myapp.route("/DestroyDisplay/")
def destroyDisplay():

    with myapp.app_context():
        Thread(target=mynode.destroyDisplay).start()
    flash('Window destroyed on node "{}"'.format(mynode.name))
    
    return redirect(url_for('.index'))
#----------------------------------------------------------------------
@myapp.route("/CreateNode/")
def activateNode():
    """
    Creates the Root Window for the desired node.
    """

    with myapp.app_context():
        Thread(target= mynode.initDisplay ).start()

    flash('Window created on node "{}"'.format(mynode.name))

    return redirect(url_for('.index'))
    
#----------------------------------------------------------------------
@myapp.route("/ListBackground")
def listBackgrounds():
    media = mynode.getMedia("Image")
    return render_template('backgrounds.html', title="Eurekaroom", name=mynode.name, image=media)

#----------------------------------------------------------------------
@myapp.route("/SetBackground/<PictureID>")
def SetBackground(PictureID):
    """
    The function that sets the background for the main window.

    Paramater:
        PictureID (str): The name of the image to set as background.
    """
    
    logger.debug("<<< Set Background >>>")

    mediapath = mynode.getMediaPath(type='image', id=PictureID)

    if mediapath != PictureID:
        try:
            mynode.getTkStatus()
            try:    
                with myapp.app_context():
                    mynode.updateWallpaper(mediapath)
                flash('Background set to: "{}"'.format(PictureID))
            except Exception as err:
                flash('Background could not be set. "{}"'.format(err))
                logger.warning("Background could not be set. {}".format(err))
        except Exception as err:
            flash('Node "{}" is not active'.format(mynode.name))
            logger.warning('Node "{}" is not active'.format(mynode.name))

    return redirect(url_for('.index'))

#----------------------------------------------------------------------
@myapp.route("/ListMedia/")
def ListMedia():
    """
    This function renders a list of available media on the current node
    """

    images = mynode.getMedia("Image")
    videos = mynode.getMedia("Video")
    
    return render_template('listmedia.html', title="Eurekaroom", name=mynode.name, image=images, video =videos)

#----------------------------------------------------------------------
@myapp.route("/PlayVideo/<VideoID>/")
def Video(VideoID):
    """
    This function plays a video.

    Paramater:
        VideoID (str): the name of the desired video
    
    Returns:
        To the home/Index page
    """
    
    logger.info('<<< Play Video >>>')

    mediapath = mynode.getMediaPath(type='video', id=VideoID) 

    if mediapath != VideoID:
        try:
            mynode.getTkStatus()
            try:
                with myapp.app_context():
                    logger.info('Passing "{}" to playVideo()'.format(mediapath))
                    Thread(target=mynode.playVideo, args=(mediapath,)).start()
                flash('Now Playing, "{}", on node "{}"'.format(VideoID, mynode.name))
            except Exception as err:
                flash('Video can not be played, "{}", on node "{}": {}'.format(VideoID, mynode.name, err))
        except Exception as err:
            flash('Node "{}" is not active. Refresh home page and "Create Node"'.format(mynode.name))
            logger.warning('Node "{}" is not active'.format(mynode.name))

    return redirect(url_for('.index'))

#----------------------------------------------------------------------
@myapp.route("/DisplayPicture/<PictureID>/<time>")
def Picture(PictureID, time):
    """
    This function displays a picture for some length of time.

    Paramater: 
        PictureID (str): The file name of the image to show.
        time (int): The length of time in seconds to display the picture for.
    """

    logger.info("<<< Display Picture >>>")

    mediapath = mynode.getMediaPath(type='image', id=PictureID)

    returnCode = 302

    if mediapath != PictureID:
        try:
            mynode.getTkStatus()
            try:
                with myapp.app_context():
                    Thread(target=mynode.playImage, args=(mediapath, time)).start()
                flash('Displaying "{}" for "{}" seconds.'.format(PictureID,time))
            except Exception as err:
                flash('"{}" can not be shown, on node "{}". Due to: {}'.format(PictureID, mynode.name, err))
                logger.debug("Picture could not be displayed. {}".format(err))
        except Exception as err:
            flash('Node "{}" is not active'.format(mynode.name))
            logger.warning('Node "{}" is not active'.format(mynode.name))
            returnCode = 303
    else:
        flash('"{}" could not be found. Check spelling'.format(mediapath))
        returnCode = 303

    return redirect(url_for('.index'), code = returnCode)

#----------------------------------------------------------------------
@myapp.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

def launchapp(port, debug=False):
    myapp.run(debug=debug, host='0.0.0.0', port=port)
