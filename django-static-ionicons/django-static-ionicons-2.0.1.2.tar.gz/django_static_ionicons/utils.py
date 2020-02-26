import os
import re

app_root = os.path.dirname(__file__)
ionicons_css_filename = os.path.abspath(os.path.join(app_root, "./static/ionicons/css/ionicons.css"))

def get_ionicons():
    with open(ionicons_css_filename, "r", encoding="utf-8") as fobj:
        text = fobj.read()
    icons = list(set(re.findall("\.(ion[a-z\-]+):", text)))
    icons.sort()
    return icons
