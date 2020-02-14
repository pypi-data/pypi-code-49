#!/usr/bin/env python
import pandas as pd
import requests
import argparse
import boto3
import json
import os
import io
from io import StringIO

class OpleClient:
    """

    """
    def __init__(self, key, secret, model_id, aws_key='ENV', aws_secret='ENV, url_base='https://prediction.ople.ai/api'):
        """

        :param key:
        :param secret:
        :param model_id:
        :param aws_key:
        :param aws_secret:
        :param url_base:
        """
        self.credentials = {'key': key, 'secret': secret}
        self.model_id = model_id
        self.url_base = url_base
        self.aws_key = aws_key
        self.aws_secret = aws_secret

    def __is_input_s3(self, input):
        """
        This checks if the input contains a dictioanry with information about a file in s3
        :param input: Dictionary with buckeet and path as keys
        :return: True or False
        """
        try:
            data = json.loads(input)
            result = all(key in data.keys() for key in ["bucket", "path"])
        except Exception as e:
            result = False
        finally:
            return result

    def __is_input_ople_format(self, input):
        """
        This function checks whether the input is in the following format
        {columns: [], rows: [[]]}
        :param input: Dictionary
        :return: True or False
        """
        try:
            data = json.loads(input)
            result = all(key in data.keys() for key in ["columns", "rows"])
        except Exception as e:
            result = False
        finally:
            return result

    def __is_input_file(self, input):
        """
        This function checks whether a local file exists
        :param input: path to local file
        :return: True or False
        """
        return True if os.path.isfile(input) else False

    def __is_input_csv_text(self, input):
        """
        This function checks whether the input is a string in csv format
        :param input: string
        :return:  True or False
        """
        result = False
        try:
            data = pd.read_csv(io.StringIO(input), sep=",")
            rows, _ = data.shape
            result = True
        except Exception as e:
            result = False
        finally:
            return result

    def predict(self, input, shap=False, global_shap=False, allow_unknown_categories=False):
        """
        :param data: input and flags for the different options for the API
        :return: returns a json with the outcomes from the prediction
        """
        try:
            # Get the Authorization Token
            r = requests.post('{}/v1/security/token'.format(self.url_base), json=self.credentials)
            token = r.json()['token']

            # Parse Input Data
            if self.__is_input_ople_format(input):
                print("- Input: Ople Prediction Format")
                data = json.loads(input)
                columns = data['columns']
                rows = data['rows']
            elif self.__is_input_s3(input):
                print('- Input: S3')
                s3 = boto3.client('s3', aws_access_key_id=self.aws_key, aws_secret_access_key=self.aws_secret)
                info = json.loads(input)
                obj = s3.get_object(Bucket=info['bucket'], Key=info['path'])
                data = pd.read_csv(io.BytesIO(obj['Body'].read()))
                columns = data.columns.values.tolist()
                rows = data.values.tolist()
            elif self.__is_input_file(input):
                print("- Input: CSV File")
                data = pd.read_csv(input)
                columns = data.columns.values.tolist()
                rows = data.values.tolist()
            elif self.__is_input_csv_text(input):
                print("- Input: CSV Formatted String")
                payload = StringIO(input.replace('\\n', '\n'))
                data = pd.read_csv(payload)
                columns = data.columns.values.tolist()
                rows = data.values.tolist()
            elif isinstance(input, pd.DataFrame):
                print("- Input: DataFrame")
                columns = input.columns.values.tolist()
                rows = input.values.tolist()
            else:
                result = "Cannot Read Input"

            # Set the payload
            payload = {
                'columns': columns,
                'rows': rows,
                'shap': shap,
                'global_shape': global_shap,
                'allow_unknown_categories': allow_unknown_categories
            }
            prediction_url = "{}/v2/models/{}/invoke".format(self.url_base, self.model_id)
            res = requests.post(prediction_url, json=payload, headers={'Authorization': 'Bearer ' + token})
            result = res.json()
        except Exception as e:
            result = "Error: {}".format(e)
        finally:
            return result

# ********************************************************************************
#                              Python Script Executable
#
# Working Commands:
# ople-client -u -s -g ./data.csv
# ople-client -u -s -g '{"bucket": "ople-dataset-nahid", "path": "data.csv"}'
# ople-client -u -s -g "age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome\n58,management,married,tertiary,no,2143,yes,no,unknown,5,may,261,1,-1,0,unknown"
# ople-client -u -s -g python3 client.py -u -s -g '{"columns": ["age", "job", "marital", "education", "default", "balance", "housing", "loan", "contact", "day", "month", "duration", "campaign", "pdays", "previous", "poutcome"], "rows": [["58", "management", "married", "tertiary", "no", "2143", "yes", "no", "unknown", "5", "may", "261", "1", "-1", "0", "unknown"]]}'
#
#
# ********************************************************************************

if __name__ == "__main__":

    # 1. Code to read input
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="shows output")
    parser.add_argument('-s','--shap', action="store_true",help="shows output")
    parser.add_argument('-g', '--global_shap', action="store_true", help="shows output")
    parser.add_argument('-u', '--allow_unknown_categories', action="store_true", help="shows output")
    parser.add_argument('-K', '--key', default="ENV", help="shows output")
    parser.add_argument('-S', '--secret', default="ENV", help="shows output")
    parser.add_argument('-AK', '--aws_key', default="ENV", help="shows output")
    parser.add_argument('-AS', '--aws_secret', default="ENV", help="shows output")
    parser.add_argument('-ID', '--model_id', default="ENV", help="shows output")

    args = parser.parse_args()

    ople_key = args.key if args.key != "ENV" else os.environ['OPLE_KEY']
    ople_secret = args.secret if args.secret != "ENV" else os.environ['OPLE_SECRET']
    ople_model_id = args.model_id if args.model_id != "ENV" else os.environ['OPLE_MODEL_ID']
    aws_key = args.aws_key if args.aws_key != "ENV" else os.environ['AWS_KEY']
    aws_secret = args.aws_secret if args.aws_key != "ENV" else os.environ['AWS_SECRET']

    print("*" * 70)
    print(" "*30 + "Ople Client")
    print("\nAccount Information:\n- Key: {}\n- Secret: {}\n- AWS Key: {}\n- AWS SECRET: {}".format(ople_key, ople_secret, aws_key, aws_secret))
    print("\nModel Information:\n- Model ID: {}".format(ople_model_id))
    print('\nPrediction Information:\n- Allow Unknown Categories: {}\n- Shap: {}\n- Global Shap: {}'.format(args.allow_unknown_categories, args.shap, args.global_shap))


    # 2. Setup Credentials of Model
    model = OpleClient(ople_key, ople_secret, ople_model_id, aws_key, aws_secret)

    # 3. Make Prediction
    result = model.predict(args.input,
                  shap=args.shap,
                  global_shap=args.global_shap,
                  allow_unknown_categories=args.allow_unknown_categories)

    print("\nResult:\n-Output: {}".format(result))
    print("*" * 70)
