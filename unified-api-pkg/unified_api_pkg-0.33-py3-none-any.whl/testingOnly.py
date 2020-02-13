import json

def testingPass(transData):
    jsonstring = """{"CMD":"SALE","TYPE":"EFTPay","ACQNAME":"ALIPAY","CARD":"ALIPAY","RESP":"00","TRACE":"000207","INVOICE":"000207","DATE":"20191221","TIME":"04418","APPCODE":"H08726","PAN":"","AMT":"000000000010","TERMINALID":"00000004","MERCHANTID":"852999900000009","REFNUM":"191221204413","ECRREF":"abc","ORDERNUM":"2019122122001421021402079632","ORITRACE":"","ORIORDERNUM":""}"""
    tempDict = json.loads(jsonstring)
    for val in tempDict:
        transData[val] = tempDict[val]
