# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:08:49 2020

@author: raghav.sharma11
"""

import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom as xmldom
import xml.dom.minicompat as mini
import os
import csv
import time

class xml_to_dataframe:
#    Time1=time.time()
    def __init__(self, path_xml):
        self.path_xml=path_xml
        self.path_domxml=path_xml.split('.')[0]+'dom.'+path_xml.split('.')[1]
        self.csv_path=path_xml.split('.')[0]+'.csv'
        self.tree=ET.parse(path_xml)
        self.root=self.tree.getroot()
        self.col=[]
        self.type_nodeList=mini.NodeList()
        self.rootList=self.getCol(self.root, None)
        self.tree.write(self.path_domxml)
        self.domtree=xmldom.parse(self.path_domxml)
        os.remove(self.path_domxml)
        self.domroot=self.domtree.documentElement
        self.tagName=[]
        self.csvfile=open(self.csv_path, 'w', newline='')
        self.csvwriter=csv.writer(self.csvfile)
        self.finalList=[]
       
    
    def getCol(self,node,parentNode):
        if node.getchildren() != []:
            childList=[]
            for child in node:
                text=self.getCol(child,node)
                childList.append(text)
            return childList
            
        else:
            if parentNode.tag+"-"+node.tag not in self.col:
                self.col.append(parentNode.tag+"-"+node.tag)
            node.tag=parentNode.tag+"-"+node.tag
    
            return node.text
        
    #print(ET.tostring(root, encoding='utf8').decode('utf8'))
#    rootList=getCol(root, None)
#    dataset=pd.DataFrame()
    
    def forFunc(self, n_count, tagName, resList):
        global finalList
        if n_count>0:
            if tagName[len(tagName)-n_count]==[]:
                n_count=n_count-1
                resList.append(None)
                self.forFunc(n_count, tagName, resList)
                
            elif type(tagName[len(tagName)-n_count])==type(self.type_nodeList):
                for i in tagName[len(tagName)-n_count]:
                    if i.hasChildNodes():
                        resList.append(i.childNodes[0].data)
                        n_count=n_count-1
                        self.forFunc(n_count,tagName, resList)
                        n_count=n_count+1
                        resList=resList[0:len(tagName)-n_count]
                    else:
                        resList.append(None)
                        n_count=n_count-1
                        self.forFunc(n_count,tagName, resList)
                        n_count=n_count+1
                        resList=resList[0:len(tagName)-n_count]
        
            else:
                resList.append(tagName[len(tagName)-n_count][0].childNodes[0].data)
                n_count=n_count-1
                self.forFunc(n_count, tagName, resList)
                
        else:
            finalList.append(resList[:])
    
    def getDataset(self,node):
        global dataset
        global tagName
        global finalList
        tagName=self.col[:]
        for index, c in enumerate(self.col):
            tagName[index]=node.getElementsByTagName(c)
        n_count=len(tagName)
#        print(tagName)
    #    count=1
    #    for index,obj in enumerate(tagName):
    #        if len(obj)!=0:
    #            count=count*len(obj)
    #            
    #    for index,obj in enumerate(tagName):
    #        resList=[]
    #        for j, data in enumerate(obj):
    #            for k in range(count//len(obj)):
    #                if data.childNodes!=[]:
    #                    resList.append(data.childNodes[0].data)
    #                else:
    #                    resList.append(None)
    #        
    #        finalList.append(resList)   
        resList=[]
        finalList=[]
        self.forFunc(n_count, tagName, resList)
    #    print(finalList)
    #    
        self.csvwriter.writerows(finalList)
    #    
    #    df=pd.DataFrame(finalList)
    ##    df_array=np.array(df)
    ##    csvwriter.writerows(df_array)
    #    dataset=dataset.append(df)
    
    def getData(self,domNode):
        if len(self.root)<=1:
            self.root=self.root.getchildren()[0]
            self.getData(domNode.getElementsByTagName(self.root.tag))
        else:
            if type(domNode)!=type(self.type_nodeList):
                childNode=domNode.getElementsByTagName(self.root.getchildren()[0].tag)
                for child in childNode:
                    self.getDataset(child)
            else:
                for domnode in domNode:
                    childNode=domnode.getElementsByTagName(self.root.getchildren()[0].tag)
                    for child in childNode:
                        self.getDataset(child)
                
    def xml2csv(self):
        self.getData(self.domroot)
        self.csvfile.close()
#        Time2=time.time()
        
#        print("Time:",Time2-Time1)
    #dataset.to_csv(csv_path, index=False, header=col)