import pandas as pd

def replaceAndCapitalizeLetter(textToCapialize, character):
    position = 0
    while position < len(textToCapialize):
        position = textToCapialize.find(character, position)
        if position == -1:
            break
        if (position+1) < len(textToCapialize):
            textToCapialize=textToCapialize[:position+1]+textToCapialize[position+1].upper()+textToCapialize[position+2:]
        position += 1 
    textToCapialize = textToCapialize.replace(character, "")
    return textToCapialize


class DBObject(object):
    def __init__(self, objectName ):
        #self._df

        self._objectName = objectName.upper()
        self._specifySQLServer = ""

        self._sourceSystemName = "OSC"
        
        self._loadSchema="DWH"
        self._loadPrefix="L"

        self._odsSchema="DWH"
        self._odsPrefix="O"

        self._encoding = "UTF8"

    
    def __str__(self):
        return "LoadingTable: {}, ODSTable: {}, ServerUri: {}".format(self.getLoadTableName(), self.getODSTableName(), self._specifySQLServer)

    def headerToSkip(self, rows):
        self._headerToSkip = rows

    def specifySQLServer(self, serverUri):
        self._specifySQLServer = serverUri

    def loadSchemaAndPrefix(self,schema, prefix):
        self._loadSchema = schema.upper()
        self._loadPrefix = prefix.upper()
    
    def odsSchemaAndPrefix(self,schema, prefix):
        self._odsSchema = schema.upper()
        self._odsPrefix = prefix.upper()

    def getLoadTableName(self):
        return "["+ self._loadSchema + "].["+ self._loadPrefix + "_"+ self._sourceSystemName +"_"+ self._objectName +"]"

    def getODSTableName(self):
        return "["+ self._odsSchema + "].["+ self._odsPrefix + "_"+ self._sourceSystemName +"_"+ self._objectName +"]"


    
    def getDataFrame(self):
        return self._df

    def loadFromCSV(self, filePath,  seperator = ';'):
        self._df = pd.read_csv(filePath,dtype = str, encoding=self._encoding, sep=seperator)
        self._df['MetaSourceSystem']=self._sourceSystemName
        
    def loadFromExcel(self, filePath, sheetName = "Sheet1",):
        self._df = pd.read_excel(filePath,dtype = str, sheet_name= sheetName)
        self._df['MetaSourceSystem']=self._sourceSystemName

    def loadFromSapTxt(self, filePath, headerToSkip = 0, delimiterChar="\t", errorBadLines=False, dropSumLine=True, dropUnnamedColumn =True):
        #Read the File
        fileType = filePath[-3:]
        if fileType.lower() == 'csv' or fileType.lower() == 'txt':
            self._df = pd.read_csv(filePath, 
                            skiprows=headerToSkip, 
                            delimiter=delimiterChar, 
                            dtype = str, 
                            error_bad_lines=errorBadLines,
                            encoding = self._encoding)

        #Drop the last row (because its normaly the sum)
        if dropSumLine:
            self.dropSum()

        #Delete all Unnamed Column
        if dropUnnamedColumn:
            self._df = self._df.loc[:, ~self._df.columns.str.contains('^Unnamed')]

        #Add a meta Field to the end of the dataframe
        self._df['MetaSourceSystem']=self._sourceSystemName

    def dropSum(self):
        self._df = self._df.drop(self._df.index[len(self._df)-1])

    def cleanHeader(self):
        #Rename Header to more sql valid format
        newHeaderArray = []
        dfHeader = self._df.columns
        for i in range(len(dfHeader)):
            newHeader = dfHeader[i]
            #Replace dot and capitalize each letter after the dot
            newHeader = replaceAndCapitalizeLetter(newHeader, ".")
            #Replace space and capitalize each letter after the dspaceot
            newHeader = replaceAndCapitalizeLetter(newHeader, " ")
            #Replace + and capitailze each letter after the +
            newHeader = replaceAndCapitalizeLetter(newHeader, "+")
            #Replace : and capitailze each letter after the +
            newHeader = replaceAndCapitalizeLetter(newHeader, ":")
            #Replace - and capitailze each letter after the -
            newHeader = replaceAndCapitalizeLetter(newHeader, "-")
            #Strip (Trim)
            newHeader = newHeader.lstrip()
            newHeader = newHeader.rstrip()

            newHeaderArray.append(newHeader)
        #Add the new Header to the dataframe
        self._df.columns = newHeaderArray



        
        




# Testing
if __name__=="__main__":
    objectToLoad = DBObject("yae2_repnn")
    objectToLoad.headerToSkip(3)

    #objectToLoad.loadFromCSV("transformedExcel.csv", ";")
    

    objectToLoad.loadFromSapTxt("yat1_ts_pernr_1500_w2.txt",3)
    objectToLoad.cleanHeader()

    objectToLoad.specifySQLServer("DRIVER={SQL Server};SERVER=SCHWSR0082;DATABASE=DBSCHBI;Trusted_Connection=yes;")

 
    biCon.loadIntoLoadTable(objectToLoad)
    biCon.loadIntoOdsTable()



    print(objectToLoad)
    print(objectToLoad.getDataFrame())
