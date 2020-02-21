#!/usr/bin/python3
from requests import Request, Session
import os
import json
#import pdb
import glob
import logging
import logging.config
import argparse

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

#logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)

_logger = logging.getLogger("|> cenit.manager")

class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ERROR = '\033[101m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[43m'
    BROWN = '\033[103m'
    PINK = '\033[45m'
    YELLOW2 = '\033[34m'
    WHITE = '\033[107m'
    BLUE = '\033[104m'
    #SUCCESS = '\033[7m'
    SUCCESS = '\033[92m'
    #SUCCESS = '\x1b[6;30;42m'
    UNDERLINE = '\033[4m'

    @classmethod
    def print_color(cls):
        x = 0
        for i in range(24):
            colors = ""
            for j in range(5):
                code = str(x+j)
                colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
            print(colors)
            x=x+5

class CenitManager(object):
    """Cenit Manager, creator, updater, droper documents"""
    def __init__(self, dir_path=None, cur_path=None, full_path=None, end_point=None, key=None, token=None, env=None, auto_bind=None, tenant=None):
        _logger.info("Initial CenitManager")
        super(CenitManager, self).__init__()
        self.dir_path = dir_path or "files"
        self.cur_path = cur_path or os.getcwd()
        self.full_path = full_path or "{}/{}".format(self.cur_path, self.dir_path)
        self.doc_types = {"json_data_type":[],"snippet":[],"algorithm":[],"flow":[],"template":[],"schema":[],"namespace":[], "observer":[], "ruby_parser":[], "plain_webhook":[], "connection":[], "sign_key":[], "application":[]}
        self.end_point = "%s/api/v2/setup/{}.json" % (end_point or "https://cenit.io")
        self.tenant = tenant
        self.key = key
        self.token = token
        self.env = env
        self.ruc = None
        self.endpoit = "https://e-beta.sunat.gob.pe"
        self.webhook = "ol-ti-itcpgem/billService"
        self.conection_options = {
                                #"sunat_beta":           {"endpoint": "https://e-beta.sunat.gob.pe", "webhook": "ol-ti-itcpgem/billService", "ruc": "", "username": "", "password": ""},
                                "sunat_beta":           {"endpoint": "https://e-beta.sunat.gob.pe", "webhook": "ol-ti-itcpfegem-beta/billService", "ruc": "", "username": "", "password": ""},
                                "sunat_production":     {"endpoint": "https://e-factura.sunat.gob.pe", "webhook": "ol-ti-itcpgem/billService", "ruc": "", "username": "", "password": ""},
                                "bizlinks_production":  {"endpoint": "https://ose.bizlinks.com.pe", "webhook": "ol-ti-itcpe/billService", "ruc": "", "username": "", "password": ""},
                                "bizlinks_demo":        {"endpoint": "https://osetesting.bizlinks.com.pe", "webhook": "ol-ti-itcpgem/billService", "ruc": "", "username": "", "password": ""},
                                "nubefact_production":  {"endpoint": "https://e-beta.sunat.gob.pe", "webhook": "ol-ti-itcpe/billService", "ruc": "", "username": "", "password": ""},
                                "nubefact_demo":        {"endpoint": "https://demo-ose.nubefact.com", "webhook": "ol-ti-itcpe/billService", "ruc": "", "username": "", "password": ""},
                                }
        self.loaded_files = False
        self.auto_bind = auto_bind
        self.options =  options = {
                          'headers': {
                            'Content-Type': 'application/json',
                            'produces': "application/json",
                            'X-Tenant-Access-Key': key,
                            'X-Tenant-Access-Token': token
                          },
                          'data': {}
                        }
        self.tenant_dict = {"account":[]}
        self.collection_dict = {"collection":[]}
        self.algorithm_dependencies = ["json_data_type", "application"]
        self.config_file = ""
        _logger.info("CenitManager Initialized")

    def update_ini_file(self, force=None):
        url = "https://cenit.io/app/ossehashsaltdocunexoossedemoose/get_tenants_info"
        session = Session()
        request = Request('GET', url)
        prepped = request.prepare()
        raw_response = session.send(prepped)
        data = raw_response.json()
        with open("current_tenants.json", "w") as f:
            f.write(json.dumps(data, indent=4))

        _, parser = self.get_input_and_config_parser()
        if isinstance(data, list):
            for d in data:
                parser.read_dict(d)
        elif isinstance(data, dict):
            parser.read_dict(data)

        ini_file_to_Write = "tmp_ini.cfg"
        if force:
            self.get_config_file_and_parser(filename_only=True)
            from datetime import datetime
            ini_file_to_Write = self.config_file
            if os.path.exists(self.config_file):
                with open(self.config_file, "r") as src, open("{}-{}.cfg".format(self.config_file[:-4], datetime.now().strftime("%Y%m%d")), 'w') as dst: dst.write(src.read())

        with open(ini_file_to_Write, "w") as ini:
            parser.write(ini)
        _logger.info(str(data))


    def get_self_dir(self, dir_path=None):
        dir_path = dir_path or self.dir_path
        if not self.cur_path.startswith("/"):
            self.cur_path = os.getcwd()

        aux_path = "{}/{}".format(self.cur_path, dir_path)
        if os.path.isdir(aux_path):
            self.full_path = aux_path
            _logger.info("Config JSON-Files PATH: [{}]".format(self.full_path))
            return True
        elif os.path.isdir(self.full_path):
            _logger.info("Config JSON-Files PATH: [{}]".format(self.full_path))
            return True
            return True

        return False

    def populate_dict_documents(self, doctype, content):
        if doctype == "account":
            self.tenant_dict[doctype].append(content)
            return
        elif doctype == "collection":
            self.collection_dict[doctype].append(content)
            return

        if isinstance(content, list):
            for dt in content:
                self.doc_types[doctype].append(dt)
        else:
            self.doc_types[doctype].append(content)

    def setup_and_bind_files(self, dir_path=None):
        #pdb.set_trace()
        _logger.info("Bind files with doc_types")
        if self.get_self_dir():
            for f in glob.glob("{}/*.json".format(self.full_path)):
                tmp_file = json.load(open(f,"r"))
                filename = f.split("/")[-1]
                if filename.startswith("_not"):
                    _logger.info(c.OKBLUE + ">>> Skip file: [{}] for current process!".format(filename) + c.ENDC)
                    continue

                if filename.find("data_type") > -1:
                    self.populate_dict_documents("json_data_type", tmp_file)
                elif filename.find("snippet") > -1:
                    self.populate_dict_documents("snippet", tmp_file)
                elif filename.find("schema") > -1:
                    self.populate_dict_documents("schema", tmp_file)
                elif filename.find("template") > -1:
                    self.populate_dict_documents("template", tmp_file)
                elif filename.find("flow") > -1:
                    self.populate_dict_documents("flow", tmp_file)
                elif filename.find("algorithms") > -1:
                    self.populate_dict_documents("algorithm", tmp_file)
                elif filename.find("tenant") > -1 or filename.find("account") > -1:
                    self.populate_dict_documents("account", tmp_file)
                elif filename.find("observer") > -1:
                    self.populate_dict_documents("observer", tmp_file)
                elif filename.find("ruby_parser") > -1:
                    self.populate_dict_documents("ruby_parser", tmp_file)
                elif filename.find("collection") > -1:
                    self.populate_dict_documents("collection", tmp_file)
                elif filename.find("connection") > -1:
                    self.populate_dict_documents("connection", tmp_file)
                elif filename.find("plain_webhook") > -1:
                    self.populate_dict_documents("plain_webhook", tmp_file)
                elif filename.find("sign_key") > -1:
                    self.populate_dict_documents("sign_key", tmp_file)
                elif filename.find("application") > -1:
                    self.populate_dict_documents("application", tmp_file)


        self.loaded_files = True
        _logger.info("Binded all files")

    def setup_options(self, key=None, token=None, env=None):
        self.key, self.token = key or self.key, token or self.token
        if not self.options["headers"]['X-Tenant-Access-Key']:
            self.options["headers"]['X-Tenant-Access-Key'] = self.key
            self.options["headers"]['X-Tenant-Access-Token'] = self.token
        _logger.info("Options Configured with crendentials:\n> key: [{}]  | token: [{}] | env: [{}]".format(self.key, self.token, self.env))

    def setup_credentials(self, key, token):
        self.key = key
        self.token = token

    def process_response(self, response):
        response_text = response.text
        json_response = response.json()
        color = c.SUCCESS
        text = response_text[:100] + (response_text[100:] and "...}")
        if "success" not in json_response.keys():
            color = c.ERROR
            text = response_text
        _logger.info("|> Operation response\n> {}\n".format(color + text + c.ENDC))

    def send(self, url, k, dtp_name=""):
        session = Session()
        request = Request('POST', url, **self.options)
        prepped = request.prepare()
        _logger.info("|> Sending DATA to [{}]\n> doc_type: [{}]->[{}] to: [{}]".format(c.PINK+self.tenant+c.ENDC, c.WHITE+k+c.ENDC, c.YELLOW+dtp_name+c.ENDC, url))
        if k not in ["account", "collection"]:
            return  self.process_response(session.send(prepped))
        else:
            return session.send(prepped)

    def save_log(self, data):
        with open("log.log", "w") as f:
            f.write(data)

    def get_datatype_name(self, dt):
        dtp_name =""
        if "name" in dt.keys():
            dtp_name = dt["name"]
            splitted = dtp_name.split(":")
            if len(splitted) > 0:
                dtp_name = splitted[-1]
        return dtp_name

    def bulk_upload(self):
        _logger.info("BULK UPLOAD Initializing")
        self.setup_options()
        if self.auto_bind and not self.loaded_files:
            self.setup_and_bind_files()

        if self.tenant_dict.get("account"):
            _logger.info(">>>>>>>>>>>>>TRY create a TENANT")
            k = "account"
            url = self.end_point.format(k)
            self.options.update({"data":json.dumps(self.tenant_dict.get(k))})
            response = self.send(url, k, "account" )

            response_json = response.json()
            response_text = response.text
            if "success" in response_json.keys():
                key = response_json["success"]["account"][0]["key"]
                token = response_json["success"]["account"][0]["token"]
                self.setup_credentials(key, token)
                self.setup_options()
                _logger.warning("Change the credentials data to new CREATED TENANT\n> new-key: [{}] | new-token: [{}]".format(self.key, self.token))

                #_logger.info("|> Operation response\n{}\n".format((response_text[:100] + "...}") if len(response_text) > 100 else response_text))
                import time
                time.sleep(3)
                _logger.info("|<<<<<<<<< TENANT CREATED!!!\n> {}\n".format(response_text[:100] + (response_text[100:] and "...}")))
            else:
                self.save_log(response_text)
                _logger.info("|<<<<<<<<< UNEXPECTED ERROR!!!\n> {}\n".format(response_text[:100] + (response_text[100:] and "...}")))

        if self.collection_dict.get("collection"):
            _logger.info(">>>>>>>>>>>>> CREATING COLLECTION!!!")
            k = "collection"
            url = self.end_point.format(k)
            self.options.update({"data":json.dumps(self.collection_dict.get(k))})

            response_text = self.send(url, k).text
            with open("log.log", "w") as f:
                f.write(response_text)
            _logger.info("|<<<<<<<<< COLLECTION CREATED!!!\n> {}\n".format(response_text[:100] + (response_text[100:] and "...}")))
            _logger.info("\n\nBULK UPLOAD Finished\n\n")
            return

        if self.doc_types["snippet"]:
            k = "snippet"
            url = self.end_point.format(k)
            for dt in self.doc_types[k]:
                self.options.update({"data":json.dumps(dt)})
                dtp_name = self.get_datatype_name(dt)
                response = self.send(url, k, dtp_name)

        for k, v in self.doc_types.items():
            url = self.end_point.format(k)
            if k == "snippet":
                continue
            if k == "sign_key":
                url = url.replace("setup", "ublpe")
            for dt in v:
                dtp_name = self.get_datatype_name(dt)
                if k in self.algorithm_dependencies:
                    algoritm_name = self.get_algorithm_name(dt, k)
                    if algoritm_name:
                        algoritm_name = self.get_algorithm_name(dt, k)
                        _logger.info("Found dependency-behavior: {}".format(algoritm_name))
                        for alg in self.doc_types["algorithm"]:
                            if alg["name"] == algoritm_name:
                                tmp_url = self.end_point.format("algorithm")
                                self.options.update({"data":json.dumps(alg)})
                                _logger.info("|> Sending DEPENDENCY [{}] for [{}]\n> doc_type: [{}]->[{}] to: [{}]".format(algoritm_name, dtp_name, c.PINK+"algorithm"+c.ENDC, c.BROWN+algoritm_name+c.ENDC, tmp_url))
                                response = self.send(tmp_url, "algorithm", algoritm_name)
                            break

                self.options.update({"data":json.dumps(dt)})
                response = self.send(url, k, dtp_name)

        _logger.info(c.BLUE+"\n\n\tBULK UPLOAD Finished to tenant: [{}]\n".format(self.tenant) +c.ENDC)

    def get_algorithm_name(self, dt, k):
        if k == "json_data_type":
            if dt["before_save_callbacks"]:
                return  dt["before_save_callbacks"][0]["name"]
        elif k == "application":
            return dt["actions"][0]["algorithm"]["name"]
        return False

    def get_input_and_config_parser(self):
        try:
            import ConfigParser
            return  raw_input, ConfigParser.RawConfigParser()
        except Exception as e:
            from configparser import ConfigParser
            return  input, ConfigParser()

    def get_config_file_and_parser(self, filename_only=None):
        inp, configParser = self.get_input_and_config_parser()
        config_file_name =  '/.cenit_manager_config.cfg'
        configFilePath = r'.{}'.format(config_file_name)
        home = os.getenv("HOME")
        if not home:
            home = os.path.expanduser("~")
        if not os.path.exists(configFilePath):
            configFilePath = "{}{}".format(home, config_file_name)
        self.config_file = configFilePath
        if filename_only:
            return configFilePath
        configParser.read(configFilePath)
        return inp, configParser


    def config_tenant(self):
        key, token, env = "", "", ""
        inp, configParser = self.get_config_file_and_parser()

        print("\n{}\n".format("List of Current TENANT's"))
        counter = 0
        for i, cnf in enumerate(configParser):
            counter = i
            if i > 0:
                print(i, cnf)

        opt = str(inp(c.BOLD + "\n\nSelect the TENANT number that use: " + c.ENDC))

        if opt:
            if opt.isdigit():
                if int(opt) > counter or int(opt) < 0:
                    _logger.info(c.FAIL +  "{}".format("Invalid TENANT Number, Canceling.") + c.ENDC)
                    return
                for i, cnf in enumerate(configParser):
                    if i == int(opt):
                        key = configParser.get(cnf, "key")
                        token = configParser.get(cnf, "token")
                        try:
                            env = configParser.get(cnf, "env")
                        except:
                            env = ""

                        _logger.info(c.OKBLUE + "\nTENANT Selected: [{}] - key: [{}] - token: [{}] - env: - [{}]\n".format(cnf, key, token, env) + c.ENDC)
                        self.tenant = cnf
                        self.key = key
                        self.token = token
                        self.env = env
                        return True
            else:
                _logger.info("{}".format("Invalid Input"))
        else:
            _logger.info("{}".format("Cancel Operation"))
        return False

    def menu(self):
        tmp_dict = {}
        _logger.info(c.OKBLUE + "\n\nListing candidate directories\n" + c.ENDC)
        i = 0
        for f in glob.glob("{}/*".format(self.cur_path)):
            if os.path.isdir(f):
                i += 1
                tmp_dict.update({i: f.split("/")[-1]})
                print("{}.- {}".format(i, f.split("/")[-1]))

        inp, _ = self.get_input_and_config_parser()
        opt = str(inp(c.BOLD + "\n\nSelect the 'directory' number that process: " + c.ENDC))

        if opt:
            if opt.isdigit():
                if int(opt) > i or int(opt) < 0:
                    _logger.info(c.FAIL +  "{}".format("Invalid DIRECTORY Number, Canceling.") + c.ENDC)
                    return
                for i, cnf in tmp_dict.items():
                    if i == int(opt):
                        self.dir_path = cnf
                        _logger.info(c.YELLOW + "\nDirectory Selected: [{}]".format(self.dir_path) + c.ENDC + "\n")
                        return True
        return True

    def get_data(self):
        #PARAMS = {'ID.value':invoice}
        #request = Request('GET', url, **self.options)
        #prepped = request.prepare()

        #r = requests.get(url = URL, params = PARAMS, headers=headers)
        pass

    def write_config(self):
        config = """
[PRD SOME TENANT]
name = ANY ENTERPRISE NAME
tenant = PRD SOME TENANT
key = ABC2343ZXCC
token = MYSECURETOKEN
env = sunat_beta sunat_production
connection_url = https://e-factura.sunat.gob.pe
webhook_path = ol-ti-itcpgem/billService
webhook_name = Produccion billSend
ruc = 20456986
username = SUNATUSER
password = SUNATPASS
connection_name = Connection
"""

        self.get_config_file_and_parser(filename_only=True)
        with open(self.config_file, "w") as f:
            f.write(config)
        print("\n\nPlease enter items for respective tenants, see example in: " + c.OKGREEN, self.config_file, "" + c.ENDC,"\n")
        print(c.SUCCESS,config,c.ENDC)
        for k, v in self.conection_options.items():
            print(c.YELLOW ,k," = ", v["endpoint"], c.ENDC)
        print(c.FAIL+"\nSpecial atemption in 'env' key, this is a 'connection url', must be a valid of next values\n")

def main():
    parser = argparse.ArgumentParser("cenit_manager")
    parser.add_argument("-d", "--dir", default="bizlinks.data", help="Directory where *.json files are located", type=str)
    parser.add_argument("-m", "--menu", default=False, help="RAISE for Menu mode", action="store_true")
    parser.add_argument("-k", "--key", default="apimode", help="KEY for connection")
    parser.add_argument("-t", "--token", default="apimode", help="TOKEN for connection")
    parser.add_argument("-e", "--env", default=False, help="ENVIRONMENT for connection")
    parser.add_argument("-i", "--ini", default=False, help="RESTORE .config file", action="store_true")
    parser.add_argument("-c", "--config", default=False, help="Make config files", action="store_true")
    parser.add_argument("-f", "--force", default=False, help="Force to overwrite .config file", action="store_true")
    parser.add_argument("-l", "--local", default=True, help="Process in premisse mode", action="store_true")
    parser.add_argument("-p", "--production", default=False, help="SEND to CENIT", action="store_true")
    parser.add_argument("-u", "--end_point", default="http://172.16.16.20:3000", help="EndPoint to send data")
    args = parser.parse_args()
    #print(args)

    if args.config:
        cm = CenitManager()
        cm.write_config()
        return

    if args.ini:
        cm = CenitManager()
        cm.update_ini_file(args.force)
        return

    if not args.production:
        cm = CenitManager(key=args.key,dir_path=args.dir , token=args.token, tenant="localhost", env=args.env, end_point=args.end_point, auto_bind=True)
        if args.menu:
            if not cm.menu():
                return
        cm.bulk_upload()
    else:
        cm = CenitManager(auto_bind=True, dir_path=args.dir)
        if cm.config_tenant():
            if not cm.menu():
                return
            cm.bulk_upload()
            #c.print_color()

if __name__ == '__main__':
    try:
        main()
        #c.print_color()
    except KeyboardInterrupt:
        _logger.warning("\n\nKeyboard Interrupt, canceling process!!!\n\n")
        try:
            import sys
            sys.exit(0)
        except SystemExit:
            import os
            os._exit(0);
