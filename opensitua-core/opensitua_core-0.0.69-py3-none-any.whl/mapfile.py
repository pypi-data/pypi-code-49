# -------------------------------------------------------------------------------
# Licence:
# Copyright (c) 2012-2019 Luzzi Valerio 
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
#
# Name:        mapfile.py
# Purpose:
#
# Author:      Luzzi Valerio
#
# Created:     26/09/2019
# -------------------------------------------------------------------------------
from .strings import isstring
from .stime import strftime
import re, requests


def hexcolor(text):
    """
    hexcolor
    """
    if text.startswith("#"):
        return text
    else:
        text = re.sub(r',',' ',text)
        arr = text.split(' ')
        arr = [int(item) for item in arr]
        if len(arr)==3:
            return "%02x%02x%02x"%tuple(arr)
        if len(arr)==4:
            return "#%02x%02x%02x%02x"%tuple(arr)

    return text

def PixelOf(value,unit,style="solid"):

    if isstring(value):
        value = value.replace(",",".")
    if float(value)<=0.1 and style=="solid" :
        return 0.5
    elif unit=="Pixel":
        return round(float(value),2)
    elif unit =="MM":
        return round(float(value)*3.779,2)
    return -1


def GetMap( url, filemap, layerid, minx, miny, maxx, maxy, px, py=0, epsg=3857, filetif="" ):
    """
    GetMap - 92.76624232772798 (srtm pixelsize)
    """
    py = abs(py) if py > 0 else px
    filetif = filetif if filetif else strftime("GetMap%H%M%S.tif",None)
    minx,miny,maxx,maxy = float(minx),float(miny),float(maxx),float(maxy)
    width  = max(maxx,minx)-min(maxx,minx)
    height = max(maxy,miny)-min(maxy,miny)

    if epsg=="4326":
        deg = math.pi/180.0 * 6378137 # Circumference/360 ==>  2*math.pi*R/360 ==> math.pi/180 * R
        px *= deg
        py *= deg

    wx = round( width / px )
    wy = round( height / abs(py) )

    env = {
        "REQUEST":"GetMap",
        "SERVICE":"WMS",
        "VERSION":"1.3.0",
        "STYLE":"",
        "CRS":"EPSG:%s"%epsg,
        "FORMAT":"image/tiff",
        "MAP":filemap,
        "LAYERS":layerid,
        #"MAP":r'D:\Users\vlr20\Projects\GitHub\OpenGIS3\var\www\webgis\virtualraster\project\virtualraster.map',
        #"LAYERS":"merit_gfi_122fe139_1026_40de_8722_6ede8f94c259",
        "BBOX": "%s,%s,%s,%s"%(minx,miny,maxx,maxy),
        "WIDTH": wx,
        "HEIGHT":wy
    }

    r = requests.get(url, params=env, stream=True)

    if r.status_code == 200:
        with open(filetif, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        return filetif

    return False