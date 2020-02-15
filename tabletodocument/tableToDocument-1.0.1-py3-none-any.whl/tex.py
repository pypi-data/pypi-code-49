import tableToDocument.toDoc as tdDoc
import pandas as pd

supportedFormats=['tex']
table='\n\\begin{center}\n'
endTable='\n\\end{center}'
bd = "\\section"
endD="\\end{document}"

def write(tx):
    if toDoc.docExists(tx.path) == False:
        return 2
    if toDoc.isDocAccessible(tx.path) == False:
        return 1
    if toDoc.isDocFile(tx.path) == False or tx.path.split('.')[-1] not in supportedFormats:
        return 3
    if toDoc.validFlag(tx.flag) == False:
        return 4

    with open('../example.tex',"r") as f:
        x = f.read()
    f.close()

    if type(tx.dataType)==SupportedDataTypes.STRING:
        final = appendToTex(x,tx.flag,tx.dataType)

    if type(tx.dataType)==SupportedDataTypes.INT:
        final = appendToTex(x,tx.flag,str(tx.dataType))

    if type(tx.dataType)==SupportedDataTypes.LIST:
        final = appendToTex(x,tx.flag,createTableFromList(tx.dataType))

    if type(tx.dataType)==SupportedDataTypes.DICT:
        final = appendToTex(x,tx.flag,createTableFromDict(tx.dataType))

    if type(tx.dataType)==SupportedDataTypes.SET:
        final = appendToTex(x,tx.flag,createTableFromSet(tx.dataType))

    if type(tx.dataType)==SupportedDataTypes.DATAFRAME:
        final = appendToTex(x,tx.flag,createTableFromDataframe(tx.dataType))

    if type(tx.dataType)==SupportedDataTypes.SERIES:
        final = appendToTex(x,tx.flag,createTableFromSeries(tx.dataType))


    with open('../example.tex',"w") as g:
        g.write(final)
    g.close()


def appendToTex(tex,flag,data):
    bg=tex.split(bd)
    #Appends the data to the final section at the bottom
    if flag=='a':
        final=bg[0]
        for k in range(1,len(bg)-1):
            final=final+bd+bg[k]
        g=bg[len(bg)-1].split(endD)
        final=final+bd+g[0]+table+data+endTable+'\n'+endD
        return final

    #Appends the data structure at the first section,at the beginning
    if flag=='b':
        getSectionName=bg[1].split('}',1)
        final=bg[0]+bd+getSectionName[0]+'}'+table+data+endTable+getSectionName[1]
        for j in range(2,len(bg)):
            final=final+bd+bg[j]
        return final

    #Appends the data at the section #data ,at the bottom of the section
    final=bg[0]
    for sec in range(1,len(bg)):
        if sec==flag:
            if sec==len(bg)-1:
                splitLastSection=bg[sec].split(endD)
                final=final+bd+splitLastSection[0]+table+data+endTable+endD
                return final
            final=final+bd+bg[sec]+table+data+endTable
        else:
            final=final+bd+bg[sec]
    return final

def createTableFromList(data):
    columnSize=1
    for i in data:
        if type(i)==SupportedDataTypes.LIST:
            if len(i)>columnSize:
                columnSize = len(i)
    rowSize = len(data)

    tb="\\begin{tabular}{ c"
    for i in range(columnSize-1):
        tb=tb+" |c"
    tb=tb+"}\n"
    for j in range(rowSize):
        if type(data[j])==SupportedDataTypes.LIST:
            for k in range(columnSize):
                try:
                    if k==columnSize-1:
                        if j==rowSize-1:
                            tb=tb+str(data[j][k])+"\n"
                        else:
                            tb=tb+str(data[j][k])+" \\\\\n"
                    else:
                        tb=tb+str(data[j][k])+" & "
                except:
                    tb=tb+"\\\\\n"
                    break
        else:
            tb=tb+str(data[j])+"\\\\\n"

    return tb

def createTableFromDict(data):
    tb = "\\begin{tabular}{c|c}\n"
    tb= tb+"KEY &  VALUE \\\\\n"
    for key,val in data.items():
        tb=tb+str(key)+" & "+str(val)+" \\\\\n"
    return tb

def createTableFromSet(data):
    tb = "\n\\begin{tabular}{ c}\n"
    tb = tb +"SET"+" \\\\\n"
    for i in data:
        tb = tb + str(i)+" \\\\\n"
    return tb

def createTableFromDataframe(data):
    tb = "\n\\begin{tabular}{"
    for c in range(len(data.columns)):
        tb = tb + " c "
    tb = tb+" c }\n &"

    for k in data.columns:
        tb = tb +str(k)+" & "
    tb=tb[:-2]+"\\\\\n"

    for c in range(len(data)):
        tb=tb+str(c+1)+" & "
        for items in data.columns:
            tb=tb+str(data[items][c])+" & "
        tb=tb[:-2]+"\\\\\n"
    return tb

def createTableFromSeries(data):
    tb = "\\begin{tabular}{c|c}\n"
    tb= tb+"KEY &  VALUE \\\\\n"
    for key,val in data.items():
        tb=tb+str(key)+" & "+str(val)+" \\\\\n"
    return tb

class SupportedDataTypes:
    STRING=type("a")
    INT=type(1)
    LIST=type([])
    DICT=type({})
    SET=type({""})
    SERIES = type(pd.Series({}))
    DATAFRAME = type(pd.DataFrame({}))
