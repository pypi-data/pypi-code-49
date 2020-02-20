# Video Write utility written by Pranjal Srivastava
# You can contact author on pranjal@codefire.in

#import needed packages
import cv2
import math

#declare the class to handle video writing
#this class encapsulates the video writer class from OpenCV. The video save from OpenCV
#fails silently for number of reasons, a few of which are:
#1. Mismatch in video frame size when video writer class was created Vs whats being saved
#2. Mismatch in file extension with which the file is being saved and video encoding
#Can be other reasons as well, most of the errors I made were generally with these 2 reasons
#Hence this class tries to take care of these 2 common scenarios. Also it adds a feature
#to save the video between a particular time frame. Look at documentation of save funtion
#for further details

class writeVideo:


	#Ctor that takes following arguments
	#filepath - path to save the video file
	#capture - video capture class object from OpenCV
	#currentframe - current frame of the video. This may not be passed when creating
	#	the object of the class. As most of the times the processing of video is not
	#	initiated when creating the object of this class.
	#fps - Required in you want to save the new video in a different fps than original video
	def __init__(self, filepath, capture, currentframe = None, fps = None ):
		
		# if current frame is passed, then we inialise the video capture size
		if currentframe is not None:
			self.frameHeight = currentframe.shape[1]
			self.frameWidth = currentframe.shape[0]
		else:
			self.frameHeight = -1
			self.frameWidth = -1
		# initialising the class level variables
		self.capture = capture
		self.filepath = filepath
		
		#get the file extension based on the path for saving video.
		ext = filepath.split('.')
		ext = ext[-1]
		
		# set the video format based on the file extension passed in the
		# to be saved file name. This will ensure that video is written
		# in the correct file format and OpenCV does capture the video
		# currently only support avi and mp4 formats
		self.formatStr = None
		if ext == "mp4":
			self.formatStr = "MP4V"
		elif ext == "avi":
			self.formatStr = "MJPG"
		
		self.fps = fps
		if self.fps is None:
			self.fps = capture.get(cv2.CAP_PROP_FPS)
		# if current frame of the video was passed then we initiate the Video writer
		self.writer = None
		if currentframe is not None:
			self.createWriter()
	
	# function used to create video writer object for the class
	def createWriter(self):
		if self.formatStr is not None:
			fourcc = cv2.VideoWriter_fourcc(*self.formatStr)
			self.writer = cv2.VideoWriter(self.filepath, fourcc, self.fps, (self.frameHeight, self.frameWidth), True)

	# This function implements video saving logic. Parameters:
	# currentframe: the current frame of video to be saved. If the video writer object
	# 		was not initialised in the ctor then it will be initialised here on the
	#		first call
	#starttime: Default value is 0. This indicates the start time for the video saving
	#		0 means the video needs to be saved from start
	#elapsedtime: Default value is -1. This indicates the lenght of video to be saved
	#		starting from starttime. -1 means full duration of video needs to be saved
	# Saving video with openCV is very error prone. This function handles the error if
	# there is any difference in the frame size, since when there is difference in frame
	# size, OpenCV simply stop saving the video.
	def save(self, currentframe, starttime = 0, elapsedtime = -1):
		
		#lazy initialisation of Video writer class
		if self.writer is None:
			if currentframe is not None:
				self.frameHeight = currentframe.shape[1]
				self.frameWidth = currentframe.shape[0]
				self.createWriter()
			else:
				return False
		# if elapsed time is -1 we need to set it to full time duration of the video
		# minus the start time
		if elapsedtime == -1 :
			frame_count =self.capture.get(cv2.CAP_PROP_FRAME_COUNT)
			fps = self.capture.get(cv2.CAP_PROP_FPS)
			elapsedtime = frame_count/fps * 1000
			elapsedtime = elapsedtime - starttime
		
		#get the current time in the video processing
		currenttime = self.capture.get(cv2.CAP_PROP_POS_MSEC)
		#check if we are in the correct time frame then we start saving the video
		if currenttime > starttime and currenttime <= starttime+elapsedtime :
			if self.frameHeight ==  currentframe.shape[1] and self.frameWidth == currentframe.shape[0]:
				if self.writer is not None :
					self.writer.write(currentframe)
					return True
			#return false if the video is not being saved
			return False
		return True
	
	# relese the Video Writer object allocaed.
	def release(self):
		if self.writer is not None :
			self.writer.release()
