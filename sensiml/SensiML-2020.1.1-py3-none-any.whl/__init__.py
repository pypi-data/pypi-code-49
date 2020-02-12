from sensiml.client import SensiML
from sensiml.widgets import DashBoard


try:
    from IPython.core.display import HTML

    display(HTML("<style>.container { width:90% !important; }</style>"))
except:
    pass

name = "sensiml"


__version__ = "2020.1.1"
__all__ = ["SensiML", "DashBoard"]
