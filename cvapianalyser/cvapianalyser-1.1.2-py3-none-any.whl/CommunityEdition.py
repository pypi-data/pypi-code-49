import requests
import json
import multiprocessing
import threading

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://myretailcorp-poc.arecabay.net',
    'Authorization': 'Bearer null',
    'X-AB-Trace-ID': 'null-93adb9098c225bbbf754a4ceca135d285477c0cbc33e957f8faf9e1c9e95a18d',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://myretailcorp-poc.arecabay.net/customer/login',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

API_SPEC = {
    "basePath": "/",
    "info": {},
    "paths": {},
    "schemes": [
        "http"
    ],
    "swagger": "2.0"
}


class CommunityEdition(object):
    def __init__(self, host_url, username, password):
        self.host_url = host_url
        self.username = username
        self.password = password
        self.total_unique_apis = 0
        self.total_api_events = 0
        self.total_apis_inspec_captured = 0
        self.api_sec_details = {"auth": 0, "noauth": 0}
        try:
            self.get_access_token()
        except:
            print("Check your CE info provided!")
            raise SystemExit

    def get_access_token(self):
        global headers
        data = {"email": self.username, "password": self.password}
        response = requests.post(self.host_url + "/ce-api/auth/tenant/login", headers=headers, data=json.dumps(data))
        if response.status_code in [500]:
            print ("Issue with the CE setup, Please check! status code: " + str(response.status_code))
            raise SystemExit
        elif response.status_code in [401, 403]:
            print ("Please check your credentials!")
            raise SystemExit
        try:
            headers["Authorization"] = "Bearer " + str(response.json()["auth_token"])
        except KeyError:
            print ("\nPlease check your Community Edition (CE) credentials!\n")
            raise SystemExit
        print("\nAuthentication to Community Edition Successful!\n")
        return response.json()["auth_token"]

    def _get_all_policies(self):
        params = (
            ('page', '1'),
            ('size', '20'),
        )

        response = requests.get(self.host_url + '/ce-api/v1/tenants/1000/policies/of/api_recorder',
                                headers=headers, params=params, verify=False)
        policies = {}
        for each in response.json()["data"]:
            policies[each["attributes"]["name"]] = each["id"]
        return policies

    def get_policyid_from_name(self, policy):
        try:
            policies_for_tenant = self._get_all_policies()
        except:
            return None
        return policies_for_tenant[policy]

    def get_api_details_for_recording(self, policy):
        global API_SPEC
        data = {"filter_attributes": {"is_api": True}}
        api_details = {}
        try:
            policyid = self.get_policyid_from_name(policy)
        except KeyError:
            print("Please check the recording name provided!")
            raise SystemExit
        if policy:
            response = requests.post(
                self.host_url + '/ce-api/v1/tenants/1000/policies/of/api_recorder/' + str(policyid) + '/assoc',
                headers=headers, data=json.dumps(data), verify=False)

            for each in response.json()["data"]["data"]["attributes"]["data"]:
                self.total_unique_apis += 1
                API_SPEC["paths"][each["grouped_api"]] = {str(each["method"]).lower(): {"parameters": []}}
                if each["body_params"]:
                    for _ in each["body_params"]:
                        API_SPEC["paths"][each["grouped_api"]][str(each["method"]).lower()]["parameters"].append({
                            "in": "body",
                            "name": _["parameter_name"],
                            "required": str(_["optional"]),
                            "type": _["parameter_datatype"]
                        })
            self.total_api_events = self.total_unique_apis
            return API_SPEC
        else:
            print("probably not a valid Policy/recording name provided")

    def _get_params_for_events(self, api_name, start_time, end_time):
        import time
        start = time.time()
        data = {"from_time": start_time,
                "to_time": end_time,
                "page": 1, "size": 5000,
                "search": {"http_host": None,
                           "api": api_name,
                           "client_ip": None,
                           "destination_ip": None,
                           "destination_port": None,
                           "http_method": None,
                           "http_rsp_status_code": None},
                "filter_attributes": {"is_api": True}}
        response = requests.post(self.host_url + '/ce-api/v1/tenants/1000/events/search', headers=headers,
                                 data=json.dumps(data), verify=False)
        all_events_captured = {}
        for event in response.json()["data"]:
            all_events_captured[event["id"]] = {
                "params": event["attributes"]["event_json"].get("http-req-body-params", []),
                "response_code": str(event["attributes"]["event_json"].get("http-rsp-Status", "")).split(" ")[0]
            }
            if event["attributes"]["event_json"].get("http-req-header-Authorization"):
                all_events_captured[event["id"]].update({"is_api_secured": [True]})
            else:
                all_events_captured[event["id"]].update({"is_api_secured": [False]})
        return all_events_captured

    def _get_api_specific_details(self, apiname, start_time, end_time):
        global headers
        self.total_apis_inspec_captured += 1
        data = {"is_api": True, "size": 13}
        if not self.total_api_events:
            response = requests.post(self.host_url + '/ce-api/v1/tenants/1000/events/search', headers=headers,
                                     data=json.dumps(data), verify=False)
            self.total_api_events = response.json()["meta"]["total"]
            print("           Total events captured for all APIs: " + str(self.total_api_events))
        all_events_captured = self._get_params_for_events(apiname, start_time, end_time)
        print("           Total events captured for " + str(apiname) + ": " + str(
            len(all_events_captured)))
        api_auth = []
        resp_code = []
        params_found_for_api = []

        for k, v in all_events_captured.items():
            params_found_for_api.extend(v["params"])
            api_auth.extend(v["is_api_secured"])
            resp_code.append(v["response_code"])

        if all(api_auth):
            self.api_sec_details["auth"] += 1
        else:
            self.api_sec_details["auth"] += 1
        return list(set(params_found_for_api)), api_auth, list(set(resp_code))

    # def _get_api_specific_details(self, groupid, start_time, end_time):
    #     global headers
    #     data = {"group_id": groupid, "start_time": start_time, "end_time": end_time, "page": 1, "size": 1}
    #
    #     response = requests.post(self.host_url + '/ce-api/v1/tenants/1000/summary/pg/discovery/api_details',
    #                              headers=headers, data=json.dumps(data), verify=False)
    #     total_count = response.json()["data"]["attributes"]["total"]
    #     data["size"] = total_count
    #     self.total_api_events += total_count
    #     response = requests.post(self.host_url + '/ce-api/v1/tenants/1000/summary/pg/discovery/api_details',
    #                              headers=headers, data=json.dumps(data), verify=False)
    #     params_found_for_api = []
    #     api_name = response.json()["data"]["attributes"]["data"][0]["api"]
    #
    #     all_events_captured = self._get_params_for_events(api_name, start_time, end_time)
    #     print("           Total events captured for " + str(api_name) + ": " + str(
    #         len(all_events_captured)))
    #     api_auth = []
    #     resp_code = []
    #     for k, v in all_events_captured.items():
    #         params_found_for_api.extend(v["params"])
    #         api_auth.extend(v["is_api_secured"])
    #         resp_code.append(v["response_code"])
    #
    #     if all(api_auth):
    #         self.api_sec_details["auth"] += 1
    #     else:
    #         self.api_sec_details["auth"] += 1
    #     return list(set(params_found_for_api)), api_auth, list(set(resp_code))

    def get_all_api_details(self, apis_to_lookup=[], time_period=604800):
        import time
        data = {"filter_attributes": {"type": "all"}, "end_time": int(time.time()),
                "start_time": int(time.time()) - time_period,
                "page": 1, "size": 200}

        response = requests.post(self.host_url + '/ce-api/v1/tenants/1000/summary/pg/discovery/api_list',
                                 headers=headers, data=json.dumps(data), verify=False)

        if response.status_code != 200:
            print("API details not returned!")
            raise SystemExit

        all_api = response.json()["data"]
        if all_api:
            all_api = all_api["attributes"]["data"]
        print("Total API(s) captured in APIShark: " + str(len(all_api)))
        self.total_unique_apis = len(all_api)
        api_info = {}

        for apigroup in all_api:
            if apis_to_lookup:
                if apigroup["api"] not in apis_to_lookup:
                    continue
            params_found = []
            params, api_auth, resp_code = self._get_api_specific_details(apigroup["api"], data["start_time"],
                                                                         data["end_time"])
            for _ in params:
                params_found.append({"in": "body",
                                     "name": _,
                                     "required": "True",
                                     "type": "?"
                                     })
            # api_info[apigroup["api"]] = {"parameters":params_found}
            responses_captured = {}
            for _ in resp_code:
                if _:
                    responses_captured[str(_)] = {"description": ""}

            API_SPEC["paths"][apigroup["api"]] = {
                str(apigroup["method"]).lower():
                    {
                        "parameters": params_found,
                        "responses": responses_captured,
                        "security": [{
                            "type": "oauth2",
                            "authorizationUrl": "",
                            "flow": "implicit",
                            "scopes": {}
                        }]
                    }
            }
        return API_SPEC


if __name__ == "__main__":
    ce = CommunityEdition("http://34.238.148.157:31316", "gaurav@cloudvector.com", "Areca123")
    # print(ce.get_api_details_for_recording("Gb_test_30_Jan"))
    print(ce.get_api_details())
