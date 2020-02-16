from chardet import detect
from xml.etree import ElementTree as ET
from enum import Enum
import pandas as pd
import tableToDocument.toDoc as toDoc
import zipfile
import os

supportedFormats = ['doc','docx','odt','xml']
ns3="{urn:oasis:names:tc:opendocument:xmlns:table:1.0}"
ns6="{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"

def write(toWord):
    if toDoc.docExists(toWord.path) == False:
        return 2
    if toDoc.isDocAccessible(toWord.path) == False:
        return 1
    if toDoc.isDocFile(toWord.path) == False or toWord.path.split('.')[-1] not in supportedFormats:
        return 3
    if toDoc.validFlag(toWord.flag) == False:
        return 4

    with zipfile.ZipFile(toWord.path,'r') as zp:
        with zp.open('content.xml','r') as cont:
            d = cont.read()

    zp.close()
    os.rename(toWord.path,toWord.path+'b')

    root = ET.fromstring(d)

    for child in root:
        if child.tag.find('body')>0:
                toXML(toWord.dataType,child[0],toWord.flag)

    ET.dump(root)
    tree = ET.ElementTree(root)
    createNewZip(toWord.path+'b',toWord.path,root)
    os.remove(toWord.path+'b')

def createNewZip(old,new,newcontent):
    zin = zipfile.ZipFile(old,'r')
    zout = zipfile.ZipFile(new,'w')
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        if(item.filename =='content.xml'):
            zout.writestr(item,ET.tostring(newcontent,method='xml'))
            continue
        zout.writestr(item,buffer)
    zout.close()
    zin.close()

def append(root,text):
    return root


class SupportedDataTypes:
    STRING=type("a")
    INT=type(1)
    LIST=type([])
    DICT=type({})
    SET=type({""})
    SERIES = type(pd.Series({}))
    DATAFRAME = type(pd.DataFrame({}))

class toXML:
    def __init__(self,data,parentXMLElement,flag):
        self.parent = parentXMLElement

        line=-1
        if flag=='b':
            line=0
        if type(flag)==SupportedDataTypes.INT:
            line=flag

        if type(data)==SupportedDataTypes.STRING:
            self.fromString(data,line)
        if type(data)==SupportedDataTypes.INT:
            self.fromInt(data,line)
        if type(data)==SupportedDataTypes.LIST:
            self.fromList(data,line)
        if type(data)==SupportedDataTypes.DICT:
            self.fromDictionary(data,line)
        if type(data)==SupportedDataTypes.SET:
            self.fromSet(data,line)
        if type(data)==SupportedDataTypes.SERIES:
            self.fromPandasSeries(data,line)
        if type(data)==SupportedDataTypes.DATAFRAME:
            self.fromPandasDataframe(data,line)



    def fromString(self,string,line):
        ad2=dict()
        ad2[ns6+'style-name'] = 'P1'
        ad=ns6+'p'
        nm = ET.Element(ad,ad2)
        nm.text = string
        if line==-1:
            self.parent.append(nm)
        else:
            self.parent.insert(line,nm)

    def fromInt(self,integ,line):
        id2=dict()
        id2[ns6+'style-name'] = 'P1'
        ind = ns6+'p'
        nm = ET.Element(ind,id2)
        nm.text = str(integ)
        if line==-1:
            self.parent.append(nm)
        else:
            self.parent.insert(line,nm)


    def fromList(self,lst,line):
        tb,tbColumn,tbRow,tcCell,tcP,tableNo = self.tableCreation(lst,line)

        for child in self.parent:
            if ns3+'name' in child.attrib.keys():
                if child.attrib[ns3+'name'] == 'TBN'+str(tableNo):

                    ET.SubElement(child,ns3+'table-column',tbColumn)
                    for i in range(len(lst)):
                        tbRow[ns3+'name']='ROW1'+str(i)
                        ET.SubElement(child,ns3+'table-row',tbRow)


                    for c2 in child:
                        if ns3+'name' in c2.attrib.keys():
                            for i in range(len(lst)):
                                if c2.attrib[ns3+'name'] == 'ROW1'+str(i):
                                    if type(lst[i]) == SupportedDataTypes.LIST:
                                        for j in range(len(lst[i])):
                                            tcCell[ns3+'name'] = 'Cell'+str(j)
                                            ET.SubElement(c2,ns3+'table-cell',tcCell)
                                        for c3 in c2:
                                            for k in range(len(lst[i])):
                                                if c3.attrib[ns3+'name'] == 'Cell'+str(k):
                                                    ET.SubElement(c3,ns6+'p',tcP).text=str(lst[i][k])

                                    else:
                                        ET.SubElement(c2,ns3+'table-cell',tcCell)
                                        for c3 in c2:
                                            ET.SubElement(c3,ns6+'p',tcP).text = str(lst[i])


    def fromDictionary(self,dct,line):
        tb,tbColumn,tbRow,tcCell,tcP,tableNo = self.tableCreation(dct,line)
        for child in self.parent:
            if ns3+'name' in child.attrib.keys():
                if child.attrib[ns3+'name'] == 'TBN'+str(tableNo):
                    ET.SubElement(child,ns3+'table-column',tbColumn)
                    for i in range(len(dct)):
                        tbRow[ns3+'name']='ROW1'+str(i)
                        ET.SubElement(child,ns3+'table-row',tbRow)

                    keys = list(dct.keys())
                    vals = list(dct.values())
                    i=0
                    for c2 in child:
                        if ns3+'name' in c2.attrib.keys():
                            if c2.attrib[ns3+'name']=='TAB1':
                                continue
                            ET.SubElement(ET.SubElement(c2,ns3+'table-cell',tcCell),ns6+'p',tcP).text = str(keys[i])
                            ET.SubElement(ET.SubElement(c2,ns3+'table-cell',tcCell),ns6+'p',tcP).text = str(vals[i])
                            i=i+1

    def fromSet(self,st,line):
        tb,tbColumn,tbRow,tcCell,tcP,tableNo = self.tableCreation(st,line)
        for child in self.parent:
            if ns3+'name' in child.attrib.keys():
                if child.attrib[ns3+'name'] == 'TBN'+str(tableNo):
                    ET.SubElement(child,ns3+'table-column',tbColumn)
                    for s in st:
                        row =ET.Element(ns3+'table-row',tbRow)
                        c1 = ET.Element(ns3+'table-cell',tcCell)
                        p1 = ET.Element(ns6+'p',tcP)
                        p1.text = str(s)
                        c1.append(p1)
                        row.append(c1)
                        child.append(row)

    def fromPandasSeries(self,ser,line):
        tb,tbColumn,tbRow,tcCell,tcP,tableNo = self.tableCreation(ser,line)
        for child in self.parent:
            if ns3+'name' in child.attrib.keys():
                if child.attrib[ns3+'name'] == 'TBN'+str(tableNo):
                    ET.SubElement(child,ns3+'table-column',tbColumn)
                    for i in range(len(ser)):
                        tbRow[ns3+'name']='ROW1'+str(i)
                        ET.SubElement(child,ns3+'table-row',tbRow)

                    keys = list(ser.index)
                    vals = list(ser)
                    i=0
                    for c2 in child:
                        if ns3+'name' in c2.attrib.keys():
                            if c2.attrib[ns3+'name'] == 'TAB1':
                                continue
                            ET.SubElement(ET.SubElement(c2,ns3+'table-cell',tcCell),ns6+'p',tcP).text = str(keys[i])
                            ET.SubElement(ET.SubElement(c2,ns3+'table-cell',tcCell),ns6+'p',tcP).text = str(vals[i])
                            i=i+1

    def fromPandasDataframe(self,df,line):
        tb,tbColumn,tbRow,tcCell,tcP,tableNo = self.tableCreation(df,line)

        for child in self.parent:
            if ns3+'name' in child.attrib.keys():
                if child.attrib[ns3+'name'] == 'TBN'+str(tableNo):

                    ET.SubElement(child,ns3+'table-column',tbColumn)
                    for i in range(len(df)+1):
                        tbRow[ns3+'name']='ROW1'+str(i)
                        ET.SubElement(child,ns3+'table-row',tbRow)


                    for c2 in child:
                        if ns3+'name' in c2.attrib.keys():
                            for i in range(len(df)+1):
                                if c2.attrib[ns3+'name'] == 'ROW1'+str(i):
                                    if i==0:
                                        ET.SubElement(ET.SubElement(c2,ns3+'table-cell',tcCell),ns6+'p',tcP).text=""
                                        for j in df.columns:
                                            ET.SubElement(ET.SubElement(c2,ns3+'table-cell',tcCell),ns6+'p',tcP).text=str(j)
                                    else:
                                        ET.SubElement(ET.SubElement(c2,ns3+'table-cell',tcCell),ns6+'p',tcP).text=str(i-1)
                                        for j in df.columns:
                                            ET.SubElement(ET.SubElement(c2,ns3+'table-cell',tcCell),ns6+'p',tcP).text=str(df[j][i-1])



    def tableCreation(self,lst,line):
        tb=dict()
        tb[ns3+'style-name'] = 'Table1'
        i=0
        for child in self.parent:
            if ns3+'name' in child.attrib.keys():
                if child.attrib[ns3+'name'] == 'TBN'+str(i):
                    i=i+1
        tb[ns3+'name']='TBN'+str(i)
        tbl=ET.Element(ns3+'table',tb)

        if line==-1:
            self.parent.append(tbl)
        else:
            self.parent.insert(line,tbl)

        tbColumn=dict()
        tbColumn[ns3+'style-name'] = 'Table1.A'
        tbColumn[ns3+'name']='TAB1'

        if type(lst)==SupportedDataTypes.LIST:
            cols= str(self.columnSize(lst))
        elif type(lst)==SupportedDataTypes.DATAFRAME:
            cols= str(len(lst.columns)+1)
        elif type(lst)==SupportedDataTypes.SET:
            cols="1"
        else:
            cols = "2"

        tbColumn[ns3+'number-columns-repeated'] = cols

        tbRow=dict()

        tcCell=dict()
        tcCell[ns3+'style-name'] = 'Table1.A1'
        tcCell['ns0:value-type'] = 'string'

        tcP=dict()
        tcP[ns3+'style-name'] = 'P1'

        return tb,tbColumn,tbRow,tcCell,tcP,i

    def columnSize(self,lst):
            maxc=1
            for i in range(len(lst)):
                if type(lst[i])==SupportedDataTypes.LIST:
                    if maxc<len(lst[i]):
                        maxc=len(lst[i])

            return maxc
