import os
import tempfile

from pptx_tools.creator import PPTXCreator
from pptx_tools.templates import TemplateExample

import pptx_tools.utils as utils
import pptx_tools.example as example

example.run()


# pp = PPTXCreator(TemplateExample())
# pp.add_slide("sdg4")
#
# my_path = os.path.dirname(os.path.abspath(__file__)) # ("delme.pdf")  # + "\\delme.pdf"
# filename = os.path.join(my_path, "delme.pdf")
# utils.save_as_pdf(pp.prs, filename)

# my_tempfile = tempfile.NamedTemporaryFile(mode="r+b", suffix="pptx", delete=False)
# pp.save(my_tempfile)
# my_tempfile.close()


# from comtypes.client import Constants, CreateObject
#
# powerpoint = CreateObject("Powerpoint.Application")
# pp_constants = Constants(powerpoint)

# print(my_tempfile.name)
# pres = powerpoint.Presentations.Open(my_tempfile.name)
# pres.SaveAs("d:\delme.pdf", pp_constants.ppSaveAsPDF)
#
# print(my_tempfile.name)


# tmp_shp = None
# try:
#     with NamedTemporaryFile(suffix='.shp', delete=False) as tmp_shp:
#
#         df.to_file(tmp_shp.name)  # Access .name here, assuming you need a str
#
#         ... do any other stuff with the file ...
# finally:
#     if tmp_shp is not None:
#         os.remove(tmp_shp.name)