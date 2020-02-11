from blogging.model import Model, new_model
from blogging.types import *
import blogging.typing as tp

class Data(Model):
    test = StringType(set_separator=',')
    test3 = StringType(set_separator=',')
    test2 = StringType()
    test1: tp.zeek_set[tp.zeek_string]

d = Data(b'1,2,3', 2, 3, 4)
print(d)
# import blogging.typing as tp

# print(tp.zeek_set[tp.zeek_addr])
# print(tp.SetType[tp.zeek_addr])

t = new_model('Test', test=StringType())
d = t('1')
print(d)

class Foo(Model):
    test = RecordType(a=StringType())

print(Foo(**{'test.a': b'test'}))
print(Foo(test=dict(a=b'test')))
