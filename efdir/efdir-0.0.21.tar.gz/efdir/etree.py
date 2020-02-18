from efdir.primitive import *
from efdir.etree import *
from lxml import etree
import elist.elist as elel

def abspath2etree(abspath):
    pl = abspath.split('/')
    pl = pl[1:]
    eles = elel.mapv(pl,lambda ele:etree.Element(ele))
    for i in range(len(eles)-1): 
        curr = eles[i]
        child = eles[i+1]
        curr.append(child)
    return(eles[-1])
    
def etree2abspath(ele):
    pl = [ele.tag]
    parent = ele.getparent()
    while(parent != None):
        pl.append(parent.tag)
        parent = parent.getparent()
    pl.append('')
    pl.reverse()
    abspath = elel.join(pl,'/')
    return(abspath)

def append_child(chtag,ele):
    chele = etree.Element(chtag)
    ele.append(chele)
    return(chele)

def disconn(ele):
    parent = ele.getparent()
    if(parent != None):
        parent.remove(ele)
    else:
        pass
    return(ele)


