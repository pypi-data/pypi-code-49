from multiprocessing import Pool
import io


class DatasetUpload():
    '''

    '''

    def __init__(self, client, datasetUploadId=None, lifecycle=None, datasetId=None, datasetInstanceId=None, uploadType=None, parts=None, createdAt=None):
        self.client = client
        self.id = datasetUploadId
        self.dataset_upload_id = datasetUploadId
        self.lifecycle = lifecycle
        self.dataset_id = datasetId
        self.dataset_instance_id = datasetInstanceId
        self.upload_type = uploadType
        self.parts = parts
        self.created_at = createdAt

    def __repr__(self):
        return f"DatasetUpload(dataset_upload_id={repr(self.dataset_upload_id)}, lifecycle={repr(self.lifecycle)}, dataset_id={repr(self.dataset_id)}, dataset_instance_id={repr(self.dataset_instance_id)}, upload_type={repr(self.upload_type)}, parts={repr(self.parts)}, created_at={repr(self.created_at)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'dataset_upload_id': self.dataset_upload_id, 'lifecycle': self.lifecycle, 'dataset_id': self.dataset_id, 'dataset_instance_id': self.dataset_instance_id, 'upload_type': self.upload_type, 'parts': self.parts, 'created_at': self.created_at}

    def refresh(self):
        self = self.describe()
        return self

    def complete_upload(self):
        return self.client.complete_upload(self.dataset_upload_id)

    def describe_upload(self):
        return self.client.describe_upload(self.dataset_upload_id)

    def upload_file_part(self, part_number, part_data):
        return self.client.upload_file_part(self.dataset_upload_id, part_number, part_data)

    def upload_file(self, file, threads=10, chunksize=1024*1024*10):
        with Pool(processes=threads) as pool:
            pool.starmap(self.upload_file_part,
                         self._yield_upload_part(file, chunksize))
        return self.complete_upload()

    def _yield_upload_part(self, file, chunksize):
        binary_file = isinstance(file, (io.RawIOBase, io.BufferedIOBase))
        part_number = 0
        while True:
            chunk = io.BytesIO() if binary_file else io.StringIO()
            length = chunk.write(file.read(chunksize))
            if length == 0:
                break
            chunk.seek(0, 0)
            part_number += 1
            yield part_number if length else -1, chunk
