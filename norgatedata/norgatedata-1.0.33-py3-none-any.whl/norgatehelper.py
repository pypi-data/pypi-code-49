import urllib
import sys
import pandas as pd
import numpy as np
import numpy.lib.recfunctions as rfn
import inspect
import csv
from enum import Enum
import requests
import json
import os
from os.path import exists, expanduser, join
import inspect
from time import time,sleep
import warnings
from errno import EEXIST
import logbook
import datetime
from .version import __version__
import platform

try:
    from packaging.version import parse
except ImportError:
    from pip._vendor.packaging.version import parse


# Global vars
logger = logbook.Logger('Norgate Data')
logbook.StreamHandler(sys.stdout).push_application()  # required for Jupyter to output
session = requests.Session()

session.headers.update({'User-Agent':'norgatedata '+__version__ + ' ' + platform.python_version() + ' ' + sys.argv[0]})
session.headers.update({'Python-Version':platform.python_version()})
session.headers.update({'Caller':sys.argv[0]})
session.headers.update({'Client':platform.node()})
session.headers.update({'ClientOS':platform.platform()})

norgate_web_api_base_url = 'http://localhost:38889/api/v1/'

#######################################################################################################
# Internal helper functions
#######################################################################################################
def build_api_url(dataitem,item,parameters=None):
    url = norgate_web_api_base_url + dataitem
    if item is not None:
        item = str(item)
        url += '/' + urllib.parse.quote(item)
    if parameters is not None:
        url += '?' + urllib.parse.urlencode(parameters)
    return url

def get_api_data(dataitem,item,parameters=None,haltonerror=True,maxretries=10,connecttimeout=5.0,readtimeout=15.0):
    trycount = 0
    success = False
    url = build_api_url(dataitem,item,parameters)
    while trycount < maxretries and not success:
        trycount+=1
        try:
            apiresponse = session.get(url)
            success = True
        except Exception:
            if maxretries > 1:
                logger.warn("Unable to obtain data from Norgate Data - perhaps NDU is not running?  Attempt " + str(trycount) + "/" + str(maxretries) + ".  Retrying... ")
            else:
                logger.warn("Unable to obtain valid status from Norgate Data - perhaps NDU is not running?")
    if not success and haltonerror:
        logger.error("Unable to obtain data from Norgate Data.  Maximum attempts reached.")
        sys.exit()
    if not success:
        return None
    return apiresponse

def checkstatus():
    r = get_api_data('status',None,None,haltonerror=False,maxretries=1,connecttimeout=1,readtimeout=1)
    if r is None:
        return False
    return True

def validate_existing_array(pandas_dataframe,numpy_ndarray,numpy_recarray,format):
    if pandas_dataframe is not None:
        start_date,end_date,limit = validate_dataframe(pandas_dataframe,format)
    if numpy_ndarray is not None:
        start_date,end_date,limit = validate_ndarray(numpy_ndarray,format)
    if numpy_recarray is not None:
        start_date,end_date,limit = validate_recarray(numpy_recarray,format)
    return start_date,end_date,limit

def validate_dataframe(pandas_dataframe,format):
    if format != 'pandas-dataframe':
        logger.error("Format specified is " + format + " but the parameter pandas_dataframe was provided.  You need to pass in an array of the same type as the format you require.  Perhaps you didn't explicitly specify the format?")
        raise ValueError
    if not(isinstance(pandas_dataframe,pd.core.frame.DataFrame)):
        logger.error(inspect.currentframe().f_back.f_code.co_name + ": pandas_dataframe passed was not a Pandas DataFrame - it is actually " + str(type(pandas_dataframe)))
        raise ValueError
    if pandas_dataframe.index.name != 'Date':
        logger.error(inspect.currentframe().f_back.f_code.co_name + ": Expected dataframe to have index of Date but found " + pandas_dataframe.index.name)
        raise ValueError
    start_date = pandas_dataframe.first_valid_index()
    end_date = pandas_dataframe.last_valid_index()
    limit = -1
    return start_date,end_date,limit

def validate_recarray(numpy_recarray,format):
    if format != 'numpy-recarray':
        logger.error("Format specified is " + format + " but the parameter numpy_recarray was specified. You need to pass in an array of the same type as the format you require.  Perhaps you didn't explicitly specify the format?")
        raise ValueError
    if not(isinstance(numpy_recarray,np.recarray)):
        logger.error(inspect.currentframe().f_back.f_code.co_name + ": numpy_recarray was not a Numpy recarray - it is actually " + str(type(numpy_recarray)))
        raise ValueError
    if numpy_recarray.dtype.names[0] != 'Date':
        logger.error(inspect.currentframe().f_back.f_code.co_name + ": Expected recarray to have first field of Date but found " + numpy_recarray.dtype.names[0])
        raise ValueError
    start_date = numpy_recarray[0][0]
    end_date = numpy_recarray[-1][0]
    limit = -1
    return start_date,end_date,limit

def validate_ndarray(numpy_ndarray,format):
    if format != 'numpy-ndarray':
        logger.error("Format specified is " + format + " but the parameter numpy_ndarray was specified.  You need to pass in an array of the same type as the format you require.  Perhaps you didn't explicitly specify the format?")
        raise ValueError
    if not(isinstance(numpy_ndarray,np.ndarray)):
        logger.error(inspect.currentframe().f_back.f_code.co_name + ": numpy_ndarray was not a Numpy ndarray array - it is actually " + str(type(numpy_ndarray)))
        raise ValueError
    if numpy_ndarray.dtype.names[0] != 'Date':
        logger.error(inspect.currentframe().f_back.f_code.co_name + ": Expected recarray to have first field of Date but found " + numpy_ndarray.dtype.names[0])
        raise ValueError
    start_date = numpy_ndarray[0][0]
    end_date = numpy_ndarray[-1][0]
    limit = -1
    return start_date,end_date,limit

def validate_api_responseORIG(r,symbol):

    if r.status == 404:
        logger.error(inspect.currentframe().f_back.f_code.co_name + ': ' + str(symbol) + " was not found")
        raise ValueError
    if not (r.status == 200 or r.status == 204) :
        logger.error(inspect.currentframe().f_back.f_code.co_name + ": Error in receiving Norgate Data - check parameters are correctly formatted/have valid parameter values")
        raise ValueError

def validate_api_response(r,symbol):
    errormsg = ''
    if 'X-Norgate-Data-Error' in r.headers:
        errormsg += r.headers['X-Norgate-Data-Error']
    if r.status_code == 404:
        logger.error(inspect.currentframe().f_back.f_code.co_name + ': ' + errormsg)
        raise ValueError
    if not (r.status_code == 200 or r.status_code == 204) :
        logger.error(inspect.currentframe().f_back.f_code.co_name + ": Error in receiving Norgate Data - check parameters are correctly formatted/have valid parameter values." + errormsg)
        raise ValueError

def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]

def create_pandas_dataframe(symbol,r,pandas_dataframe=None,lowercase_columns=False,datetimeformat='',timezone=''):
    recordcount = int(r.headers['X-Norgate-Data-Record-Count'])
    if lowercase_columns:
        fieldnames = r.headers['X-Norgate-Data-Field-Names'].lower().split(',')
    else:
        fieldnames = r.headers['X-Norgate-Data-Field-Names'].split(',')
    formats = r.headers['X-Norgate-Data-Field-Formats'].split(',')
    fieldcount = int(r.headers['X-Norgate-Data-Field-Count'])
    npdates = np.frombuffer(r.content,formats[0],recordcount) 
    if datetimeformat == 'datetime' or datetimeformat == 'date':
        dt = npdates.dtype
        dt = dt.descr
        if datetimeformat == 'datetime':
            dt[0]  = (dt[0][0],datetime.datetime)
        else:
            dt[0]  = (dt[0][0],datetime.date)
        dt = np.dtype(dt)
        npdates = npdates.astype(dt)
    npdates = npdates.copy()
    indicatorType = []
    for i in range(1,fieldcount):
        indicatorType.append((fieldnames[i],formats[i]))
    npdata = np.frombuffer(r.content,indicatorType,-1,recordcount * 8)
    npdata = npdata.copy()
    pdf = pd.DataFrame(data=npdata,index=npdates)
    if timezone is not None and timezone != '' and timezone != 'naive':
        pdf.tz_localize(timezone,copy=False)
    pdf.name = symbol
    if pandas_dataframe is None:
        return pdf
    pandas_dataframe = pd.merge(pandas_dataframe,pdf, how='left', left_index=True, right_index=True)
    return pandas_dataframe

def create_numpy_ndarray(r,np_ndarray=None, datetimeformat='',timezone=''):
    recordcount = int(r.headers['X-Norgate-Data-Record-Count'])
    fields = r.headers['X-Norgate-Data-Field-Names'].split(',')
    formats = r.headers['X-Norgate-Data-Field-Formats'].split(',')
    fieldcount = int(r.headers['X-Norgate-Data-Field-Count'])
    indicatorType = []
    for i in range(0,fieldcount):
        indicatorType.append((fields[i],formats[i]))
    npdata = np.frombuffer(r.content,indicatorType,recordcount)
    print (npdata)
    if datetimeformat == 'datetime' or datetimeformat == 'date':
        dt = npdata.dtype
        dt = dt.descr
        print (dt)
        if datetimeformat == 'datetime':
            dt[0] = (dt[0][0],datetime.datetime)
        else:
            dt[0] = (dt[0][0],datetime.date)
        dt = np.dtype(dt)
        npdata = npdata.astype(dt)
        if datetimeformat == 'datetime':
            timezero = datetime.time()
            # we have to convert each row manually since Numpy doesn't convert a date object with no time
            for row in npdata:
                row[0] = datetime.datetime.combine(row[0],timezero)

    if np_ndarray is not None:
        np_ndarray = rfn.join_by("Date",np_ndarray,npdata)
        return np_ndarray
    return npdata

def create_numpy_recarray(r,np_recarray=None, datetimeformat='',timezone=''):
    npdata = create_numpy_ndarray(r)
    if datetimeformat == 'datetime' or datetimeformat == 'date':
        dt = npdata.dtype
        dt = dt.descr
        if datetimeformat == 'datetime':
            dt[0] = (dt[0][0],datetime.datetime)
        else:
            dt[0] = (dt[0][0],datetime.date)
        dt = np.dtype(dt)
        npdata = npdata.astype(dt)
        if datetimeformat == 'datetime':
            timezero = datetime.time()
            # we have to convert each row manually since Numpy doesn't convert a date object with no time
            for row in npdata:
                row[0] = datetime.datetime.combine(row[0],timezero)

    npdata2 = npdata.view(np.recarray)
    if np_recarray is not None:
        np_recarray = rfn.join_by("Date",np_recarray,npdata2)
        return np_recarray
    return npdata2

def version_checker(currentversion, package):
    ensure_norgatedata_root()
    jsonfile = norgatedata_root() + "\\" + package + "_release_version.json" # this file is part of the package distribution
    newversion = '0'
    if os.path.isfile(jsonfile):
        file1 = open(jsonfile,"r")
        newversion = json.load(file1)
        file1.close()
    if not (os.path.isfile(jsonfile)) or (os.path.isfile(jsonfile) and (time() - os.path.getmtime(jsonfile) > 60 * 60)): # Check once an hour
        newversion = get_latest_pypi_version(package)
        file1 = open(jsonfile,"w")
        file1.write('"' + newversion + '"')
        file1.close()
    if newversion > currentversion:
        logger.warn("**PACKAGE VERSION WARNING*** You have version (" + currentversion + ") of the " + package + " package installed.  A newer version " + newversion + " is available and is a recommended upgraded.")

def get_latest_pypi_version(package):
    """Return version of package on pypi.python.org using json."""
    url_pattern = 'https://pypi.python.org/pypi/{package}/json'
    version = parse('0')
    try:
        req = requests.get(url_pattern.format(package=package))
        if req.status_code == requests.codes.ok:
            j = json.loads(req.text) # .encode(req.encoding))
            releases = j.get('releases', [])
            for release in releases:
                ver = parse(release)
                if not ver.is_prerelease:
                    version = max(version, ver)
    except:
        logger.warn ('Warning: Unable to obtain version data of ' + package + ' from pypi - perhaps you are offline?')
    return version.public

def norgatedata_root():
    """
    Get the root directory for all Norgate Data managed files.
    These files are primarily used for version checking/warning that a new version is available

    Returns
    -------
    root : string
        Path to the zipline root dir.
    """
    environ = os.environ
    root = environ.get('NORGATEDATA_ROOT', None)
    if root is None:
        root = expanduser('~/.norgatedata')
    return root


def ensure_norgatedata_root():
    """
    Ensure that the Norgate Data root directory exists for config files
    """
    ensure_directory(norgatedata_root())

def ensure_directory(path):
    """
    Ensure that a directory named "path" exists.
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == EEXIST and os.path.isdir(path):
            return
        raise


def decode_date(content,format='iso'):
    """
    Turns various datetime representations string or bytearray dates into other Python dates
    """

    if len(content) == 0:
        return None
    if type(content) == bytes:
        dateval = bytes.decode(content)
    elif type(content) == str:
        if content == 'now' or content == 'today':
            dateval = datetime.datetime.now().strftime('%Y-%m-%d')
        else:
            dateval = content
    elif type(content) == datetime:
        dateval = content.strptime(date,'%Y-%m-%d')
    elif type(content) == date:
        dateval = content.strptime(date,'%Y-%m-%d')
    elif type(content) == np.datetime64:
        dateval = content.strptime(date,'%Y-%m-%d')

    try:
        if dateval == '9999-12-31':
            return None
        if dateval == '':
            return None
        if format == 'iso':
            if (len(dateval) == 10):
                return dateval
            return date.strptime(date,'%Y%m%d').strftime('%Y-%m-%d')
        if format == 'datetime':
            if (len(date) == 10):
                return datetime.datetime.strptime(dateval,'%Y-%m-%d')
            return datetime.datetime.strptime(dateval,'%Y%m%d')
        if format == 'date':
            if (len(dateval) == 10):
                return datetime.date.strptime(dateval,'%Y-%m-%d')
            return date.strptime(dateval,'%Y%m%d')
        if format == 'pandas-timestamp':
            return pd.Timestamp(dateval, tz='UTC')
        if format == 'numpy-datetime64ns':
            return np.datetime64(dateval)
        if format == 'numpy-datetime64nsutc':
            return np.datetime64(dateval, tz='UTC')
    except:
        logger.warn("Invalid date or format provided for conversion " + str(dateval) +  " into format " + format)
        return None
    logger.error("Unknown date format provided - " + str(format))
    raise ValueError


def encode_date_to_iso(date):
    if isinstance(date,str):
        valid = False
        if date == 'now':
            return datetime.datetime.now
        try:
            validate_date = datetime.datetime.strptime(date,'%Y-%m-%d')
            valid = True
        except:
            pass
        try:
            if not valid:
                validate_date = datetime.datetime.strptime(date,'%Y%m%d') # Also try without dashes
            valid = True
        except:
            pass
        if not valid:
            logger.error("Date provided doesn't appear to be YYYY-MM-DD format")
            raise ValueError
        else:
            return validate_date.strftime('%Y-%m-%d')
    if isinstance(date,np.datetime64):
        return np.datetime_as_string(date, unit='D')
    if isinstance(date,pd.Timestamp):
        return date.to_pydatetime().strftime('%Y-%m-%d')
    if isinstance(date,datetime.datetime):
        return date.strftime('%Y-%m-%d')
    logger.error("Date provided was of type " + str(type(date)) + ", which cannot be converted to text")
    raise ValueError
