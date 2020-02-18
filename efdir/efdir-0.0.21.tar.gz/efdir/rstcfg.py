import elist.elist as elel
from lxml.etree import XML as LXML
from nvhtml import engine
from efdir import r2x


def get_dir_list(ele):
    pl = []
    parent = ele.getparent()
    while(parent != None):
        if(parent.tag == 'list_item'):
            child = parent.getchildren()[0]
            pl = elel.unshift(pl,child.text)
        else:
            pass
        parent = parent.getparent()
    return(elel.join(pl,"/"))

def get_dirs(rst_str):
    xml_str = r2x.r2x(rst_str)
    root = LXML(xml_str)
    mat = engine.WFS(root).mat
    dirs = []
    for i in range(mat.__len__()):
        layer = mat[i]
        for each in layer:
            pl = each["pl"]
            if('paragraph' in pl):
                dir = get_dir_list(each["node"])
                dirs.append(dir)
            else:
                pass
    return(dirs)


