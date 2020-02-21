from flask import Flask, request, jsonify
from functools import wraps
import requests
import pyodbc


class SalureConnectQuark(object):
    def __init__(self):
        app = Flask(__name__)
        app.config['APPLICATION_ROOT'] = '/quark/api'

        # Following the authenticate functions which will handle requests without an Authorization Header
        def check_auth(token, customer):
            try:
                # Check with the token in the header, if this is a valid token and a valid customer
                url = 'https://salureconnect.com/api/v1/customers'
                headers = {'Authorization': f"SalureToken {token}"}
                response = requests.get(url=url, headers=headers)
                # Check if the token_id and the customer_id and the check_combinations are valid
                if 200 <= response.status_code <= 300 and response.json()[0] == customer:
                    return True
                else:
                    return False
            except Exception as e:
                print(e)
                return False

        def authenticate():
            message = {'message': "Authenticate with a correct customer and token header."}
            response = jsonify(message)
            response.status_code = 401
            response.headers['WWW-Authenticate'] = 'Authorization="SalureToken token"'

            return response

        def requires_auth(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                try:
                    # Get the customer and token from the headers.
                    customer = request.headers['salure-customer']
                    token = request.headers['Authorization'][12:]
                    # If there are no customer or token header, return a 401
                    if not customer or not token:
                        return authenticate()
                    # Check if the customer / token combination is valid
                    elif not check_auth(token, customer):
                        return authenticate()
                    return f(*args, **kwargs)
                except:
                    return authenticate()
            return decorated

        @app.route('/quark/api/', methods=['GET'])
        def home():
            return 'This SalureConnect Quark agent is of your service. \n' \
                   'To get all the available endpoints for this specific customer, go to https://<customer-dns>/api/endpoints. There is an explanation for each endpoint. \n' \
                   'The base url is \'https://<customer-dns>/api/\' \n' \
                   'Don\'t forget to give the correct headers for authorization. \n' \

        @app.route('/quark/api/endpoints', methods=['GET'])
        @requires_auth
        def endpoints():
            """
            Contains information about each endpoint so that the caller knows which endpoint should be used for what
            :return: a JSON with all the endpoints and their information
            """
            try:
                # Get all the tasks from a specific customer
                response = jsonify({
                    'endpoints': [
                        {'upload_xml_metacom': 'Give an XML in the body in blob format. This endpoint takes the blob, converts to XML and places it in the correct folder'},
                        {'download_hours_metacom': 'The webserver pick a file from a certain location, returns this in the body and writes the file on location to a archive folder'},
                        {'upload_csv_ad': 'Give a CSV to the endpoint. The webserver transfered this file to the correct location'},
                        {'write_to_fam_sql_view': 'Give a JSON in the body. The webserver will enter the data from the JSON into the corresponding SQL view'}
                    ]
                })
                response.status_code = 200
                return response
            except Exception as e:
                return 'You\'ve tried to get all the endpoints. This returned the following error: {}'.format(e)


        @app.route('/quark/api/upload_xml_metacom', methods=['GET'])
        @requires_auth
        def upload_xml_metacom():
            try:
                args = request.args
                task_id = args['task_id']
                if not task_id:
                    return 'Enter the following parameter and value: task_id=value. To get all available tasks, call the /tasks endpoint.'
                else:
                    # Get all the tasks from a specific customer
                        message = {
                            'task_id': task_id,
                            'result': 'Started successfully'
                        }
                        response = jsonify({'execution_report': message})
                        response.status_code = 200
                        return response
            except Exception as e:
                return f'You\'ve tried to call the upload_xml_metacom endpoint. This returned the following error: {e}'

        @app.route('/quark/api/download_hours_metacom', methods=['GET'])
        @requires_auth
        def download_hours_metacom():
            try:
                response = jsonify({'execution_report': 'Endpoint not available yet'})
                response.status_code = 200
                return response
            except Exception as e:
                return f'You\'ve tried to call the download_hours_metacom endpoint. This returned the following error: {e}'

        @app.route('/quark/api/upload_csv_ad', methods=['GET'])
        @requires_auth
        def upload_csv_ad():
            try:
                response = jsonify({'execution_report': 'Endpoint not available yet'})
                response.status_code = 200
                return response
            except Exception as e:
                return f'You\'ve tried to call the upload_csv_ad endpoint. This returned the following error: {e}'

        @app.route('/quark/api/write_to_fam_sql_view', methods=['GET'])
        @requires_auth
        def write_to_fam_sql_view():
            try:
                response = jsonify({'execution_report': 'Endpoint not available yet'})
                response.status_code = 200
                return response
            except Exception as e:
                return f'You\'ve tried to call the write_to_fam_sql_view endpoint. This returned the following error: {e}'

        # Some error handlers
        @app.errorhandler(404)
        def not_found(error=None):
            message = {
                'status': 404,
                'message': 'Not Found: ' + request.url,
            }
            response = jsonify(message)
            response.status_code = 404
            return response


        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=8888)


SalureConnectQuark()

