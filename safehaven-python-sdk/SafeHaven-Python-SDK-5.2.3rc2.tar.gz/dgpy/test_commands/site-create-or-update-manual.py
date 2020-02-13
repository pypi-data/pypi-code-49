#!/usr/bin/python
#
# Add a MANUAL site (which means a site that does not have
# cloud-specific API credentials).
#
from __future__ import print_function, absolute_import, unicode_literals
import sys
from dgpy.cms_client import CmsClient
from dgpy.errors     import GrpcError

if len(sys.argv) != 2:
    print("Usage: %s <site-name>" % sys.argv[0], file=sys.stderr)
else:
    try:
        res = CmsClient().site_update_manual(sys.argv[1])
    except GrpcError as e:
        print("Failed to add MANUAL site {0}: {1}".format(sys.argv[1], e))
    else:
        print("Adding MANUAL site {0} Job ID: {1}".format(sys.argv[1], res.job_id))
