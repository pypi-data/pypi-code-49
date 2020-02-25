#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:22:45 2020

@author: dakuoko
"""
        
#import users csv list and pull email column into list
import pandas as pd
import csv
import requests




def createCsvAndWriter(nameOfCsv):
    csvObject = open(str(nameOfCsv), 'w')
    csvObjectWriter = csv.writer(csvObject)
    return csvObjectWriter


def postApiRequest(apiUrl):
    r = requests.post(apiUrl)
    data = r.json()
    return data


#def loadVals(url, csvToWrite, userData, dataKeys):
#    varsArray = []
#    varsArray = [url, csvToWrite, userData, dataKeys]
#ß    return varsArray
#loadVals('http', 'fdf', 'ee', 'ddd')


#def writeDataTo(keys, data):
#    createCsvAndWriter(nameOfCsv).writerow(keys)
#    for i in range(len(data)):
#        createCsvAndWriter(nameOfCsv).writerow(data[i].values()) 






def matchColumns(csv1, c1col1, c1col2, csv2, c2col1, c2col2):
    matches = open('matches.csv', 'w')
    csv1Na = open('csv1Na.csv', 'w')
    csv2Na = open('csv2Na.csv', 'w')
    #cirrusUsers = open('cirrusUsers.csv', 'w')

    
#read users and leavers email lists
    readCsv1 = pd.read_csv(csv1).fillna(value = 'na')
    readCsv2 = pd.read_csv(csv2).fillna(value = 'na')
    
    out1 = csv.writer(matches)
    
    #leavers missing email
    out2 = csv.writer(csv1Na)
    
    #users missing email
    out3 = csv.writer(csv2Na)
    
    
    csv1Col1 = list(readCsv1[c1col1])
    csv1Col2 = list(readCsv1[c1col2])
    csv2Col1 = list(readCsv2[c2col1])
    csv2Col2 = list(readCsv2[c2col2])

#compare elements in csv1Col1 and csv2Col1 and return matches
    matchedElements = list(set(x.lower() for x in csv1Col1) & set(x.lower() for x in csv2Col1))
    for e in range(len(matchedElements)):
        if matchedElements[e] != 'na':
            out1.writerow([matchedElements[e],])

    naAtcsv1Col1=[]
    naAtcsv2Col1=[]


#if na found in csv2Col1, return the equivalent element in csv2Col2
    for i in range(len(csv2Col1)):
        if csv2Col1[i] == 'na':
            naAtcsv2Col1.append(csv2Col2[i])
    for e in range(len(naAtcsv2Col1)):
        out2.writerow([naAtcsv2Col1[e],])
        
    
#if na found in csv1Col1, return the equivalent element in csv1Col2
    for i in range(len(csv1Col1)):
        if csv1Col1[i] == 'na':
            naAtcsv1Col1.append(csv1Col2[i])
    for e in range(len(naAtcsv1Col1)):
        out3.writerow([naAtcsv1Col1[e],])
        

#SAMPLE USAGE:   -->  matchColumns('Piwik_users.csv', 'email', 'alias', 'leavers.csv', 'Email', 'Name of employee or applicant') 