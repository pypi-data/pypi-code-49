# --------------------------------------------------------------------
# Abiquo REST-API
# --------------------------------------------------------------------

# modules
import collections
import csv
import io
import json
from collections import OrderedDict
from abiquo.client import Abiquo, ObjectDto
from abiquo_env import ABIQUO_ENV
from ec4sap import config



# --------------------------------------------------------------------
class ABQ_Cache:
    
    def __contains__(self,key):
        return key in self.__dict__
        
    def __getattr__(self,key):
        try:
            if key in self.__dict__:
                return self.__dict__[key]
        except:
            return None
        
    def __setattr__(self,key,value):
        self.__dict__[key] = value

    def __dir__(self):
        d = []
        for key in self.__dict__: d.append(key)
        return d

    def remove(self, key):
        try:
            self.__dict__.pop(key,None)
        except:
            pass

# --------------------------------------------------------------------
class ABQ_Object:
    req_accept = "application/json"
    req_accept_list = "application/json"
    req_url = ""
    data = None
    dataList = []
    env = None
    response = 0
    respMessage = ""
    respHasError = False

    
    def __init__(self, obj, data):
        self.env = obj.env
        self.req_url = obj.req_url
        self.req_accept = obj.req_accept
        self.req_accept_list = obj.req_accept_list
        self.data = data

    def __repr__(self):
        try:
            return "URL:%s, Type: %s" % (self.req_url, self.req_accept)
        except:
            return "<???>"

    def __str__(self):
        try:
            return "URL:%s, Type: %s" % (self.req_url, self.req_accept)
        except:
            return "<???>"


    def clone(self, obj):
        self.env = obj.env
        self.data = obj.data
        return self

    def _analyzeResponse(self):
        self.respHasError = False
        self.respMessage = "ok"
        if self.response > 299:
            try:
                self.respMessage = self.data.json['collection'][0]['message']
            except:
                self.respMessage = "API request failed"
            self.respHasError = True


    def _get(self, url="", isList=False):
        api = Abiquo(url if url.startswith("http") else self.env.api_url + url, auth=self.env.getOAuth(), verify=config.CFG_VERIFY_SSL)
        p = {"limit":"10000"}
        self.response, self.data = api.get(headers={'Accept': (self.req_accept_list if isList else self.req_accept) + "; version=%s" % self.env.api_version}, params=p)
        self._analyzeResponse()
        return self

    def get(self, id=0):
        url = (self.req_url+"/%s" % id) if id>0 else self.req_url
        return self._get(url)

        
    def getAll(self, pdata=None, link=None, filter=None, filterMap=None, keys=None, meta=None):
        fPar = "has"
        fVal = None
        csvkeys = OrderedDict(keys) if keys!=None else None
        if filter != None:
            fa = filter.split("=")
            if len(fa)>1:
                fPar = fa[0]
                fVal = fa[1]
            else:
                fVal = filter
         
        if pdata == None:
            url = (self.req_url+"?%s=%s" % (fPar,fVal)) if filter!=None else self.req_url
            self._get(url, isList=True)
        else:
            self.response, self.data = pdata.follow(link).get(params={fPar:fVal, "limit": "64000"})
        self._analyzeResponse()
        self.dataList = []
        if self.data != None:
            for js in self.data.json['collection']:
                item = ObjectDto(js, auth=self.data.auth, verify=self.data.verify)
                if meta!=None:
                    item.json.update(meta)
                if self.isInFilter(item,filterMap):
                    if csvkeys != None:
                        row = collections.OrderedDict()
                        for k in csvkeys:
                            try: row[k] = "%s" % self._csvValue(js, csvkeys[k])
                            except: row[k] = ""
                        self.dataList.append(row)
                    else:
                        self.dataList.append(item)
        return self

    def match(self, pattern, text):
        if pattern == text: return True
        if len(pattern) > 1 and pattern[0] == '*' and len(text) == 0: return False
        if len(pattern) != 0 and pattern[0] == '*': return self.match(pattern[1:], text) or self.match(pattern, text[1:])
        return False

    def isInFilter(self, obj=None, filtermap=None):
        if obj == None: return False
        if filtermap == None: return True
        for key in filtermap.keys():
            try:
                val = obj.__getattr__(key)
                if "*" not in filtermap[key] and val not in filtermap[key]: return False
            except:
                return False
        return True

    def count(self):
        return len(self.dataList)
        
    def item(self, index=0):
        return ABQ_Object(self,self.dataList[index])
    
    def csvHeader(self, csv_delimiter=';', csv_quote='"'):
        si = io.BytesIO()
        cw = csv.writer(si, delimiter=csv_delimiter, quotechar=csv_quote, quoting=csv.QUOTE_MINIMAL)
        cw.writerow(self.dataList[0].keys())
        return si.getvalue().strip("\r\n")
    
    def csvRow(self, index=0, csv_delimiter=';', csv_quote='"'):
        si = io.BytesIO()
        cw = csv.writer(si, delimiter=csv_delimiter, quotechar=csv_quote, quoting=csv.QUOTE_MINIMAL)
        row = self.dataList[index].values()
        row = [s.encode('utf-8') for s in row]
        cw.writerow(row)
        return si.getvalue().strip("\r\n")       
    
    def _csvValue(self, js, key):
        try:
            if key.endswith("*"):
                return ",".join(filter(None,[self._csvValue(js, key.replace('*','0')),
                                             self._csvValue(js, key.replace('*','1')),
                                             self._csvValue(js, key.replace('*','2')),
                                             self._csvValue(js, key.replace('*','3')),
                                             self._csvValue(js, key.replace('*','4'))]))
            else:
                if key in js:
                    return js[key]            
                else:
                    return next((link for link in js['links'] if link['rel'] == key), "")["title"]
        except:
            return ""

    def dump(self):
        return json.dumps(self.data.json, indent=4)

    def toString(self):
        return "(AbiquoObject)"

    def __dir__(self):
        d = []
        for key in self.__dict__: d.append(key)
        return d

    def __getattr__(self, key):
        if key==None: return None
        try:
            if key in self.__dict__:
                return self.__dict__[key]            
            elif key in self.data.__dict__:
                return self.data.__dict__[key]
            elif key in self.data.json:
                return self.data.json[key]
            else:
                return next((link for link in self.data.json['links'] if link['rel'] == key), None)["title"]
        except:
            return None
        
    def setLinkValue(self, rel, id):
        for link in self.data.json['links']:
            if link['rel'] == rel:
                value = link['href'].split("/")
                value[len(value)-1] = id
                link['href'] = "/".join(value)

    def getLinkValue(self, rel):
        for link in self.data.json['links']:
            if link['rel'] == rel:
                return link['href']
        return self.req_url

    def getLinkType(self, rel):
        for link in self.data.json['links']:
            if link['rel'] == rel:
                return link['type']
        return self.req_url

    def refresh(self):
        # more complex than needed because of issue in abiquo client (follow)
        link = 'edit' if self.data._has_link('edit') else 'self'
        obj = Abiquo(url=self.getLinkValue(link), auth=self.data.auth, headers={'accept' : self.data.content_type},verify=self.data.verify)
        self.response, self.data = obj.get()


# --------------------------------------------------------------------
class ABQ_User(ABQ_Object):
    
    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/enterprises/_/users"
        self.req_accept = "application/vnd.abiquo.user+json"
        self.req_accept_list = "application/vnd.abiquo.users+json"
        
    def getRole(self):
        r = ABQ_Role(self.env)
        r.response, r.data = self.data.follow("role").get()
        r._analyzeResponse()
        return r

    def toString(self):
        return "(User) id: %s, user: %s %s" % (self.id, self.name, self.surname)

     
# --------------------------------------------------------------------
class ABQ_SessionUser(ABQ_User):
    
    def __init__(self, env):
        self.env = env
        self.req_url = "/login"
        self.req_accept = "application/vnd.abiquo.user+json"
        self.req_accept_list = "application/vnd.abiquo.users+json"

    def setTenant(self, tenantId=0):
        self.setLinkValue("enterprise",tenantId)
        self.response, self.data = self.data.put()

    def getSessionApplication(self):
        app = self.getApplications()
        for i in range(app.count()):
            if app.item(i).apiKey == self.env.app_key:
                return app.item(i)
        return None

    def getApplications(self, search=None, filtermap=None):
        app = ABQ_Application(self.env)
        return app.getAll(pdata=self.data, link="applications", filter=search, filterMap=filtermap)

    def toString(self):
        return "(SessionUser) id: %s, user: %s %s" % (self.id, self.name, self.surname)

# --------------------------------------------------------------------
class ABQ_Application(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/enterprises/<enterprise>/users/<user>/applications"
        self.req_accept = "application/vnd.abiquo.role+json"
        self.req_accept_list = "application/vnd.abiquo.role+json"

    def toString(self):
        return "(Application) id: %s, name: %s %s" % (self.id, self.name, self.surname)


# --------------------------------------------------------------------
class ABQ_Role(ABQ_Object):
    
    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/roles"
        self.req_accept = "application/vnd.abiquo.application+json"
        self.req_accept_list = "application/vnd.abiquo.applications+json"
        
    def getPrivileges(self):
        r = ABQ_RolePrivilege(self.env)
        r.response, r.data = self.data.follow("privileges").get()
        r._analyzeResponse()
        return r

    def toString(self):
        return "(Role) id: %s, user: %s %s" % (self.id, self.name, self.surname)

# --------------------------------------------------------------------
class ABQ_RolePrivilege(ABQ_Object):
    
    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/roles/<role>/action/privileges"
        self.req_accept = "application/vnd.abiquo.privileges+json"
        self.req_accept_list = "application/vnd.abiquo.privileges+json"

    def toString(self):
        return "(Privileges) id: %s, user: %s %s" % (self.id, self.name, self.surname)

# --------------------------------------------------------------------
class ABQ_Datacenter(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/datacenters"
        self.req_accept = "application/vnd.abiquo.datacenter+json"
        self.req_accept_list = "application/vnd.abiquo.datacenters+json"

    def toString(self):
        return  "(Datacenter) id: %s, datacenter: %s " % (self.id, self.name)

# --------------------------------------------------------------------
class ABQ_Location(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/cloud/locations"
        self.req_accept = "application/vnd.abiquo.datacenter+json"
        self.req_accept_list = "application/vnd.abiquo.datacenters+json"

    def getAllVDC(self, search=None):
        d = ABQ_Device(self.env).getFromLocation(self.id)
        vdc = ABQ_vDC(self.env)
        vdc.dataList = []
        for t in d.dataList:
            vl = ABQ_vDC(self.env)
            vl.getAll(pdata=t, link="virtualdatacenters",filter=search)
            vdc.dataList.extend(vl.dataList)
        return vdc

    def getTemplates(self, search=None):
        vmt = ABQ_vApp(self.env)
        return vmt.getAll(pdata=self.data, link="templates",filter=search)

    def getTemplate(self, id):
        vmt = ABQ_Template(self.env)
        vmt.req_url = self.getLinkValue("templates")
        return vmt.get(id)

    def toString(self):
        return  "(Location) id: %s, location: %s " % (self.id, self.name)

# --------------------------------------------------------------------
class ABQ_Device(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/cloud/locations/<datacenter>/devices"
        self.req_accept = "application/vnd.abiquo.device+json"
        self.req_accept_list = "application/vnd.abiquo.devices+json"

    def getFromLocation(self, id):
        self.req_url = "/cloud/locations/%s/devices" % id
        return self.getAll()

# --------------------------------------------------------------------
class ABQ_Enterprise(ABQ_Object):
    
    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/enterprises"
        self.req_accept = "application/vnd.abiquo.enterprise+json"
        self.req_accept_list = "application/vnd.abiquo.enterprises+json"     
        
    def getVM(self, id=0):
        vm = ABQ_VM(self.env)
        vm.response, vm.data = self.data.follow("virtualmachines").get(id)
        vm._analyzeResponse()
        return vm

    def getAllVM(self, search=None, filtermap=None):
        vm = ABQ_VM(self.env)
        return vm.getAll(pdata=self.data, link="virtualmachines",filter=search,filterMap=filtermap)

    def getIPs(self, search=None, filtermap=None):
        ip = ABQ_IPAdress(self.env)
        return ip.getAll(pdata=self.data, link="ips",filter=search,filterMap=filtermap)

    def getAllVDC(self, search=None):
        vdc = ABQ_vDC(self.env)
        return vdc.getAll(pdata=self.data, link="cloud/virtualdatacenters",filter=search)


# --------------------------------------------------------------------
class ABQ_vDC(ABQ_Object):
    
    def __init__(self, env):
        self.env = env
        self.req_url = "/cloud/virtualdatacenters"
        self.req_accept = "application/vnd.abiquo.virtualdatacenter+json"
        self.req_accept_list = "application/vnd.abiquo.virtualdatacenters+json" 

    def getVApp(self, id=0):
        vapp = ABQ_vApp(self.env)
        vapp.response, vapp.data = self.data.follow("virtualappliances").get(str(id))
        vapp._analyzeResponse()
        return vapp

    def getAllVApp(self, search=None):
        vapp = ABQ_vApp(self.env)
        return vapp.getAll(pdata=self.data, link="virtualappliances",filter=search)
    
    def getAllVlan(self, search=None):
        vlan = ABQ_vLan(self.env)
        return vlan.getAll(pdata=self.data, link="privatenetworks",filter=search, meta={"enterprise":self.enterprise})

    def getVM(self, id=0):
        vm = ABQ_VM(self.env)
        vm.response, vm.data = self.data.follow("virtualmachines").get(id) 
        vm._analyzeResponse()
        return vm

    def getAllVM(self, search=None):
        vm = ABQ_VM(self.env)
        return vm.getAll(pdata=self.data, link="virtualmachines",filter=search)    



# --------------------------------------------------------------------
class ABQ_vApp(ABQ_Object):
    
    def __init__(self, env):
        self.env = env
        self.req_url = "/cloud/virtualdatacenters/<vdc>/virtualappliances"
        self.req_accept = "application/vnd.abiquo.virtualappliance+json"
        self.req_accept_list = "application/vnd.abiquo.virtualappliances+json"    
        

    def getVM(self, id=0):
        vm = ABQ_VM(self.env)
        vm.response, vm.data = self.data.follow("virtualmachines").get(id) 
        vm._analyzeResponse()
        return vm

    def getAllVM(self, search=None):
        vm = ABQ_VM(self.env)
        vm._analyzeResponse()
        return vm.getAll(pdata=self.data, link="virtualmachines",filter=search)

    def getVDC(self):
        vdc = ABQ_vDC(self.env)
        vdc.response, vdc.data = self.data.follow("virtualdatacenter").get()
        vdc._analyzeResponse()
        return vdc
      
# --------------------------------------------------------------------
class ABQ_VM(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/virtualmachines"
        self.req_accept = "application/vnd.abiquo.virtualmachine+json"
        self.req_accept_list = "application/vnd.abiquo.virtualmachines+json"     

    def scanAllTenant(self, filter=None, keys=None, asAdmin=True, filterMap=None, stopOnMatch=False, verbose=False):
        if asAdmin: return self.getAll(filter=filter, keys=keys, filterMap=filterMap)
        if verbose: print "> get all enterprises..."
        tl = ABQ_Enterprise(self.env).getAll()
        self.dataList = []
        for t in tl.dataList:
            if len(self.dataList)==0 or stopOnMatch==False:
                if verbose: print "> scan enterprise %s..." % t.name
                vl = ABQ_VM(self.env)
                vl.getAll(pdata=t, link="virtualmachines",filter=filter, filterMap=filterMap, keys=keys)
                self.dataList.extend(vl.dataList)
        return self
        
    def getByName(self, name, asAdmin=True, stopOnMatch=False, verbose=False):
        fm = {}
        fm["name"] = [name]
        self.scanAllTenant(filter=("vmname=%s" % name), asAdmin=asAdmin, filterMap=fm, stopOnMatch=stopOnMatch, verbose=verbose)
        if self.count()==1: self.data = self.dataList[0]
        return self

    def getByIP(self, ip, asAdmin=True, stopOnMatch=False, verbose=False):
        fm = {}
        fm["usedBy"] = ["*"]
        fm["ip"] = ip
        ipaddr = ABQ_BlueIPAdress(self.env)
        ipaddr.scanAllTenant(filter=ip, filterMap=fm, asAdmin=asAdmin, stopOnMatch=stopOnMatch, verbose=verbose)
        if ipaddr.count()!=1:
            ipaddr = ABQ_IPAdress(self.env)
            ipaddr.scanAllTenant(filter=ip, filterMap=fm, stopOnMatch=stopOnMatch, verbose=verbose)
        if ipaddr.count()==1:
            self.response, self.data = ipaddr.dataList[0].follow("virtualmachine").get()
            self._analyzeResponse()
        self.dataList = ipaddr.dataList
        return self

    def getVMData(self):
        vmd = ABQ_VMData(self.env)
        vmd.response, vmd.data = self.data.follow("metadata").get()
        vmd._analyzeResponse()
        return vmd

    def getTemplate(self):
        vmt = ABQ_Template(self.env)
        vmt.response, vmt.data = self.data.follow("virtualmachinetemplate").get()
        vmt._analyzeResponse()
        return vmt

    def getVApp(self):
        vapp = ABQ_vApp(self.env)
        vapp.response, vapp.data = self.data.follow("virtualappliance").get()
        vapp._analyzeResponse()
        return vapp

    def getEnterprise(self):
        ent = ABQ_Enterprise(self.env)
        ent.response, ent.data = self.data.follow("enterprise").get()
        ent._analyzeResponse()
        return ent

    def getUser(self):
        usr = ABQ_User(self.env)
        usr.response, usr.data = self.data.follow("user").get()
        usr._analyzeResponse()
        return usr

    def getEvents(self, severity=["*"]):
        fm = {}
        fm["severity"] =severity
        return ABQ_Event(self.env).getAll(filter=("virtualMachine=%s" % self.name),filterMap=fm)

    def getTasks(self, type=None):
        tsks = ABQ_Task(self.env)
        tsks.getAll(pdata=self.data, link="tasks", filterMap={"type":type} if type is not None else None)
        tsks._analyzeResponse()
        return tsks

    def protect(self, reason=""):
        self.response, self.data = self.data.follow("protect").post(headers={'Content-Type': "text/plain"}, data=reason)
        self._analyzeResponse()
        return self

    def unprotect(self):
        self.response, self.data = self.data.follow("unprotect").post()
        self._analyzeResponse()
        return self

    def deleteVM(self):
        self.response, self.data = self.data.follow("edit").delete()
        self._analyzeResponse()
        return self

    def cloneVM(self):
        dta = {"links":[]}
        self.response, self.data = self.data.follow("clone").post(headers={'Content-Type': "application/vnd.abiquo.virtualmachinecloneoptions+json; version=4.5"}, data=dta)
        self._analyzeResponse()
        return self

    def _analyzeIPs(self, identifier):
        ip = []
        if identifier in self.getLinkType("nic0"): ip.append(self.nic0)
        if identifier in self.getLinkType("nic1"): ip.append(self.nic1)
        if identifier in self.getLinkType("nic2"): ip.append(self.nic2)
        if identifier in self.getLinkType("nic3"): ip.append(self.nic3)
        if identifier in self.getLinkType("nic4"): ip.append(self.nic4)
        return ip

    def getGreenNetIPs(self):
        return self._analyzeIPs("privateip")

    def getBlueNetIPs(self):
        return self._analyzeIPs("publicip")

    def getSMZIPs(self):
        return self._analyzeIPs("externalip")

    def create(self, label=None, vapp=None, template=None):
        reqdata = {}
        reqdata["links"] =  [{"rel":"virtualmachinetemplate", "href":template.getLinkValue("edit")}]
        reqdata["label"] = label if label is not None else template.name
        reqdata["vdrpEnabled"] = True
        reqdata["generateGuestInitialPassword"] = False
        request_url = vapp.getLinkValue("virtualmachines")

        vm = Abiquo(url=request_url, auth=vapp.data.auth, headers={'accept': "application/vnd.abiquo.virtualmachine+json"}, verify=config.CFG_VERIFY_SSL)
        self.response, self.data = vm.post(headers={'Content-Type': "application/vnd.abiquo.virtualmachine+json"}, data=json.dumps(reqdata))
        self._analyzeResponse()
        return self

    def deploy(self):
        request = ABQ_Request(self.env)
        url = self.getLinkValue("deploy")
        vm = Abiquo(url=url, auth=self.data.auth, headers={'accept': request.req_accept}, verify=config.CFG_VERIFY_SSL)
        request.response, request.data = vm.post(headers={'Content-Type': request.req_accept})
        return request.getTask()

    def stop(self):
        request = ABQ_Request(self.env)
        url = self.getLinkValue("state")
        dta = {"state":"OFF","links":[]}
        vm = Abiquo(url=url, auth=self.data.auth, headers={'accept': request.req_accept}, verify=config.CFG_VERIFY_SSL, data=dta)
        request.response, request.data = vm.post(headers={'Content-Type': request.req_accept})
        return request.getTask()

    def start(self):
        request = ABQ_Request(self.env)
        url = self.getLinkValue("state")
        dta = {"state":"ON","links":[]}
        vm = Abiquo(url=url, auth=self.data.auth, headers={'accept': request.req_accept}, verify=config.CFG_VERIFY_SSL, data=dta)
        request.response, request.data = vm.post(headers={'Content-Type': request.req_accept})
        return request.getTask()

    def pause(self):
        request = ABQ_Request(self.env)
        url = self.getLinkValue("state")
        dta = {"state":"PAUSED","links":[]}
        vm = Abiquo(url=url, auth=self.data.auth, headers={'accept': request.req_accept}, verify=config.CFG_VERIFY_SSL, data=dta)
        request.response, request.data = vm.post(headers={'Content-Type': request.req_accept})
        return request.getTask()


# --------------------------------------------------------------------
class ABQ_Template(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/enterprises/<tenant>/datacenterrepositories/<dcr>/virtualmachinetemplates"
        self.req_accept = "application/vnd.abiquo.virtualmachinetemplate+json"
        self.req_accept_list = "application/vnd.abiquo.virtualmachinetemplates+json"


# --------------------------------------------------------------------
class ABQ_VMData(ABQ_Object):
    
    def __init__(self, env):
        self.env = env
        self.req_url = "/cloud/virtualdatacenters/<vdc>/virtualappliances/<vapp>/virtualmachines/<vm>/metadata"
        self.req_accept = "application/vnd.abiquo.metadata+json"
        self.req_accept_list = "application/vnd.abiquo.metadata+json"

# --------------------------------------------------------------------
class ABQ_Backup(ABQ_Object):

    def __init__(self, env, vm):
        self.env = env
        self.req_url = "%s/virtualmachines/%s/backup/results" % (vm.getLinkValue("virtualappliance"), vm.id)
        self.req_accept = "application/vnd.abiquo.backupresult+json"
        self.req_accept_list = "application/vnd.abiquo.backupresults+json"

    # def scanAllVM(self, keys=None):
    #     fm = {}
    #     fm["severity"] =severity
    #     vm = ABQ_VM(ENV)
    #     vm.scanAllTenant(asAdmin=(cache.session.scope == "Global scope"),filterMap=config.CFG_VM_FILTER)

# --------------------------------------------------------------------
class ABQ_vLan(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/cloud/virtualdatacenters/<virtualdatacenter>/privatenetworks"
        self.req_accept = "application/vnd.abiquo.vlan+json"
        self.req_accept_list = "application/vnd.abiquo.vlans+json"

    def getvDC(self):
        vdc = ABQ_vDC(self.env)
        vdc.response, vdc.data = self.data.follow("virtualdatacenter").get()
        vdc._analyzeResponse()
        return vdc

    def scanAllTenant(self, verbose=False):
        if verbose: print "> get all enterprises..."
        tl = ABQ_Enterprise(self.env).getAll()
        self.dataList = []
        t = ABQ_Enterprise(self.env)
        for t in tl.dataList:
            if verbose: print "> scan enterprise %s..." % t.name
            vl = ABQ_vDC(self.env)
            vl.getAll(pdata=t, link="cloud/virtualdatacenters", filter=None)
            for v in vl.dataList:
                if verbose: print "> scan vdc %s..." % v.name
                vlan = ABQ_vLan(self.env)
                vlan.getAll(pdata=v, link="privatenetworks", filter=None, meta={"enterprise":t.name})
                self.dataList.extend(vlan.dataList)
        return self


# --------------------------------------------------------------------
class ABQ_IPAdress(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/enterprises/<enterprise>/action/ips"
        self.req_accept = "application/vnd.abiquo.privateip+json"
        self.req_accept_list = "application/vnd.abiquo.privateips+json"

    def scanAllTenant(self, filter=None, keys=None, filterMap=None, stopOnMatch=False, verbose=False):
        if verbose: print "> get all tenants..."
        tl = ABQ_Enterprise(self.env).getAll()
        self.dataList = []
        for t in tl.dataList:
            if verbose: print "> scan greennet for tenant %s..." % t.name
            vl = ABQ_IPAdress(self.env)
            vl.getAll(pdata=t, link="ips",filter=filter, filterMap=filterMap, keys=keys, meta={"networkType":"greennet","enterprise":t.name})
            self.dataList.extend(vl.dataList)
        return self

# --------------------------------------------------------------------
class ABQ_BlueIPAdress(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/admin/datacenters/_/network/action/publicips"
        self.req_accept = "application/vnd.abiquo.publicip+json"
        self.req_accept_list = "application/vnd.abiquo.publicips+json"

    def setURLFromDatacenter(self, id):
        self.req_url = "/admin/datacenters/%s/network/action/publicips" % id

    def setURLFromVDC(self, id):
        self.req_url = "/api/cloud/virtualdatacenters/%s/publicips/purchased" % id

    def scanAllTenant(self, filter=None, keys=None, filterMap=None, asAdmin=True, stopOnMatch=False, verbose=False):
        if asAdmin:
            tl = ABQ_Datacenter(self.env).getAll()
            self.dataList = []
            for t in tl.dataList:
                vl = ABQ_IPAdress(self.env)
                vl.getAll(pdata=t, link="externalips",filter=filter, filterMap=filterMap, keys=keys,meta={"networkType":"smz"})
                self.dataList.extend(vl.dataList)
                bl = ABQ_BlueIPAdress(self.env)
                bl.setURLFromDatacenter(t.id)
                bl.getAll(filter=filter, filterMap=filterMap, keys=keys,meta={"networkType":"bluenet"})
                self.dataList.extend(bl.dataList)
            return self
        else:
            if verbose: print "> get all vDC..."
            vdc = ABQ_Location(self.env).get(1).getAllVDC()
            for v in vdc.dataList:
                if verbose: print "> scan bluenet for vDC %s..." % v.name
                vl = ABQ_IPAdress(self.env)
                vl.getAll(pdata=v, link="externalips",filter=filter, filterMap=filterMap, keys=keys,meta={"networkType":"smz"})
                self.dataList.extend(vl.dataList)
                bl = ABQ_BlueIPAdress(self.env)
                bl.getAll(pdata=v, link="purchased", filter=filter, filterMap=filterMap, keys=keys, meta={"networkType": "bluenet"})
                self.dataList.extend(bl.dataList)
            return self


# --------------------------------------------------------------------
class ABQ_Event(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/events"
        self.req_accept = "application/vnd.abiquo.event+json"
        self.req_accept_list = "application/vnd.abiquo.events+json"


# --------------------------------------------------------------------
class ABQ_Request(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/"
        self.req_accept = "application/vnd.abiquo.acceptedrequest+json"
        self.req_accept_list = "application/vnd.abiquo.acceptedrequest+json"

    def getTask(self):
        tsk = ABQ_Task(self.env)
        tsk.response, tsk.data = self.data.follow("status").get()
        tsk._analyzeResponse()
        return tsk

# --------------------------------------------------------------------
class ABQ_Task(ABQ_Object):

    def __init__(self, env):
        self.env = env
        self.req_url = "/cloud/virtualdatacenters/_/virtualappliances/_/virtualmachines/_/tasks"
        self.req_accept = "application/vnd.abiquo.taskextended+json"
        self.req_accept_list = "application/vnd.abiquo.tasks+json"

    def getExtended(self, id=0, taskId=None):
        link = self.dataList[id]._extract_link("self")
        tsk = ABQ_Task(self.env)._get(url=link["href"])
        return tsk

    def getJobAttr(self, key):
        for job in self.data.json['jobsExtended']['collection']:
            if key in job: return job[key]
        return None

    def setJobAttr(self, key, value):
        for job in self.data.json['jobsExtended']['collection']:
            if key in job:
                job[key] = value

    def isRunning(self):
        return self.data.state in ["STARTED"]

    def isPending(self):
        return self.data.state in ["QUEUEING", "PENDING"]


# --------------------------------------------------------------------
class ABIQUO_API:
    env = ABIQUO_ENV(None)
    api = None
    oauth = None
    
    # ----------------------------------------------------------------
    def __init__(self, env):
        self.env = env
        self.api = Abiquo(self.env.api_url, auth=self.env.getOAuth(), verify=config.CFG_VERIFY_SSL)
        
    # ----------------------------------------------------------------
    def getUser(self):
        code, result = self.api.login.get(headers={'Accept':'application/vnd.abiquo.user+json'})
        self._analzyeResponse()
        return ABQ_User(result.json)