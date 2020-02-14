#!/usr/bin/env python3
# coding: utf-8


"""
 	This module contains the dataSet for the coulomb counter and the defintion
 	of the Coulomb_counter class.

	This class allows to read and use data from a USB connection with the
	coulomb_counter_cc75.
"""


from threading import Thread
from os.path import expanduser
from typing import Iterator, Union, List, Dict, Any

from serial import Serial


__all__ = [
	"Coulomb_counter"
]


dataSet = [
	{
		"name": "First byte",
		"nb_byte": 1,
		"coeff": 1,
		"unit": "",
		"check": {
			"min_included": 0,
			"max_included": 255,
			"step": 1
		}
	},
	{
		"name": "Percentage",
		"nb_byte": 1,
		"coeff": 1,
		"unit": "%",
		"check": {
			"min_included": 0,
			"max_included": 100,
			"step": 1
		}
	},
	{
		"name": "Voltage",
		"nb_byte": 2,
		"coeff": 100,
		"unit": "V",
		"check": {
			"min_included": 0,
			"max_included": 500,
			"step": 0.01
		}
	},
	{
		"name": "Capacity",
		"nb_byte": 4,
		"coeff": 1000,
		"unit": "Ah",
		"check": {
			"min_included": 0.1,
			"max_included": 5000,
			"step": 0.001
		}
	},
	{
		"name": "Current",
		"nb_byte": 4,
		"coeff": 1000,
		"unit": "A",
		"check": {
			"min_included": 0,
			"max_included": 750,
			"step": 0.001
		}
	},
	{
		"name": "Remaining Time",
		"nb_byte": 4,
		"coeff": 1,
		"unit": "s",
		"check": {
			"min_included": 0,
			"max_included": 359999,
			"step": 1
		}
	},
	{
		"name": "Check sum",
		"nb_byte": 1,
		"coeff": 1,
		"unit": "",
		"check": {
			"min_included": 0,
			"max_included": 255,
			"step": 1
		}
	}
]


class Coulomb_counter(Thread):
	"""
		This class represents a coulomb counter cc75.

		This class is a thread, it means that the run method will be called in
		parallel to the main program as soon as the start method is called in
		the main program.
		There is alse a launch method which can be called from the main program
		and will do the same things as run (start) but not in parallel.

		Attributes:
			NB_BYTES:		The number of byte in a complete frame from the
							coulomb counter cc75.

			launched:		The control variable for knowing if the thread is
							launched or not.

			dataSet:		A list of dictionary containing the data received
							from the coulomb counter, and parameters to read
							them in a right way.

			USBcomm:		The serial connection USB with the coulomb counter
							cc75.

		Methods:
			__init__:		The class constructor. It initializes the thread and
							the launched attribute, it loads data parameters to
							the dataSet attribute and it creates the serial
							connection USB.

			__iter__:		Allows to iterate on the dataSet list more easily

			__getitem__:	Allows to access to the dataSet attribute or a
							dictionary in the dataSet attribute more easily.

			__str__:		Pleasantly displays the data from the coulomb
							counter c75.

			process:		Retrieves data in the form of bytes from the coulomb
							counter cc75, saves it in the dataSet attribute and
							return True except if a data is not coherent, return
							False.

			run:			If this method is called from the start mathod
							(inherited from the Thread class), it is running in
							parallel of the main program. The method reads data
							from serial connection USB with the coulomb counter
							cc75, it calls the process method and, it calls the
							onUpdate method if the process method returns True

			stop:			Stops the run method (whether in a thread or not)
							and	closes the serial connection USB with the
							coulomb counter cc75.

			launch:			Calls the run method (not in a thread, so not in
							parallel to the main program) and manages the
							keyboard interrupt.

			onUpdate:		This empty function is called each time the data
							from the coulomb counter is read successfully. This
							method should be redefined by the user with the
							behavior he wants the program to have after each
							data update.
	"""

	NB_BYTES = 17
	CONFIG_FILE_PATH = expanduser("~") + "/.local/coulomb_counter_cc75_py/coulomb_counter.json"

	def __init__(self, port: str):
		"""
			Contructor of the class coulomb_counter.

			This method does:
				_ 	Initialize the thread.
				_ 	Initialize the launched attribute to False.
				_ 	Load data parameters to the dataSet attribute.
				_ 	Create the serial connection USB with the coulomb counter
					cc75.
				_ 	Close the serial connection USB with the coulomb counter
					cc75.

			:param port:	The USB port of the coulomb counter cc75.
			:type port:		str
			:return:		A soft representation of the coulomb counter with
							no values.
			:rtype:			Coulomb_counter

			:Example:

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")

			.. note:: You may have read and write permission on the USB port.
		"""
		Thread.__init__(self)
		self.launched = False
		self.dataSet = dataSet[:]
		self.USBcomm = Serial(port, 19200)
		self.USBcomm.close()

	def __iter__(self) -> Iterator[Dict]:
		"""
			Iterator of the class coulomb_counter.

			This method puts the iterator of the dataSet attribute list as
			Coulomb_counter iterator.

			:return:	The iterator of the dataSet attribute list.
			:rtype:		Iterator[Dict]

			:Example:

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> for dict in coulomb_counter:
			... 	print(dict)

			.. seealso:: __getitem__(self, item_name)
		"""
		return iter(self["list"])

	def __getitem__(self, item_name: Any) -> Union[List[Dict[str, Union[str, int]]], Dict[str, Union[str, int]]]:
		"""
			Make the Coulomb_counter class subscriptable.

			This method allows to get back:
				_	The dataSet attribute list of dictionary if the item_name is
					"list".
				_ 	The dict in the dataSet attribute whose value for the
					"name" key is item_value.
			If item_name is neither "list" nor one of a dictionary value for the
			key "name", raise a KeyError.

			:param item_name:	The key.
			:type port:			Any
			:return:			The dataSet attribute list of dictionary or a
								dictionary from the dataSet attribute list.
			:rtype:				List[Dict[str, [str or int]]] or
								Dict[str, [str or int]]

			:Example:

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> coulomb_counter["list"]

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> coulomb_counter["Current"]

			.. seealso:: __iter__(self)
		"""
		if item_name == "list":
			return self.dataSet
		for data in self:
			if item_name == data["name"]:
				return data
		raise KeyError(item_name)

	def __str__(self) -> str:
		"""
			Pleasantly displays the data from the coulomb counter cc75.

			This method allows display the data from the coulomb counter cc75
			as a dictionary but with one key: value by line.

			:return:	The string which can be displayed.
			:rtype:		str

			:Example:

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> print(coulomb_counter)
		"""
		string = "{\n"
		for data in self:
			string +="\t" + str(data["name"])
			if "value" in data.keys():
				string += ": " + str(data["value"])
				if data["unit"] != "":
					string += " " + str(data["unit"])
			string += ",\n"
		string = string[:-2] + "\n}"
		return string

	def process(self, USBdata: bytes) -> bool:
		"""
			Process, check and save data from the frame to the dataSet attribute list.

			This method does:
				_	Check the data length.
				_	Calculate the check sum based on the frame received.
				_	For each data in the frame (= each dictionary in the dataSet
					attribute list):
					_	Read the number of bytes required for the data
					_	Reorder the bytes for the data.
					_	Check if the value is coherent
					_	Remap the value depending on the unit
				_	Check if the check sum read at the end of the frame is equal
					to the check sum calculated earlier.
			If one of the checks is not validated, this method return False. If
			all checks are validated, this method return True

			:param USBdata:	The data reads with the USBcomm attribute serial..
			:type port:		bytes
			:return:		A bool represented if the data is coherent or not.
			:rtype:			bool

			:Example:

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> data = coulomb_counter.USBcomm.read(size=coulomb_counter.NB_BYTES)
			>>> print(coulomb_counter.process(data))

			.. seealso:: run(self)
			.. note:: Negative value for the Current are not taken into account.
		"""
		# Checking the data length
		if len(USBdata) != self.NB_BYTES:
			return False
		# Calculation of the check sum
		checkSum = sum([byte for byte in USBdata[1:-1]])%256
		# Reading data
		index = 0
		for data in self:
			# Getting all byte for the data
			data["value"] = USBdata[index:index+data["nb_byte"]]
			index += data["nb_byte"]
			# Reordering bytes (do not have an effect if there is only 1 byte in the data)
			data["value"] = data["value"][::-1]
			# Getting the base 10 value and checking if the value is coherent
			data["value"] = int(data["value"].hex(), base=16)
			min = int(data["check"]["min_included"]*data["coeff"])
			max = int(data["check"]["max_included"]*data["coeff"]) + 1
			if not data["value"] in range(min, max):
				return False
			# Remaping the data if necessary
			if data["coeff"] != 1:
				data["value"] /= data["coeff"]
		# Checking the check sum
		return checkSum == self["Check sum"]["value"]

	def run(self) -> None:
		"""
			The maine method: reads and process data.

			This method can be called when the launch method is called in the
			main program, or when the start method (inherit from the Thread
			class) is called (in this case, this run method will be executed in
			parallel of the main program.).
			This method does:
				_	Nothing if the launched attribute is already equal to True
					(It means that the run method is already in execution.).
				_	Open the USBcomm attribute port to read data.
				_	While the launched attribute is equal to True:
					_	Read the number of byte needed to have a complete frame.
					_	Process data readed, and, if te process method return
						True:
						_	Called the onUpdate method which should be redefined
							by the user.

			:rtype:	None

			:Example:

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> coulomb_counter.start() # execute the run method in parallel of the main program

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> coulomb_counter.launcht() # execute the run method in the main program

			.. seealso:: start(self), stop(self), launch(self), onUpdate(self)
		"""
		if not self.launched:
			self.launched = True
			self.USBcomm.open()
			while self.launched:
				data = self.USBcomm.read(size=self.NB_BYTES)
				if self.process(data):
					self.onUpdate()

	def stop(self) -> None:
		"""
			Stop the run method.

			Check if the run method is executed, and, if yes, stop it by
			changing the launched attribute value to False and close the USBcomm
			attribute port to read data.

			:rtype: None

			:Example:

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> coulomb_counter.start()	# execute the run method in parallel of the main program
			>>> coulomb_counter.stop()	# stop the thread.

			.. seealso:: start(self), run(self), launch(self)
		"""
		if self.launched:
			self.launched = False
			self.USBcomm.close()

	def launch(self) -> None:
		"""
			Execute the run method and manage the KeyboardInterrupt.

			Execute the run method (not in a Thread like if we use the start
			mathod inherited from the Thread class.).

			:rtype:	None

			:Example:

			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> coulomb_counter.launch() # execute the run method in the main program

			.. seealso:: run(self), stop(self)
		"""
		try:
			self.run()
		except KeyboardInterrupt as e:
			self.stop()
			raise KeyboardInterrupt(e)

	def onUpdate(self) -> None:
		"""
			This method should be redefined by the user.

			This method is called after reading coherent data on the USBcomm
			attribute Serial. It should be redefined by user if he wants the
			prograamm to have a specific behavior in this case.

			:rtype:	None

			:Example:

			>>> Coulomb_counter.noUpdate = lambda self: print(self)
			>>> coulomb_counter = Coulomb_counter("/dev/ttyUSB0")
			>>> coulomb_counter.launch()

			.. seealso:: start(self), run(self), launch(self)
			.. note:: This method should be redefined by the user.
		"""
		pass


if __name__ == "__main__":
	Coulomb_counter.onUpdate = lambda self: print(self)
	sensor = Coulomb_counter("/dev/ttyUSB0")
	try:
		sensor.launch()
	except KeyboardInterrupt:
		pass
	finally:
		sensor.stop()
