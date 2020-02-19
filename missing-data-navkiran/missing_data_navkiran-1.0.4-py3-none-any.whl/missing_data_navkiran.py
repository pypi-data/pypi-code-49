#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:33:01 2020

@author: Navkiran
"""

def fill_categorical(df,columns):
    for col in columns:
        frq = df[col].dropna().mode()[0]
        df[col] = df[col].fillna(value=frq)

def fill_numerical(df,columns,argument=0):
    for col in columns:
        dicty = {
                0:df[col].mean(),
                1:df[col].median(),
                2:df[col].mode()[0]
                }
        val = dicty.get(argument)
        df[col] = df[col].fillna(value=val)

def impute(df,argument):
    categorical_columns = list(set(df.columns) - set(df._get_numeric_data().columns))
    numerical_columns = df._get_numeric_data().columns
    newdf = df.copy()
    fill_categorical(newdf,categorical_columns)
    fill_numerical(newdf,numerical_columns,argument)
    return newdf

def filler(df,argument):
    dicty = {
            0:'ffill',
            1:'bfill'
            }
    newdf = df.fillna(method=dicty.get(argument))
    return newdf
    
def dropval(df,along=0):
    newdf = df.dropna(axis=along)
    return newdf

    