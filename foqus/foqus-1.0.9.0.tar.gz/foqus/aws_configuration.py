from foqus.configuration import *
from foqus.database import logger, PostgreSQL

import botocore
import boto3
import json
import pickle
import pyarrow.parquet as pq
import s3fs
import urllib

# initialising database
db = PostgreSQL()


def upload_file_into_s3(file, chemin, ext=None):
    '''

    :param file: file to upload to S3
    :param chemin: the location in which we will upload the file in S3
    :param ext: the extension of the file (if you wish to change when uploading)
    :return: Nothing to return
    '''

    s3 = boto3.resource('s3', aws_access_key_id=AWS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_KEY)
    fichier = file.split('/')[-1]
    if ext is None:
        file_to_upload = chemin + fichier
    else:
        file_to_upload = chemin + fichier + "." + ext
    try:
        logger.info('Uploading file into %s' %file_to_upload)
        data = open(file, 'rb')
        s3.Bucket('trynfit-bucket').put_object(Key=file_to_upload, Body=data)
    except Exception as e:
        logger.error('Error in uploading file %s'%e)


def delete_from_s3(file):
    '''

    :param file: file to delete from s3
    :return: 0 if object deleted else -1

    '''

    s3 = boto3.resource('s3', aws_access_key_id=AWS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_KEY)
    try:
        s3.Object('trynfit-bucket', file).delete()
        return 0
    except Exception as e:
        logger.error('Error in deleting file %s error is %s' %(file, e))
        return -1


def delete_folder(prefix_to_delete):
    '''

    :param prefix_to_delete: prefix of the directory to delete
    :return: Nothing to return
    '''

    s3 = boto3.resource('s3', aws_access_key_id=AWS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_KEY)
    delete_keys = {}
    try:
        objects_to_delete = s3.meta.client.list_objects(Bucket="trynfit-bucket", Prefix=prefix_to_delete)
        delete_keys['Objects'] = [{'Key': k} for k in [obj['Key'] for obj in objects_to_delete.get('Contents', [])]]

        s3.meta.client.delete_objects(Bucket="trynfit-bucket", Delete=delete_keys)
        logger.info("Directory deleted successfully %s" % prefix_to_delete)
    except Exception as e:
        logger.error("Error deleting directory %s error is %s" % (prefix_to_delete, e))


def list_object_folder(prefix):
    '''

    :param prefix: the prefix of the diretcory to list the file into
    :return: list of the objects in the directory
    '''
    s3 = boto3.resource('s3', aws_access_key_id=AWS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_KEY)
    files = []
    try:
        paginator = s3.meta.client.get_paginator('list_objects')
        pages = paginator.paginate(Bucket=AWS_STORAGE_BUCKET_NAME, Prefix=prefix)
        for page in pages:
            for key in page['Contents']:
                files.append(key['Key'])
        return files
    except Exception as e:
        logger.error("Errorororor %s" % e)
        return []


def load_file_from_url(url):
    '''

    :param url: url of the file to load
    :return: return vector if file exist else None
    '''
    s3 = s3fs.S3FileSystem(key=AWS_KEY_ID, secret=AWS_SECRET_KEY)
    try:
        vector = pq.ParquetDataset('s3://%s'
                                   % (AWS_STORAGE_BUCKET_NAME + '/' + url),
                                   filesystem=s3).read_pandas().to_pandas()
        return vector
    except Exception as e:
        logger.warning('%s file not loaded %s ' % (url, e))
        return None


def load_file_json_s3(prefix):
    '''
    :param prefix: the prefix of the json file to load
    :return: the json content if file exists else None
    '''
    s3 = boto3.resource('s3', aws_access_key_id=AWS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_KEY)
    try:
        content_object = s3.Object('trynfit-bucket', prefix)
        file_content = content_object.get()['Body'].read().decode('utf-8')

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            logger.error("File doen't exist")
        file_content = None
    json_content = json.loads(file_content)
    return json_content


def load_pickle_file(prefix):
    '''
    :param prefix: prfix of the pickle file to load
    :return: the pickle file if exists else None
    '''
    try:
        base_url = AWS_S3_CUSTOM_DOMAIN + AWS_STORAGE_BUCKET_NAME + '/'
        file = urllib.request.urlopen(base_url + prefix)
        pickle_data = pickle.load(file)
        return pickle_data
    except Exception as e:
        logger.error("Error loading pickle file %s" % e)
        return None


def list_subdirectories(prefix):
    '''
    :param prefix: prfix of the directory to get all subcategories under it
    :return: list with all subcategories
    '''
    s3 = boto3.resource('s3', aws_access_key_id=AWS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_KEY)
    subdirectories = []
    caractere_to_split = prefix.split('/')[-1]
    if caractere_to_split == "":
        caractere_to_split = prefix.split('/')[-2]
    paginator = s3.meta.client.get_paginator('list_objects')
    pages = paginator.paginate(Bucket=AWS_STORAGE_BUCKET_NAME)
    for page in pages:
        for key in page['Contents']:
            if caractere_to_split in key['Key'] and prefix in key['Key']:
                project = key['Key'].split('/')[-2]
                if project not in subdirectories:
                    subdirectories.append(project)
    return subdirectories


def move_directory(prefix, directory):
    s3 = boto3.resource('s3', aws_access_key_id=AWS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_KEY)
    try:
        files = list_object_folder(prefix)
        for file in files:
            prefix_element = file['Key']
            copy_source = {'Bucket': 'trynfit-bucket', 'Key': prefix_element}
            s3.meta.client.copy(copy_source, 'trynfit-bucket', prefix_element.replace('workspace', directory))
        delete_folder(prefix)
        return True
    except Exception as e:
        logger.error("Errorororor %s" % e)


def load_vectors_from_s3(vectors, users):
    '''
    :param vectors: dict with vectors names and values initialised to empty dict
    :param users: list of all users in database
    :return: json with all vectors with values
    '''
    for user in users:
        vector_path = 'BACKUP/workspace/vectors/' + str(user[8]) + '/' + str(user[1]) + '/'
        try:
            vectors_client = list_object_folder(vector_path)
            for vector in vectors_client:
                try:
                    vector_name = vector['Key'].split('.parquet')[0].split('/')[-1]

                    if vector_name:
                        project_name = vector_name.split('_' + user[1])[0]
                        status = db.get_status_project(STATUS_PROJECT_TABLE, user[1], user[8], 'similars', project_name)
                        if status and status[0] == 2:
                            if vector_name not in vectors.keys():
                                logger.info('Vector to load  =====> %s' % (vector['Key'].split('.parquet')[0] + '.parquet'))
                                vector_data = ''
                                if vector_data is not None:
                                    vectors[vector_name] = vector_data
                                    logger.info('Vector %s  loaded successfully for client %s '
                                                % (vector_name, str(user[1])))
                                else:
                                    logger.info(
                                        'Vector %s not loaded for client %s vector is None'
                                        % (vector['Key'].split('.parquet')[0].split('/')[-1], str(user[1])))
                        else:
                            logger.info('Status Project not 2 %s %s' %(project_name, status))
                            continue
                except Exception as e:
                    logger.warning("Vector not loaded %s error %s" %(vector, e))
        except Exception as e:
            logger.warning("Can't get the parquet file for client %s with domaine %s error %s"
                           % (str(user[1]), str(user[8]), e))
    logger.info("Vectors keys : %s" % vectors.keys())
    return vectors

