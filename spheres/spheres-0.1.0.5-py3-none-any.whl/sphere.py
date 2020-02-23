from spheres import *

def Sphere(obj):
	return View(obj,\
		 		to_client=lambda view:\
				 	{"stars": [xyz.tolist() for xyz in spin_XYZ(view.get())],\
				 	 "phase": [1,0]},\
		 		from_client=lambda data: qt.Qobj(XYZ_spin(data["stars"])),\
		 		js_class="Sphere")