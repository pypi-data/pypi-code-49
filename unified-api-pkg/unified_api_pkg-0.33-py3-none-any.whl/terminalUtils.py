PAX_S60 = 2
SPECTRA_T300 = 1
LANDI_A8 = 0

#pure_chinese_line_length = 42
#mix_line_length = 40


bilingualDict = {
	"SALE":"銷售",
    "VOID":"撤銷",
    "REFUND":"退款",
    "RETRIEVAL":"查詢",
    "MID":"商戶號",
    "TID":"終端號",
    "DATE":"日期",
    "TIME":"時間",
    "BATCH":"批次號",
    "TRACE":"交易號",
    "PAN":"卡號",
    "EXPDATE":"有效期",
    "APPCODE":"授權碼",
    "REFNUM":"參考號",
    "TOTAL":"總計",
    "NET":"淨額",
    "SIGNATURE":"簽名",
    "NOSIGNATURE":"不需簽名",
    "ACCEPTED":"接受",
    "REJECTED":"不接受"
}

haseLoyaltyDict = {
    "HSD":"HASE CASH$",
    "JDD":"enJoy$"
}

sign_list = ["M","S","C","F","W","A","B"]

dccCurCodeDict = {
    "036" : "AUD",
    "124" : "CAD",
    "156" : "CNY",
    "196" : "CPY",
    "208" : "DKK",
    "344" : "HKD",
    "352" : "ISK",
    "356" : "INR",
    "360" : "IDR",
    "392" : "JPY",
    "410" : "KRW",
    "446" : "MOP",
    "458" : "MYR",
    "470" : "MTL",
    "554" : "NZD",
    "578" : "NOK",
    "608" : "PHP",
    "702" : "SGD",
    "710" : "ZAR",
    "752" : "SEK",
    "756" : "CHF",
    "764" : "THB",
    "826" : "GBP",
    "840" : "USD",
    "901" : "TWD",
    "978" : "EUR"
}


#Pack transData
def formatTransDataTerminal(rawData,transData,modelType):
    if modelType == PAX_S60:
        print("PAX S60")
        #CMD and TYPE
        if rawData[0:1] == "0":
            transData["CMD"] = "EDC"
            transData["TYPE"] = "SALE"
        elif rawData[0:1] == "2":
            transData["CMD"] = "EDC"
            transData["TYPE"] = "REFUND"
        elif rawData[0:1] == "3":
            transData["CMD"] = "EDC"
            transData["TYPE"] = "VOID"
        elif rawData[0:1] == "4":
            transData["CMD"] = "EDC"
            transData["TYPE"] = "RETRIEVAL"
        elif rawData[0:1] == "5":
            transData["CMD"] = "EPS"
            transData["TYPE"] = "SALE"
        elif rawData[0:1] == "6":
            transData["CMD"] = "EPS"
            transData["TYPE"] = "RETRIEVAL"
        elif rawData[0:1] == "@":
            transData["CMD"] = "UPI"
            transData["TYPE"] = "SALE"
        elif rawData[0:1] == "A":
            transData["CMD"] = "UPI"
            transData["TYPE"] = "VOID"
        elif rawData[0:1] == "D":
            transData["CMD"] = "UPI"
            transData["TYPE"] = "RETRIEVAL"
        elif rawData[0:1] == "I" or rawData[0:1] == "J" or rawData[0:1] == "K":
            transData["CMD"] = "EDC"
            transData["TYPE"] = "MEMBER"
        elif rawData[0:1] == "P":
            transData["CMD"] = "VAC"
            transData["TYPE"] = "MEMBER"
        elif rawData[0:1] == "Q":
            transData["CMD"] = "VAC"
            transData["TYPE"] = "VOID"

        
        #discard the MessageType
        rawData = rawData[1:]
        if transData["CMD"] == "EDC":
            if transData["TYPE"] != "MEMBER":
                transData["RESP"] = rawData[0:3]
                rawData = rawData[3:]
                transData["RESPMSG"] = rawData[0:20]
                rawData = rawData[20:]
                #ignore 1 byte original trans type
                rawData = rawData[1:]
                transData["ECRREF"] = rawData[0:16]
                rawData = rawData[16:]
                try:
                    transData["AMT"] = float(rawData[0:12])/100
                    rawData = rawData[12:]
                    transData["TIPS"] = float(rawData[0:12])/100
                    rawData = rawData[12:]
                except:
                    transData["AMT"] = 0.00
                    transData["TIPS"] = 0.00
                    rawData = rawData[12:]
                    rawData = rawData[12:]

                transData["DATE"] = rawData[0:8]
                rawData = rawData[8:]
                transData["TIME"] = rawData[0:6]
                rawData = rawData[6:]
                transData["CARD"] = rawData[0:10]
                rawData = rawData[10:]
                transData["PAN"] = rawData[0:19]
                rawData = rawData[19:]
                transData["EXPDATE"] = rawData[0:4]
                rawData = rawData[4:]
                transData["TERMINALID"] = rawData[0:8]
                rawData = rawData[8:]
                transData["MERCHANTID"] = rawData[0:15]
                rawData = rawData[15:]
                transData["TRACE"] = rawData[0:6]
                transData["INVOICE"] = rawData[0:6]
                rawData = rawData[6:]
                transData["BATCHNO"] = rawData[0:6]
                rawData = rawData[6:]
                transData["APPCODE"] = rawData[0:6]
                rawData = rawData[6:]
                transData["REFNUM"] = rawData[0:12]
                rawData = rawData[12:]

                #DCC
                if rawData[0:3] != "   ":
                    transData["CURRCODE"] = rawData[0:3]
                    rawData = rawData[3:]
                    transData["FXRATE"] = float(rawData[1:8])/(10 ** int(rawData[0:1]))
                    rawData = rawData[8:]
                    transData["FOREIGNAMT"] = float(rawData[0:12])/100
                    rawData = rawData[12:]
                else:
                    rawData = rawData[3:]
                    rawData = rawData[8:]
                    rawData = rawData[12:]

                #Entry Mode
                transData["ENTRYMODE"] = rawData[0:1]
                rawData = rawData[1:]

                if transData["ENTRYMODE"] in sign_list:
                    transData["SIGNBLOCK"] = "N"
                else:
                    transData["SIGNBLOCK"] = "Y"

                #Loyalty
                #if the HASE is completely new. It may treat as normal card also. 
                if rawData[0:60] != "{:060d}".format(0) and rawData[0:60] != "".ljust(60):
                    print("is HASE")

                    #Cash Dollar
                    hsd_dict = {}

                    #enjoy Dollar
                    enjoy_dict = {}

                    enjoy_dict["REDEEMED"] = float(rawData[0:12])
                    rawData = rawData[12:]
                    hsd_dict["REDEEMED"] = float(rawData[0:12])
                    rawData = rawData[12:]

                    transData["NETAMT"] = float(rawData[0:12])
                    rawData = rawData[12:]
                    
                    enjoy_dict["BAL"] = float(rawData[0:12])
                    rawData = rawData[12:]
                    hsd_dict["BAL"] = float(rawData[0:12])
                    rawData = rawData[12:]

                    full_loy_dict = {
                        "HSD":hsd_dict,
                        "JDD":enjoy_dict
                    }
                    transData["LOYALTY"] = full_loy_dict
                else: #Dont care the rest
                    print("not HASE")    
            else:
                #Membership function
                transData["RESP"] = rawData[0:3]
                rawData = rawData[3:]
                transData["RESPMSG"] = rawData[0:20]
                rawData = rawData[20:]
                transData["ECRREF"] = rawData[0:16]
                rawData = rawData[16:]
                transData["DATE"] = rawData[0:8]
                rawData = rawData[8:]
                transData["TIME"] = rawData[0:6]
                rawData = rawData[6:]
                transData["CARD"] = rawData[0:10]
                rawData = rawData[10:]
                transData["PAN"] = rawData[0:19]
                rawData = rawData[19:]
                transData["EXPDATE"] = rawData[0:4]
                rawData = rawData[4:]
                transData["TERMINALID"] = rawData[0:8]
                rawData = rawData[8:]
                transData["MERCHANTID"] = rawData[0:15]
                rawData = rawData[15:]
                transData["ENTRYMODE"] = rawData[0:1]
                rawData = rawData[1:]
                transData["CIAMID"] = rawData[0:20]
                rawData = rawData[20:]
                transData["PROGRAMID"] = rawData[0:20]
                rawData = rawData[20:]
                #ignore rest

        elif transData["CMD"] == "EPS":
            transData["RESP"] = rawData[0:3]
            rawData = rawData[3:]
            transData["RESPMSG"] = rawData[0:20]
            rawData = rawData[20:]
            transData["ECRREF"] = rawData[0:16]
            rawData = rawData[16:]
            #ignore 12-digit total amount and 12-digit other amount
            rawData = rawData[12:]
            rawData = rawData[12:]
            transData["DATE"] = rawData[0:8]
            rawData = rawData[8:]
            transData["TIME"] = rawData[0:6]
            rawData = rawData[6:]
            transData["PAN"] = rawData[0:19]
            rawData = rawData[19:]
            transData["TERMINALID"] = rawData[0:8]
            rawData = rawData[8:]
            transData["MERCHANTID"] = rawData[0:15]
            rawData = rawData[15:]
            transData["TRACE"] = rawData[0:6]
            transData["INVOICE"] = rawData[0:6]
            rawData = rawData[6:]
            transData["BANKINVALUEDAY"] = rawData[0:4]
            rawData = rawData[4:]
            transData["DEBITACCOUNTNO"] = rawData[0:28]
            rawData = rawData[28:]
            transData["BANKADDITIONALRESP"] = rawData[0:20]
            rawData = rawData[20:]
            transData["CARD"] = rawData[0:10]
            rawData = rawData[10:]
            #ignore 3-digit brand name
            rawData = rawData[3:]
            #ignore 6-digit billing currency
            rawData = rawData[6:]
            try:
                transData["AMT"] = float(rawData[0:12])/100
                rawData = rawData[12:]
                transData["CASHBACKAMT"] = float(rawData[0:12])/100
                rawData = rawData[12:]
            except:
                transData["AMT"] = 0.00
                transData["CASHBACKAMT"] = 0.00
                rawData = rawData[12:]
                rawData = rawData[12:]            
            transData["ACINDICATOR"] = rawData[0:3]
            rawData = rawData[3:]
            transData["REFNUM"] = rawData[0:6]
            rawData = rawData[6:]
            transData["SIGNBLOCK"] = "N"
            #ignore the Filler
        elif transData["CMD"] == "UPI":
            transData["RESP"] = rawData[0:3]
            rawData = rawData[3:]
            transData["RESPMSG"] = rawData[0:20]
            rawData = rawData[20:]
            #ignore 1 byte original trans type
            rawData = rawData[1:]
            transData["ECRREF"] = rawData[0:16]
            rawData = rawData[16:]
            try:
                transData["AMT"] = float(rawData[0:12])/100
                rawData = rawData[12:]
                rawData = rawData[12:]
            except:
                transData["AMT"] = 0.00
                rawData = rawData[12:]
                rawData = rawData[12:]
            transData["DATE"] = rawData[0:8]
            rawData = rawData[8:]
            transData["TIME"] = rawData[0:6]
            rawData = rawData[6:]
            transData["CARD"] = rawData[0:10]
            rawData = rawData[10:]
            transData["PAN"] = rawData[0:19]
            rawData = rawData[19:]
            transData["EXPDATE"] = rawData[0:4]
            rawData = rawData[4:]
            transData["TERMINALID"] = rawData[0:8]
            rawData = rawData[8:]
            transData["MERCHANTID"] = rawData[0:15]
            rawData = rawData[15:]
            transData["TRACE"] = rawData[0:6]
            transData["INVOICE"] = rawData[0:6]
            rawData = rawData[6:]
            transData["BATCHNO"] = rawData[0:6]
            rawData = rawData[6:]
            transData["APPCODE"] = rawData[0:6]
            rawData = rawData[6:]
            transData["REFNUM"] = rawData[0:12]
            rawData = rawData[12:]
            transData["SIGNBLOCK"] = rawData[0:1]
            #ignore the rest      
        elif transData["CMD"] == "VAC":
            transData["RESP"] = rawData[0:3]
            rawData = rawData[3:]
            transData["RESPMSG"] = rawData[0:20]
            rawData = rawData[20:]
            #ignore 1 byte original trans type
            rawData = rawData[1:]
            transData["ECRREF"] = rawData[0:16]
            rawData = rawData[16:]
            try:
                transData["AMT"] = float(rawData[0:12])/100
                rawData = rawData[12:]
                rawData = rawData[12:]
            except:
                transData["AMT"] = 0.00
                rawData = rawData[12:]
                rawData = rawData[12:]

            transData["DATE"] = rawData[0:8]
            rawData = rawData[8:]
            transData["TIME"] = rawData[0:6]
            rawData = rawData[6:]
            transData["CARD"] = rawData[0:10]
            rawData = rawData[10:]
            transData["PAN"] = rawData[0:19]
            rawData = rawData[19:]
            transData["EXPDATE"] = rawData[0:4]
            rawData = rawData[4:]
            transData["TERMINALID"] = rawData[0:8]
            rawData = rawData[8:]
            transData["MERCHANTID"] = rawData[0:15]
            rawData = rawData[15:]
            transData["TRACE"] = rawData[0:6]
            transData["INVOICE"] = rawData[0:6]
            rawData = rawData[6:]
            transData["BATCHNO"] = rawData[0:6]
            rawData = rawData[6:]
            transData["APPCODE"] = rawData[0:6]
            rawData = rawData[6:]
            transData["REFNUM"] = rawData[0:12]
            rawData = rawData[12:]
            try:
                transData["VACBALANCE"] = float(rawData[0:12])/100
                rawData = rawData[12:]
            except:
                transData["VACBALANCE"] = 0.00
                rawData = rawData[12:]
            transData["VACEXPDATE"] = rawData[0:8]
            rawData = rawData[8:]
            #ignore the rest
    elif modelType == 1:
        print("Spectra T300")
    else:
        print("modelType:"+str(modelType))

def formatDateTimeInReceipt(isDate,content):
    if isDate:
        #using date format "/"
        return content[0:4] + "/" + content[4:6] + "/" + content[6:]
    else:
        #using time format ":"
        return content[0:2] + ":" + content[2:4] + ":" + content[4:]

def mix_2_column_b(column1_header_chinese,column1_header_english,value1,column2_header_chinese,column2_header_english,value2):
    finial_content = ""
    col_content = column1_header_chinese + " " + column1_header_english
    length = len(column1_header_chinese)*2 + 1 + len(column1_header_english)
    space = 19 - length - len(value1)

    finial_content = col_content + " "*space + value1 +"  "

    col_content = column2_header_chinese + " " + column2_header_english
    length = len(column2_header_chinese)*2 + 1 + len(column2_header_english)
    space = 19 - length - len(value2)

    finial_content = finial_content + col_content + " "*space + value2

    return finial_content

def mix_1_column_b(header_chinese,header_english,value):
    finial_content = ""
    col_content = header_chinese + " " + header_english
    length = len(header_chinese)*2 + 1 + len(header_english)
    space = 40 - length - len(value)
    finial_content = col_content + " "*space + value

    return finial_content

def mix_1_column(header_english,value):
    finial_content = ""
    length = len(header_english)
    space = 40 - length - len(value)
    finial_content = header_english + " "*space + value

    return finial_content

def print_at_middle(content,isEnglish):
    content_length = 0
    line_length = 0 
    if isEnglish:
        content_length = len(content)
        line_length = 40
    else:
        content_length = len(content) * 2
        line_length = 42
    
    space = (int)((line_length - content_length) / 2)
    
    

    return " "*space + content + " "*space

def print_at_middle_b(content_chinese,content_english):
    content_length = len(content_chinese)*2 + 1 + len(content_english)

    content = content_chinese + " " + content_english
    space = (40 - content_length) / 2

    return " "*space + content + " "*space

def print_at_both_end(content1,content2):
    content_length = len(content1) + len(content2)

    space = 40 - content_length

    return conten1 + " "*space + content2

#Pack receipt
def formatTransReceiptTerminal(transData,printOut,props):
    if transData["CMD"] == "EDC" or transData["CMD"] == "UPI" or transData["CMD"] == "VAC":
        #Anfield should not has receipt
        if (transData["CMD"] != "EDC" or transData["TYPE"] != "MEMBER"):
            printOut.append(bilingualDict[transData["TYPE"]] +" "+ transData["TYPE"])
            printOut.append("")
            printOut.append(mix_2_column_b(bilingualDict["DATE"],"DATE",formatDateTimeInReceipt(True,transData["DATE"]),bilingualDict["TIME"],"TIME",formatDateTimeInReceipt(False,transData["TIME"])))
            printOut.append(mix_2_column_b(bilingualDict["BATCH"],"BATCH",transData["BATCHNO"],bilingualDict["TRACE"],"TRACE",transData["TRACE"]))
            printOut.append(mix_1_column_b(bilingualDict["MID"],"MID",transData["MERCHANTID"]))
            printOut.append(mix_1_column_b(bilingualDict["TID"],"TID",transData["TERMINALID"]))
            printOut.append(mix_1_column_b(bilingualDict["PAN"],"PAN",transData["PAN"] + " " + transData["ENTRYMODE"]))
            printOut.append(mix_1_column_b(bilingualDict["EXPDATE"],"EXPDATE",transData["EXPDATE"][0:2] + "/"+ transData["EXPDATE"][2:4]))
            printOut.append(transData["CARD"][2:])
            printOut.append(mix_1_column_b(bilingualDict["APPCODE"],"APPCODE",transData["APPCODE"]))
            printOut.append(mix_1_column_b(bilingualDict["REFNUM"],"REFNUM",transData["REFNUM"]))
            printOut.append(mix_1_column("ECRREF",transData["ECRREF"]))
            printOut.append("")

            if "LOYALTY" in transData:
                printOut.append(mix_1_column_b(bilingualDict["TOTAL"],"TOTAL",props["region"]+" "+str(transData["AMT"])))
                loy = transData["LOYALTY"]
                for looping in loy:
                    dollar = loy[looping]
                    printOut.append(mix_1_column(haseLoyaltyDict[looping],props["region"]+" "+str(dollar["REDEEMED"])))
                printOut.append("-"*40)
                printOut.append(mix_1_column_b(bilingualDict["NET"],"NET",props["region"]+" "+str(transData["NETAMT"])))

                printOut.append("")
                printOut.append("")

                printOut.append(" "*34 + "BAL")
                for looping in loy:
                    dollar = loy[looping]
                    printOut.append(mix_1_column(haseLoyaltyDict[looping],str(dollar["BAL"])))
            elif "CURRCODE" in transData:
                #DCC section
                printOut.append("FX RATE: "+ str(transData["FXRATE"]))
                printOut.append(print_at_middle_b(bilingualDict["TOTAL"],"TOTAL"))
                printOut.append(print_at_both_end("HKD []",dccCurCodeDict[transData["CURRCODE"]]+" [X]"))
                printOut.append(print_at_both_end(str(transData["AMT"]),str(transData["FOREIGNAMT"])))
            else:
                #normal section
                printOut.append(mix_1_column_b(bilingualDict["TOTAL"],"TOTAL",props["region"]+" "+str(transData["AMT"])))
    elif transData["CMD"] == "EPS":
        if transData["RESP"] == "000":
            #approve transaction
            printOut.append(bilingualDict[transData["TYPE"]] +" "+ transData["TYPE"])
            printOut.append("")
            printOut.append(mix_2_column_b(bilingualDict["DATE"],"DATE",formatDateTimeInReceipt(True,transData["DATE"]),bilingualDict["TIME"],"TIME",formatDateTimeInReceipt(False,transData["TIME"])))
            printOut.append(mix_1_column_b(bilingualDict["MID"],"MID",transData["MERCHANTID"]))
            printOut.append(mix_1_column_b(bilingualDict["TID"],"TID",transData["TERMINALID"]))
            printOut.append(mix_1_column_b(bilingualDict["PAN"],"PAN",transData["PAN"]))
            printOut.append(mix_1_column("ISN",transData["TRACE"]))
            printOut.append(mix_1_column("A/C",transData["DEBITACCOUNTNO"]))
            printOut.append(mix_1_column("A/C INDICATOR",transData["ACINDICATOR"]))

            printOut.append(mix_1_column("PURCHASE",props["region"]+" "+str(transData["AMT"])))
            printOut.append(mix_1_column("CASHBACK",props["region"]+" "+str(transData["CASHBACKAMT"])))
            printOut.append("-"*40)
            printOut.append(mix_1_column("TOTAL",props["region"]+" "+str(transData["AMT"]+transData["CASHBACKAMT"])))
            printOut.append("")
            #need to test pure chinese position
            printOut.append("*"*40)
            printOut.append("")
            printOut.append(print_at_middle(bilingualDict["ACCEPTED"],False))
            printOut.append(print_at_middle("ACCEPTED",True))
            printOut.append("")
            printOut.append("*"*40)
        elif "E" in transData["RESP"]:
            #internal reject
            print("Reject EPS")
        else:
            #online reject
            printOut.append("X"*40)
            printOut.append("X"*40)
            printOut.append(print_at_middle(bilingualDict["REJECTED"],False))
            printOut.append(print_at_middle("REJECTED",True))
            printOut.append("X"*40)
            printOut.append("X"*40)
            printOut.append(bilingualDict[transData["TYPE"]] +" "+ transData["TYPE"])
            printOut.append("")
            printOut.append(mix_2_column_b(bilingualDict["DATE"],"DATE",formatDateTimeInReceipt(True,transData["DATE"]),bilingualDict["TIME"],"TIME",formatDateTimeInReceipt(False,transData["TIME"])))
            printOut.append(mix_1_column_b(bilingualDict["MID"],"MID",transData["MERCHANTID"]))
            printOut.append(mix_1_column_b(bilingualDict["TID"],"TID",transData["TERMINALID"]))
            printOut.append(mix_1_column_b(bilingualDict["PAN"],"PAN",transData["PAN"]))
            printOut.append(mix_1_column("ISN",transData["TRACE"]))
            printOut.append(mix_1_column("A/C",transData["DEBITACCOUNTNO"]))
            printOut.append(mix_1_column("A/C INDICATOR",transData["ACINDICATOR"]))
            printOut.append(mix_1_column("TOTAL",props["region"]+" "+str(transData["AMT"]+transData["CASHBACKAMT"])))







