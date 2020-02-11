import boto3
import pandas as pd
import io

class S3FileHandler:
    """
    Performs read, write, move, copy actions on files in S3 buckets operations on various files
    """

    s3 = boto3.resource('s3')

    def __init__(self, source, key):
        self.source = source
        self.key = key
        self.filetype = self.extract_filetype()

    def set_source(self, source):
        self.source = source

    def set_key(self, key):
        self.key = key

    def extract_filetype(self):
        try:
            filetype = self.key.split('/')[-1].split('.')[-1]
            return filetype
        except:
            return None

    def copy(self, target, new_key=None):
        copy_source = {
            'Bucket': self.source,
            'Key': self.key
        }

        if new_key == None:
            new_key = self.key

        self.s3.meta.client.copy(CopySource=copy_source, Bucket=target, Key=new_key)
        print('Copied file to {}:{}'.format(target, self.key))

    def delete(self):
        self.s3.meta.client.delete_object(Bucket=self.source, Key=self.key)
        print('Deleted file {}:{}'.format(self.source, self.key))

    def move(self, target):
        self.s3.meta.client.copy(self.source, target, self.key)
        self.delete()
        self.source = target
        print('Moved file to {}:{}'.format(target, self.key))

    def get_object(self):
        obj = self.s3.meta.client.get_object(Bucket=self.source, Key=self.key)
        return obj

    def put_object(self, obj, target, key):
        self.s3.meta.client.put_object(Body=obj, Bucket=target, Key=key)
        print('Put file {}:{}'.format(target, key))

    def read_csv(self, sep=',', dtype=None):
        if (self.filetype == 'csv'):
            obj = self.get_object()
            bytes_obj = io.BytesIO(obj['Body'].read())
            self.dataframe = pd.read_csv(bytes_obj, sep=sep, dtype=dtype)
            return self.dataframe
        else:
            raise AttributeError('Not a .csv file')

    def read_excel(self, dtype=None):
        if (self.filetype in ['xlsx', 'xls']):
            obj = self.get_object()
            bytes_obj = io.BytesIO(obj['Body'].read())
            self.dataframe = pd.read_excel(bytes_obj, dtype=dtype)
            return self.dataframe
        else:
            raise AttributeError('Not a .xlsx file')

    def read_json(self, dtype=None):
        if (self.filetype == 'json'):
            obj = self.get_object()
            str_obj = obj['Body'].read().decode('UTF-8')
            self.dataframe = pd.read_json(str_obj, dtype=dtype)
            return self.dataframe
        else:
            raise AttributeError('Not a .json file')

    def read_file(self, dtype=None, sep=','):
        if self.filetype == 'json':
            self.read_json(dtype=dtype)
        elif self.filetype == 'csv':
            self.read_csv(dtype=dtype, sep=sep)
        elif self.filetype in ['xlsx', 'xls']:
            self.read_excel(dtype=dtype)
        else:
            raise AttributeError("Filetype '.{}' not recognized".format(self.filetype))

    def to_dict(self, orient='records'):
        try:
            dict_ = self.dataframe.to_dict(orient=orient, into=NativeDict)
            return dict_
        except:
            raise AttributeError('Dataframe not present')

    def to_json(self, orient='records'):
        try:
            json = self.dataframe.to_json(orient=orient)
            return json
        except:
            raise AttributeError('Dataframe not present')

    def put_csv(self, target, key, sep=','):
        try:
            csv_file = self.to_csv(sep=sep)
            self.put_object(obj=csv_file, target=target, key=key)
        except:
            raise AttributeError('Dataframe not present')

    def put_excel(self, target, key, excel_writer=None):
        try:
            excel_file = self.to_excel(excel_writer=excel_writer)
            self.put_object(obj=excel_file, target=target, key=key)
        except:
            raise AttributeError('Dataframe not present')

    def put_json(self, target, key, orient='records'):
        try:
            json_file = self.to_json(orient=orient)
            self.put_object(obj=json_file, target=target, key=key)
        except:
            raise AttributeError('Dataframe not present')


class NativeDict(dict):
    """
        Helper class to ensure that only native types are in the dicts produced by
        :func:`to_dict() <pandas.DataFrame.to_dict>`

        .. note::

            Needed until `#21256 <https://github.com/pandas-dev/pandas/issues/21256>`_ is resolved.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(((k, self.convert_if_needed(v)) for row in args for k, v in row), **kwargs)

    @staticmethod
    def convert_if_needed(value):
        """
            Converts `value` to native python type.

            .. warning::

                Only :class:`Timestamp <pandas.Timestamp>` and numpy :class:`dtypes <numpy.dtype>` are converted.
        """
        if pd.isnull(value):
            return None
        if isinstance(value, pd.Timestamp):
            return value.to_pydatetime()
        if hasattr(value, 'dtype'):
            mapper = {'i': int, 'u': int, 'f': float}
            _type = mapper.get(value.dtype.kind, lambda x: x)
            return _type(value)
        return value
