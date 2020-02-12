"""
WHO API call python package Odata protocol <code for humanity>
@arghadeep.chaudhury@gmail.com
Date: 10-02-2020
Source : https://www.who.int/data/gho/info/gho-odata-api
"""
import requests
import json
import pandas as pd

"""
Retrieving the list of available dimensions
"""
def getDimension():

    dimresp=requests.get("https://ghoapi.azureedge.net/api/Dimension")
    dimrespdata=json.loads(dimresp.content)
    return dimrespdata['value']
"""
Retrieving a list of available values for a specific dimension
"""
def DimensionValues():

    DimensionValuesres=requests.get("https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues")
    DimensionValuesresdata=json.loads(DimensionValuesres.content)
    return DimensionValuesresdata['value']
"""
Retrieving the indicators list
"""
def IndicatorValue():

    indicatorval=requests.get("https://ghoapi.azureedge.net/api/Indicator")
    indicatorvaldata=json.loads(indicatorval.content)
    return indicatorvaldata['value']
"""
To select only the indicators which contain a specific text.Retrieving the indicators list
"""
def IndFilterlike(IndicatorNameVal):

    apistr="https://ghoapi.azureedge.net/api/Indicator?$filter=contains(IndicatorName,'"+IndicatorNameVal+"')"
    IndFilterVal=requests.get(apistr)
    IndFilterValdata=json.loads(IndFilterVal.content)
    return IndFilterValdata['value']
"""
To select only the indicators that have a specific title,Retrieving the indicators list
"""
def IndFilterSpec(Tindicator):

    specstr="https://ghoapi.azureedge.net/api/Indicator?$filter=IndicatorName eq '"+Tindicator+"'"
    IndFilterSpecdata=requests.get(specstr)
    IndFilterSpecdatajson=json.loads(IndFilterSpecdata.content)
    return IndFilterSpecdatajson['value']
"""
Specify an indicator to download by specifying the indicator code. 
This will return all associated data for that specific indicator.
Retrieving indicator data
"""
def IndData(IndCode):

    indstr="https://ghoapi.azureedge.net/api/"+IndCode
    IndDataApi=requests.get(indstr)
    IndDataJson=json.loads(IndDataApi.content)
    return IndDataJson['value']
"""
Retrieving All Ind data,
Warning : Please set our context memory size before calling this function
"""
def IndAllData():

    dffnlalldata=pd.DataFrame()
    fndata=IndicatorValue()
    for fulldata in fndata:
        df=IndData(fulldata['IndicatorCode'])
        df=pd.DataFrame(df)
        dffnlalldata=pd.concat([dffnlalldata,df])
    return dffnlalldata