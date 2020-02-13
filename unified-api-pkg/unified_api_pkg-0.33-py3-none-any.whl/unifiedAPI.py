#Provide Unified API in here
from .qrcode import saleQR,voidSaleQR,refundQR,retrievalQR
from .terminal import openPort, closePort,saleTerminal,refundTerminal,voidSaleTerminal,retrievalTerminal,membershipTerminal
from .terminalUtils import formatTransReceiptTerminal


class UnifiedAPI():
	props = {}

	def __init__(self):
		#get all the properties in the file
		with open("eftsolutions.properties", "r") as f:
				l = f.read()
		f.close()
		prop_list = l.split("\n")

		for item in prop_list:
			try:
				item_list = item.split("=")
				self.props[item_list[0]] = item_list[1]
			except:
				#empty line caused exception
				pass

	#Dictonary for transData,List for printOut
	def SaleQR(self,payment_type, qr_code, ecr_ref, amount, additional_amount,transData,printOut):
		printOut.clear()
		result = saleQR(qr_code,ecr_ref,amount,transData,printOut)
		return result

	def Sale(self,payment_type,ecr_ref,amount,additional_amount,payment_option,transData,printOut):
		printOut.clear()
		result = saleTerminal(payment_type,ecr_ref,amount,additional_amount,payment_option,transData,printOut)
		formatTransReceiptTerminal(transData,printOut,self.props)
		return result

	def Void(self,payment_type,invoice,originalECRREF,transData,printOut):
		printOut.clear()
		if payment_type is "QR":
			result = voidSaleQR(invoice,transData,printOut)
			return result
		elif payment_type is "EDC" or payment_type is "UPI" or "VAC":
			result = voidSaleTerminal(payment_type,invoice,originalECRREF,transData,printOut)
		else:
			return -1
			
	def Refund(self,payment_type,ecr_ref,amount,originalTransRef,transData,printOut):
		printOut.clear()
		if payment_type is "QR":
			result = refundQR(ecr_ref,amount,originalTransRef,transData,printOut)
			return result
		elif payment_type is "EDC":
			result = refundTerminal(payment_type,ecr_ref,amount,transData,printOut)
			return result
		else:
			return "PE"

	def Retrieval(self,payment_type,invoice,ecr_ref,transData,printOut):
		printOut.clear()
		if payment_type is "QR":
			result = retrievalQR(invoice,ecr_ref,transData,printOut)
			return result
		elif payment_type is "EDC" or payment_type is "EPS":
			result = retrievalTerminal(payment_type,invoice,transData,printOut)
			return result
		else:
			return -1
	
	def Membership(self,payment_type,ecr_ref,option,amount,ciamID,transData,printOut):
		printOut.clear()
		if payment_type is "EDC" or payment_type is "VAC":
			result = membershipTerminal(payment_type,ecr_ref,option,amount,ciamID,transData,printOut)
			return result
		else:
			return -1

	def OpenEDCCom(self):
		model = 0
		if self.props["EdcModel"] == "PAX_S60":
			model = 2
		elif self.props["EdcModel"] == "SPECTRA_T300":
			model = 1
		else:
			model = 0
		result = openPort(self.props["EdcCom"],self.props["LogLocation"],model)
		return result

	def CloseEDCCom(self):
		result = closePort()
		return result