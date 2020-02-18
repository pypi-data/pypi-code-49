# import json
# import os
#
import os

import LinkFusions as lf

lf.CLIENT_SECRET = 'RrAcveMhXdQC7rPMTqqzuLbe05zRtEVIM6HmV3U8DxlXTnJW3QPDQBZAymAh6TBmV9O1ie9U21xxrfhGVbBL5CuPQm5YaSxyImxcJIIBKOkAg28dlQZKWsnR2Mgb5MAb'
lf.CLIENT_ID = 'GPj7I9FxcybyHCEeZ50UQ84LMmjhTOU0MzlIIhjh'
lf.USER = 'admin@localhost.com'
lf.PASSWORD = 'greatness2011'

lf.__dev__ = 'local'

fusion = lf.LinkFusions()
# file = open(os.path.join(os.path.dirname(__file__), 'sample', 'me.png'), 'rb')
# fusion.Campaign.create(name='Damilola Next', logo=(file.name, file), company='Trasherd')
fusion.Campaign.list()