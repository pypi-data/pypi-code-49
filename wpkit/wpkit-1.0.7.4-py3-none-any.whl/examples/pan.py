from wpkit.pan import Pan
p=Pan('./myspace')
import wpkit
from wpkit.basic import PointDict
cmd=PointDict(op='newFile',params=PointDict(filename='test.html',location='./myspace',content="yes"))
p.execute(cmd)
cmd=PointDict(op='synch')
p.execute(cmd)