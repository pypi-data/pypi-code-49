import os
import json
from .CommunityEdition import CommunityEdition

api_coverage_details = {}
overall_api_stats = {"total_mandatory_missing": {"one": 0, "two": 0, "three": 0, "four": 0, "five+": 0},
                     "total_optional_missing": {"one": 0, "two": 0, "three": 0, "four": 0, "five+": 0},
                     "total_mandatory_parameters": {"one": 0, "two": 0, "three": 0, "four": 0, "five+": 0},
                     "total_optional_parameters": {"one": 0, "two": 0, "three": 0, "four": 0, "five+": 0},
                     "auth": 0, "noauth": 0, "cumulative_total_mandatory": 0, "cumulative_total_optional": 0,
                     "total_response_codes": 0}
overall_spec_stats = {"total_mandatory_parameters": {"one": 0, "two": 0, "three": 0, "four": 0, "five+": 0},
                      "total_optional_parameters": {"one": 0, "two": 0, "three": 0, "four": 0, "five+": 0},
                      "auth": 0, "noauth": 0, "cumulative_total_mandatory": 0, "cumulative_total_optional": 0,
                      "total_response_codes": 0}
api_details_captured = {}


class CVAPIAnalyser(object):
    def __init__(self, input_spec, ceobj, ce_recording):
        if not self._check_file_exists(input_spec):
            print("Input SPEC file doesnt exist! Please check the path")
            raise SystemExit
        self.ceobj = ceobj
        with open(input_spec) as specobj:
            self.input_spec = json.loads(specobj.read())
        self.input_spec_filename = input_spec.split("/")[-1]
        self.policy_name = ce_recording

    @staticmethod
    def _check_file_exists(f):
        if os.path.exists(f):
            return True
        return False

    def _update_overall_spec_stats(self, key, num_of_params):
        global overall_spec_stats
        if num_of_params == 1:
            overall_spec_stats[key]["one"] += 1
        elif num_of_params == 2:
            overall_spec_stats[key]["two"] += 1
        elif num_of_params == 3:
            overall_spec_stats[key]["three"] += 1
        elif num_of_params == 4:
            overall_spec_stats[key]["four"] += 1
        elif num_of_params >= 5:
            overall_spec_stats[key]["five+"] += 1

        if "total_mandatory_parameters" in key:
            overall_spec_stats["cumulative_total_mandatory"] += num_of_params
        elif "total_optional_parameters" in key:
            overall_spec_stats["cumulative_total_optional"] += num_of_params

    def _update_overall_stats(self, key, num_of_params):
        global overall_api_stats
        if num_of_params == 1:
            overall_api_stats[key]["one"] += 1
        elif num_of_params == 2:
            overall_api_stats[key]["two"] += 1
        elif num_of_params == 3:
            overall_api_stats[key]["three"] += 1
        elif num_of_params == 4:
            overall_api_stats[key]["four"] += 1
        elif num_of_params >= 5:
            overall_api_stats[key]["five+"] += 1

        if "total_mandatory_parameters" in key:
            overall_api_stats["cumulative_total_mandatory"] += num_of_params
        elif "total_optional_parameters" in key:
            overall_api_stats["cumulative_total_optional"] += num_of_params

    def check_api_coverage(self):
        global api_details_captured
        global overall_api_stats
        if self.policy_name:
            print("\nScanning through the recording " + str(self.policy_name) + "\n")
            print("Total API(s) in input SPEC: " + str(len(self.input_spec["paths"])))
            api_details_recorded = self.ceobj.get_api_details_for_recording(self.policy_name)
        else:
            print("\nRecording not provided so scanning through all APIs captured in last one week\n")
            print("Total API(s) in input SPEC: " + str(len(self.input_spec["paths"])))
            api_details_recorded = self.ceobj.get_all_api_details(list(self.input_spec["paths"].keys()))
            # api_details_recorded = self.ceobj.get_all_api_details()
        api_details_captured = api_details_recorded["paths"]
        for spec_api in self.input_spec["paths"]:
            if spec_api not in api_coverage_details:
                api_coverage_details[spec_api] = {"mandatory": {}, "optional": {}}
            if spec_api in api_details_recorded["paths"]:
                api_detail_recorded = api_details_recorded["paths"][spec_api]
                mandatory_params_in_spec = 0
                optional_params_in_spec = 0
                for api_method in self.input_spec["paths"][spec_api]:
                    params_recorded = [p["name"] for p in api_detail_recorded[str(api_method).lower()]["parameters"]]
                    respcode_recorded = [_ for _ in api_detail_recorded[str(api_method).lower()]["responses"]]
                    auth = [True for _ in self.input_spec["paths"][spec_api][api_method].get("security", [{}])
                            if len(_) > 0]
                    respcode_inspec = list(self.input_spec["paths"][spec_api][api_method].get("responses", {}).keys())
                    overall_api_stats["total_response_codes"] += len(respcode_recorded)
                    overall_spec_stats["total_response_codes"] += len(respcode_inspec)
                    if auth:
                        overall_spec_stats["auth"] += 1
                    else:
                        overall_spec_stats["noauth"] += 1
                    api_coverage_details[spec_api]["respcode_inspec"] = respcode_inspec
                    api_coverage_details[spec_api]["respcode_recorded"] = respcode_recorded
                    try:
                        api_coverage_details[spec_api]["respcode_coverage"] = \
                            (len(respcode_recorded) / len(respcode_inspec)) * 100
                    except ZeroDivisionError:
                        api_coverage_details[spec_api]["respcode_coverage"] = "?"
                    if self.input_spec["paths"][spec_api][api_method]["parameters"]:
                        for param in self.input_spec["paths"][spec_api][api_method]["parameters"]:
                            param_name = param["name"]
                            param_mandatory = param["required"]
                            if param_mandatory:
                                mandatory_params_in_spec += 1
                            else:
                                optional_params_in_spec += 1
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
                    self._update_overall_spec_stats("total_mandatory_parameters", mandatory_params_in_spec)
                    self._update_overall_spec_stats("total_optional_parameters", optional_params_in_spec)
            else:
                api_coverage_details[spec_api] = {}

        for api, params in api_coverage_details.items():
            if api == "stats":
                continue
            if params.get("mandatory"):
                coverage = (int(list(params["mandatory"].values()).count("recorded")) / len(params["mandatory"])) * 100
            else:
                coverage = 0
            if params.get("optional"):
                optional_coverage = (int(list(params["optional"].values()).count("recorded")) / len(
                    params["optional"])) * 100
            else:
                optional_coverage = 0
            api_coverage_details[api]["coverage"] = int(coverage)
            api_coverage_details[api]["optional_coverage"] = int(optional_coverage)

            if params.get("mandatory"):
                api_coverage_details[api]["mandatory_missing"] = list(params["mandatory"].values()).count(
                    "not recorded")
            else:
                api_coverage_details[api]["mandatory_missing"] = 0
            if params.get("optional"):
                api_coverage_details[api]["optional_missing"] = list(params["optional"].values()).count("not recorded")
            else:
                api_coverage_details[api]["optional_missing"] = 0

            self._update_overall_stats("total_mandatory_missing", api_coverage_details[api]["mandatory_missing"])
            self._update_overall_stats("total_optional_missing", api_coverage_details[api]["optional_missing"])

            self._update_overall_stats("total_mandatory_parameters",
                                       len([k for k, v in params.get("mandatory", {}).items() if v == "recorded"]))
            self._update_overall_stats("total_optional_parameters",
                                       len([k for k, v in params.get("optional", {}).items() if v == "recorded"]))

            mandatory_params_in_spec = []
            optional_params_in_spec = []

            for method in self.input_spec["paths"][api]:
                for p in self.input_spec["paths"][api][method].get("parameters", []):
                    if p.get("required"):
                        mandatory_params_in_spec.append(p["name"])
                    else:
                        optional_params_in_spec.append(p["name"])
            api_coverage_details[api]["mandatory_params_in_spec"] = mandatory_params_in_spec
            api_coverage_details[api]["optional_params_in_spec"] = optional_params_in_spec
            overall_api_stats["total_apis_captured"] = self.ceobj.total_unique_apis
            overall_api_stats["total_apis_in_spec"] = len(self.input_spec["paths"])
            overall_api_stats["total_api_events_captured"] = self.ceobj.total_api_events
            overall_api_stats["apis_in_spec_not_captured"] = list(
                set(list(self.input_spec["paths"].keys())) - set(list(api_details_captured)))
            overall_api_stats["apis_in_spec_captured"] = self.ceobj.total_apis_inspec_captured
            try:
                if overall_spec_stats["cumulative_total_optional"] == 0:
                    overall_coverage_score = ((7*(int(overall_api_stats["apis_in_spec_captured"]) / int(overall_api_stats["total_apis_in_spec"])) +
                                          2*(int(overall_api_stats["cumulative_total_mandatory"]) / int(overall_spec_stats["cumulative_total_mandatory"])) + (
                                          1*(int(overall_api_stats["cumulative_total_optional"]) / 1)))/10) * 100
                else:
                    overall_coverage_score = ((7 * (int(overall_api_stats["apis_in_spec_captured"]) / int(
                        overall_api_stats["total_apis_in_spec"])) +
                                               2 * (int(overall_api_stats["cumulative_total_mandatory"]) / int(
                                overall_spec_stats["cumulative_total_mandatory"])) + (
                                                       1 * (int(overall_api_stats["cumulative_total_optional"]) / int(
                                                   overall_spec_stats["cumulative_total_optional"])))) / 10) * 100
            except ZeroDivisionError:
                overall_coverage_score = "?"
            overall_api_stats["overall_coverage_score"] = overall_coverage_score
        return api_coverage_details

    def generate_report(self):
        from jinja2 import Environment, FileSystemLoader
        import os
        import datetime

        root = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(root, 'templates')
        env = Environment(loader=FileSystemLoader(templates_dir))
        template = env.get_template('index.html')
        test_start_time = datetime.date.today() - datetime.timedelta(7)
        test_end_time = datetime.date.today()
        filename = os.path.join(os.getcwd(), 'ce_coveragereport.html')
        with open(filename, 'w') as fh:
            fh.write(template.render(
                ce_url=str(self.ceobj.host_url),
                ce_recorder=self.policy_name,
                input_api_spec=self.input_spec_filename,
                api_test_window=test_start_time.strftime('%d, %b %Y') + " to " + test_end_time.strftime('%d, %b %Y'),
                api_details=api_coverage_details,
                api_stats=overall_api_stats,
                api_spec_stats=overall_spec_stats,
                total_mandatory_params={"inspec": overall_spec_stats["cumulative_total_mandatory"],
                                        "apishark": overall_api_stats["cumulative_total_mandatory"]},
                total_optional_params={"inspec": overall_spec_stats["cumulative_total_optional"],
                                       "apishark": overall_api_stats["cumulative_total_optional"]},
                api_security_Details={
                    "inspec": {"auth": overall_spec_stats["auth"], "noauth": overall_spec_stats["noauth"]},
                    "apishark": {"auth": self.ceobj.api_sec_details["auth"],
                                 "noauth": self.ceobj.api_sec_details["noauth"]}}
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
        os.path.join(os.getcwd(), "ce_coveragereport.html")))
    print("\n")
    an.generate_report()


if __name__ == "__main__":
    main()
