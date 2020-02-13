#!/usr/bin/python
#
# Print the list of all registered CMS users.
#
from __future__ import print_function, absolute_import, unicode_literals
from dgpy.cms_client import CmsClient

print("Registered CMS users:")
for i, user in enumerate(CmsClient().user_list()):
    print("#%d: %s" % (i, user))
