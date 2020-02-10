from google.cloud import storage
from google.cloud.storage import Blob
import json
import gcsfs
import pandas as pd


class GCS(object):
    def __init__(self, bucket_name=None, project_id=None, cred_file_path=None):
        self.bucket_name = bucket_name

        if cred_file_path is None:
            self.client = storage.Client()
        else:
            self.client = storage.Client.from_service_account_json(cred_file_path)

        if bucket_name is not None:
            self.bucket = self.client.get_bucket(bucket_name)
        else:
            self.bucket = None

        if cred_file_path is None:
            if project_id is None:
                self.fs = gcsfs.GCSFileSystem()
            else:
                self.fs = gcsfs.GCSFileSystem(project=project_id)
        else:
            if project_id is None:
                self.fs = gcsfs.GCSFileSystem(token=cred_file_path)
            else:
                self.fs = gcsfs.GCSFileSystem(project=project_id, token=cred_file_path)

        if project_id is not None:
            self.client.project = project_id

    def __get_bucket_name(self, bucket_name):
        if bucket_name is None:
            bucket_name = self.bucket_name
        return bucket_name

    def __get_bucket(self, bucket_name):
        if bucket_name is None:
            bucket = self.bucket
        else:
            bucket = self.client.get_bucket(bucket_name)
        return bucket

    def read_json(self, file_name, bucket_name=None):
        bucket = self.__get_bucket(bucket_name)
        blob = bucket.get_blob(file_name)
        content = blob.download_as_string()
        decoded = content.decode("utf-8")
        return json.loads(decoded)

    def read_csv(self, file_name, delimiter=';', header='infer', names=None, bucket_name=None):
        bucket_name = self.__get_bucket_name(bucket_name)
        url = "gs://{}/{}".format(bucket_name, file_name)
        df = pd.read_csv(url, sep=delimiter, header=header, names=names, encoding='utf-8')
        return df

    def read_parquet(self, file_name, bucket_name=None):
        bucket_name = self.__get_bucket_name(bucket_name)
        with self.fs.open(bucket_name + '/' + file_name) as f:
            df = pd.read_parquet(f, engine='pyarrow')
        return df

    def list_all_objects(self, prefix=None, bucket_name=None, return_type='URL'):
        bucket = self.__get_bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=prefix)
        bucket_objects = list(blobs)
        if return_type == 'URL':
            bucket_objects_list = []
            for item in bucket_objects:
                bucket_objects_list.append("gs://{}/{}".format(bucket.name, item.name))
            return bucket_objects_list
        else:
            return bucket_objects

    def df_to_csv(self, df, file_name, delimiter=';', header=True, index=False, bucket_name=None):
        df1 = pd.DataFrame(df)
        bucket_name = self.__get_bucket_name(bucket_name)
        file_name = "gs://{}/{}".format(bucket_name, file_name)
        df1.to_csv(file_name, sep=delimiter, header=header, index=index, encoding='utf-8')

    def df_to_parquet(self, df, file_name, bucket_name=None):
        df1 = pd.DataFrame(df)
        bucket_name = self.__get_bucket_name(bucket_name)
        file_name = "gs://{}/{}".format(bucket_name, file_name)
        df1.to_parquet(file_name, engine='pyarrow')

    def df_to_json_list(self, df, file_name, orient='records', bucket_name=None):
        data = pd.DataFrame(df).to_dict('records')
        bucket = self.__get_bucket(bucket_name)
        blob = Blob(file_name, bucket)
        uploading_data_as_string = json.dumps(data)
        return blob.upload_from_string(uploading_data_as_string, content_type='application/json')

    def dict_to_json(self, df, file_name, orient='records', bucket_name=None):
        bucket = self.__get_bucket(bucket_name)
        blob = Blob(file_name, bucket)
        uploading_data_as_string = json.dumps(df)
        return blob.upload_from_string(uploading_data_as_string, content_type='application/json')

    def upload_file(self, local_file, gcs_file_name, bucket_name=None):
        bucket = self.__get_bucket(bucket_name)
        blob = bucket.blob(gcs_file_name)
        blob.upload_from_filename(local_file)

    def download_file(self, gcs_file_name, local_file_name, bucket_name=None):
        bucket = self.__get_bucket(bucket_name)
        blob = bucket.blob(gcs_file_name)
        blob.download_to_filename(local_file_name)

    ''' 
        def delete_bucket(self, bucket_name): 
            bucket = self.__get_bucket(bucket_name)
            _bucket = bucket.get_bucket(bucket_name)
            _bucket.delete()
            print('Bucket {} deleted'.format(_bucket.name))
    '''
if __name__ == '__main__':

    # With default value: (i. e. if you only work within one bucket)
    gcs_handler = GCS(bucket_name='search-sensors-gdwh-raw-data-k8-v4-445679621038-test-jg')
    # Without defaults:
    #gcs_handler = GCS()

    # Read json from GCS into dictionary:
    #df = gcs_handler.read_json('dev/1000testfiles/10/2.json')
    #print(df)

    # Read parquet file from GCS into pandas dataframe:
    #df = gcs_handler.read_parquet('test/prod_depora_2019_04_12_03_03_7b1f7312-5ccf-11e9-b2d7-0a580ac98e3d-PURCH_PRICE.parquet',  bucket_name='search-sensors-gdwh-raw-data-k8-v4-445679621038-test-jg')
    #print(df)

    # Read csv file from GCS into pandas dataframe:
    #df = gcs_handler.read_csv('test/test.csv')
    #print(df)


    # List all objects of a bucket with and without prefix
    # bucket_objects = gcs_handler.list_all_objects(prefix='test/')
    # print(bucket_objects)

    #df = pd.DataFrame({'col1': [1,2,3], 'col2': ['string1', 'string2', 'string3']})
    # df = {'test': 1}
    #cs_handler.df_to_csv(df=df, file_name='test/test.csv')
    # gcs_handler.df_to_parquet(df=df, file_name='test/test.parquet')
    # gcs_handler.df_to_json_list(df=df, file_name='test/test.json')
    # gcs_handler.dict_to_json(df, file_name="test/dict_test.json")


    # Upload a local file:
    # gcs_handler.upload_file(local_file='../README.md', gcs_file_name='test/README.md')

    # Download file from GCS:
    gcs_handler.download_file('test/test.csv', 'hallo.csv')



