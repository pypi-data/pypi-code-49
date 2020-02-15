from .project import Project
from .model_instance import ModelInstance


class Model():
    '''

    '''

    def __init__(self, client, name=None, modelId=None, modelConfig=None, createdAt=None, modelInstance={}, project={}):
        self.client = client
        self.id = modelId
        self.name = name
        self.model_id = modelId
        self.model_config = modelConfig
        self.created_at = createdAt
        self.model_instance = ModelInstance(
            client, **modelInstance) if modelInstance else None
        self.project = Project(client, **project) if project else None

    def __repr__(self):
        return f"Model(name={repr(self.name)}, model_id={repr(self.model_id)}, model_config={repr(self.model_config)}, created_at={repr(self.created_at)}, model_instance={repr(self.model_instance)}, project={repr(self.project)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'name': self.name, 'model_id': self.model_id, 'model_config': self.model_config, 'created_at': self.created_at, 'model_instance': self.model_instance.to_dict() if self.model_instance else None, 'project': self.project.to_dict() if self.project else None}

    def refresh(self):
        self = self.describe()
        return self

    def create_deployment(self, name, description=None, deployment_config=None):
        return self.client.create_deployment(self.model_id, name, description, deployment_config)

    def cancel_training(self):
        return self.client.cancel_model_training(self.model_id)

    def delete(self):
        return self.client.delete_model(self.model_id)

    def describe(self):
        return self.client.describe_model(self.model_id)

    def get_metrics(self):
        return self.client.get_model_metrics(self.model_id)

    def list_instances(self):
        return self.client.list_model_instances(self.model_id)

    def wait_for_training(self, timeout=None):
        return self.client._poll(self, {'PENDING', 'TRAINING'}, delay=30, timeout=timeout)

    def wait_for_evaluation(self, timeout=None):
        return self.client._poll(self, {'PENDING', 'TRAINING', 'EVALUATING'}, delay=30, timeout=timeout)

    def get_status(self):
        return self.describe().model_instance.lifecycle
