import os
import json
from .CommunityEdition import CommunityEdition

api_coverage_details = {}


class CVAPIAnalyser(object):
    def __init__(self, input_spec, ceobj, ce_recording):
        if not self._check_file_exists(input_spec):
            print("Input SPEC file doesnt exist! Please check the path")
            raise SystemExit
        self.ceobj = ceobj
        with open(input_spec) as specobj:
            self.input_spec = json.loads(specobj.read())
        self.policy_name = ce_recording

    @staticmethod
    def _check_file_exists(f):
        if os.path.exists(f):
            return True
        return False

    def check_api_coverage(self):
        if self.policy_name:
            print("\nScanning through the recording "+str(self.policy_name)+"\n")
            api_details_recorded = self.ceobj.get_api_details_for_recording(self.policy_name)
        else:
            print("\nRecording not provided so scanning through all APIs captured in last one week\n")
            api_details_recorded = self.ceobj.get_all_api_details()
        for spec_api in self.input_spec["paths"]:
            if spec_api not in api_coverage_details:
                api_coverage_details[spec_api] = {"mandatory":{},"optional":{}}
            if spec_api in api_details_recorded["paths"]:
                api_detail_recorded = api_details_recorded["paths"][spec_api]
                for api_method in self.input_spec["paths"][spec_api]:
                    params_recorded = [p["name"] for p in api_detail_recorded[str(api_method).lower()]["parameters"]]
                    if self.input_spec["paths"][spec_api][api_method]["parameters"]:
                        for param in self.input_spec["paths"][spec_api][api_method]["parameters"]:
                            param_name = param["name"]
                            param_mandatory = param["required"]
                            if param["name"] in params_recorded:
                                if param_mandatory:
                                    api_coverage_details[spec_api]["mandatory"].update({param["name"]: "recorded"})
                                else:
                                    api_coverage_details[spec_api]["optional"].update({param["name"]: "recorded"})
                            else:
                                if param_mandatory:
                                    api_coverage_details[spec_api]["mandatory"].update({param["name"]: "not recorded"})
                                else:
                                    api_coverage_details[spec_api]["optional"].update({param["name"]: "not recorded"})
                    else:
                        api_coverage_details[spec_api].update({"_": "recorded"})
            else:
                api_coverage_details[spec_api] = {}
        for api,params in api_coverage_details.items():
            if params.get("mandatory"):
                coverage = (int(list(params["mandatory"].values()).count("recorded"))/len(params["mandatory"]))*100
            else:
                coverage = 0
            api_coverage_details[api]["coverage"] = coverage
        return api_coverage_details

    def generate_report(self):
        from jinja2 import Environment, FileSystemLoader
        import os

        root = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(root, 'templates')
        env = Environment(loader=FileSystemLoader(templates_dir))
        template = env.get_template('index.html')

        filename = os.path.join(root, 'ce_coveragereport.html')
        with open(filename, 'w') as fh:
            fh.write(template.render(
                ce_url=str(self.ceobj.host_url),
                ce_recorder=self.policy_name,
                api_details=api_coverage_details,
            ))

def main():
    import sys
    import getpass
    import yaml
    if os.path.exists(os.path.join(os.getcwd(), "my_cesetup.yaml")):
        with open(os.path.join(os.getcwd(), "my_cesetup.yaml")) as fobj:
            ce_details = yaml.load(fobj, Loader=yaml.FullLoader)
    else:
        ce_details = {}
    print("*****" * 20)
    print ("CloudVector CommunityEdition - Coverage analysis plugin")
    print("*****" * 20)
    print("\nCommunity Edition(CE) details from my_cesetup.yaml:\n\t" + str(ce_details) + "\n")
    if ce_details.get("ce_host"):
        ce_host = ce_details["ce_host"]
    else:
        ce_host = input("Enter CommunityEdition(CE) host in format <host>:<port> : ")
    if ce_details.get("ce_username"):
        ce_username = ce_details["ce_username"]
    else:
        ce_username = input("Enter your CommunityEdition(CE) username : ")
    ce_password = getpass.getpass(prompt="CommunityEdition(CE) password:")
    if ce_details.get("ce_recording"):
        ce_recording = ce_details["ce_recording"]
    else:
        ce_recording = input("Enter recording in CE to compare with : ")
    ceobj = CommunityEdition("http://" + ce_host, ce_username, ce_password)
    if ce_details.get("input_apispec"):
        input_spec = ce_details["input_apispec"]
    else:
        input_spec = input("Enter absolute path to API SPEC to compare against : ")
    an = CVAPIAnalyser(input_spec, ceobj, ce_recording)
    an.check_api_coverage()
    print("\n\n........... Checking API coverage details on the recording " + str(
        ce_recording) + " for the API SPEC input\n")
    print("API Coverage details:  " + str(api_coverage_details))
    print("\n")
    print("Report generated: " + str(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "ce_coveragereport.html")))
    print("\n")
    an.generate_report()


if __name__ == "__main__":
    main()
