
from chcko.chcko import conf
globals().update({k:v for k,v in conf.__dict__.items() if not k.startswith('__')})

