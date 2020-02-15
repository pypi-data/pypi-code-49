from .dataset_instance import DatasetInstance


class Dataset():
    '''

    '''

    def __init__(self, client, datasetId=None, name=None, sourceType=None, refreshPolicy=None, createdAt=None, datasetInstance={}):
        self.client = client
        self.id = datasetId
        self.dataset_id = datasetId
        self.name = name
        self.source_type = sourceType
        self.refresh_policy = refreshPolicy
        self.created_at = createdAt
        self.dataset_instance = DatasetInstance(
            client, **datasetInstance) if datasetInstance else None

    def __repr__(self):
        return f"Dataset(dataset_id={repr(self.dataset_id)}, name={repr(self.name)}, source_type={repr(self.source_type)}, refresh_policy={repr(self.refresh_policy)}, created_at={repr(self.created_at)}, dataset_instance={repr(self.dataset_instance)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'dataset_id': self.dataset_id, 'name': self.name, 'source_type': self.source_type, 'refresh_policy': self.refresh_policy, 'created_at': self.created_at, 'dataset_instance': self.dataset_instance.to_dict() if self.dataset_instance else None}

    def refresh(self):
        self = self.describe()
        return self

    def attach_to_project(self, project_id, project_dataset_type):
        return self.client.attach_dataset_to_project(self.dataset_id, project_id, project_dataset_type)

    def delete(self):
        return self.client.delete_dataset(self.dataset_id)

    def describe(self):
        return self.client.describe_dataset(self.dataset_id)

    def read_instance_from_cloud(self):
        return self.client.read_dataset_instance_from_cloud(self.dataset_id)

    def list_instances(self):
        return self.client.list_dataset_instances(self.dataset_id)

    def create_instance_upload(self):
        return self.client.create_dataset_instance_upload(self.dataset_id)

    def remove_from_project(self, project_id):
        return self.client.remove_dataset_from_project(self.dataset_id, project_id)

    def wait_for_import(self, timeout=900):
        return self.client._poll(self, {'PENDING', 'IMPORTING'}, timeout=timeout)

    def wait_for_inspection(self, timeout=900):
        return self.client._poll(self, {'PENDING', 'IMPORTING', 'INSPECTING'}, timeout=timeout)

    def get_status(self):
        return self.describe().dataset_instance.lifecycle
