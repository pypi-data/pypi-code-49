import oss2
from itertools import islice
import os
import shutil

import sys
import logging

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(asctime)-s %(levelname)-7s %(name)-s.%(funcName)s(): %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S')


class OSSDataHelper():

    def __init__(self, config):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config = config
        self.connect()

    def connect(self):

        oss_access_key_id = 'LTAI4Fj25FynVVxTeDkhb37R'
        oss_secret_access_key = 'VWWImh6A5AsIeWbbajCwOHeJqhTlbt'
        endpoint = 'http://oss-ap-northeast-1.aliyuncs.com'

        auth = oss2.Auth(oss_access_key_id, oss_secret_access_key)

        bucket_name = 'polo-dynamic-pricing'

        self.bucket_name = bucket_name
        self.bucket = oss2.Bucket(auth, endpoint, bucket_name)

    def list_objects(self, prefix=''):
        self.connect()
        keys = []
        for obj in oss2.ObjectIterator(self.bucket, prefix=prefix, delimiter = '/'):
            if not obj.is_prefix():
                keys.append(obj.key)
        self.logger.info('list_objects from %s with prefix %s: %s' % (self.bucket_name, prefix, str(keys)))
        return keys

    def list_folders(self, prefix=''):
        self.connect()
        keys = []
        for obj in oss2.ObjectIterator(self.bucket, prefix=prefix, delimiter = '/'):
            if obj.is_prefix():
                keys.append(obj.key)
        self.logger.info('list_folders from %s with prefix %s: %s' % (self.bucket_name, prefix, str(keys)))
        return keys


    def upload_file(self, oss_object_name, local_file):
        self.connect()
        self.logger.info('put %s to oss (bucket=%s, key=%s)' % (local_file, self.bucket_name, oss_object_name))


        self.bucket.put_object_from_file(oss_object_name, local_file)

    def upload_folder(self, oss_folder, local_dir):

        if oss_folder[-1] != '/':
            self.logger.warn('not a valid ossfolder %s' % oss_folder)
            return
        if local_dir[-1] != '/':
            self.logger.warn('not a valid local_dir %s' % local_dir)
            return

        self.connect()
        self.logger.info('put %s to oss (bucket=%s, key=%s)' % (local_dir, self.bucket_name, oss_folder))

        files = os.listdir(local_dir)
        for file in files:
            local_file = '%s%s' % (local_dir, file)
            oss_object_name = '%s%s' % (oss_folder, file)
            try: 
                self.upload_file(oss_object_name, local_file)
            except Exception as e:
                self.logger.warning("failed to upload file %s to s3://%s/%s" % (local_file, sself.bucket_name, oss_object_name))
                self.logger.warning(e)


    def download_file(self, oss_object_name, local_file):
        self.connect()
        self.logger.info('get %s from oss (bucket=%s, key=%s)' % (local_file, self.bucket_name, oss_object_name))
        try:
            self.mkdir("/".join(local_file.split('/')[:-1]) + "/")
            self.bucket.get_object_to_file(oss_object_name, local_file)
        except:
            raise

    def download_folder(self, oss_folder, local_dir):

        if oss_folder[-1] != '/':
            self.logger.warn('not a valid ossfolder %s' % oss_folder)
            return
        if local_dir[-1] != '/':
            self.logger.warn('not a valid local_dir %s' % local_dir)
            return

        self.connect()
        self.logger.info('get %s from oss (bucket=%s, key=%s)' % (local_dir, self.bucket_name, oss_folder))

        objs = self.list_objects(prefix=oss_folder)
        if len(objs)==0:
            return

        self.mkdir(local_dir)
        for obj in objs:
            local_file = '%s%s'% (local_dir, obj[len(oss_folder):])
            #self.logger.info('local_dir=%s, s3path=%s, s3path[len(s3folder):]=%s' % (local_dir, s3path, s3path[len(s3folder):]))
            self.download_file(obj, local_file)

    def delete_file(self, oss_object_name):
        self.connect()

        try:
            self.bucket.delete_object(oss_object_name)
        except:
            raise

    def delete_folder(self, oss_folder):
        
        if oss_folder[-1] != '/':
            self.logger.warn('not a valid ossfolder %s' % oss_folder)
            return

        self.connect()

        self.logger.info('delete folder in oss (bucket=%s, key=%s)' % (self.bucket_name, oss_folder))

        objs = self.list_objects(prefix=oss_folder)
        if len(objs)==0:
            return

        for obj in objs:
            self.delete_file(obj)


    def mkdir(self, root_dir):
        try :
            if not os.path.exists(root_dir):
                self.logger.info('create local dir: %s' % root_dir)
                os.makedirs(root_dir)
        except e:
            raise

    def rmdir(self, root_dir):
        '''
        Caution!
        It's dangerous like 'rm -rf'
        '''
        if root_dir[0]!='/':
            shutil.rmtree(root_dir)