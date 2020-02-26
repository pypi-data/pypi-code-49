# --------------------------------------------------------------------
# CMS(-Orch) REST-API
# --------------------------------------------------------------------

# modules
import json
import requests
import dateutil.parser
from datetime import datetime


# --------------------------------------------------------------------
class CMS_ObjectItem:
    def __init__(self, data):
        if type(data) == str or type(data) == unicode:
            self.data = json.loads(data)
        else:
            self.data = data

    def __dir__(self):
        return dir(type(self)) + self.data.keys()

    def __getattr__(self, key):
        if key in self.data:
            if type(self.data[key]) == dict or (type(self.data[key]) == unicode and (self.data[key]).startswith('{')): return CMS_ObjectItem(self.data[key])
            else: return self.data[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.data

    def __str__(self):
        return json.dumps(self.data)

    def __eq__(self, other):
        if other is None: return False
        return self.data == other.data

    def __ne__(self, other):
        return not self.__eq__(other)

    def dump(self):
        return json.dumps(self.data, indent=4)

# --------------------------------------------------------------------
# General CMS Object
# --------------------------------------------------------------------
class CMS_Object:

    def __init__(self, env, headers=None, verify=True):
        self.env = env
        self.url = env.api_url
        self.auth = env.basic_auth
        self.headers = {self.url: headers}
        self.verify = verify
        self.session = requests.session()
        self.data = None
        self.status_code = 200

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __dir__(self):
        return dir(type(self)) + self.data.keys()

    def hasData(self):
        try:
            return len(self)>0
        except:
            return False

    def dump(self):
        return json.dumps(self.data, indent=4)

    def getNext(self, id=None, params=None, headers=None):
        return self._request('get', self.url)

    def get(self, id=None, filter=None, order=None, max=None):
        uri = self.req_url
        params = {}
        if id != None: uri = "%s(%s)" % (uri,id)
        if filter != None: params["$filter"] = filter
        if order != None: params["$orderby"] = order
        if max != None: params["$top"] = max
        return self._request('get', self.url+uri,params=params)

    def post(self, uri="", params=None, headers=None, data=None):
        return self._request('post', self.url+self.req_url+uri,
            params=params, headers=headers, data=data)

    def delete(self, uri="", params=None, headers=None, data=None):
        return self._request('delete', self.url+self.req_url+uri,
            params=params, headers=headers, data=data)

    def _request(self, method, url, params=None, headers=None, data=None):
        parent_headers = self.headers[url] if url in self.headers else {}
        response = self.session.request(method,
                                        url,
                                        auth=self.auth,
                                        params=params,
                                        data=data,
                                        verify=self.verify,
                                        headers=self._merge_dicts(parent_headers, headers))
        self.data = None
        if len(response.text) > 0:
            try:
                self.data = response.json()
            except ValueError:
                pass
        self.status_code = response.status_code
        if response.status_code != 200:
            print "[ERROR] %s - %s" % (response.status_code, response.reason)
            print response.url
            print response.text
        return self

    def _merge_dicts(self, x, y):
        new_dict = {}
        if x:
            new_dict.update(x)
        if y:
            new_dict.update(y)
        return new_dict

    def __getitem__(self, item):
        if self.data != None:
            if "value" in self.data:
                return CMS_ObjectItem(self.data["value"][item])
            else:
                return CMS_ObjectItem(self.data)
        else:
            return None

    def __len__(self):
        try:
            return len(self.data["value"])
        except:
            return 0
            #return 1 if self.data != None else 0

    def __getattr__(self, key):
        try:
            if key in self.__dict__: return self.__dict__[key]
            else: return self.__getitem__(0).__getattr__(key)
        except:
            return None

    def __iter__(self):
        try:
            if "value" in self.data:
                for json in self.data['value']:
                    yield CMS_ObjectItem(json)
                while self.nextPage():
                    for json in self.data['value']:
                        yield CMS_ObjectItem(json)
            else:
                yield CMS_ObjectItem(self.data)
        except KeyError:
            raise TypeError('object is not iterable')


    def _hasMore(self):
        try:
            return "odata.nextLink" in self.data
        except:
            return False

    def nextPage(self):
        if not self._hasMore(): return False
        self.url = self.data["odata.nextLink"]
        self.getNext()
        return True

# --------------------------------------------------------------------
class CMS_EntityKind(CMS_Object):
    req_url = "/Core/EntityKinds"

# --------------------------------------------------------------------
class CMS_Tenant(CMS_Object):
    req_url = "/Core/Tenants"

    def getByAbqId(self, tenantId):
        t = self.get(filter="ExternalId eq 'admin/enterprises/%s'" % tenantId)
        self.data = t.data
        return self

    def impersonationHeader(self):
        return {"Biz-Dfch-Tenant-Id":self[0].Id}

    def getTenantManagerInformation(self):
        response = self.post(uri="/Current", headers=self.impersonationHeader())
        return response

# --------------------------------------------------------------------
class CMS_Folder(CMS_Object):
    req_url = "/Core/Folders"

    def getForVM(self, id):
        f = self.get(filter="Name eq '%s'" % id)
        self.data = f.data
        return self

    def getNodes(self):
        n = CMS_Node(self.env)
        try: return n.get(filter="ParentId eq %s" % self[0].Id)
        except: return n

    def getJobs(self):
        j = CMS_Job(self.env)
        try: return j.get(filter="RefId eq '%s'" % self[0].Id)
        except: return j

    def registerVM(self, name, tenantId, vdcId, vappId, vmId, platformId="Platform_100", description=None):
        # set tenant
        tenant = CMS_Tenant(self.env).getByAbqId(tenantId).getTenantManagerInformation()
        # todo: test if tenant is valid or raise error

        # create folder
        ts = str(datetime.now())
        rdp = {"platformId":platformId,
                 "virtualMachineHref":"cloud/virtualdatacenters/%s/virtualappliances/%s/virtualmachines/%s"%(vdcId,vappId,vmId)}
        rd = {"Name":name,
              "Description":description,
              "EntityKindId":self.env.entityType["FOLDER"],
              "ParentId":tenant.NodeId,
              "Parameters":str(rdp),
              "CreatedById":"1",
              "ModifiedById":"1",
              "Created": ts,
              "Modified": ts,
              "Tid": tenant.Id
              }
        rp = {"Tenant-Id":"admin/enterprises/%s"%tenantId, "Platform_Id":platformId}
        response = self.post(params=rp, data=rd, headers=tenant.impersonationHeader())

        # load folder
        self.getForVM(name)
        if not self.hasData():
            # rollback folder
            # raise error
            return
        folderId = self[0].Id

        # create external node
        rd = {"ExternalId":"cloud/virtualdatacenters/%s/virtualappliances/%s/virtualmachines/%s"%(vdcId,vappId,vmId),
              "ExternalType":platformId,
              "CreatedById":"1",
              "ModifiedById":"1",
              "Created": ts,
              "Modified": ts,
              "Tid": tenant.Id,
              "Name":name,
              "NodeId":long(folderId)}
        externalNode = CMS_ExternalNode(self.env)
        response = externalNode.post(params=rp, data=rd, headers=tenant.impersonationHeader())

        # create entity bag for os type
        rd = {"EntityId":folderId,
              "EntityKindId":1,
              "CreatedById":"1",
              "ModifiedById":"1",
              "Created": ts,
              "Modified": ts,
              "Tid": tenant.Id,
              "Name":name,
              "Name":"OS",
              "Type":"FACT",
              "Value":"RHEL_64"}
        entityBag = CMS_EntityBag(self.env)
        response = entityBag.post(params=rp, data=rd, headers=tenant.impersonationHeader())

        # create entity bag for os version
        rd = {"EntityId":folderId,
              "EntityKindId":1,
              "CreatedById":"1",
              "ModifiedById":"1",
              "Created": ts,
              "Modified": ts,
              "Tid": tenant.Id,
              "Name":name,
              "Name":"OS.Version",
              "Type":"FACT",
              "Value":"7"}
        response = entityBag.post(params=rp, data=rd, headers=tenant.impersonationHeader())

        # create entity bag for use of swisscom template
        rd = {"EntityId":folderId,
              "EntityKindId":1,
              "CreatedById":"1",
              "ModifiedById":"1",
              "Created": ts,
              "Modified": ts,
              "Tid": tenant.Id,
              "Name":name,
              "Name":"SwisscomTemplate",
              "Type":"FACT",
              "Value":"true"}
        response = entityBag.post(params=rp, data=rd, headers=tenant.impersonationHeader())

# --------------------------------------------------------------------
class CMS_ExternalNode(CMS_Object):
    req_url = "/Core/ExternalNodes"

# --------------------------------------------------------------------
class CMS_EntityBag(CMS_Object):
    req_url = "/Core/EntityBags"


# --------------------------------------------------------------------
class CMS_Node(CMS_Object):
    req_url = "/Core/Nodes"

    def getSubNodes(self):
        n = CMS_Node(self.env)
        try: return n.get(filter="ParentId eq %s" % self[0].Id, order="Created desc")
        except: return n

    def getForVM(self, id):
        return self.get(filter="Name eq '%s'" % id)

    def getJobs(self):
        j = CMS_Job(self.env)
        try: return j.get(filter="RefId eq '%s'" % self[0].Id)
        except: return j

    def getState(self):  # same as getJobs but sounds better
        return self.getJobs()

    def getCredentials(self):
        return CMS_Credentials(self.env).getForVM(self.Name)

    def getOrders(self):
        return CMS_Order(self.env).getForVM(self[0].Id)

# --------------------------------------------------------------------
class CMS_Job(CMS_Object):
    req_url = "/Core/Jobs"

    def getForNode(self, obj):
        return self.get(filter="RefId eq '%s'" % obj.Id, order="Created desc")

    def hasError(self):
        e = self.Error
        return type(e)!=unicode and e.Succeeded==False

# --------------------------------------------------------------------
class CMS_Credentials(CMS_Object):
    req_url = "/Core/ManagementCredentials"

    def getForVM(self, id):
        return self.get(filter="substringof('%s',Description) eq true" % id, order="Created desc")

# --------------------------------------------------------------------
class CMS_Order(CMS_Object):
    req_url = "/Diagnostics/AuditTrails"

    def getForVM(self, id):
        return self.get(filter="substringof('Node.Id\":\"%s\"',Parameters) eq true" % id, order="Created desc")

# --------------------------------------------------------------------
class CMS_User(CMS_Object):
    req_url = "/Core/Users"

    def getCreator(self, obj):
        return self.get(obj.CreatedById)

    def getModifier(self, obj):
        return self.get(obj.ModifiedById)

# --------------------------------------------------------------------
class CMS_AuditTrail(CMS_Object):
    req_url = "/Diagnostics/AuditTrails"


# --------------------------------------------------------------------
class CMS_ArchivedWorkflow():

    def __init__(self, env, order):
        # start of workflow (job add)
        self.workflow = []
        self.workflow.append(order)
        self.message = ""
        self.os = "n.a."
        self.product = ""
        self.category = ""

        # load and analyze node
        self.node = CMS_AuditTrail(env).get(filter="EntityId eq '%s' and EntityType eq 'Node'" % order.Current.RefId, order="Id asc", max=1)

        name = self.node.Name
        if "Red Hat" in name or "RHEL" in name: self.os = "RHEL"
        elif "SUSE" in name or "SLES" in name: self.os = "SLES"
        elif "WIN2" in name or "Windows" in name or "Ready Win" in name: self.os = "Windows"

        # analyze product category
        if self.os != "n.a.":
            self.category = "MOS"
            self.product = "MOS %s" %self.os

        if "SAP Ready" in name:
            self.category = "SAP Ready"
            self.product = "SAP Ready %s" % self.os
        if "FS Config" in name:
            self.category = "SAP Ready FS"
            self.product = "SAP Ready FS %s" % self.os
        if "Agent Based Backup" in name:
            self.category = "ABB"
            if "Networker" in name:
                self.product = "ABB Networker"
            else:
                self.product = "ABB Avamar"

        # load workflow steps (job modify)
        jobs = CMS_AuditTrail(env).get(filter="EntityType eq 'Job' and EntityId eq '%s' and Id gt %s and EntityState eq 'Modified' and Name ne 'biz.dfch.CS.Appclusive.Core.OdataServices.Core.Node'" % (order.EntityId, order.Id), order="Id asc", max=10)
        for r in jobs:
            if int(r.CreatedById) in env.wfuser and r.Name != "Deleted" and not str(r.Name).startswith("Backup"):
                self.workflow.append(r)
            else:
                break


        # analyze result
        job = self.workflow[-1]
        if job.EntityState == "Modified" or job.EntityState == "Deleted":
            if "Error" in job.Current:
                self.result = "Error"
                self.message = str(job.Current.Error.Message).replace('\n', '|')
            elif str(job.Name).startswith("Workflow failed"):
                self.result = "Error"
                self.message = str(job.Name).replace('\n', '|')
            elif str(job.Current.Name).startswith("Workflow succeeded") or str(job.Name).startswith(
                    "Workflow succeeded"):
                self.result = "Ok"
            else:
                self.result = "unknown"

    def __dir__(self):
        return dir(type(self)) + ["id"]

    def __getattr__(self, key):
        if key == "id": return self.workflow[0].EntityId
        if key == "vm": return self.workflow[0].Current.ConditionParameters.vm.name
        if key == "start": return dateutil.parser.parse(self.workflow[0].Created)
        if key == "end": return dateutil.parser.parse(self.workflow[-1].Created)
        if key == "steps": return len(self.workflow)
        if key == "step": return self.workflow
        if key == "name": return self.node.Name

        if key in self.__dict__: return self.__dict__[key]
        return None

# --------------------------------------------------------------------
class CMS_ArchivedOrder(CMS_Object):
    req_url = "/Diagnostics/AuditTrails"

    def get(self, id=None, filter=None, order="Id asc", max=None):
        f = "CreatedById eq 1 and EntityType eq 'Job' and EntityState eq 'Added' and Name eq 'biz.dfch.CS.Appclusive.Core.OdataServices.Core.Node'"
        if filter!=None: f = f + " and " + filter
        return CMS_Object.get(self, id, filter=f, order=order, max=max)

# --------------------------------------------------------------------
class CMS_ArchivedChangeWorkflow():

    def __init__(self, env, order):
        # start of workflow (job add)
        self.workflow = []
        self.workflow.append(order)
        self.message = ""
        self.os = "n.a."
        self.product = ""
        self.category = ""

        # load workflow steps (job modify)
        jobs = CMS_AuditTrail(env).get(filter="EntityType eq 'Job' and EntityId eq '%s' and Id gt %s and EntityState eq 'Modified' and Name ne 'biz.dfch.CS.Appclusive.Core.OdataServices.Core.Node'" % (order.EntityId, order.Id), order="Id asc", max=10)
        print "--------------------------------------------------------"
        print order.dump()
        for r in jobs:
            if int(r.CreatedById) in env.wfuser and r.Name != "Deleted":
                self.workflow.append(r)
                print r.dump()
            else:
                break


        # analyze result
        job = self.workflow[-1]
        if job.EntityState == "Modified" or job.EntityState == "Deleted":
            if "Error" in job.Current:
                self.result = "Error"
                self.message = str(job.Current.Error.Message).replace('\n', '|')
            elif str(job.Name).startswith("Workflow failed"):
                self.result = "Error"
                self.message = str(job.Name).replace('\n', '|')
            elif str(job.Current.Name).startswith("Workflow succeeded") or str(job.Name).startswith(
                    "Workflow succeeded"):
                self.result = "Ok"
            else:
                self.result = "unknown"

    def __dir__(self):
        return dir(type(self)) + ["id"]

    def __getattr__(self, key):
        if key == "id": return self.workflow[0].EntityId
        if key == "vm": return self.workflow[0].Current.ConditionParameters.vm.name
        if key == "start": return dateutil.parser.parse(self.workflow[0].Created)
        if key == "end": return dateutil.parser.parse(self.workflow[-1].Created)
        if key == "steps": return len(self.workflow)
        if key == "step": return self.workflow
        if key == "name": return self.node.Name

        if key in self.__dict__: return self.__dict__[key]
        return None

# --------------------------------------------------------------------
class CMS_ArchivedChange(CMS_Object):
    req_url = "/Diagnostics/AuditTrails"

    def get(self, id=None, filter=None, order="Id asc", max=None):
        f = "CreatedById gt 15 and EntityType eq 'Job' and EntityState eq 'Modified' and substringof('\"Condition\":\"\"', Current) eq false and substringof('\"Error\":\"\"', Current) eq false"
        if filter!=None: f = f + "and " + filter
        return CMS_Object.get(self, id, filter=f, order=order, max=max)

