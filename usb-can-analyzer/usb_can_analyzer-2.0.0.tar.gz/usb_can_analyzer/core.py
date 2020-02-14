#!/usr/bin/env python3
# coding: utf-8

"""
	This module only contains the defintion of the Converter class.

	This class allows to read/write data on a CAN bus with the usb can analyzer.
"""


from typing import Union, Tuple

from serial import Serial

from usb_can_analyzer.useful import getNbByte


__all__ = [
	"Converter"
]


class Converter():
	"""
		This class represents a usb can analyzer.

		This class allows to read/write data from/to a CAN bus with the usb can
		analyzer. The two mains methods are sendMessage and readMessage. The
		second one should be used in a thread and listen continuously.

		Attributes:
			STANDARD, EXTENDED:		Those two attributes represents the ID msg
									type.
			ID_MSG_TYPE_SIZE:		This dictionary links the two ID msg type to
									the size of the ID msg in bytes.

			DATA, REMOTE:			Those two attributes represents the msg type.
			TYPE_MSG:				This tuple groups the 2 msg types.

			FIRST_BYTE, LAST_BYTE:	Those two bytes (must be add/ are) at the
									begin and at the end of each msg with the
									usb can analyzer.

			comUSB:					The serial connection USB with the usb can
									analyzer.
		Methods:
			__init__:				The class constructor. It initializes the ID
									msg type for the usb can analyzer it creates
									the serial connection USB.

			sendMessage:			This method creates the msg frame and send
									it to the usb can analyzer calling
									differents Methods in the WRITTING PART.
			createConfigByte:		This method creates the config byte to send
									to usb can analyzer.
			createMsgID:			This method checks and reverses the message
									ID for the usb can analyzer.
			createPayload:			This method checks and adapt the paylaoad for
									the usb can analyzer.

			readMessage:			This method reads data from the serial
									connection USB with the usb can analyzer and
									returns the decomposed data.
			getConfigByte:			This method returns the decomposed data from
									the	readed config byte.
			getMsgID:				This method returns the msgID from the readed
									msg id bytes.
			getMsgPayload:			This method returns the payload readed from
									the payload bytes.

			__del__:				This method close the serial connection USB
									with the usb can analyzer before the obkect
									to be destroyed.
	"""
	# ID MSG
	STANDARD, EXTENDED = (0, 1)	# ID MSG type
	ID_MSG_TYPE_SIZE = {		# ID MSG size in byte
		STANDARD: 2,
		EXTENDED: 4
	}
	# TYPE FRAME
	DATA, REMOTE = (0, 1)
	TYPE_MSG = (DATA, REMOTE)

	FIRST_BYTE = b'\xaa'	# Constant use for the USB protocol with the converter USB/CAN.
	LAST_BYTE = b'\x55'		# Constant use for the USB protocol with the converter USB/CAN.

	def __init__(self, port: str = "/dev/ttyUSB0", baudrate: int = 9600, idMsgType: int = STANDARD):
		"""
			Contructor of the class usb can analyzer.

			This method does:
				_	Check and initialize msg type.
				_	Create the serial connection USB with the usb can analyzer.

			:param port:		The USB port of the usb can analyzer.
			:param baudrate:	The baudrato for the usb communication with
								the usb can analyzer.
			:param idMsgType:	The ID msg Type used on the bus can for the usb
								can analyzer.
			:type port:			str
			:type baudrate:		int
			:type idMsgType:	int
			:return:			A soft representation of the usb can analyzer.
			:rtype:				Converter

			:Example:

			>>> converter = Converter()

			>>> converter = Converter(idMsgType=Converter.EXTENDED)

			.. note::	You may have read and write permission on the USB port.
		"""
		if idMsgType not in Converter.ID_MSG_TYPE_SIZE.keys():	# We check that the idMsgType is a suitable value.
			raise ValueError("Not a valid idMsgSize: " + str(idMsgType))
		self.idMsgType = idMsgType
		self.comUSB = Serial(port, baudrate, timeout=0)

	# WRITING PART
	def sendMessage(self, msgType: int, msgID: int, payload: str = "") -> None:
		"""
			This method allows to write data to the usb can analyzer.

			This method does:
				_	Creates the msg frame, calling other methods.
				_	Write the msg frame to the serial connection USB with the usb
					can analyzer.

			:param msgType:		The msg type. (DATA - 0 or REMOTE - 1)
			:param msgID:		The msgID we want to send.
			:param payload:		The payload we want to send.
			:type msgType:		int
			:type msgID:		int
			:type idMsgType:	str
			:rtype:	None

			:Example:

			>>> converter = Converter()
			>>> converter.sendMessage(Converter.DATA, 43, "ab32")
			>>> converter.sendMessage(Converter.REMOTE, 43)

			.. seealso::	createConfigByte(self, idMsg, payload, typeMsg)
							createMsgID(self, msgID)
							createPayloadlaunch(self, data)
			.. note::		You may have read and write permission on the USB
							port.
			.. todo::		Manage the msgID and payload as
							Union[int, str, bytes].
		"""
		if msgType == self.REMOTE and payload != "":
			raise ValueError("A REMOTE msg can not have a payload.")
		msgID = self.createMsgID(msgID)
		frame = (
			self.FIRST_BYTE
			+ self.createConfigByte(msgID, payload, msgType)
			+ msgID
			+ self.createPayload(payload)
			+ self.LAST_BYTE
		)
		self.comUSB.write(frame)

	def createConfigByte(self, idMsg: Union[int, str, bytes], payload: Union[int, str, bytes], typeMsg: int = DATA) -> bytes:
		"""
			This method creates the config byte for the sendMessage method.

			This method does:
				_	Checks if the param values are suitable.
				_	Creates the base config byte.
				_	Puts some bits to 1 on the base config byte if necessary.
				_	Puts the payload size at the end on 4 bits
				_	Returns the config byte value as a bytes object with
					hexadecimal digits.

			:param idMsg:		The id msg - must on 2 or 4 bytes dependig on
								the id msg type.
			:param payload:		The payload we want to send.
			:param typeMsg:		The msg type. (DATA - 0 or REMOTE - 1)
			:type idMsg:		Union[int, str, bytes]
			:type payload:		Union[int, str, bytes]
			:type typeMsg:		int
			:return:			A bytes object representing the config byte.
			:rtype:				bytes
		"""
		idMsgNbByte = getNbByte(idMsg)					# We check that the number of bytes for the msg ID is not too large.
		if idMsgNbByte > Converter.ID_MSG_TYPE_SIZE[self.idMsgType]:
			raise ValueError("idMsg too large: " + str(idMsg))
		payloadNbByte = getNbByte(payload)	# We check that payload is not too to large.
		if payloadNbByte > 0b1111:
			raise ValueError("payload too large. It must contain at the most " + str(0b1111) + " bytes. payload: " + str(payload) + ", nb bytes: " + str(payloadNbByte))
		if typeMsg not in Converter.TYPE_MSG:		# We check that typeFrame is either DATA or REMOTE.
			raise ValueError("Not a valid type frame: " + str(typeFrame))

		configByte  = 0b11000000												# We set the 2 first bits to 1 for the converter USB/CAN.
		configByte += 0b00100000 if self.idMsgType == Converter.EXTENDED else 0	# If necessary, we change the bit associated with the number of byte in the msg id.
		configByte += 0b00010000 if typeMsg == Converter.REMOTE else 0			# If necessary, we change the bit associated with the msg type (REMOTE ou DATA).
		configByte += getNbByte(payload)										# We add the number of bytes for the payload
		return bytes.fromhex(format(configByte, "02x"))

	def createMsgID(self, msgID: int) -> bytes:
		"""
			This method creates the msg ID for the sendMessage method.

			This method does:
				_	Checks if the msgID is not a value too large.
				_	Add some 0 if necessary to have the msgID on the right
					number of bytes.
				_	Returns the msgID value as a bytes object with hexadecimal
					digits, after reversing it.

			:param msgID:		The msgID we want to send.
			:type msgID:		int
			:return:			A bytes object representing the msg ID.
			:rtype:				bytes


			.. todo::	Check if the msgID is not a value too large.
			.. todo::	Manage the msgID as str or bytes.
		"""
		if type(msgID) == int:
			msgID = format(msgID, "0"+str(self.ID_MSG_TYPE_SIZE[self.idMsgType]*2)+"x")
		return bytes.fromhex(msgID)[::-1]

	def createPayload(self, data: str) -> bytes:
		"""
			This method creates the payload for the sendMessage method.

			This method does:
				_	Checks if the data is not too large.
				_	Add a 0 if necessary to have the payload on a integer
					number ofbytes.
				_	Returns the payload value as a bytes object with hexadecimal
					digits.

			:param data:		The msgID we want to send.
			:type data:			str
			:return:			A bytes object representing the payload.
			:rtype:				bytes


			.. todo::	Manage the data as int or bytes.
		"""
		if len(data) > 0b1111*2:
			raise ValueError("Too many hexadecimal digits.")
		if len(data) % 2 == 1:
			data = "0" + data
		return bytes.fromhex(data)

	# READING PART
	def readMessage(self) -> Tuple[int, int, bytes]:
		"""
			This method allows to read data from the usb can analyzer.

			This method does:
				_	Check it reads the first and last bytes.
				_	Call other methods to read the frame.
				_	Return the decomposed data

			:return:	A tuple with the msg type (DATA - 0 or REMOTE - 1),
						the msg ID and the payload.
			:rtype:		Tuple[int, int, str]

			:Example:

			>>> converter = Converter()
			>>> print(converter.readMessage())

			.. todo::		check if the message is corrupted.
			.. seealso::	getConfigByte(self)
							getMsgID(self, lengthID)
							getMsgPayloadlaunch(self, lengthPayload)
			.. note::		You may have read and write permission on the USB
							port.
		"""
		if (self.comUSB.read() != self.FIRST_BYTE): return -1
		msgType, lengthID, lengthPayload = self.getConfigByte()
		msgID = self.getMsgID(lengthID)
		msgPayload = self.getMsgPayload(lengthPayload)
		if(self.comUSB.read() != self.LAST_BYTE): return -1
		return msgType, msgID, msgPayload

	def getConfigByte(self) -> Tuple[int, int, int]:
		"""
			This method reads and decomposes the config byte.

			This method does:
				_	Read the config byte.
				_	Decompose the config byte to find the msg type (DATA - 0 or
					REMOTE - 1), le length ID and the length payload.
				_	Return those 3 values.

			:return:	A tuple with the msg type (DATA - 0 or REMOTE - 1), the
						msg ID and the payload.
			:rtype:		Tuple[int, int, str]
		"""
		configByte = int(self.comUSB.read().hex(), base=16)
		msgType = Converter.TYPE_MSG[int(format(configByte, 'b')[3])]
		lengthID = Converter.ID_MSG_TYPE_SIZE[int(format(configByte, 'b')[2])]
		lengthPayload = int(format(configByte, "x")[1], base=16)
		return msgType, lengthID, lengthPayload

	def getMsgID(self, lengthID: int) -> int:
		"""
			This method reads the msg ID bytes.

			This method does:
				_	Read the msg ID bytes.
				_	Reverse it and change it as int to return.

			:param lengthID:	The msg ID length.
			:type msgID:		int
			:return:			The msg ID.
			:rtype:				int
		"""
		msgID = bytes()
		for i in range(lengthID): msgID += self.comUSB.read()
		msgID = int(msgID[::-1].hex(), base=16)
		return msgID

	def getMsgPayload(self, lengthPayload: int) -> bytes:
		"""
			This method reads the payload bytes.

			This method does:
				_	Read and return the payload bytes.

			:param lengthPayload:	The payload length.
			:type msgID:			int
			:return:				The payload.
			:rtype:					bytes
		"""
		msgPayload = bytes()
		for i in range(lengthPayload): msgPayload += self.comUSB.read()
		return msgPayload

	def __del__(self) -> None:
		"""
			Destructor of the class Converter.

			This method does:
				_	Closes the serial connection USB with the usb can analyzer.
				_	Destroy the serial connection USB with the usb can analyzer.

			:rtype:	None
		"""
		self.comUSB.close()
		del self.comUSB


if __name__ == "__main__":
	converter = Converter("/dev/ttyUSB0")
	try:
		while True:
#			converter.sendMessage(Converter.DATA, 20, input())
			data = converter.readMessage()
			if type(data) != int:
				print(data)
	except KeyboardInterrupt:
		pass
	finally:
		del converter
