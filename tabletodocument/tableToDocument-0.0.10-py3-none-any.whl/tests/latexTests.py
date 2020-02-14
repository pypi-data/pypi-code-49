import sys
sys.path.insert(1,'..')

import toDoc
import random
import pandas as pd

#toDoc.toTex('/home/pantelis-g/Documents/programming/tableToDocument/example.tex','a',[[2,3,4],[7,8,9],[11],123,[3,4,1,2]])


#toDoc.toTex('/home/pantelis-g/Documents/programming/tableToDocument/example.tex','b',{1:[2,3,4],'ba':[7,8,9],2:[11],'bab':123,3:[3,4,1,2]})

#toDoc.toTex('/home/pantelis-g/Documents/programming/tableToDocument/example.tex','a',pd.DataFrame({"cow":[1,16],"sheep":[2,12],"dog":[3,19],"cat":[4,10]}))

toDoc.toTex('/home/pantelis-g/Documents/programming/tableToDocument/example.tex','a',pd.Series({1:1,2:2,4:"bow",5:[1,2,3]}))
