import time
from datetime import datetime
import json
import requests 
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
 
import math
class p_maintenance:
    
    def current():
        
        offsetI=512
        API_ENDPOINT =  "http://192.168.1.7/DataCollection/Api/DataAll"
#API_ENDPOINT = "http://pastebin.com/api/api_post.php"
# Software SPI configuration:
        CLK  = 11 #18
        MISO = 9 #23
        MOSI = 10 #24
        CS   = 8 #25
        mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
        print(datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f"))
        index = 1
        data = []
        while True:
            
            sumI=0;
            I_RATIO = 111.1 *((5000/1000.0) /1024) #5v5000 supply voltage
            Irs=I_RATIO*math.sqrt(sumI/1480)
            Power=Irs*220
            now = datetime.now()
            data.append({'Datetime':now.strftime("%m-%d-%Y %H:%M:%S.%f"),
              'Current':"{0:2f}".format(Irs),
              'Power':"{0:2f}".format(Power)})
            if index == 10000:
         
                r = requests.post(url = API_ENDPOINT, json = data)
                #index = 0
                print(now.strftime("%m-%d-%Y %H:%M:%S.%f"))
                data = []
                index = 0
            index = index + 1
    
    