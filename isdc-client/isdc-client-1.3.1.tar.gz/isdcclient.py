from io import StringIO, BytesIO

import requests

from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3.util.timeout import Timeout
from requests.adapters import HTTPAdapter


try:
    import pandas as pd
    have_pandas = True
except ImportError:
    have_pandas = False

try:
    import numpy as np
    have_numpy = True
except ImportError:
    have_numpy = False


def get_with_retries(url, params=None):
    s = requests.Session()

    timeout = Timeout(100, 100, 100)

    retries = Retry(total=10,
                    read=10,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])

    s.mount('http://', HTTPAdapter(max_retries=retries))

    return s.get(url, params=params, timeout=100).content.strip(b"\"\n").replace(b"\\n",b"\n")


class ISDCClient(object):

    def __init__(self,isdc_server="www.isdc.unige.ch"):
        self.isdc_server=isdc_server

    @property
    def isdc_url(self):
        return "https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/integralhk/api/v1.0/"
        #return "http://%s/~savchenk/spiacs-online/spiacs.pl"%self.isdc_server

    def genlc(self,target,utc,span,format=None, debug=True):
        url = self.isdc_url + "genlc/{target}/{t0_utc}/{dt_s}".format(target=target, t0_utc=utc, dt_s=span)
    
        if debug:
            print(url)

        lc_raw=get_with_retries(url)



        if format is None:
            return lc_raw

        if format == "numpy":
            if not have_numpy:
                raise Exception("need numpy installed to format as numpy")

            return np.genfromtxt(BytesIO(lc_raw.replace(b"\\n", b"").replace(b"<br>", b"")), invalid_raise=False)

        if format == "pandas":
            if not have_pandas:
                raise Exception("need pandas installed to format as pandas")

            if not have_pandas:
                raise Exception("need numpy installed to format as numpy")

            df=pd.read_csv(BytesIO(lc_raw.replace(b"\\n", b"").replace(b"<br>", b"")),
                           delim_whitespace=True,
                           names=["ijd","seconds_relative","counts","seconds_since_midnight"],
                           skiprows=5)
    
            if debug:
                print(df)
            df.seconds_relative-=float(span)
            return df

    def getscw(self,intime):
        #return get_with_retries(self.isdc_url+"?requeststring="+intime,params=dict(generate="scw",submit="Submit")).content[:12]
        return get_with_retries("https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/timesystem/api/v1.0/converttime/ANY/{}/SCWID".format(intime))

ic = ISDCClient()

def genlc(target,utc,span,format=None):
    return ic.genlc(target,utc,span,format)

def getscw(intime):
    return ic.getscw(intime)
