#! /usr/bin/python
# ------------------------------------------------------------------------
# EC4SAP Command Line Interface (CLI)
# ------------------------------------------------------------------------

# modules
import argparse
import sys
import warnings
from datetime import datetime
import time

from ec4sap.abiquo_api import *
from ec4sap import config

# ------------------------------------------------------------------------
def main():

    # --------------------------------------------------------------------
    # setup argument parser
    # --------------------------------------------------------------------
    parser = argparse.ArgumentParser(description='EC4SAP CLI V0.5')
    parser.add_argument('-f', '--filter', help="filter search")
    parser.add_argument('-v', '--verbose', help="print full json dump", action="store_true")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--get', help="print abiquo object")
    group.add_argument('--list', help="search abiquo objects")
    group.add_argument('--export', help="export abiquo objects", choices=["user","vm","greenet","bluenet", "dns"])
    group.add_argument('--create', help="create abiquo object", choices=["vm"])
    group.add_argument('--register', help="register a new application in abiquo", action="store_true")
    group.add_argument('--impersonate', help="impersonate session user", action="store_true")
    group.add_argument('--delete', help="delete vm", action="store_true")
    parser.add_argument('--deploy', help="deploy created vm", action="store_true")
    parser.add_argument('--start', help="start vm", action="store_true")
    parser.add_argument('--stop', help="stop vm", action="store_true")
    parser.add_argument('--pause', help="pause vm", action="store_true")

    parser.add_argument('-env', help="named EC4SAP environment (e.q. prd,int)", default=config.CFG_ENV_DEFAULT)
    parser.add_argument('-app', help="set application name")
    parser.add_argument('-token', help="set OAuth2 bearer token")

    parser.add_argument('-location', help="load location (datacenter)", default=1)
    parser.add_argument('-template', help="load template from location")
    parser.add_argument('-tenant', help="load tenant with id <TENANT>")
    parser.add_argument('-user', help="load user with id <USER>")
    parser.add_argument('-role', help="load user-role of cached user", action="store_true")
    parser.add_argument('-privileges', help="load privileges of cached user-role", action="store_true")
    parser.add_argument('-vdc', help="load vdc with id <VDC> for cached tenant")
    parser.add_argument('-vapp', help="load vapp with id <VAPP> for cached vdc")
    parser.add_argument('-vm', help="load vm <VM> can be an id (inwith vapp), the abiquo-id or an ip adress")
    parser.add_argument('-vmdata', help="load metadata of cached vm", action="store_true")
    parser.add_argument('-vmtemplate', help="load template of cached vm", action="store_true")

    args = parser.parse_args()

    warnings.filterwarnings(config.CFG_DEBUG)
    cli = CLI(args.env)

    # --------------------------------------------------------------------
    # load objects
    # --------------------------------------------------------------------
    if args.tenant!=None: cli.getTenant(args.tenant)
    if args.user!=None: cli.getUser(args.user)
    if args.role: cli.getRole()
    if args.privileges: cli.getPrivileges()
    if args.location!=None: cli.getLocation(args.location)
    if args.template!=None: cli.getTemplate(args.template)
    if args.vdc!=None: cli.getVDC(args.vdc)
    if args.vapp!=None: cli.getVApp(args.vapp)
    if args.vm!=None: cli.getVM(args.vm)
    if args.vmdata: cli.getVMData()
    if args.vmtemplate: cli.getTemplate()

    # --------------------------------------------------------------------
    # list multiple objects
    # --------------------------------------------------------------------
    if args.list!=None:
        if args.list == "location": cli.getAllLocations(filter=args.filter, verbose=args.verbose)
        elif args.list=="template": cli.getAllTemplates(filter=args.filter, verbose=args.verbose)
        elif args.list=="tenant": cli.getAllTenants(filter=args.filter, verbose=args.verbose)
        elif args.list=="user": cli.getAllUser(filter=args.filter, verbose=args.verbose)
        elif args.list=="application": cli.getAllAllApplications(filter=args.filter, verbose=args.verbose)
        elif args.list=="vdc": cli.getAllVDCs(filter=args.filter, verbose=args.verbose)
        elif args.list=="vapp": cli.getAllVApps(filter=args.filter, verbose=args.verbose)
        elif args.list=="vm": cli.getAllVMs(filter=args.filter, verbose=args.verbose)
        elif args.list=="allvm": cli.getAllVMsGlobal(filter=args.filter, verbose=args.verbose)
        elif args.list=="vlan": cli.getAllVlan(filter=args.filter, verbose=args.verbose)
        elif args.list=="allvlan": cli.getAllVlanGlobal(filter=args.filter, verbose=args.verbose)
        elif args.list=="ip": cli.getAllIP(filter=args.filter, verbose=args.verbose)
        elif args.list=="bluenet": cli.getAllBlueNetIP(filter=args.filter, verbose=args.verbose)
        elif args.list=="greennet": cli.getAllGreenNetIP(filter=args.filter, verbose=args.verbose)
        elif args.list=="backup": cli.getBackupResult(verbose=args.verbose)
        elif args.list=="events": cli.getEvents(severity=args.filter, verbose=args.verbose)
        elif args.list=="tasks": cli.getVMTasks(type=args.filter, verbose=args.verbose)

    # --------------------------------------------------------------------
    # export multiple objects
    # --------------------------------------------------------------------
    elif args.export!=None:
        if args.export=="user": cli.exportAllUser(filter=args.filter)
        elif args.export=="vm": cli.exportAllVMs(filter=args.filter)
        elif args.export=="bluenet": cli.exportAllBlueNetIP(filter=args.filter)
        elif args.export=="greennet": cli.exportAllGreenNetIP(filter=args.filter)
        elif args.export=="dns": cli.getAllGreenNetIP(filter=args.filter, verbose=args.verbose,dnsexport=True)

    # --------------------------------------------------------------------
    # print single object
    # --------------------------------------------------------------------
    elif args.get!=None: cli.printObject(args.get)

    # --------------------------------------------------------------------
    # register application
    # --------------------------------------------------------------------
    elif args.register:
        if args.app==None or args.token==None:
            printError("ERROR: missing parameter for application registration")
        else:
            if cli.register(name=args.app, token=args.token):
                print("OK: Registration of application '%s' successful" % args.app)
                cli.printCredentials()
            else:
                print("ERROR: could not register %s" % args.app)

    # --------------------------------------------------------------------
    # impersonate
    # --------------------------------------------------------------------
    elif args.impersonate:
        if args.tenant is None:
            printError("ERROR: missing tenant parameter")
        else:
            if cli.setTenant(args.tenant):
                cli.printSessionStatus()

    # --------------------------------------------------------------------
    # create vm
    # --------------------------------------------------------------------
    elif args.create!=None and args.create=="vm":
        if args.location is None: printError("ERROR: missing location parameter")
        elif args.vdc is None: printError("ERROR: missing vdc parameter")
        elif args.vapp is None: printError("ERROR: missing vapp parameter")
        elif args.template is None: printError("ERROR: missing template parameter")
        else: cli.createVM()
        if args.deploy: cli.deployVM()

    elif args.deploy:
        if not "vm" in cli.cache: printError("ERROR: missing vm parameter")
        else: cli.deployVM()

    # --------------------------------------------------------------------
    # create vm
    # --------------------------------------------------------------------
    elif args.start:
        if not "vm" in cli.cache: printError("ERROR: missing vm parameter")
        else: cli.startVM()

    elif args.stop:
        if not "vm" in cli.cache: printError("ERROR: missing vm parameter")
        else: cli.staopVM()

    elif args.pause:
        if not "vm" in cli.cache: printError("ERROR: missing vm parameter")
        else: cli.pauseVM()


    # --------------------------------------------------------------------
    # delete vm
    # --------------------------------------------------------------------
    elif args.delete!=None and args.delete=="vm":
        if not "vm" in cli.cache: printError("ERROR: missing vm parameter")
        else: cli.deleteVM()

    # --------------------------------------------------------------------
    # no command - switch to console mode
    # --------------------------------------------------------------------
    else:
        openConsole(cli)

# ------------------------------------------------------------------------
def printError(message):
    msg = message + "\n" if message is not None else "\n"
    sys.stderr.write(msg)

# ------------------------------------------------------------------------
def openConsole(preload=None):

    # --------------------------------------------------------------------
    # instance of command line interface
    # --------------------------------------------------------------------
    abq = preload if preload != None else CLI(config.CFG_ENV_DEFAULT)

    # --------------------------------------------------------------------
    # suppress warnings (comment out for debug reason)
    # --------------------------------------------------------------------
    warnings.filterwarnings(config.CFG_DEBUG)

    # --------------------------------------------------------------------
    # help text
    # --------------------------------------------------------------------
    start_txt = "\nAbiquo Console V0.1\nType 'help' for more information or CR for sessioninfo\n"

    def printCmdUnknownError(cmd):
        print "ERROR: command '%s' not defined, use 'help' for more information" % cmd

    help = {}
    help["overview"] = "Abiquo Console V0.1\nThese shell commands are defined internally.  Type `help' to see this list\n"\
        "Type `help name' to find out more about the function `name'.\n\n"\
        "reg      register a new application in abiquo\n"\
        "auth     authenticate user with oauth2 token\n"\
        "set      set and adapt session parameter\n"\
        "print    print session data\n"\
        "list     search abiquo objects\n"\
        "export   export list as csv data\n"\
        "get      get load a single abiquo object\n"\
        "lock     protect vm\n"\
        "unlock   release vm\n" \
        "clone    clone vm\n" \
        "delete   delete vm\n" \
        "deploy   deploy newly created vm\n" \
        "start    start vm\n" \
        "stop     stop vm\n" \
        "pause    pause vm\n" \
        "clear    clear cache\n" \
        "exit     exit Abiquo console"

    help["reg"] = \
        "reg:          register a new application in abiquo\n"\
        "syntax:       reg <application> <bearer>\n"\
        "precondition: environment is set (via set env)\n"\
        "parameter:    application - name of the application to register in abiquo\n"\
        "              bearer      - openAM or oneIDB access-token"

    help["auth"] = \
        "auth:         authenticate user with oauth token\n"\
        "syntax:       auth <bearer>\n"\
        "precondition: environment is set, application is registered\n"\
        "parameter:    bearer - openAM or oneIDB access-token"

    help["set"] = \
        "set:          set and adapt session parameter\n"\
        "syntax:       set [env|tenant] <value>\n"\
        "env:          named environement (e.q. prd,int)\n"\
        "tenant:       impersonate session user, value: tenant id"

    help["create"] = \
        "vm:           create vm on loaded vApp and template"

    help["print"] = \
        "print:        print cached session data\n"\
        "syntax:       print [env|session|sessionuser|sessionapp|tokens|vminfo|cache|<object>]\n\n"\
        "env:          environment (name, url, version)\n"\
        "session:      session status (envirnoment, status, user, active tenant)\n"\
        "sessionuser:  json dump of session user object\n"\
        "sessionapp:   json dump of session application context\n"\
        "tokens:       print oauth1 tokens of session\n"\
        "vminfo:       print detailed info of loaded vm object\n"\
        "<object>:     json dump of cached object"

    help["list"] = \
        "list:         search abiquo objects, use -v vor detailed output\n"\
        "syntax:       list [user|tenant|vdc|vapp|vm|allvm] <filter> [-v] \n\n"\
        "user:         get users in global scope\n"\
        "tenant:       get tenants\n"\
        "lopcation:    get locations (datacenter)\n"\
        "template:     get available temaplates for location\n"\
        "vdc:          get virtual datacenters\n" \
        "vlan:         get vlans (inwith loaded vdc)\n"\
        "allvlan:      get vlans for all tenants\n"\
        "vapp:         get virtual appliances (inwith loaded vdc)\n"\
        "vm:           get virtual machines (inwith loaded vapp)\n"\
        "allvm:        get virtual machines for all tenants\n"\
        "backup:       get image based backups for loaded vm\n"\
        "ip:           get ip adresses for loaded tenant\n"\
        "greenip:      get green-net ip adresses for all tenants\n"\
        "blueip:       get blue-net ip adresses for all tenants\n"\
        "tasks:        get tasks (with type in filter) for loaded vm\n"\
        "events:       get events (with severity in filter) for loaded vm"

    help["export"] = \
        "export:       search abiquo objects and export as csv data\n"\
        "syntax:       export [allvm|greenip|blueip] <filter>\n\n"\
        "allvm:        get virtual machines for all tenants\n"\
        "greenip:      get green-net ip adresses for all tenants\n"\
        "blueip:       get blue-net ip adresses for all tenants\n" \
        "dns:          get all greennet ip adresses for dns export"

    help["get"] = \
        "get:          load abiquo object in cache\n"\
        "syntax:       get [user|role|privileges|tenant|vdc|vapp|vm|vmdata] <id>\n\n"\
        "user:         load user with id <id>\n"\
        "role:         load user-role of cached user\n"\
        "privileges:   load privileges of cached user-role\n"\
        "tenant:       load tenant with id <id>\n"\
        "vdc:          load vdc with id <id> for cached tenant\n"\
        "vapp:         load vapp with id <id> for cached vdc\n"\
        "vm:           load vm with id <id> for cached vapp\n"\
        "vmdata:       load metadata of cached vm\n"\
        "template:     load template of with id <id> or cached vm if not defined"

    # --------------------------------------------------------------------
    # console loop
    # --------------------------------------------------------------------
    cmd = ""
    flag = ""
    arg1 = None
    arg2 = None
    arg3 = None

    print start_txt
    abq.printSessionStatus()
    while True:
        arg = raw_input("\n>>> ").replace('  ',' ').split(' ')
        cmd = arg[0].lower()
        flag = ""
        arg1 = (arg[1] if len(arg)>1 else None)
        arg2 = (arg[2] if len(arg)>2 else None)
        arg3 = (arg[3] if len(arg)>3 else None)

        if arg2!=None and arg2.startswith("-"):
            flag=arg2
            arg2=None
        if arg3!=None and arg3.startswith("-"):
            flag=arg3

        if cmd == "exit":
            print "Bye.\n"
            quit()

        # ----------------------------------------------------------------
        # help
        # ----------------------------------------------------------------
        if cmd == "help":
            try:
                if arg1 is None: print help["overview"]
                else: print help[arg1]
            except:
                printCmdUnknownError(arg1)

        elif cmd == "":
            abq.printSessionStatus()
            abq.printCacheStatus()

        # ----------------------------------------------------------------
        # authenticate ENV token
        # ----------------------------------------------------------------
        elif cmd == "auth":
            if abq.authenticate(arg1) is False:
                print("ERROR: could not authenticate")
                print abq.ENV.error_msg
            else:
                print("OK: Authentication successful")

        # ----------------------------------------------------------------
        # register application
        # ----------------------------------------------------------------
        elif cmd == "reg":
            if arg1 is None:
                print "ERROR: application name missing"
            elif abq.register(name=arg1, token=arg2) is False:
                print("ERROR: could not register")
                print abq.ENV.error_msg
            else:
                print("OK: Registration of application '%s' successful" % arg1)
                abq.printCredentials()

        # ----------------------------------------------------------------
        # set session values
        # ----------------------------------------------------------------
        elif cmd == "set" and arg1 == "env":
            abq = CLI(arg2)
            abq.printSessionStatus()

        elif cmd == "set" and arg1 == "tenant" and arg2 is not None:
            if abq.setTenant(arg2): abq.printSessionStatus()

        # ----------------------------------------------------------------
        # cache
        # ----------------------------------------------------------------
        elif cmd == "clear":
            abq.printSessionStatus()
            abq.printCacheStatus()

        # ----------------------------------------------------------------
        # dump data
        # ----------------------------------------------------------------
        elif cmd == "print":
            abq.printObject(arg1)

        # ----------------------------------------------------------------
        # refresh data
        # ----------------------------------------------------------------
        elif cmd == "refresh":
            if arg1 in abq.cache:
                abq.cache.__getattr__(arg1).refresh()
                abq.printObject(arg1)

        # ----------------------------------------------------------------
        # get user
        # ----------------------------------------------------------------
        elif cmd == "get" and arg1 == "user":
            if abq.getUser(arg2): print abq.cache.user.toString()

        elif cmd == "list" and arg1 == "user":
            abq.getAllUser(filter=arg2, verbose=(flag == "-v"))

        elif cmd == "export" and arg1 == "user":
            abq.exportAllUser(filter=arg2)

        # ----------------------------------------------------------------
        # get application
        # ----------------------------------------------------------------

        elif cmd == "list" and arg1 == "application":
            abq.getAllAllApplications(filter=arg2, verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get role and privileges
        # ----------------------------------------------------------------
        elif cmd == "get" and arg1 == "role":
            if abq.getRole():
                print "id: %s, user: %s %s" % (abq.cache.user.id, abq.cache.user.name, abq.cache.user.surname)

        elif cmd == "get" and arg1 == "privileges":
            if abq.getPrivileges():
                print "id: %s, user: %s %s" % (abq.cache.user.id, abq.cache.user.name, abq.cache.user.surname)

        # ----------------------------------------------------------------
        # get tenant (enterprises)
        # ----------------------------------------------------------------
        elif cmd == "get" and arg1 == "tenant":
            if abq.getTenant(id=arg2):
                print "id: %s, tenant: %s " % (abq.cache.tenant.id, abq.cache.tenant.name)

        elif cmd == "list" and arg1 == "tenant":
            abq.getAllTenants(filter=arg2, verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get location
        # ----------------------------------------------------------------
        elif cmd == "get" and arg1 == "location":
            if abq.getLocation(arg2):
                print "id: %s, vDC: %s " % (abq.cache.location.id, abq.cache.location.name)

        elif cmd == "list" and arg1 == "location":
            abq.getAllLocations(filter=arg2, verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get vdc
        # ----------------------------------------------------------------
        elif cmd == "get" and arg1 == "vdc":
            if abq.getVDC(arg2):
                print "id: %s, vDC: %s " % (abq.cache.vdc.id, abq.cache.vdc.name)

        elif cmd == "list" and arg1 == "vdc":
            abq.getAllVDCs(filter=arg2, verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get vApp
        # ----------------------------------------------------------------
        elif cmd == "get" and arg1 == "vapp":
            if abq.getVApp(arg2):
                print "id: %s, vDC: %s " % (abq.cache.vapp.id, abq.cache.vapp.name)

        elif cmd == "list" and arg1 == "vapp":
            abq.getAllVApps(filter=arg2, verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get vLan
        # ----------------------------------------------------------------
        elif cmd == "list" and arg1 == "vlan":
            abq.getAllVlan(filter=arg2, verbose=(flag == "-v"))

        elif cmd == "list" and arg1 == "allvlan":
            abq.getAllVlanGlobal(filter=arg2, verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get vm
        # ----------------------------------------------------------------
        elif cmd == "get" and arg1 == "vm":
            if abq.getVM(arg2):
                print "id: %s, vm: %s " % (abq.cache.vm.id, abq.cache.vm.name)

        elif cmd == "list" and arg1 == "vm":
            abq.getAllVMs(filter=arg2, verbose=(flag == "-v"))

        elif cmd == "list" and arg1 == "allvm":
            abq.getAllVMsGlobal(filter=arg2, verbose=(flag == "-v"))

        elif cmd == "export" and arg1 == "allvm":
            abq.exportAllVMs(filter=arg2)

        # ----------------------------------------------------------------
        # create vm
        # ----------------------------------------------------------------
        elif cmd == "create" and arg1 == "vm":
            if abq.createVM(label=arg2): print "vm created"

        elif cmd == "deploy" and arg1 == "vm":
            if abq.deployVM():
                abq.waitForTask(task=abq.cache.task)

        # ----------------------------------------------------------------
        # start/stop vm
        # ----------------------------------------------------------------
        elif cmd == "start" and arg1 == "vm":
            if abq.startVM():
                abq.waitForTask(task=abq.cache.task)

        elif cmd == "stop" and arg1 == "vm":
            if abq.stopVM():
                abq.waitForTask(task=abq.cache.task)

        elif cmd == "pause" and arg1 == "vm":
            if abq.pauseVM():
                abq.waitForTask(task=abq.cache.task)

        # ----------------------------------------------------------------
        # lock/unlock vm
        # ----------------------------------------------------------------
        elif cmd == "lock" and arg1 == "vm":
            if abq.lockVM(): print "vm locked"

        elif cmd == "unlock" and arg1 == "vm":
            if abq.unlockVM(): print "vm unlocked"

        # ----------------------------------------------------------------
        # delete vm
        # ----------------------------------------------------------------
        elif cmd == "delete" and arg1 == "vm":
            if abq.deleteVM(): print "vm deleted"

        # ----------------------------------------------------------------
        # clone vm
        # ----------------------------------------------------------------
        elif cmd == "clone" and arg1 == "vm":
            if abq.cloneVM(): print "vm cloned"

        # ----------------------------------------------------------------
        # get vm metadata
        # ----------------------------------------------------------------
        elif cmd == "get" and arg1 == "vmdata":
            if abq.getVMData():
                print abq.cache.vmdata.dump()

        # ----------------------------------------------------------------
        # get vm template
        # ----------------------------------------------------------------
        elif cmd == "get" and arg1 == "template":
            if abq.getTemplate(arg2):
                print "id: %s, template: %s " % (abq.cache.template.id, abq.cache.template.name)

        elif cmd == "list" and arg1 == "template":
            abq.getAllTemplates(filter=arg2, verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get backup result
        # ----------------------------------------------------------------
        elif cmd == "list" and arg1 == "backup":
            abq.getBackupResult(verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get events for vm
        # ----------------------------------------------------------------
        elif cmd == "list" and arg1 == "events":
            abq.getEvents(severity=arg2, verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get tasks for vm
        # ----------------------------------------------------------------
        elif cmd == "list" and arg1 == "tasks":
            abq.getVMTasks(type=arg2, verbose=(flag == "-v"))

        # ----------------------------------------------------------------
        # get ip adresses
        # ----------------------------------------------------------------
        elif cmd == "list" and arg1 == "ip":
            abq.getAllIP(filter=arg2, verbose=(flag == "-v"))

        elif cmd == "list" and arg1 == "blueip":
            abq.getAllBlueNetIP(filter=arg2, verbose=(flag == "-v"))

        elif cmd == "export" and arg1 == "blueip":
            abq.exportAllBlueNetIP(filter=arg2)

        elif cmd == "list" and arg1 == "greenip":
            abq.getAllGreenNetIP(filter=arg2, verbose=(flag == "-v"))

        elif cmd == "export" and arg1 == "greenip":
            abq.exportAllGreenNetIP(filter=arg2)

        elif cmd == "export" and arg1 == "dns":
            abq.getAllGreenNetIP(filter=arg2, verbose=(flag == "-v"), dnsexport=True)

        # ----------------------------------------------------------------
        # unknown command
        # ----------------------------------------------------------------
        else:
            printCmdUnknownError(cmd)

# ------------------------------------------------------------------------
class CLI:

    # --------------------------------------------------------------------
    # globals
    # --------------------------------------------------------------------
    ENV = None
    cache = ABQ_Cache()
    isOnline = False

    # --------------------------------------------------------------------
    # constructor and other fun stuff
    # --------------------------------------------------------------------
    def __init__(self, env=config.CFG_ENV_DEFAULT):
        self.setEnv(env)

    def __ne__(self, other):
        return not self == other

    # --------------------------------------------------------------------
    # check for error in response
    # --------------------------------------------------------------------
    @staticmethod
    def printErrorIfFailed(obj):
        try:
            if obj.respHasError:
                printError("ERROR: (%s) %s" % (obj.respCode, obj.respMessage))
                return False
            return True
        except:
            printError("ERROR: object not found in cache")
            return False

    # --------------------------------------------------------------------
    # print  object
    # --------------------------------------------------------------------
    def printObject(self, obj="cache"):
        if obj == "tokens":
            self.printCredentials()
        elif obj == "env":
            self.printEnvironment()
        elif obj == "session":
            self.printSessionStatus()
        elif obj == "sessionuser":
            print self.cache.session.dump()
        elif obj == "vminfo":
            self.printVMInfo()
        elif obj == "cache":
            self.printCacheStatus()
        else:
            try:
                print self.cache.__getattr__(obj).dump()
            except:
                printError("ERROR: %s is not loaded" % obj)

    # --------------------------------------------------------------------
    # print credentials
    # --------------------------------------------------------------------
    def printCredentials(self):
        print "Application Name   : %s" % self.ENV.app_name
        print "Application Key    : %s" % self.ENV.app_key
        print "Application Secret : %s" % self.ENV.app_secret
        print "Acess Token        : %s" % self.ENV.access_token
        print "Access Secret      : %s" % self.ENV.access_secret

    # --------------------------------------------------------------------
    # print session status
    # --------------------------------------------------------------------
    def printSessionStatus(self):
        if self.isOnline:
            print "Environment    : %s" % self.ENV.name
            print "Application    : %s" % self.ENV.app_name
            print "Status         : online"
            print "Session-User   : %s" % self.cache.session.name
            print "Session-Scope  : %s" % self.cache.session.scope
            print "Impersonation  : %s" % self.cache.session.enterprise
        else:
            print "Environment    : %s" % self.ENV.name
            print("URL            : %s" % self.ENV.api_url)
            print("Version        : %s" % self.ENV.api_version)
            print "Status         : offline"

    def printEnvironment(self):
        print("Name    : %s" % self.ENV.name)
        print("URL     : %s" % self.ENV.api_url)
        print("Version : %s" % self.ENV.api_version)

    def printCacheStatus(self):
        if self.isOnline:
            print "\nCached Objects"
            for co in self.cache.__dict__:
                print ("   | %s                 " % co)[:17] + ": %s" % self.cache.__getattr__(co).name

    # --------------------------------------------------------------------
    # print vm info
    # --------------------------------------------------------------------

    def printVMInfo(self):
        if "vm" in self.cache:
            vm = self.cache.vm
            template = vm.getTemplate()

            print "General"
            print "  | State     : %s %s" % (vm.state, "(locked)" if vm.protected == True else "")
            print "  | Name      : %s" % vm.name
            print "  | Label     : %s" % vm.label
            print "  | FQDN      : %s" % vm.fqdn
            print "  | Owner     : %s" % vm.user
            print "  | Created   : %s" % datetime.fromtimestamp(long(vm.creationTimestamp) / 1000)
            print "  | Tenant    : %s" % vm.enterprise
            print "  | vDC       : %s" % vm.virtualdatacenter
            print "  | vApp      : %s" % vm.virtualappliance
            print "\nConfiguration"
            print "  | Template  : %s" % vm.virtualmachinetemplate
            print "  | OS        : %s (Version %s)" % (template.osType, template.osVersion)
            print "  | CPU       : %s" % vm.cpu
            print "  | Cores     : %s" % (vm.coresPerSocket if vm.coresPerSocket is not None else "n.a.")
            print "  | RAM (MB)  : %s" % vm.ram
            print "  | Datastore : %s" % vm.datastoretier0
            print "  | GreenNet  : %s" % ",".join(vm.getGreenNetIPs())
            print "  | BlueNet   : %s" % ",".join(vm.getBlueNetIPs())
            print "  | SMZ       : %s" % ",".join(vm.getSMZIPs())
            if vm.backuppolicies is not None and len(vm.backuppolicies) > 0:
                print "  | Backup    : %s" % vm.backuppolicies[0]["links"][0]["title"]

        else:
            printError("ERROR: no vm loaded")


    # ----------------------------------------------------------------
    # authenticate ENV token
    # ----------------------------------------------------------------
    def authenticate(self, token):
        return self.ENV.authenticate(token)

    # ----------------------------------------------------------------
    # register application
    # ----------------------------------------------------------------
    def register(self, name, token):
        if self.ENV.register_app(name, token) is False or self.authenticate(token) is False:
            return False
        else:
            return True

    # ----------------------------------------------------------------
    # set session values
    # ----------------------------------------------------------------
    def setEnv(self, name):
        self.ENV = ABIQUO_ENV(name)
        self.cache = ABQ_Cache()
        self.cache.session = ABQ_SessionUser(self.ENV)
        self.isOnline = (self.cache.session.get().respHasError == False)
        if self.isOnline:
            self.cache.sessionapp = self.cache.session.getSessionApplication()
            self.ENV.app_name = self.cache.sessionapp.name

    def setTenant(self, id=0):
        self.cache.session.setTenant(id)
        return self.printErrorIfFailed(self.cache.session)

    # ----------------------------------------------------------------
    # cache
    # ----------------------------------------------------------------
    def clearCache(self):
        self.cache = ABQ_Cache()
        self.cache.session = ABQ_SessionUser(self.ENV)
        self.isOnline = (self.cache.session.get().respHasError == False)

    # ----------------------------------------------------------------
    # get user
    # ----------------------------------------------------------------
    def getUser(self, id=0):
        self.cache.user = ABQ_User(self.ENV).get(id=id)
        return self.printErrorIfFailed(self.cache.user)


    def getAllUser(self, filter=None, verbose=False):
        users = ABQ_User(self.ENV)
        users.getAll(filter=filter)
        self.printErrorIfFailed(users)
        for i in range(users.count()):
            u = users.item(i)
            if verbose:
                print u.dump()
            else:
                print "id: %s (%s), user: %s, %s, email: %s" % (u.id, u.active, u.name, u.surname, u.email)
        print "found %s user" % users.count()


    def exportAllUser(self, filter=None):
        users = ABQ_User(self.ENV)
        users.getAll(filter=filter, keys={"ID": "id", "Name": "name", "E-Mail": "email"})
        print users.csvHeader()
        for i in range(users.count()):
            print users.csvRow(i)

    # ----------------------------------------------------------------
    # get application
    # ----------------------------------------------------------------
    def getAllAllApplications(self, filter=None, verbose=False):
        app = self.cache.session.getApplications()
        self.printErrorIfFailed(app)
        for i in range(app.count()):
            u = app.item(i)
            if verbose:
                print u.dump()
            else:
                print "id: %s, app: %s, key: %s" % (u.id, u.name, u.apiKey)
        print "found %s applications" % app.count()

    # ----------------------------------------------------------------
    # get role and privileges
    # ----------------------------------------------------------------
    def getRole(self):
        if "user" not in self.cache:
            printError("ERROR: no user in cache")
            return False
        else:
            self.cache.role = self.cache.user.getRole()
            return self.printErrorIfFailed(self.cache.role)

    def getPrivileges(self):
        if "role" not in self.cache:
            printError("ERROR: no role in cache")
            return False
        else:
            self.cache.privileges = self.cache.role.getPrivileges()
            return self.printErrorIfFailed(self.cache.privileges)

    # ----------------------------------------------------------------
    # get tenant (enterprises)
    # ----------------------------------------------------------------
    def getTenant(self, id=0):
        self.cache.tenant = ABQ_Enterprise(self.ENV).get(id=id)
        return self.printErrorIfFailed(self.cache.tenant)

    def getAllTenants(self, filter=None, verbose=False):
        tenant = ABQ_Enterprise(self.ENV)
        tenant.getAll(filter=filter)
        self.printErrorIfFailed(tenant)
        for i in range(tenant.count()):
            u = tenant.item(i)
            if verbose:
                print u.dump()
            else:
                print "id: %s, tenant: %s" % (u.id, u.name)
        print "found %s tenants" % tenant.count()

    # ----------------------------------------------------------------
    # get location
    # ----------------------------------------------------------------
    def getLocation(self, id=0):
        self.cache.location = ABQ_Location(self.ENV).get(id=id)
        return self.printErrorIfFailed(self.cache.location)

    def getAllLocations(self, filter=None, verbose=False):
        loc = ABQ_Location(self.ENV)
        loc.getAll(filter=filter)
        self.printErrorIfFailed(loc)
        for i in range(loc.count()):
            u = loc.item(i)
            if verbose:
                print u.dump()
            else:
                print "id: %s, location: %s" % (u.id, u.name)
        print "found %s locations" % loc.count()

    # ----------------------------------------------------------------
    # get vdc
    # ----------------------------------------------------------------
    def getVDC(self, id=0):
        self.cache.vdc = ABQ_vDC(self.ENV).get(id=id)
        return self.printErrorIfFailed(self.cache.vdc)

    def getAllVDCs(self, filter=None, verbose=False):
        loc = ABQ_Location(self.ENV).get(1)
        vdc = loc.getAllVDC(search=filter)
        for i in range(vdc.count()):
            u = vdc.item(i)
            if verbose:
                print u.dump()
            else:
                print "id: %s, vDC: %s, tenant: %s" % (u.id, u.name, u.enterprise)
        print "found %s vdc" % vdc.count()

    # ----------------------------------------------------------------
    # get vLan
    # ----------------------------------------------------------------
    def getAllVlan(self, filter=None, verbose=False):
        if "vdc" not in self.cache:
            printError("ERROR: no vdc in cache")
        else:
            vlan = self.cache.vdc.getAllVlan(filter)
            self.printErrorIfFailed(vlan)
            for i in range(vlan.count()):
                u = vlan.item(i)
                if verbose:
                    print u.dump()
                else:
                    print "id: %s, vLan: %s, net: %s/%s, domain: %s" % (u.id, u.name, u.address, u.mask, u.sufixDNS)
            print "found %s vlan" % vlan.count()

    def getAllVlanGlobal(self, filter=None, verbose=False):
        vlan = ABQ_vLan(self.ENV)
        vlan.scanAllTenant(verbose=verbose)
        self. printErrorIfFailed(vlan)
        #print "tenant;vdc;subnet;mask;subnet name;domains"
        for i in range(vlan.count()):
            u = vlan.item(i)
            if verbose:
                print u.dump()
            else:
                print "tenant: %s, vdc: %s, vLan: %s, net: %s/%s, domain: %s" % (u.enterprise, u.virtualdatacenter, u.name, u.address, u.mask, u.sufixDNS)
                #print "%s;%s;%s;%s;%s;%s" % (vdc.enterprise, u.virtualdatacenter, u.address, u.mask, u.name, u.sufixDNS)
        print "found %s vlan" % vlan.count()


    # ----------------------------------------------------------------
    # get vApp
    # ----------------------------------------------------------------
    def getVApp(self, id=0):
        if "vdc" not in self.cache:
            printError("ERROR: no vdc in cache")
            return False
        else:
            self.cache.vapp = self.cache.vdc.getVApp(id)
            return self.printErrorIfFailed(self.cache.vapp)

    def getAllVApps(self, filter=None, verbose=False):
        if "vdc" not in self.cache:
            printError("ERROR: no vdc in cache")
        else:
            vapp = self.cache.vdc.getAllVApp(filter)
            self.printErrorIfFailed(vapp)
            for i in range(vapp.count()):
                u = vapp.item(i)
                if verbose:
                    print u.dump()
                else:
                    print "id: %s, vApp: %s" % (u.id, u.name)
            print "found %s vapp" % vapp.count()

    # ----------------------------------------------------------------
    # get vm
    # ----------------------------------------------------------------
    def getVM(self, id):
        self.cache.remove("vm")
        if id is not None and id.startswith("ABQ_"):
            vm = ABQ_VM(self.ENV).getByName(id, asAdmin=(self.cache.session.scope == "Global scope"))
            if vm.respHasError == False and vm.count() == 1: self.cache.vm = vm
        elif id is not None and len(id.split('.')) == 4:
            vm = ABQ_VM(self.ENV).getByIP(id)
            if not vm.respHasError: self.cache.vm = vm
        else:
            if "vapp" in self.cache:
                self.cache.vm = self.cache.vapp.getVM(id)
            elif "vdc" in self.cache:
                self.cache.vm = self.cache.vdc.getVM(id)
            elif "tenant" in self.cache:
                self.cache.vm = self.cache.tenant.getVM(id)
        if "vm" not in self.cache:
            printError("ERROR: vm %s not found" % id)
            return False
        else:
            return True

    def getAllVMs(self, filter=None, verbose=False):
        vm = None
        if "vapp" in self.cache:
            vm = self.cache.vapp.getAllVM(filter)
        elif "vdc" in self.cache:
            vm = self.cache.vdc.getAllVM(filter)
        elif "tenant" in self.cache:
            vm = self.cache.tenant.getAllVM(filter)
        self.printErrorIfFailed(vm)
        for i in range(vm.count()):
            u = vm.item(i)
            if verbose:
                print u.dump()
            else:
                print "id: %s, vm: %s, state: %s %s" % (u.id, u.name, u.state, ("(locked)" if u.protected == True else ""))
        print "found %s vm" % vm.count()

    def getAllVMsGlobal(self, filter=None, verbose=False):
        vm = ABQ_VM(self.ENV)
        vm.scanAllTenant(filter=filter, asAdmin=(self.cache.session.scope == "Global scope"),
                         filterMap=config.CFG_VM_FILTER)
        self. printErrorIfFailed(vm)
        for i in range(vm.count()):
            u = vm.item(i)
            if verbose:
                print u.dump()
            else:
                print "id: %s, type: %s, vdc: %s, vapp: %s, fqdn: %s, name: %s, nic0: %s, nic1: %s" % (
                u.id, u.type, u.virtualdatacenter, u.virtualappliance, u.fqdn, u.name, u.nic0, u.nic1)
        print "found %s vm" % vm.count()

    def exportAllVMs(self, filter=None):
        vm = ABQ_VM(self.ENV)
        vm.scanAllTenant(filter=filter, asAdmin=(self.cache.session.scope == "Global scope"), keys=config.CSV_FORMAT_VM,
                         filterMap=config.CFG_VM_FILTER)
        print vm.csvHeader()
        for i in range(vm.count()):
            print vm.csvRow(i)

    # ----------------------------------------------------------------
    # create vm
    # ----------------------------------------------------------------
    def createVM(self, label=None):
        try:
            if "vapp" not in self.cache: printError("ERROR: no vApp in cache")
            elif "template" not in self.cache: printError("ERROR: no template in cache")
            else:
                self.cache.vm = ABQ_VM(self.ENV)
                if self.cache.vm.create(label=label, vapp=self.cache.vapp, template=self.cache.template).respHasError == False:
                    return True
                else:
                    return self.printErrorIfFailed(self.cache.vm)
        except:
            printError("ERROR: create vm failed")
            return False

    def deployVM(self):
        try:
            if "vm" not in self.cache: printError("ERROR: no vm in cache")
            else:
                self.cache.task = self.cache.vm.deploy()
                if self.cache.task.respHasError == False:
                    return True
                else:
                    return self.printErrorIfFailed(self.cache.task)
        except:
            printError("ERROR: deploy vm failed")
            return False


    # ----------------------------------------------------------------
    # lock/unlock vm
    # ----------------------------------------------------------------
    def lockVM(self):
        try:
            if self.cache.vm.protect(reason="locked by ec4sap console").respHasError == False:
                return True
            else:
                return self.printErrorIfFailed(self.cache.vm)
        except:
            printError("ERROR: lock vm failed")
            return False

    def unlockVM(self):
        try:
            if self.cache.vm.unprotect().respCode == False:
                return True
            else:
                return self.printErrorIfFailed(self.cache.vm)
        except:
            printError("ERROR: unlock vm failed")
            return False

    # ----------------------------------------------------------------
    # start/stop vm
    # ----------------------------------------------------------------
    def startVM(self):
        try:
            if self.cache.vm.start().respHasError == False:
                return True
            else:
                return self.printErrorIfFailed(self.cache.vm)
        except:
            printError("ERROR: start vm failed")
            return False

    def stopVM(self):
        try:
            if self.cache.vm.stop().respHasError == False:
                return True
            else:
                return self.printErrorIfFailed(self.cache.vm)
        except:
            printError("ERROR: stop vm failed")
            return False

    def pauseVM(self):
        try:
            if self.cache.vm.pause().respHasError == False:
                return True
            else:
                return self.printErrorIfFailed(self.cache.vm)
        except:
            printError("ERROR: pause vm failed")
            return False

    # ----------------------------------------------------------------
    # delete vm
    # ----------------------------------------------------------------
    def deleteVM(self):
        try:
            if self.cache.vm.deleteVM(reason="requested by user").respHasError == False:
                return True
            else:
                return self.printErrorIfFailed(self.cache.vm)
        except:
            printError("ERROR: delete vm failed")
            return False


    # ----------------------------------------------------------------
    # clone vm
    # ----------------------------------------------------------------
    def cloneVM(self):
        try:
            if self.cache.vm.cloneVM().respHasError == False:
                return True
            else:
                return self.printErrorIfFailed(self.cache.vm)
        except:
            printError("ERROR: clone vm failed")
            return False

    # ----------------------------------------------------------------
    # get vm metadata
    # ----------------------------------------------------------------
    def getVMData(self):
        self.cache.vmdata = self.cache.vm.getVMData()
        return self.printErrorIfFailed(self.cache.vmdata)

    # ----------------------------------------------------------------
    # get vm template
    # ----------------------------------------------------------------
    def getTemplate(self, id=0):
        if id==0:
            if "vm" not in self.cache:
                printError("ERROR: no vm in cache")
            else:
                self.cache.template = self.cache.vm.getTemplate()
        else:
            if "location" not in self.cache:
                printError("ERROR: no location in cache")
            else:
                self.cache.template = self.cache.location.getTemplate(id)
        return self.printErrorIfFailed(self.cache.template)

    def getAllTemplates(self, filter=None, verbose=False):
        if "location" not in self.cache:
            printError("ERROR: no location in cache")
        else:
            vmt = self.cache.location.getTemplates(search=filter)
            self.printErrorIfFailed(vmt)
            for i in range(vmt.count()):
                u = vmt.item(i)
                if verbose:
                    print u.dump()
                else:
                    print "id: %s, os: %s %s, cpu: %s, ram: %s, name: %s" % (u.id, u.osType, u.osVersion, u.cpuRequired, u.ramRequired, u.name)
            print "found %s templates for location" % vmt.count()


    # ----------------------------------------------------------------
    # get backup result
    # ----------------------------------------------------------------
    def getBackupResult(self, verbose=False):
        if "vm" not in self.cache:
            printError("ERROR: no vm in cache")
        else:
            bck = ABQ_Backup(self.ENV, self.cache.vm).getAll()
            self.printErrorIfFailed(bck)
            for i in range(bck.count()):
                u = bck.item(i)
                if verbose:
                    print u.dump()
                else:
                    if u.status == "FAILED":
                        print "(%s) created: %s" % (u.status, u.creationDate)
                    else:
                        print "(%s) id: %s, size: %s, created: %s, expires: %s" % (
                        u.status, u.name, u.sizeInMb, u.creationDate, u.expirationDate)
            print "found %s backups for vm" % bck.count()

    # ----------------------------------------------------------------
    # get events for vm
    # ----------------------------------------------------------------
    def getEvents(self, severity=None, verbose=False):
        if "vm" not in self.cache:
            printError("ERROR: no vm in cache")
        else:
            s = ["*"]
            if severity is not None: s = severity.split(",")
            evt = self.cache.vm.getEvents(severity=s)
            self.printErrorIfFailed(evt)
            for i in range(evt.count()):
                u = evt.item(i)
                if verbose:
                    print u.dump()
                else:
                    if u.status == "FAILED":
                        print "(%s) created: %s" % (u.status, u.creationDate)
                    else:
                        print "(%s) date: %s, user: %s, action: %s" % (
                        u.severity, u.timestamp, u.performedBy, u.actionPerformed)
            print "found %s events for vm" % evt.count()

    # ----------------------------------------------------------------
    # get tasks for vm
    # ----------------------------------------------------------------
    def getVMTasks(self, type=None, verbose=False):
        if "vm" not in self.cache:
            printError("ERROR: no vm in cache")
        else:
            tsk = self.cache.vm.getTasks(type=type)
            self.printErrorIfFailed(tsk)
            for i in reversed(range(tsk.count())):
                u = tsk.item(i)
                if verbose:
                    print u.dump()
                else:
                    print "(%s) task:%s, date:%s, user:%s, state:%s" % (u.taskId, u.type, u.timestamp, u.user, u.state)
            print "found %s tasks for vm" % tsk.count()


    # ----------------------------------------------------------------
    # get ip adresses
    # ----------------------------------------------------------------
    def getAllIP(self, filter=None, verbose=None):
        if "tenant" not in self.cache:
            printError("ERROR: no tenant in cache")
        else:
            ip = self.cache.tenant.getIPs(search=filter)
            self.printErrorIfFailed(ip)
            for i in range(ip.count()):
                u = ip.item(i)
                if verbose:
                    print u.dump()
                else:
                    print "ip: %s, network: %s, vm: %s" % (u.ip, u.networkName, u.usedBy)
            print "found %s ips for tenant" % ip.count()

    def getAllBlueNetIP(self, filter=None, verbose=None):
        ip = ABQ_BlueIPAdress(self.ENV)
        ip.scanAllTenant(filter=filter, filterMap=config.CFG_IP_FILTER,
                         asAdmin=(self.cache.session.scope == "Global scope"))
        self.printErrorIfFailed(ip)
        for i in range(ip.count()):
            u = ip.item(i)
            if verbose:
                print u.dump()
            else:
                print "ip: %s, type: %s, network: %s, vm: %s" % (u.ip, u.networkType, u.networkName, u.usedBy)
        print "found %s ips" % ip.count()


    def exportAllBlueNetIP(self, filter=None):
        ip = ABQ_BlueIPAdress(self.ENV)
        ip.scanAllTenant(filter=filter, keys=config.CSV_FORMAT_IP, filterMap=config.CFG_IP_FILTER)
        print ip.csvHeader()
        for i in range(ip.count()):
            print ip.csvRow(i)


    def getAllGreenNetIP(self, filter=None, verbose=None, dnsexport=False):
        ip = ABQ_IPAdress(self.ENV)
        ip.scanAllTenant(filter=filter, filterMap=config.CFG_IP_FILTER)
        self.printErrorIfFailed(ip)
        if dnsexport: print "tenant;vdc;vlan;vm;fqdn;ip"
        for i in range(ip.count()):
            u = ip.item(i)
            if dnsexport:
                vm = ABQ_VM(self.ENV)
                vm.response, vm.data = u.data.follow("virtualmachine").get()
                vm._analyzeResponse()
                print "%s;%s;%s;%s;%s;%s" % (vm.enterprise, u.virtualdatacenter, u.networkName, vm.name, vm.fqdn, u.ip)
            else:
                if verbose:
                    print u.dump()
                else:
                    print "vdc: %s, vlan: %s, vm: %s, ip: %s" % (u.virtualdatacenter, u.networkName, u.usedBy, u.ip)
        print "found %s ips" % ip.count()


    def exportAllGreenNetIP(self, filter=None):
        ip = ABQ_IPAdress(self.ENV)
        ip.scanAllTenant(filter=filter, keys=config.CSV_FORMAT_IP, filterMap=config.CFG_IP_FILTER)
        print ip.csvHeader()
        for i in range(ip.count()):
            print ip.csvRow(i)

    # ----------------------------------------------------------------
    # wait while task is running
    # ----------------------------------------------------------------
    def waitForTask(self, task=None):
        animation = "|/-\\"
        while task.isRunning():
            for i in range(8):
                sys.stdout.write("\r"+animation[i % len(animation)]+" "+task.state)
                sys.stdout.flush()
                time.sleep(0.5)
            task.refresh()
        print "\r",task.state


# ------------------------------------------------------------------------
# script constructor
# ------------------------------------------------------------------------
if __name__ == "__main__" : main()

