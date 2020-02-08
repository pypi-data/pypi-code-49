#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:23:47 2020

@author: smcclendon3
"""

import requests
import pandas as pd




def request_all_documents(token):
    url = 'https://www.lojipath.com/request/documents/'
    if token:
        headers = {'Authorization': 'Token'+ ' ' + token}
        
        r = requests.get(url, headers = headers)
        
        return(r.json())
    else:
        return('must supply account token')




def request_document(token, description):
    url = 'https://www.lojipath.com/request/document/' + description + '/'
    if token and description:
        headers = {'Authorization': 'Token'+ ' ' + token}
        
        r = requests.get(url, headers = headers)
        
        return(pd.DataFrame(r.json()))
    else:
        return('must supply account token and description')





def request_all_forecasts(token):
    url = 'https://www.lojipath.com/request/forecasts/'
    if token:
        headers = {'Authorization': 'Token'+ ' ' + token}
        
        r = requests.get(url, headers = headers)
        
        return(r.json())
    else:
        return('must supply account token')






def request_forecast(token, pk):
    url = 'https://www.lojipath.com/request/forecast/' + pk + '/'
    if token and pk:
        headers = {'Authorization': 'Token'+ ' ' + token}
        
        r = requests.get(url, headers = headers)
        
        return(pd.DataFrame(r.json()))
    else:
        return('must supply account token and description')




def generate_forecasts(token, pk, description, number, exp_month, exp_year, cvc):
    
    url = 'https://www.lojipath.com/generate/forecasts/' + pk + '/' + description + '/' + number + '/' + exp_month + '/' + exp_year + '/' + cvc + '/'
    
    if token and pk:
        headers = {'Authorization': 'Token'+ ' ' + token}
        
        r = requests.get(url, headers = headers)
        
        return(pd.DataFrame(r.json()))
    else:
        return('must supply account token and description')
    





def generate_forecasts_CC(token, pk, description, number, exp_month, exp_year, cvc, couponcode):
    
    url = 'https://www.lojipath.com/generate/forecastsCC/' + pk + '/' + description + '/' + number + '/' + exp_month + '/' + exp_year + '/' + cvc + '/' + couponcode + '/'
    
    if token and pk:
        headers = {'Authorization': 'Token'+ ' ' + token}
        
        r = requests.get(url, headers = headers)
        
        return(pd.DataFrame(r.json()))
    else:
        return('must supply account token and description')





def upload_document(token, description, forecast_period, file_path):
    
    url = 'https://www.lojipath.com/upload/' + description + '/' + forecast_period + '/'
    try:
        response = requests.post(
                    url,
                    files = {'document': open(file_path, 'rb')},
                    headers = {'Authorization': 'Token'+ ' ' + token}
                    )
        
        return(response)
    except:
        return('unable to upload document')
        





















