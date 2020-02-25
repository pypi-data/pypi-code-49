from __future__ import absolute_import

import os
from jpype import *

__cells_jar_dir__ = os.path.dirname(__file__)
addClassPath(os.path.join(__cells_jar_dir__, "lib", "aspose-cells-20.2.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "lib", "bcprov-jdk15on-160.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "lib", "JavaClassBridge.jar"))

__all__ = ['api']