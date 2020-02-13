import clr
import json
clr.AddReference("System.Collections")
clr.AddReference(r"paymentQR")

from System.Collections import ArrayList
from System import String
from .paymentQR import TransRecord
from .paymentQR import paymentQRAPI

testingQR=paymentQRAPI()
testdata = TransRecord()
arraylist = ArrayList()
result = -1

def saleQR(code, ecrRef, amount, transData, stringList):
    print("QRcode sale called")
    result = testingQR.SaleQR(code,ecrRef,amount,testdata,arraylist)
    jsonString = testdata.toJSONString()
    tempDict = json.loads(jsonString)
    for val in tempDict:
        transData[val] = tempDict[val]
    for val in arraylist:
        stringList.append(val)
    return result


def voidSaleQR(invoice,transData,stringList):
    result = testingQR.Void(invoice,"",testdata,arraylist)
    jsonString = testdata.toJSONString()
    tempDict = json.loads(jsonString)
    for val in tempDict:
        transData[val] = tempDict[val]
    for val in arraylist:
        stringList.append(val)
    return result

def refundQR(EcrRef,Amount,originalData,transData,stringList):
	if "TID" in originalData and "APPV" in originalData and "REFNUM" in originalData:
		oriDataString = originalData["TID"]+originalData["APPV"]+originalData["REFNUM"]
	result = testingQR.Refund(EcrRef,Amount,oriDataString,testdata,arraylist)
	jsonString = testdata.toJSONString()
	tempDict = json.loads(jsonString)
	for val in tempDict:
		transData[val] = tempDict[val]
	for val in arraylist:
		stringList.append(val)
	return result

def retrievalQR(invoice,ecrRef,transData,stringList):
    result = testingQR.Retrieval(invoice,ecrRef,testdata,arraylist)
    jsonString = testdata.toJSONString()
    tempDict = json.loads(jsonString)
    for val in tempDict:
        transData[val] = tempDict[val]
    for val in arraylist:
        stringList.append(val)
    return result
	

