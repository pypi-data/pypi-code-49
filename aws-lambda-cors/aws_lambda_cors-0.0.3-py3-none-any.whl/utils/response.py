import json
from aws_lambda_cors.utils.headers import HEADERS


class AwsLambdaResponse:
    def __init__(self, body, headers, status_code=200):
        
        self.status_code = status_code
        self.body = body
        self.headers = {**HEADERS, **headers}
    
    def parse(self, status_code=None):
        if not status_code:
            status_code = self.status_code
        return {
            "statusCode": status_code,
            "headers": self.headers,
            "body": json.dumps(self.body)
        }
    
    def __str__(self):
        return json.dumps({
            "statusCode": self.status_code,
            "headers": self.headers,
            "body": json.dumps(self.body)
        })
    

    def accepted_origins(self, origins):
        if len(origins) == 0:
            raise Exception('origins cannot be empty')
        self.headers['Access-Control-Allow-Origin'] = ', '.join(origins)
    
    def allowed_methods(self, methods=('GET', 'POST', 'OPTIONS')):
        self.headers['Access-Control-Allow-Methods'] = ', '.join(methods)

    def set_header(self, header):
        self.headers = {**self.headers, **header}
