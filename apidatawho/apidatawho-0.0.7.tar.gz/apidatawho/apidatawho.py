"""
WHO API call python package Odata protocol <code for humanity>
@arghadeep.chaudhury@gmail.com
Date: 10-02-2020
Source : https://www.who.int/data/gho/info/gho-odata-api
"""
import requests
import json
import pandas as pd
#import whoami
from json2xml import json2xml
import yaml
import os
#apistrs=whoami.whoAmI()

def getAPIParams():
   with open(os.path.dirname(os.path.abspath('__file__')).replace('\\', '/')+'/apidatawho/config/config.yml') as info:
       info_dict = yaml.load(info)
   return info_dict
APIParam=getAPIParams()
class whoApi:
    def getDimension(self,oparam='JSON'):
        dimresp=requests.get(APIParam['URI']['getDim'])
        dimrespdata=json.loads(dimresp.content)
        if oparam=='JSON':
            return dimrespdata['value']
        elif oparam=='DF':
            return pd.DataFrame(dimrespdata['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(dimrespdata['value']).to_xml()
        else:
            return 'Param missing'
    def DimensionValues(self,oparam='JSON'):
        DimensionValuesres=requests.get(APIParam['URI']['getDimValues'])
        DimensionValuesresdata=json.loads(DimensionValuesres.content)
        if oparam=='JSON':
            return DimensionValuesresdata['value']
        elif oparam=='DF':
            return pd.DataFrame(DimensionValuesresdata['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(DimensionValuesresdata['value']).to_xml()
        else:
            return 'Param missing'
    def IndicatorValue(self,oparam='JSON'):
        indicatorval=requests.get(APIParam['URI']['getIndValues'])
        indicatorvaldata=json.loads(indicatorval.content)
        if oparam=='JSON':
            return indicatorvaldata['value']
        elif oparam=='DF':
            return pd.DataFrame(indicatorvaldata['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(indicatorvaldata['value']).to_xml()
        else:
            return 'Param missing'
    def IndFilterlike(self,IndicatorNameVal,oparam='JSON'):
        apistr=str(APIParam['URI']['getIndFilterVal'])+str(IndicatorNameVal)+"')"
        IndFilterVal=requests.get(apistr)
        IndFilterValdata=json.loads(IndFilterVal.content)
        if oparam=='JSON':
            return IndFilterValdata['value']
        elif oparam=='DF':
            return pd.DataFrame(IndFilterValdata['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(IndFilterValdata['value']).to_xml()
        else:
            return 'Param missing'
    def IndFilterSpec(self,Tindicator,oparam='JSON'):
        specstr=str(APIParam['URI']['getIndFilterSpecVal'])+str(Tindicator)+"'"
        IndFilterSpecdata=requests.get(specstr)
        IndFilterSpecdatajson=json.loads(IndFilterSpecdata.content)
        if oparam=='JSON':
            return IndFilterSpecdatajson['value']
        elif oparam=='DF':
            return pd.DataFrame(IndFilterSpecdatajson['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(IndFilterSpecdatajson['value']).to_xml()
        else:
            return 'Param missing'
    def IndData(self,IndCode,oparam='JSON'):
        print(APIParam['URI']['getIndData'])
        indstr=str(APIParam['URI']['getIndData'])+str(IndCode)
        IndDataApi=requests.get(indstr)
        IndDataJson=json.loads(IndDataApi.content)
        if oparam=='JSON':
            return IndDataJson['value']
        elif oparam=='DF':
            return pd.DataFrame(IndDataJson['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(IndDataJson['value']).to_xml()
        else:
            return 'Param missing'
    def IndAllData(self):
        dffnlalldata=pd.DataFrame()
        fndata=IndicatorValue()
        for fulldata in fndata:
            df=IndData(fulldata['IndicatorCode'])
            df=pd.DataFrame(df)
            dffnlalldata=pd.concat([dffnlalldata,df])