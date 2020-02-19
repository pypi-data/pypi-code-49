import sys
import ctypes
class Protocol:
	# Basic half-duplex RS485. Always receiving until you send data.
	PROTOCOL_RS485 = 1
	# Uses full-duplex RS422 communication.
	PROTOCOL_RS422 = 2
	# Allows communication with DMX512-compatible devices, such as stage lighting
	PROTOCOL_DMX512 = 3

	@classmethod
	def getName(self, val):
		if val == self.PROTOCOL_RS485:
			return "PROTOCOL_RS485"
		if val == self.PROTOCOL_RS422:
			return "PROTOCOL_RS422"
		if val == self.PROTOCOL_DMX512:
			return "PROTOCOL_DMX512"
		return "<invalid enumeration value>"
