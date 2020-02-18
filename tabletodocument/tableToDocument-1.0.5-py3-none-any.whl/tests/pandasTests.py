import sys
sys.path.insert(1,'..')

import toDoc
import pandas as pd


#Import Series at the end of the document
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','a',pd.Series({1:1,2:2,4:"bow",5:[1,2,3]}))

#Import series at the beginning of the document
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','b',pd.Series({1:6,2:12,3:18,4:"bow",5:[1,2,3]}))

#Import series at a specific line
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',5,pd.Series({1:10,2:20,4:"bow",5:[1,2,3],'a':19}))
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',8,pd.Series({'a':[2,4,5,11],'b':[46,8,None,12],"c":[77,36,45,None],"d":[3,4,1,2],'e':[88,3,6,1]}))

#Import dataframe at the bottom of the file
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','a',pd.DataFrame({'a':[1,2],'b':[2,4],"bow":[5,6],'sowl':[1,3]}))

#Import dataframe at the begining of the file
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','b',pd.DataFrame({'a':[1,2],'b':[2,4],"bow":[5,6],'sowl':[1,3]}))

#Import dataframe at a specific line
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',4,pd.DataFrame({'a':[1,2,9],'b':[2,4,9],"bow":[5,6,9],'sowl':[1,3,9]}))
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','b',pd.DataFrame({'a':[1,2],'b':[2,4],"bow":[5,6],'sowl':[1,3]}))
