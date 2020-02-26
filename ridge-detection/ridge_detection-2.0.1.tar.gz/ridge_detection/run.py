"""
MIT License

Copyright (c) 2020 Max Planck Institute of Molecular Physiology

Author: Luca Lusnig (luca.lusnig@mpi-dortmund.mpg.de)
Author: Thorsten Wagner (thorsten.wagner@mpi-dortmund.mpg.de)
Author: Markus Stabrin (markus.stabrin@mpi-dortmund.mpg.de)
Author: Fabian Schoenfeld (fabian.schoenfeld@mpi-dortmund.mpg.de)
Author: Tapu Shaikh (tapu.shaikh@mpi-dortmund.mpg.de)
Author: Adnan Ali (adnan.ali@mpi-dortmund.mpg.de)


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from ridge_detection.lineDetector import LineDetector
from ridge_detection.params import Params
from ridge_detection.basicGeometry import reset_counter
from ridge_detection.helper import displayContours,save_to_disk
from datetime import datetime
from PIL import Image
from  mrcfile import open as mrcfile_open
import logging


def run(param,folder_save_out="."):
    start=datetime.now()
    day,hour=str(start).replace("-","").replace(":","").split(" ")
    logging.basicConfig(filename="ridge_detection_"+day+"_"+hour.split(".")[0]+'.log',filemode='w', level=logging.DEBUG)
    logging.info(" STARTING TIME: "+ str(start))

    params = Params(param)

    logging.info("params loaded from '"+param["path_to_file"]+"'")
    logging.info(params)

    try:
        img=mrcfile_open(param["path_to_file"]).data
    except ValueError:
        img=Image.open(param["path_to_file"])
    reset_counter()

    detect = LineDetector(params=param)
    result = detect.detectLines(img)
    resultJunction =detect.junctions
    out_img,img_only_lines = displayContours(params,result,resultJunction)
    if params.get_saveOnFile() is True:
        save_to_disk(out_img,img_only_lines,folder_save_out=folder_save_out)

    logging.info(" FINAL TIME: "+ str(datetime.now()))
    logging.info(" TOTAL EXECUTION TIME: " + str(datetime.now()-start))
