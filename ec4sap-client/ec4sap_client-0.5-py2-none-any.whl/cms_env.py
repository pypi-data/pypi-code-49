# --------------------------------------------------------------------
# CMS REST-API - Configuration
# --------------------------------------------------------------------

from ec4sap import config

# --------------------------------------------------------------------
class CMS_ENV:

    api_url = None
    basic_auth = None
    oidb_token = None
    wfuser = None
    entityType = {}

    def __init__(self, name, auth=None, token=None):
        self.api_url = config.CFG_CMS_URL[name]
        self.basic_auth = auth
        self.oidb_token = token
        self.wfuser = config.CFG_CMS_WFUSER[name]
        self.entityType = config.CFG_CMS_ENTITY_TYPE[name]

# --------------------------------------------------------------------
CMS_INT = CMS_ENV(name="int", auth=("sapmgmt\SA-Int-elwistester","xlnsHDsJ7vj9zpuxH6Gl"))
CMS_PRD1 = CMS_ENV(name="prd", auth=("sapmgmt\SA-Prd-elwistester","z82BXBmmv0hGCI9c5ivj"))
CMS_PRD = CMS_ENV(name="prd", auth=("sapmgmt\SA-Prd-reporting","Bg2cEQ2YB2ERgeNeNOA7"))

