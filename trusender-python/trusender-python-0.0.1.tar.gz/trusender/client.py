import requests
import json

class Client(object):
    def __init__(self, auth_token):
        self.auth_token = auth_token

    def send_email(self, template_name, to_address, data_mapping):
        deliver_status = False
        endpoint = "https://api.trusender.com/v1/sendEmail"
        request_data = {'auth_token': self.auth_token, 'email': to_address, 'template_name': template_name, "data_mapping": data_mapping}
        print("initiating sending email...")
        response = self.send_api_request(endpoint, request_data)
        print(response)
        print("Email Delivered Successfully..!")
        return request_data

    def send_api_request(self, endpoint, request_data):
        request_data = json.dumps(request_data);

        headers  = {'Accept': 'application/json', 'Content-Type': 'application/json'}

        response = requests.post(endpoint, headers=headers, data=request_data)

        return response;