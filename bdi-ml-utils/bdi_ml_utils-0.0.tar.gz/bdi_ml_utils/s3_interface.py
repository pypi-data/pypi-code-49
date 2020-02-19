from .metrics import Metric
from time import time
import os
import boto3


class S3Interface:
    def __init__(self, logger, metric_builder, s3_bucket):
        self.logger = logger
        self.metric_builder = metric_builder
        self.s3_bucket = s3_bucket
        self.s3_client = boto3.client('s3')

    def download_files(self, s3_key, local_key, metric_key=''):
        """
        params:
        - prefix: pattern to match in s3
        - local: local path to folder in which to place files
        - bucket: s3 bucket with target contents
        - client: initialized s3 client object
        """
        keys = []
        next_token = ''
        base_kwargs = {
            'Bucket': self.s3_bucket,
            'Prefix': s3_key,
        }

        self.logger.info('Start downloading files from: {bucket}/{key}'.format(bucket=self.s3_bucket, key=s3_key))
        start_time = time()

        while next_token is not None:
            kwargs = base_kwargs.copy()
            if next_token != '':
                kwargs.update({'ContinuationToken': next_token})
            results = self.s3_client.list_objects_v2(**kwargs)
            contents = results.get('Contents')
            for i in contents:
                if i.get('Size') > 0:
                    k = i.get('Key')
                    keys.append(k)
            next_token = results.get('NextContinuationToken')
        for k in keys:
            local_file_path = os.path.join(local_key, k.split('/')[-1])
            if not os.path.exists(os.path.dirname(local_file_path)):
                os.makedirs(os.path.dirname(local_file_path))
            self.logger.info('downloading s3://{}/{} to {}'.format(self.s3_bucket, k, local_file_path))
            self.s3_client.download_file(self.s3_bucket, k, local_file_path)

        total_time = (time() - start_time) / 60 / 60

        if metric_key:
            metrics = Metric(metric_key, total_time)
            self.metric_builder.append(metrics)

        self.logger.info('Finished downloading, took {}'.format(total_time))

    def upload_files(self, files, s3_key):
        self.logger.info('Start uploading files to s3')
        for file in files:
            full_key = os.path.join(s3_key, file)
            self.logger.debug('uploading {} to s3://{}/{}'.format(file, self.s3_bucket, full_key))
            self.s3_client.upload_file(file, self.s3_bucket, full_key)
        self.logger.info('Finished uploading')

    def upload_object(self, s3_key, obj):
        self.logger.info('Start uploading object to: s3://{bucket}/{key}'.format(bucket=self.s3_bucket, key=s3_key))
        self.s3_client.put_object(Bucket=self.s3_bucket, Key=s3_key, Body=obj)
        self.logger.info('Finished uploading')
