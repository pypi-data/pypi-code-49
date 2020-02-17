import numpy as np

from innolab_utils.pylon_camera_dll.Test.traces_gui import IndexGUI


file_path = "C:\\Users\\maxim.kuzminsky\\Desktop\\spot_test.csv"
app = IndexGUI(file_path)
app.root.mainloop()

