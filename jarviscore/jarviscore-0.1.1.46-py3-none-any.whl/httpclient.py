from requests import get, patch, put, post
from .settings import Settings
from .log import Log
from .model import Model
from .errors import DBConnectionUndefined
from urllib import parse

class WebResponse():
    def __init__(self, data:dict):
        self.status = data["status"]
        self.message = data["message"]
        self.code = data["code"]
        self.text = data["text"]
        self.json = data["json"]

    def __repr__(self):
        return f"[{self.status}]({self.message}): {self.text}"


class HTTPClient():

    def __init__(self, owner:str, db_user=None, db_pass=None):
        self.log = Log("Web Handler", f"Web Handler: {owner}")
        self.useModel = False
        if db_user is not None and db_pass is not None:
            self.model = Model(user=db_user, password=db_pass)
            self.useModel = True

    def GetFromTwitch(self, url: str) -> dict:
        headers = self.__get_twitch_headers(url)
        return self.Get(url, headers=headers)

    def GetFromDiscord(self, url: str) -> dict:        
        headers = self.__get_discord_headers()
        return self.Get(url, headers=headers)

    def PostFormToTwitch(self, url:str,  body: dict):
        headers = self.__get_twitch_headers(url)
        return self.PostForm(url=url, body=body, headers=headers)

    def PostFormToDiscord(self, url:str,  body: dict):
        headers = self.__get_discord_headers()
        return self.PostForm(url=url, body=body, headers=headers)

    def PostJSONToTwitch(self, url:str,  body: dict):
        headers = self.__get_twitch_headers(url)
        return self.PostJSON(url=url, body=body, headers=headers)

    def PostJSONToDiscord(self, url:str,  body: dict):
        headers = self.__get_discord_headers()
        return self.PostJSON(url=url, body=body, headers=headers)



    def Get(self, url: str, headers: dict = None) -> dict:
        """Get request"""           
        self.log.debug(f"Sending new GET request to '{url}'.")
        try:
            response = get(url=url, headers=headers)
        except Exception as ex:
            return self.__exception_response(str(ex))
        rt = self.__process_response(response)
        self.log.debug("returning: \n{}".format(rt))
        return rt


    
    def PostForm(self, url:str,  body: dict, headers: dict = None):
        if headers is None:
            setting = Settings()
            headers = {
                "Client-ID": setting.get_setting("tokens.twitch.user"), 
                "content-type": 'application/x-www-form-urlencoded', 
            }
        self.log.debug(f"Sending new POST request to '{url}'.")
        try:
            response = post(url=url, headers=headers, data=body)
        except Exception as ex:
            return self.__exception_response(str(ex))
        rt = self.__process_response(response)
        self.log.debug("returning: \n{}".format(rt))
        return rt
    
    def PostJSON(self, url:str,  body: dict, headers: dict = None):
        if headers is None:
            setting = Settings()
            headers = {
                "Client-ID": setting.get_setting("tokens.twitch.user"), 
                "content-type": 'application/json', 
            }
        self.log.debug(f"Sending new POST request with JSON body to '{url}'.")
        response = post(url=url, headers=headers, json=body)
        try:
            rt = self.__process_response(response)
        except Exception as ex:
            return self.__exception_response(str(ex))
        self.log.debug("returning: \n{}".format(rt))
        return rt
    
    def __exception_response(self, message):
        self.log.warn("An exception occrred when attempting to contact the server. Exception: " + message)
        return WebResponse ({
            "status": "error",
            "message": "an exception occurred when attempting to contact server.",
            "code": 600,
            "text": message,
            "json": {"error": message}
        })


    def __process_response(self, response):
        if response.status_code == 200:
            self.log.debug("Response: 200 | OK")
            return WebResponse ({
                "status": "ok",
                "message": "response ok",
                "code": response.status_code,
                "text": response.text,
                "json": response.json()
            })
        elif response.status_code == 201:
            self.log.debug("Response: 201 | OK")
            return WebResponse ({
                "status": "ok",
                "message": "no data returned",
                "code": response.status_code,
                "text": "No Data",
                "json": {"No Data"}
            })
        elif response.status_code == 202:
            self.log.debug("Response: 202 | Accepted")
            return WebResponse ({
                "status": "ok",
                "message": "accepted",
                "code": response.status_code,
                "text": "No Data",
                "json": {"No Data"}
            })
        elif response.status_code == 204:
            self.log.debug("Response: 204 | No Content")
            return WebResponse ({
                "status": "ok",
                "message": "no content",
                "code": response.status_code,
                "text": "No Data",
                "json": {"No Data"}
            })
        elif response.status_code == 400:
            self.log.info("Response: 400 | Bad Request")
            return WebResponse ({
                "status": "error",
                "message": "bad request",
                "code": response.status_code,
                "text": response.text,
                "json": response.json()
            })
        elif response.status_code == 401:
            self.log.info("Response: 401 | Unauthorised Request")
            return WebResponse ({
                "status": "error",
                "message": "unauthorised request",
                "code": response.status_code,
                "text": response.text,
                "json": response.json()
            })
        elif response.status_code == 404:
            self.log.info("Response: 404 | Resource not found")
            return WebResponse ({
                "status": "error",
                "message": "resource not found",
                "code": response.status_code,
                "text": response.text,
                "json": response.json()
            })
        else:
            self.log.error("Response: {} | Error Response\n{}".format(response.status_code, response.text))
            return WebResponse ({               
                "status": "error",
                "message": "server returned an error",
                "code": response.status_code,
                "text": response.text,
                "json": response.json()
            })

    def __get_twitch_headers(self, url: str) -> dict:
        setting = Settings()
        if not self.useModel:
            headers = {
                "Client-ID" : setting.get_setting("tokens.twitch.user"),   
            }
        else:
            jOAUTH = self.model.fetchOne("select t.AccessToken\
                from Tokens t inner join Identity u on t.IdentityID = u.IdentityID\
                where u.TwitchID = '181055138' and t.TokenType = 'Twitch'")
            if "kraken" in url:
                headers = {
                    "Client-ID" : setting.get_setting("tokens.twitch.user"),
                    "Authorization": "OAuth " + jOAUTH[0],
                    "Accept": "application/vnd.twitchtv.v5+json"
                }
            else:
                headers = {
                    "Client-ID" : setting.get_setting("tokens.twitch.user"),
                    "Authorization": "Bearer " + jOAUTH[0]
                }
        return headers

    
    def __get_discord_headers(self) -> dict:
        setting = Settings()
        headers = {
            "Client-ID": "{}".format(setting.get_setting("integration.discord.client")),
            "User-Agent": setting.get_setting("integration.discord.agent"),
            "Authorization": "Bot {}".format(setting.get_setting("integration.discord.key"))
        }
        return headers