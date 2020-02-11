from .node import *
class Color:
    orange="#edd2a7"
class QButton(Button):
    __secceed_name__=True
    style=StyleAttr(padding="0.25em",width="100%",background_color="#edd2a7")
    title="Qbutton"
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.click("alert('this is a QButton.')")
    def click(self,func):
        self.onclick=func
class QBox(Div):
    __secceed_name__=True
    style=StyleAttr(width="100%",height="100%",border="solid white 1px",min_height="25px",display="inline-block",margin="0 0 0 0",box_sizing="border-box")
    _class='Q-Box'
    def setHeight(self,height):
        self.css(height="%s"%height)
        return self
class QCell(Span):
    __secceed_name__=True
    style=StyleAttr(height="25px",width="25px",border="solid gray 1px")
class QTable(Table):
    __secceed_name__=True

class QRow(Div):
    __secceed_name__=True
    _class='row'
class QCol(Div):
    __secceed_name__=True
    _class='col'

