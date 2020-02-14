import sys
import ctypes
class RTS_CTS_Mode:
	# RTS is never set, and CTS is ignored.
	RTS_CTS_MODE_DISABLED = 1
	# RTS Pin requests to transmit data. CTS input confirms we can send data.
	RTS_CTS_MODE_REQUEST_TO_SEND = 2
	# RTS signals this device can receive data. CTS confirms we can send data.
	RTS_CTS_MODE_READY_TO_RECEIVE = 3

	@classmethod
	def getName(self, val):
		if val == self.RTS_CTS_MODE_DISABLED:
			return "RTS_CTS_MODE_DISABLED"
		if val == self.RTS_CTS_MODE_REQUEST_TO_SEND:
			return "RTS_CTS_MODE_REQUEST_TO_SEND"
		if val == self.RTS_CTS_MODE_READY_TO_RECEIVE:
			return "RTS_CTS_MODE_READY_TO_RECEIVE"
		return "<invalid enumeration value>"
