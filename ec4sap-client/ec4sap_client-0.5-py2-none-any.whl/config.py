# --------------------------------------------------------------------
# Configuration for EC4SAP Clients
# --------------------------------------------------------------------

#
# Debug level
#
# ignore | default | error
#
CFG_DEBUG="ignore"

#
# Verify SSL Certificate
#
#
CFG_VERIFY_SSL=False

#
# Abiquo API Endpoints
#
#CFG_ABQ_URL_INT = "https://testportal.sap.cloudservice.swisscom.com/api"
CFG_ABQ_URL_INT = "https://ss008034.itoper.local/api"
CFG_ABQ_VERSION_INT = "4.5"

#CFG_ABQ_URL_PRD = "https://portal.sap.cloudservice.swisscom.com/api"
CFG_ABQ_URL_PRD = "https://ss002346.itoper.local/api"
CFG_ABQ_VERSION_PRD = "4.5"

CFG_ENV_DEFAULT = "int"

#
# CSV Export : Format of a row
#
# map with Column-Name / Column-Value
#
CSV_FORMAT_VM = [("FQDN", "fqdn"),
                 ("CREATED", "creationTimestamp"),
                 ("ABQ_ID", "name"),
                 ("VAPP", "virtualappliance"),
                 ("TENANT", "enterprise"),
                 ("CPU", "cpu"),
                 ("RAM", "ram"),
                 ("Backup", "backuppolicies"),
                 ("IP", "nic*")]

CSV_FORMAT_IP = [("IP", "ip"),
                 ("VDC", "virtualdatacenter"),
                 ("NETWORK", "networkName"),
                 ("VM", "usedBy")]
#
# vm filter
#
# for full list see: https://wiki.abiquo.com/api/latest/virtualmachine.html
#
CFG_VM_FILTER = {}
CFG_VM_FILTER["type"] = ["MANAGED","CAPTURED"]
#CFG_VM_FILTER["protected"] = [True,False]
#CFG_VM_FILTER["state"] = ["ON","OFF", "PAUSED", "CONFIGURED", "LOCKED", "NOT_ALLOCATED", "ALLOCATED", "UNKNOWN"]

#
# ip filter
#
# for full list see: https://wiki.abiquo.com/api/latest//privateip.html
#
CFG_IP_FILTER = {}
CFG_IP_FILTER["usedBy"] = ["*"]

# --------------------------------------------------------------------
#
# CMS API Endpoints
#
CFG_CMS_URL = {}
CFG_CMS_URL["int"] = "https://testportal.sap.cloudservice.swisscom.com/cms"
CFG_CMS_URL["prd"] = "https://portal.sap.cloudservice.swisscom.com/cms"

#
# CMS internal workflow user
#
# static user ids configured for int and prd (ask the orch team)
#
CFG_CMS_WFUSER = {}
CFG_CMS_WFUSER["int"] = [3,9]
CFG_CMS_WFUSER["prd"] = [14,15]

#
# CMS entity types
#

CFG_CMS_ENTITY_TYPE = {}
CFG_CMS_ENTITY_TYPE["int"] = {"FOLDER":"28"}
CFG_CMS_ENTITY_TYPE["prd"] = {"FOLDER":"28"}

#
# CMS platform id
#

CFG_CMS_PLATFORM_ID = {"int": "Platform_100",
                       "prd":"Platform_100"}

