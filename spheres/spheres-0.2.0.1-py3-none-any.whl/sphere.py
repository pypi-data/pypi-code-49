from spheres import *

def Sphere(obj):
	return View(obj,\
		 		to_client=lambda view:\
				 	{"stars": spin_XYZ(view),\
				 	 "phase": [1,0]},\
		 		from_client=lambda data: XYZ_spin(data["stars"]),\
		 		js_class="Sphere")