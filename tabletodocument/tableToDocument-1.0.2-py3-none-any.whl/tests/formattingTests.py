import sys
sys.path.insert(1,'..')

import toDoc
import random

w = lambda x: [random.randint(40,100) for i in range(x)]

#Writing string at the end
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','a',"line at the bottom")

#Writing string at the beginning
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','b',"line at the beginning")

#writing string at specific lines
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',10,"line at the line 10")
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',2,"line at the line 2")
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',11,"line at the line 11")

#writing int at the bottom
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','a',1227)

#Writing int at the beginning
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','b',33)

#Writing int at specific lines
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',10,10)
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',4,4)
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',-2,-2)

#Writing list at the bottom
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','a',[[1,2,3],[5,6,7],[8,9,10],[11,11,11]])

#Writing list at the top
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','b',[[10,20,30,56],[5,6,7],[8,9,10],[11,11,11,14]])

#Writing at a specific line
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',3,[[10,20,30,56],[11,11,11,14]])
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',5,[[5,6,7],[8,9,10]])


#Writing dictionary at the bottom
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','a',{'a':[10,20,30,56],12:[5,6,7],'b':[8,9,10],14:[11,11,11,14]})

#Writing dictionary at the top
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','b',{'a':[10,20],'b':[30,56],1:[5,6,7],2:[8,9,10],3:[11,11],4:[11,14],'c':"believe"})

#Writing at specific lines
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',3,{"thor":[10,20,30,56],"thanos":[5,6,7],"doomsday":[8,9,10],"zoom":[11,11,11,14]})
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',6,{"drJones":[10,20,30,56],"x-men":[5,6,7],"superman":[8,9,10],"flash":[11,11,11,14]})

#Writing set at the end
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','a',{3,4,1,2})

#Writing set at the beginning
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt','b',{"cow","sheep","chicken","horse"})

#Writing set at specific line
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',33,{3,4,1,2})
#toDoc.toWord('/home/pantelis-g/Desktop/ps.odt',14,{"a","b","c"})
