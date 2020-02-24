import requests
import time
import os,sys
from redis import Redis
import json

#Timestamp converter
global r
r = time.ctime(time.time())

#redis connection instance
global rmaster

class daymark():
	#Function to initialize basic configuration
	def init(redis_end_point):
		"""
		Connects to redis master running inside the same kubernetes cluster in 'default' namespace
		"""
		if redis_end_point:
			redisEndPoint = redis_end_point
			rmaster = Redis(host = redisEndPoint, port=6379, db=0)
			pubsub = rmaster.pubsub()
			return rmaster
		else:
			sys.exit("No endpoint to connect")
	
	def logError(errorMsg, envVar, instance):
		"""
		function logs string to stdout in red & exits the code after publishing in redis
		"""	
		if errorMsg:
			print("\033[1;31;40m %s: %s \n " % (r, errorMsg) + "\n > Unfortunately Exiting the system!")
			rmaster = instance
			msg = {
				"id": envVar,
				"status": "FAILED",
				"message": errorMsg
			} 	#The message that will be streamed in redis
			streamMsg = json.dumps(msg)
			rmaster.publish('jobs', streamMsg)
			sys.exit(errorMsg)
		else:
			sys.exit(1)
	
	def logSuccessful(successMsg, envVar, instance):
		"""
		function logs string to stdout in green & exits the code after publishing in redis
		"""	
		if successMsg:
			print("\033[1;32;40m %s: %s \n" % (r, successMsg) + "> Successfully Exiting the system!")
			rmaster = instance
			msg = {
				"id": envVar,
				"status": "COMPLETED",
				"message": successMsg
			}	#The message that will be streamed in redis
			streamMsg = json.dumps(msg)
			rmaster.publish('jobs', streamMsg)
			sys.exit(successMsg)
		else:
			sys.exit(0)

	def logWarning(warningMsg):
		"""
		#function logs string to stdout in yellow
		"""
		print("\033[1;33;40m %s time = %s \n" % (warningMsg, r))
	
	def getProgress(file_processed_count, total_file_count):
		"""
		function returns the progress percentage
		"""	
		processedCount = file_processed_count
		totalCount = total_file_count
		per =  int(((processedCount/totalCount))*100) 	#Percentage
		return per	

	def showProgress(self, file_processed_count):
		"""
		function shows the progress
		"""
		processedCount = file_processed_count
		prog = '%d files (%.2f%%)' % (file_processed_count, self.percentDone())
		return prog

	def getEnvVar(name):
		"""
		Function to get environment variable
		"""
		envVar = name
		id = os.environ[envVar]
		return id

	def setProgress(key, value, instance):
		"""
		Set progress in redis-master
		"""		
		rmaster = instance
		envVar = key
		percentage = value
		msg = {
				"id": envVar,
				"progress": percentage
			}
		streamMsg = json.dumps(msg)
		rmaster.publish('progress', streamMsg)


