import psycopg2
import configparser
import os
from os import environ as env
import dotenv

datasets = [
    'AsnicarF_2017',
    'BackhedF_2015',
    'Bengtsson-PalmeJ_2015',
    'BritoIL_2016',
    'Castro-NallarE_2015',
    'ChengpingW_2017',
    'ChngKR_2016',
    'CosteaPI_2017',
    'DavidLA_2015',
    'DhakanDB_2019',
    'FengQ_2015',
    'FerrettiP_2018',
    'GopalakrishnanV_2018',
    'HanniganGD_2017',
    'Heitz-BuschartA_2016',
    'HMP_2012',
    'JieZ_2017',
    'KarlssonFH_2013',
    'KieserS_2018',
    'KosticAD_2015',
    'LeChatelierE_2013',
    'LiJ_2014',
    'LiJ_2017',
    'LiSS_2016',
    'LiuW_2016',
    'LomanNJ_2013',
    'LoombaR_2017',
    'LouisS_2016',
    'MatsonV_2018',
    'NielsenHB_2014',
    'Obregon-TitoAJ_2015',    
    'OhJ_2014',
    'OlmMR_2017',
    'PasolliE_2018',
    'QinJ_2012',
    'QinN_2014',
    'RampelliS_2015',
    'RaymondF_2016',
    'SchirmerM_2016',
    'ShiB_2015',
    'SmitsSA_2017',
    'TettAJ_2016',
    'TettAJ_2019_a',
    'TettAJ_2019_b',
    'TettAJ_2019_c',
    'ThomasAM_2018a',
    'ThomasAM_2018b',
    'VatanenT_2016',
    'VincentC_2016',
    'VogtmannE_2016',
    #'WenC_2017',
    'XieH_2016',
    'YeZ_2018',
    'YuJ_2015',
    'ZeeviD_2015',
    'ZellerG_2014'
    ]

def get_psql_connection_string():
    try:
        host = env['psql_host']
        dbname = env['dbname']
        username = env['username']
        password = env['password']
        port = 5432

    except KeyError:

        dotenv.load_dotenv()
        host = env['psql_host']
        dbname = env['dbname']
        username = env['username']
        password = env['password']
        port = 5432


    conn_string = "user=%s password=%s dbname=%s host=%s port = %s" % (username, password, dbname, host, port)
    return conn_string

def get_connection(conn_string=None):

    conn_string = conn_string or get_psql_connection_string()
    return psycopg2.connect(conn_string)
