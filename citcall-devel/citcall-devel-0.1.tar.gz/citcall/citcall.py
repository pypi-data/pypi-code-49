import requests
import json
import re
import base64

class Citcall:
    """
    This is the Python Class client library for use Citcall's API. 
    To use this, you'll need a Citcall account and Your IP has been filtered in citcall system. 
    See citcall documentation for more information. This is currently a beta release. 
    """

    URL_CITCALL = "https://gateway.citcall.com"
    VERSION = "/v3"
    METHOD_SMS = "/sms"
    METHOD_SYNC_MISCALL = "/call"
    METHOD_ASYNC_MISCALL = "/asynccall"
    METHOD_VERIFY_MOTP = "/verify"

    
    def __init__(self, userid, apikey):
        """
        The constructor for Citcall class.

        Parameters :
            userid (str) : your userid
            apiker (str) : your apikey  
        """
        self.userid = userid
        self.apikey = apikey


    def sync_miscall(self, param):
        """
        Synchronous miscall

        Parameters :
            param (dict)
        Returns : 
            (dict)

        """
        if ("msisdn" in param.keys() and "gateway" in param.keys()):
            msisdn = param["msisdn"]
            gateway = param["gateway"]
            if (gateway > 5 or gateway < 0):
                ret = {
                    "rc":"06",
                    "info":"invalid gateway"
                }
                return ret
            else:
                _continue = False
                msisdn = self.clean_msisdn(msisdn)
                msisdn = re.sub('/[^0-9]/', '', msisdn)
                if (msisdn[0:2] == "62"):
                    if (len(msisdn) > 10 and len(msisdn) < 15):
                        prefix = msisdn[0:5]
                        if (msisdn > 13):
                            if (self.is_three(prefix)):
                                _continue = True
                        else:
                            _continue = True
                else:
                    if (len(msisdn) > 9 and len(msisdn) < 18):
                        _continue = True
                
                if (_continue):
                    param_hit = {
                        "msisdn":msisdn,
                        "gateway":gateway,
                    }
                    valid_verify = True
                    if ("valid_time" in param.keys()):
                        valid_time = param['valid_time']
                        if (isinstance(valid_time,int) and valid_time > 0):
                            if ("limit_try" in param.keys()):
                                limit_try = param["limit_try"]
                                if (not isinstance(valid_time, int) and valid_time <=0 ):
                                    valid_verify = False
                                else:
                                    param_hit["valid_time"] = valid_time
                                    param_hit["limit_try"] = limit_try
                        else:
                            valid_verify = False

                    
                    if (valid_verify):
                        method = "sync_miscall"
                        ret = self.send_request(param_hit,method)
                    else:
                        ret = {
                            "rc":"06",
                            "info":"invalid verify data"
                        }
                        return ret
                else:
                    ret = {
                        "rc":"06",
                        "info":"invalid verify data"
                    }
                    return ret
                
                return json.loads(ret)

    
    def async_miscall(self, param):
        """
        Asynchronous miscall

        Parameters :
            param (dict)

        Returns :
            (dict)
        """
        if ("msisdn" in param.keys() and "gateway" in param.keys()):
            msisdn = param["msisdn"]
            gateway = param["gateway"]

            if (gateway > 5 or gateway < 0):
                ret = {
                    "rc":"06", # 06
                    "info":"invalid gateway",
                }
                return ret
            else:
                _continue = False
                msisdn = self.clean_msisdn(msisdn)
                msisdn = re.sub('/[^0-9]/', '', msisdn)
                if (msisdn[0:2] == "62"):
                    if (len(msisdn) > 10 and len(msisdn) < 15):
                        prefix = msisdn[0:5]
                        if (len(msisdn) > 13):
                            if (self.is_three(prefix)):
                                _continue = True
                        else:
                            _continue = True
                else:
                    if (len(msisdn) > 9 and len(msisdn) < 18):
                        _continue = True
                

                if (_continue):
                    param_hit = {
                        "msisdn":msisdn,
                        "gateway":gateway,
                    }
                    valid_verify = True
                    if ("valid_time" in param.keys()):
                        valid_time = param["valid_time"]
                        if (isinstance(valid_time, int) and valid_time > 0):
                            if ("limit_try" in param.keys()):
                                limit_try = param["limit_try"]
                                if (not isinstance(valid_time, int) and valid_time <= 10):
                                    valid_verify = False
                                else:
                                    param_hit["valid_time"] = valid_time
                                    param_hit["limit_try"] = limit_try

                        else:
                            valid_verify = False

                    if (valid_verify):
                        method = "async_miscall"
                        ret = self.send_request(param_hit,method)
                    else:
                        ret = {
                            "rc":"06",
                            "info":"invalid verify data",
                        }
                        return ret

        else:
            return json.loads(ret)


    def sms(self, param):
        """
        SMS

        Parameters :
            param (dict)

        Returns :
            (dict)
        
        """
        if ("msisdn" in param.keys() and "senderid" in param.keys() and "text" in param.keys()):
            msisdn = param["msisdn"]
            senderid = param["senderid"]
            text = param["text"]
            list_baru = []
            _list = msisdn.split(",")
            for val in _list:    
                msisdn = self.clean_msisdn(val)
                msisdn = re.sub('/[^0-9]/', '', msisdn)
                if (msisdn[0:2] == "62"):
                    if (len(msisdn) > 10 and len(msisdn) < 15):
                        prefix = msisdn[0:5]
                        if (len(msisdn) > 13):
                            if (self.is_three(prefix)):
                                list_baru.append(msisdn)

                    else:
                        ret = {
                            "rc":"06",
                            "info":"invalid msisdn or msisdn has invalid format!",
                        }
                        return ret
                else:
                    if (len(msisdn) > 9 and len(msisdn) < 18):
                        list_baru.append(msisdn)
                    else:
                        ret = {
                            "rc":"06",
                            "info":"invalid msisdn or msisdn has invalid format!",
                        }
                        return ret

            msisdn = ",".join(list_baru)
            if (senderid.lower().strip() == "citcall"):
                senderid = senderid.upper()
            param_hit = {
                "msisdn":msisdn,
                "senderid":senderid,
                "text":text,
            }
            method = "sms"
            ret = self.send_request(param_hit, method)
        else:
            ret = {
                "rc":"88",
                "info":"missing parameter",
            }
            return ret

        return json.loads(ret)


    def verify_motp(self, param):
        """ 
        Verify Miscall OTP

        Parameters :
            param (dict)

        Returns :
            (dict)

        """
        if ("msisdn" in param.keys() and "trxid" in param.keys() and "token" in param.keys()):
            if (param["token"].isnumeric()):
                if (len(param["token"]) > 3):
                    msisdn = param["msisdn"]
                    trxid = param["trxid"]
                    token = param["token"]
                    _continue = False
                    msisdn = self.clean_msisdn(msisdn)
                    msisdn = re.sub('/[^0-9]/', '', msisdn)
                    if (msisdn[0:2] == "62"):
                        if (len(msisdn) > 10 and len(msisdn) < 15):
                            prefix = msisdn[0:5]
                            if (len(msisdn) > 13):
                                if (self.is_three(prefix)):
                                    _continue = True
                            else:
                                _continue = True
                    else:
                        if (len(msisdn) > 9 and len(msisdn) < 18):
                            _continue = True

                    if (_continue):
                        param_hit = {
                            "msisdn":msisdn,
                            "trxid":trxid,
                            "token":token,
                        }
                        method = "verify_otp"
                        ret = self.send_request(param_hit, method)
                    else:
                        ret = {
                            "rc":"06",
                            "info":"invalid mobile number"
                        }
                        return ret
                else:
                    ret = {
                        "rc":"06",
                        "info":"invalid token, token length minimum 4 digits",
                    }
                    return ret

            else:
                ret = {
                    "rc":"06",
                    "info":"invalid token, token length minimum 4 digits",
                }
                return ret

        else:
            ret = {
                "rc":"88",
                "info":"missing parameter",
            }
            return ret
        
        return json.loads(ret)

    
    def send_request(self, param, method):
        """
        Sending request to Citcall API

        Parameters :
            param (dict)
            method (str)

        Returns :
            res (str)

        """
        userid = self.userid
        apikey = self.apikey

        tmp_auth = userid + ":" + apikey
        auth = base64.b64encode(tmp_auth.encode())

        if (method == "sync_miscall"):
            action = Citcall.METHOD_SYNC_MISCALL
        elif (method == "async_miscall"):
            action = Citcall.METHOD_ASYNC_MISCALL
        elif (method == "sms"):
            action = Citcall.METHOD_SMS
        elif (method == "verify_otp"):
            action = Citcall.METHOD_VERIFY_MOTP
        else:
            # code
            pass

        url = Citcall.URL_CITCALL + Citcall.VERSION + action
        content = json.dumps(param)
        headers = {
            "Content-Type":"application/json",
	        "Authorization":auth,
            "Content-Length":str(len(content))
        }

        response = requests.post(url, data=content, headers=headers)
        res = response.text
        return res


    def clean_msisdn(self, msisdn):
        """
        Clean Msisdn

        Parameters :
            msisdn (str)

        Returns :
            msisdn (str)

        """
        if (msisdn[0:1] != "+"):
            msisdn = "+" + msisdn
        if (msisdn[0:2] == "+0"):
            msisdn = "+62" + msisdn[2:]
        if (msisdn[0:1] == "0"):
            msisdn = "+62" + a[2:]
        return msisdn


    def is_three(self, prefix):
        """
        Cek prefix is three

        Parameters :
            prefix (str)

        Returns :
            (boolean)
        """
        if (prefix == "62896"):
            return True
        elif (prefix == "62897"):
            return True
        elif (prefix == "62898"):
            return True
        elif (prefix == "62899"):
            return True
        elif (prefix == "62895"):
            return True
        else:
            return False






            


