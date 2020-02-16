







class MountInfo(object):

	def __init__(self, device:str, mountPoint:str, fsType:str, options:dict):
		self.__device = device
		self.__mountPoint = mountPoint
		self.__fsType = fsType
		self.__options = options
	#

	def __eq__(self, other):
		if isinstance(other, MountInfo):
			return self.__mountPoint == other.__mountPoint
		elif isinstance(other, str):
			return self.__mountPoint == other
		else:
			raise TypeError()
	#

	def __ne__(self, other):
		if isinstance(other, MountInfo):
			return self.__mountPoint != other.__mountPoint
		elif isinstance(other, str):
			return self.__mountPoint != other
		else:
			raise TypeError()
	#

	#
	# Is this a regular device like "/dev/sda1" or "/dev/nvme0n1p3" or is this something like "proc" or "udev"?
	#
	@property
	def isRegularDevice(self) -> bool:
		return self.__device.startswith("/") and not self.__mountPoint.startswith("/snap/")
	#

	@property
	def isSnapDevice(self) -> bool:
		return self.__mountPoint.startswith("/snap/")
	#

	@property
	def isNetworkDevice(self) -> bool:
		return self.__device.find(":/") > 0
	#

	@property
	def isReadOnly(self) -> bool:
		return "ro" in self.__options
	#

	#
	# The device. This is something like "/dev/sda", "/dev/nvme0n1p3", "proc" or "udev".
	#
	@property
	def device(self) -> str:
		return self.__device
	#

	#
	# The mount point. This is something like "/", "/sys/fs/cgroup/perf_event" or "/snap/core/8213".
	#
	@property
	def mountPoint(self) -> str:
		return self.__mountPoint
	#

	#
	# The type of the file system used. This is something like "cgroup", "tmpfs", "proc", "squashfs" or "ext4".
	#
	@property
	def fsType(self) -> str:
		return self.__fsType
	#

	#
	# THe mount options. This is something like "rw,nodev,relatime,fd=32,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=1140" converted to a dictionary. The dictionary keys are the individual options, the dictionary values the values of the mount options. If no values are assigned for a key `None` is used for the value.
	#
	@property
	def options(self) -> dict:
		return self.__options
	#

	def toJSON(self):
		return {
			"device": self.__device,
			"mountPoint": self.__mountPoint,
			"fsType": self.__fsType,
			"options": self.__options,
			"isRegularDevice": self.isRegularDevice,
			"isNetworkDevice": self.isNetworkDevice,
		}
	#

	def dump(self, prefix:str = ""):
		if prefix is None:
			prefix = ""
		print(prefix + "MountInfo(")
		print(prefix + "\tdevice:", self.__device)
		print(prefix + "\tmountPoint:", self.__mountPoint)
		print(prefix + "\tfsType:", self.__fsType)
		print(prefix + "\toptions:", self.__options)
		print(prefix + "\tisRegularDevice:", self.isRegularDevice)
		print(prefix + "\tisNetworkDevice:", self.isNetworkDevice)
		print(")")
	#

	#
	# This method is invoked by `Mounter` to parse a mount information text line.
	#
	@staticmethod
	def _parseFromMountLine(line):
		assert isinstance(line, str)

		# print(":: " + line)

		elements = line.split(' ')
		while len(elements) > 6:
			elements[1] = elements[1] + elements[2]
			del elements[2]
		options = dict()
		for optionLine in elements[3].split(","):
			pos = optionLine.find("=")
			if pos < 0:
				options[optionLine] = None
			else:
				options[optionLine[0:pos]] = optionLine[pos + 1:]

		# print("=>", (elements[0], elements[1], elements[2], options))

		return MountInfo(elements[0], elements[1], elements[2], options)
	#

	def __str__(self):
		s = [
			"MountInfo(device=",
			self.__device,
			", mountPoint=",
			self.__mountPoint,
			", fsType=",
			self.__fsType,
		]
		if self.isRegularDevice:
			s.append(", isRegularDevice")
		if self.isNetworkDevice:
			s.append(", isNetworkDevice")
		if self.isSnapDevice:
			s.append(", isSnapDevice")
		if self.isReadOnly:
			s.append(", isReadOnly")
		s.append(")")
		return "".join(s)
	#

	def __repr__(self):
		return self.__str__()
	#

#












