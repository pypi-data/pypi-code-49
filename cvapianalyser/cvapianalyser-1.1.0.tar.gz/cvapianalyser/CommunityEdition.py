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
        params = (
            ('is_api', 'true'),
        )
        api_details = {}
        try:
            policyid = self.get_policyid_from_name(policy)
        except KeyError:
            print("Please check the recording name provided!")
            raise SystemExit
        if policy:
            response = requests.get(
                self.host_url + '/ce-api/v1/tenants/1000/policies/of/api_recorder/' + str(policyid) + '/assoc',
                headers=headers, params=params, verify=False)
            for each in response.json()["data"]["data"]["attributes"]["data"]:
                API_SPEC["paths"][each["grouped_api"]] = {str(each["method"]).lower(): {"parameters": []}}
                if each["body_params"]:
                    for _ in each["body_params"]:
                        API_SPEC["paths"][each["grouped_api"]][str(each["method"]).lower()]["parameters"].append({
                            "in": "body",
                            "name": _["parameter_name"],
                            "required": str(_["optional"]),
                            "type": _["parameter_datatype"]
                        })
            return API_SPEC
        else:
            print("probably not a valid Policy/recording name provided")

    def _get_params_for_event(self, headers, eventid, all_events_captured):
        response = requests.get(self.host_url + '/ce-api/v1/tenants/1000/events/' + str(eventid), headers=headers,
                                verify=False)
        all_events_captured[eventid] = response.json()["data"]["attributes"]["event_json"].get("http-req-body-params",
                                                                                               [])
        # return response.json()["data"]["attributes"]["event_json"].get("http-req-body-params", [])

    def _get_api_specific_details(self, groupid, start_time, end_time):
        global headers
        manager = multiprocessing.Manager()
        all_events_captured = manager.dict()
        data = {"group_id": groupid, "start_time": start_time, "end_time": end_time, "page": 1, "size": 1}

        response = requests.post(self.host_url + '/ce-api/v1/tenants/1000/summary/pg/discovery/api_details',
                                 headers=headers, data=json.dumps(data), verify=False)
        total_count = response.json()["data"]["attributes"]["total"]
        data["size"] = total_count
        self.total_api_events += total_count
        response = requests.post(self.host_url + '/ce-api/v1/tenants/1000/summary/pg/discovery/api_details',
                                 headers=headers, data=json.dumps(data), verify=False)
        params_found_for_api = []
        api_name = response.json()["data"]["attributes"]["data"][0]["api"]

        print("    Total events captured for " + str(api_name) + ": " + str(
            len(response.json()["data"]["attributes"]["data"])))
        jobs = []
        for event in response.json()["data"]["attributes"]["data"]:
            #p = multiprocessing.Process(target=self._get_params_for_event,
            #                            args=(headers, event["id"], all_events_captured))
            p = threading.Thread(target=self._get_params_for_event,
                                 args=(headers, event["id"], all_events_captured))
            jobs.append(p)
            p.start()

        for _ in jobs:
            _.join()

        for k, v in all_events_captured.items():
            params_found_for_api.extend(v)
        return list(set(params_found_for_api))

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
            for _ in self._get_api_specific_details(apigroup["group_id"], data["start_time"], data["end_time"]):
                params_found.append({"in": "body",
                                     "name": _,
                                     "required": "True",
                                     "type": "?"
                                     })
            # api_info[apigroup["api"]] = {"parameters":params_found}
            API_SPEC["paths"][apigroup["api"]] = {
                str(apigroup["method"]).lower():
                    {
                        "parameters": params_found
                    }
            }
        return API_SPEC


if __name__ == "__main__":
    ce = CommunityEdition("http://34.238.148.157:31316", "gaurav@cloudvector.com", "Areca123")
    # print(ce.get_api_details_for_recording("Gb_test_30_Jan"))
    print(ce.get_api_details())
