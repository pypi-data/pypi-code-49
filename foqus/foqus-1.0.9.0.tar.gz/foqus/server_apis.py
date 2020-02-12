import ast
import json

import requests
from foqus.mqueue import *

import logging
import coloredlogs
import time
from flask import jsonify, make_response

if USE_LOG_AZURE:

    from azure_storage_logging.handlers import TableStorageHandler

    # configure the handler and add it to the logger
    logger = logging.getLogger(__name__)
    handler = TableStorageHandler(account_name=LOG_AZURE_ACCOUNT_NAME,
                                  account_key=LOG_AZURE_ACCOUNT_KEY,
                                  extra_properties=('%(hostname)s',
                                                    '%(levelname)s'))
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
else:

    logger = logging.getLogger(__name__)
    coloredlogs.install()
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(LOG_PATH + 'trynfit_debug.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s', '%d/%b/%Y %H:%M:%S')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        try:
            data = json.loads(result)
            data['log_time'] = (te - ts)
            logger.info('%r  %2.2f s (try)' % (method.__name__, (te - ts)))
        except Exception as e:
            data = {}
            data['data'] = result
            data['log_time'] = (te - ts)
            logger.info('%r  %2.2f s (except)' % (method.__name__, (te - ts)))

        return (data)
    return timed


def format_to_json_response(response):
    response_dict = "{'Response': 'OK',\n" \
                    " 'Similars': [\n"
    for i in range(len(response)):
        if i == len(response) - 1:
            response_dict += "      '" + str(response[i]) + "'\n"
        else:
            response_dict += "      '" + str(response[i]) + "',\n"
    response_dict += "   ]\n}"

    return ast.literal_eval(response_dict)


def rest_api_request( server, request_type, user_api_key, operation, customer_name, customer_type, customer_universe,
                     project_name, body, customer_email, customer_password, type_user, first_name, last_name,
                      phone_number, job, number_of_staff, plan, cms_if_exist, url_cms, new_email, new_password,
                      new_password_verif, subject_of_email, message_email, month_num, ip, token_cms):
    try:
        # REST API tests
        s = requests.Session()
        s.auth = (customer_name, user_api_key)
        s.headers.update({'Content-Type': 'application/json'})
        data = {'user_apikey': user_api_key,
                'operation': operation,
                'customer_name': customer_name,
                'customer_type': customer_type,
                'customer_universe': customer_universe,
                'project_name': project_name,
                'customer_email': customer_email,
                'customer_password': customer_password,
                'type_user': type_user,
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
                'job': job,
                'number_of_staff': number_of_staff,
                'plan': plan,
                'cms_if_exist': cms_if_exist,
                'url_cms': url_cms,
                'new_email': new_email,
                'new_password': new_password,
                'new_password_verif': new_password_verif,
                'subject_of_email': subject_of_email,
                'message_email': message_email,
                'body': body,
                'month_num': month_num,
                'ip': ip,
                'token_cms': token_cms
                }

        url = server + "/api/" + operation
        if request_type.lower() == 'get':
            r = s.get(url=url, data=json.dumps(data))
        elif request_type.lower() == 'post':
            r = s.post(url=url, data=json.dumps(data))
        elif request_type.lower() == 'put':
            r = s.put(url=url, data=json.dumps(data))
        else:
            logger.error("Unsupported request type: " + str(request_type))
            return
        return r
    except:
        logger.error("No connection with the webserver")
        return make_response(jsonify({"response": "Bad request"}), 400)


@timeit
def get_similars_if_exist(user_apikey, customer_name, customer_type, project_name, body, ip):
        rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                              mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
        value = rpc_queue.call(headers={'user_apikey': user_apikey,
                                        'operation': 'get_similars_if_exist',
                                        'customer_name': customer_name,
                                        'customer_type': customer_type,
                                        'project_name': project_name,
                                        'ip': ip
                                        },
                               message_body=body)
        rpc_queue.close()
        return value.decode('utf-8')

# api_authentication
@timeit
def customer_authentication(customer_email, customer_password, body, type_user):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'type_user': type_user,
                                    'operation': 'client_authentication',
                                    'customer_name': "",
                                    'customer_type': "",
                                    'user_apikey': "",
                                    'customer_password': customer_password},
                           message_body=body)
    value = value.decode('utf-8')
    return value


# api_authentication
@timeit
def get_api_key_expiration(customer_name, customer_type, user_apikey):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'operation': 'get_apikey_expiration',
                                    'user_apikey': user_apikey},
                           message_body="")
    value = value.decode('utf-8')
    return value


# api_inscription
@timeit
def customer_inscription(customer_email, customer_type, customer_name, body, type_user):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'operation': 'client_inscription',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'type': type_user,
                                    'user_apikey': ""},
                           message_body=body)
    value = value.decode('utf-8')
    return value


# Similarities
def process_customer_stream_from_json(user_apikey, customer_name, customer_type, project_name, body):
    my_queue_json = RabbitMQ(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                             mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD,
                             mqueue_name=MESSAGE_QUEUE_INPUT_NAME,
                             headers={'user_apikey': user_apikey,
                                      'operation': 'process_customer_stream_from_json',
                                      'customer_name': customer_name,
                                      'customer_type': customer_type,
                                      'project_name': project_name
                                      })
    my_queue_json.publish(body)


# Cms process
def process_customer_stream_cms(user_apikey, customer_name, customer_type, project_name, body):
    my_queue_json = RabbitMQ(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                             mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD,
                             mqueue_name=MESSAGE_QUEUE_INPUT_NAME,
                             headers={'user_apikey': user_apikey,
                                      'operation': 'process_customer_stream_cms',
                                      'customer_name': customer_name,
                                      'customer_type': customer_type,
                                      'project_name': project_name
                                      })
    my_queue_json.publish(body)




def shopify_training(user_apikey, customer_name, customer_type, project_name, body):
    my_queue_json = RabbitMQ(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                             mqueue_port=MESSAGE_QUEUE_PORT,
                             mqueue_user=MESSAGE_QUEUE_USER,
                             mqueue_password=MESSAGE_QUEUE_PASSWORD,
                             mqueue_name=MESSAGE_QUEUE_INPUT_NAME,
                             headers={'user_apikey': user_apikey,
                                      'operation': 'shopify_training',
                                      'customer_name': customer_name,
                                      'customer_type': customer_type,
                                      'project_name': project_name,
                                      'url_shop': body
                                      })
    my_queue_json.publish(body)


# Trainings and Classifications
def text_training(user_apikey, customer_name, customer_type, customer_universe, body, project_name):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'user_apikey': user_apikey,
                                    'operation': 'text_training',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'project_name': project_name,
                                    'customer_universe': customer_universe},
                           message_body=body)
    value = value.decode('utf-8')
    return value


def equilibrate_customer_training_samples(user_apikey, customer_name, customer_type, customer_universe, body):
    my_queue_json = RabbitMQ(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                             mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD,
                             mqueue_name=MESSAGE_QUEUE_INPUT_NAME,
                             headers={'user_apikey': user_apikey,
                                      'operation': 'equilibrate_customer_training_samples',
                                      'customer_name': customer_name,
                                      'customer_type': customer_type,
                                      'customer_universe': customer_universe})
    my_queue_json.publish(body)


def image_training(user_apikey, customer_name, customer_type, customer_universe):
    my_queue_json = RabbitMQ(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                             mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD,
                             mqueue_name=MESSAGE_QUEUE_INPUT_NAME,
                             headers={'user_apikey': user_apikey,
                                      'operation': 'image_training',
                                      'customer_name': customer_name,
                                      'customer_type': customer_type,
                                      'customer_universe': customer_universe})
    my_queue_json.publish('')


#
# def predict_customer(user_apikey, customer_name, customer_type, customer_universe, body):
#     my_queue_json = mqueue.RabbitMQ(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
#                              mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD,
#                              mqueue_name=MESSAGE_QUEUE_INPUT_NAME,
#                              headers={'user_apikey': user_apikey,
#                                       'operation': 'predict_customer',
#                                       'customer_name': customer_name,
#                                       'customer_type': customer_type,
#                                       'customer_universe': customer_universe})
#     my_queue_json.publish(body)


def predict_customer(user_apikey, customer_name, customer_type, customer_universe, body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'user_apikey': user_apikey,
                                    'operation': 'predict_customer',
                                    'customer_name': customer_name,
                                    'customer_universe': customer_universe,
                                    'customer_type': customer_type},
                           message_body=body)
    return value.decode('utf-8')

@timeit
def predict_image(user_apikey, customer_name, customer_type, body, project_name):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'user_apikey': user_apikey,
                                    'operation': 'predict_image',
                                    'customer_name': customer_name,
                                    'project_name': project_name,
                                    'customer_type': customer_type},
                           message_body=body)
    return value


def detect_missing_images(user_apikey, customer_name, customer_type, project, body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'user_apikey': user_apikey,
                                    'operation': 'get_missed_images',
                                    'customer_name': customer_name,
                                    'project': project,
                                    'customer_type': customer_type},
                           message_body=str(body))
    return value

@timeit
def get_historic(user_apikey, customer_name, customer_type, body, project_name, month_num):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'user_apikey': user_apikey,
                                    'operation': 'get_historic',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'project_name': project_name,
                                    'month_num': month_num},
                           message_body=body)

    return value


def process_customer_training_classification(user_apikey, customer_name, customer_type, customer_universe, body, project_name):
    my_queue_json = RabbitMQ(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                             mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD,
                             mqueue_name=MESSAGE_QUEUE_INPUT_NAME,
                             headers={'user_apikey': user_apikey,
                                    'operation': 'process_customer_training_classification',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'project_name': project_name,
                                    'customer_universe': customer_universe})
    my_queue_json.publish(body)


def get_historic_client(customer_name, customer_type):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_historic_client',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type},
                           message_body='')

    return value

@timeit
def get_list_all_clients_with_projects(body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={
        'operation': 'get_list_all_clients_with_projects'
    },
        message_body=body)

    return value


def get_number_post_per_clients(body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={
        'operation': 'get_number_post_per_clients'
    },
        message_body=body)

    return value


def update_user_apikey(customer_name, customer_type, body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'update_user_apikey',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type
                                    },
                           message_body=body)
    value = value.decode('utf-8')
    return value


# detection_error
def detection_error_training(user_apikey, customer_name, customer_type, customer_universe, body):
    my_queue_json = RabbitMQ(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                             mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD,
                             mqueue_name=MESSAGE_QUEUE_INPUT_NAME,
                             headers={'user_apikey': user_apikey,
                                      'operation': 'detection_error_training',
                                      'customer_name': customer_name,
                                      'customer_type': customer_type,
                                      'customer_universe': customer_universe})
    my_queue_json.publish(body)





@timeit
def get_specified_project_status(user_apikey, customer_name, customer_type, project_name, body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_specified_project_status',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'project_name': project_name,
                                    'user_apikey': user_apikey
                                    },
                           message_body=body)
    value = value.decode('utf-8')
    return value


# new functions
def get_client_payment_status(customer_name, customer_type):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_client_payment_status',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type
                                    },
                           message_body="")

    value = value.decode('utf-8')
    return value

@timeit
def get_payment_status_for_client(user_apikey, customer_name, customer_type):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_payment_status_for_client',
                                    'user_apikey': user_apikey,
                                    'customer_name': customer_name,
                                    'customer_type': customer_type
                                    },
                           message_body="")

    value = value.decode('utf-8')
    return value


@timeit
def get_client_statistics(user_apikey, customer_name, customer_type):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_client_statistics',
                                    'customer_name': customer_name,
                                    'user_apikey': user_apikey,
                                    'customer_type': customer_type
                                    },
                           message_body="")
    value = value.decode('utf-8')
    return value


def get_statistics_for_admin(customer_name, customer_type):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_statistics_for_admin',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type},
                           message_body='')
    value = value.decode('utf-8')
    return value


def all_historic_users_management(body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'all_historic_users_management'
                                    },
                           message_body=body)
    value = value.decode('utf-8')
    return value


@timeit
def get_details_trainings_for_client(user_apikey, customer_name, customer_type, project_name):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_details_trainings_for_client',
                                    'customer_name': customer_name,
                                    'user_apikey': user_apikey,
                                    'customer_type': customer_type,
                                    'project_name': project_name
                                    },
                           message_body="")

    value = value.decode('utf-8')
    return value


def get_details_trainings_for_admin(customer_name, customer_type, project_name):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_details_trainings_for_admin',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'project_name': project_name},
                           message_body='')
    value = value.decode('utf-8')
    return value


def all_historic_users_management_customer(body):
  rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                               mqueue_port=MESSAGE_QUEUE_PORT,
                               mqueue_user=MESSAGE_QUEUE_USER,
                               mqueue_password=MESSAGE_QUEUE_PASSWORD)
  value = rpc_queue.call(headers={'operation': 'all_historic_users_management_customer'
                                  },
                         message_body=body)
  value=value.decode('utf-8')
  return value


# api_can_create_users
def can_create_users(customer_email, body, type_user, type_new_user, email, password,entreprise, nom, prenom,num_tel, domaine):
  rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                               mqueue_port=MESSAGE_QUEUE_PORT,
                               mqueue_user=MESSAGE_QUEUE_USER,
                               mqueue_password=MESSAGE_QUEUE_PASSWORD)
  value = rpc_queue.call(headers={'customer_email': customer_email,
                                  'type_user' : type_user,
                                  'type_new_user': type_new_user,
                                  'email': email,
                                  'password' : password,
                                  'entreprise' : entreprise,
                                  'nom': nom,
                                  'prenom': prenom,
                                  'num_tel': num_tel,
                                  'domaine': domaine,
                                  'operation': 'can_create_users',
                                  'customer_name': "",
                                  'customer_type': "",
                                  'user_apikey': ""},
                         message_body=body)
  value=value.decode('utf-8')
  return value


def can_delete_users(customer_email, body, type_user, email):
  rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                               mqueue_port=MESSAGE_QUEUE_PORT,
                               mqueue_user=MESSAGE_QUEUE_USER,
                               mqueue_password=MESSAGE_QUEUE_PASSWORD)
  value = rpc_queue.call(headers={'customer_email': customer_email,
                                  'type_user' : type_user,
                                  'email': email,
                                  'operation': 'can_delete_users',
                                  'customer_name': "",
                                  'customer_type': "",
                                  'user_apikey': ""},
                         message_body=body)
  value=value.decode('utf-8')
  return value


def can_edit_users(customer_email, body, type_user, email, password, entreprise, nom, prenom, num_tel, domaine):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                                 mqueue_port=MESSAGE_QUEUE_PORT,
                                 mqueue_user=MESSAGE_QUEUE_USER,
                                 mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'type_user': type_user,
                                    'email': email,
                                    'password': password,
                                    'entreprise': entreprise,
                                    'nom': nom,
                                    'prenom': prenom,
                                    'num_tel': num_tel,
                                    'domaine': domaine,
                                    'operation': 'can_edit_users',
                                    'customer_name': "",
                                    'customer_type': "",
                                    'user_apikey': ""},
                           message_body=body)
    value = value.decode('utf-8')
    return value


def can_view_users(customer_email, body, type_user):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                                 mqueue_port=MESSAGE_QUEUE_PORT,
                                 mqueue_user=MESSAGE_QUEUE_USER,
                                 mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'type_user': type_user,
                                    'operation': 'can_view_users',
                                    'customer_name': "",
                                    'customer_type': "",
                                    'user_apikey': ""},
                           message_body=body)
    value = value.decode('utf-8')
    return value


def can_view_customers(customer_email, body, type_user):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                                 mqueue_port=MESSAGE_QUEUE_PORT,
                                 mqueue_user=MESSAGE_QUEUE_USER,
                                 mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'type_user': type_user,
                                    'operation': 'can_view_customers',
                                    'customer_name': "",
                                    'customer_type': "",
                                    'user_apikey': ""},
                           message_body=body)
    value = value.decode('utf-8')
    return value


def can_update_apikey(customer_email, type_user,email, body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                                 mqueue_port=MESSAGE_QUEUE_PORT,
                                 mqueue_user=MESSAGE_QUEUE_USER,
                                 mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'type_user': type_user,
                                    'operation': 'can_update_apikey',
                                    'email': email},
                           message_body=body)
    value = value.decode('utf-8')
    return value


def can_delete_project(customer_email, type_user,customer_name, customer_type, project_name,body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                                 mqueue_port=MESSAGE_QUEUE_PORT,
                                 mqueue_user=MESSAGE_QUEUE_USER,
                                 mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'type_user': type_user,
                                    'operation': 'can_delete_project',
                                    'project_name': project_name,
                                    'customer_name': customer_name,
                                    'customer_type': customer_type},
                           message_body=body)
    value = value.decode('utf-8')
    return value


def creation_entreprise_package(customer_email, type_user, plan_name, total,max_images_training,body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                                 mqueue_port=MESSAGE_QUEUE_PORT,
                                 mqueue_user=MESSAGE_QUEUE_USER,
                                 mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'type_user': type_user,
                                    'operation': 'creation_entreprise_package',
                                    'plan_name': plan_name,
                                    'total': total,
                                    'max_images_training': max_images_training},
                           message_body=body)
    value = value.decode('utf-8')
    return value


def get_all_plans_payement(customer_email, type_user,body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                                 mqueue_port=MESSAGE_QUEUE_PORT,
                                 mqueue_user=MESSAGE_QUEUE_USER,
                                 mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'type_user': type_user,
                                    'operation': 'get_all_plans_payement'},
                           message_body=body)
    value = value.decode('utf-8')
    return value


def all_status_projects(customer_name, customer_type, body):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'all_status_projects',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type
                                    },
                           message_body=body)
    value = value.decode('utf-8')
    return value

@timeit
def all_status_project(user_apikey, customer_name, customer_type):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'all_status_project',
                                    'customer_name': customer_name,
                                    'user_apikey': user_apikey,
                                    'customer_type': customer_type},
                           message_body='')

    return value.decode("utf-8")


@timeit
def customer_info(data):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_customer_info',
                                    'data': data},
                           message_body='')

    rpc_queue.close()
    return value.decode("utf-8")


@timeit
def save_client_reviews(user_apikey, customer_name, customer_type, body, project_name, review,url_image):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'user_apikey': user_apikey,
                                    'operation': 'save_client_reviews',
                                    'customer_name': customer_name,
                                    'project_name': project_name,
                                    'customer_type': customer_type,
                                    'review' : review,
                                    'url_image' : url_image},
                           message_body=body)
    return value.decode('utf-8')


@timeit
def customer_registration(customer_email, customer_type, customer_name, customer_password, first_name, last_name,
                          phone_number, job,
                          number_of_staff, plan, cms_if_exist, url_cms,token_cms):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'operation': 'customer_registration',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'customer_password': customer_password,
                                    'first_name': first_name,
                                    'last_name': last_name,
                                    'phone_number': phone_number,
                                    'job': job,
                                    'number_of_staff': number_of_staff,
                                    'plan': plan,
                                    'cms_if_exist': cms_if_exist,
                                    'url_cms': url_cms,
                                    'token_cms': token_cms
                                    },
                           message_body="")

    value = value.decode('utf-8')
    return value


def update_profile(customer_email, customer_name, first_name, last_name,
                   phone_number, job, new_email):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'operation': 'update_profile',
                                    'customer_name': customer_name,
                                    'first_name': first_name,
                                    'last_name': last_name,
                                    'phone_number': phone_number,
                                    'job': job,
                                    'new_email': new_email},
                           message_body="")

    value = value.decode('utf-8')
    return value


def change_password(customer_email, customer_password, new_password, new_password_verif):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_password': customer_password,
                                    'operation': 'change_password',
                                    'new_password': new_password,
                                    'new_password_verif': new_password_verif,

                                    'customer_email': customer_email
                                    },
                           message_body="")

    value = value.decode('utf-8')
    return value


def forget_password(customer_email):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'forget_password',
                                    'customer_email': customer_email
                                    },
                           message_body="")

    value = value.decode('utf-8')
    return value


def contact(first_name, customer_email, subject_of_email, message_email):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                          mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER,
                          mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'contact',
                                    'first_name': first_name,
                                    'customer_email': customer_email,
                                    'subject_of_email': subject_of_email,
                                    'message_email': message_email
                                    },
                           message_body="")

    value = value.decode('utf-8')
    return value


@timeit
def get_connected_customer_info(customer_email):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_connected_customer_info',
                                    'customer_email': customer_email},
                           message_body='')

    return value.decode("utf-8")

@timeit
def get_connected_customer_cms_info(customer_name, customer_type, cms):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS, mqueue_port=MESSAGE_QUEUE_PORT,
                          mqueue_user=MESSAGE_QUEUE_USER, mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'operation': 'get_connected_customer_cms_info',
                                    'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'cms': cms},
                           message_body='')

    return value.decode("utf-8")


def delete_user_data(customer_name, customer_type):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                                 mqueue_port=MESSAGE_QUEUE_PORT,
                                 mqueue_user=MESSAGE_QUEUE_USER,
                                 mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_name': customer_name,
                                    'customer_type': customer_type,
                                    'operation': 'delete_user_data'},
                           message_body="")
    value = value.decode('utf-8')
    return value


def delete_user_data_from_email(customer_email):
    rpc_queue = RpcClient(mqueue_address=MESSAGE_QUEUE_ADDRESS,
                                 mqueue_port=MESSAGE_QUEUE_PORT,
                                 mqueue_user=MESSAGE_QUEUE_USER,
                                 mqueue_password=MESSAGE_QUEUE_PASSWORD)
    value = rpc_queue.call(headers={'customer_email': customer_email,
                                    'operation': 'delete_user_data_from_email'},
                           message_body="")
    value = value.decode('utf-8')
    return value