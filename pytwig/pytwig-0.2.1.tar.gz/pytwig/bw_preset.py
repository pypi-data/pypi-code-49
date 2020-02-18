from pytwig import bw_file
from pytwig import bw_object

class BW_Preset_File(bw_file.BW_File):
	def __init__(self):
		super().__init__('preset')
		self.contents = bw_object.BW_Object(1377)

	def get_preset(self):
		return self.contents.get(5153)
