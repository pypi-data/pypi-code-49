from .dataset_upload import DatasetUpload


class DatasetInstance():
    '''

    '''

    def __init__(self, client, datasetInstanceId=None, lifecycle=None, lifecycleMsg=None, datasetId=None, tag=None, size=None, inspectingStartedAt=None, inspectingCompletedAt=None, createdAt=None, datasetUpload={}):
        self.client = client
        self.id = datasetInstanceId
        self.dataset_instance_id = datasetInstanceId
        self.lifecycle = lifecycle
        self.lifecycle_msg = lifecycleMsg
        self.dataset_id = datasetId
        self.tag = tag
        self.size = size
        self.inspecting_started_at = inspectingStartedAt
        self.inspecting_completed_at = inspectingCompletedAt
        self.created_at = createdAt
        self.dataset_upload = DatasetUpload(
            client, **datasetUpload) if datasetUpload else None

    def __repr__(self):
        return f"DatasetInstance(dataset_instance_id={repr(self.dataset_instance_id)}, lifecycle={repr(self.lifecycle)}, lifecycle_msg={repr(self.lifecycle_msg)}, dataset_id={repr(self.dataset_id)}, tag={repr(self.tag)}, size={repr(self.size)}, inspecting_started_at={repr(self.inspecting_started_at)}, inspecting_completed_at={repr(self.inspecting_completed_at)}, created_at={repr(self.created_at)}, dataset_upload={repr(self.dataset_upload)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'dataset_instance_id': self.dataset_instance_id, 'lifecycle': self.lifecycle, 'lifecycle_msg': self.lifecycle_msg, 'dataset_id': self.dataset_id, 'tag': self.tag, 'size': self.size, 'inspecting_started_at': self.inspecting_started_at, 'inspecting_completed_at': self.inspecting_completed_at, 'created_at': self.created_at, 'dataset_upload': self.dataset_upload.to_dict() if self.dataset_upload else None}

    def refresh(self):
        self = self.describe()
        return self
