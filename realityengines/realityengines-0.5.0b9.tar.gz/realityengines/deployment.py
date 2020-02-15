from .model import Model
from .project import Project


class Deployment():
    '''

    '''

    def __init__(self, client, deploymentId=None, name=None, lifecycle=None, lifecycleMsg=None, description=None, deploymentConfig=None, metrics=None, deployedAt=None, createdAt=None, model={}, project={}):
        self.client = client
        self.id = deploymentId
        self.deployment_id = deploymentId
        self.name = name
        self.lifecycle = lifecycle
        self.lifecycle_msg = lifecycleMsg
        self.description = description
        self.deployment_config = deploymentConfig
        self.metrics = metrics
        self.deployed_at = deployedAt
        self.created_at = createdAt
        self.model = Model(client, **model) if model else None
        self.project = Project(client, **project) if project else None

    def __repr__(self):
        return f"Deployment(deployment_id={repr(self.deployment_id)}, name={repr(self.name)}, lifecycle={repr(self.lifecycle)}, lifecycle_msg={repr(self.lifecycle_msg)}, description={repr(self.description)}, deployment_config={repr(self.deployment_config)}, metrics={repr(self.metrics)}, deployed_at={repr(self.deployed_at)}, created_at={repr(self.created_at)}, model={repr(self.model)}, project={repr(self.project)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'deployment_id': self.deployment_id, 'name': self.name, 'lifecycle': self.lifecycle, 'lifecycle_msg': self.lifecycle_msg, 'description': self.description, 'deployment_config': self.deployment_config, 'metrics': self.metrics, 'deployed_at': self.deployed_at, 'created_at': self.created_at, 'model': self.model.to_dict() if self.model else None, 'project': self.project.to_dict() if self.project else None}

    def refresh(self):
        self = self.describe()
        return self

    def delete(self):
        return self.client.delete_deployment(self.deployment_id)

    def describe(self):
        return self.client.describe_deployment(self.deployment_id)

    def update(self, name=None, description=None):
        return self.client.update_deployment(self.deployment_id, name, description)

    def wait_for_deployment(self, timeout=120):
        return self.client._poll(self, {'PENDING', 'DEPLOYING'}, timeout=timeout)

    def get_status(self):
        return self.describe().lifecycle
