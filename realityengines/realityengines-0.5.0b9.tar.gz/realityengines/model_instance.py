

class ModelInstance():
    '''

    '''

    def __init__(self, client, modelInstanceId=None, lifecycle=None, lifecycleMsg=None, modelId=None, tag=None, trainingStartedAt=None, trainingCompletedAt=None, evaluatingStartedAt=None, evaluatingCompletedAt=None, createdAt=None):
        self.client = client
        self.id = modelInstanceId
        self.model_instance_id = modelInstanceId
        self.lifecycle = lifecycle
        self.lifecycle_msg = lifecycleMsg
        self.model_id = modelId
        self.tag = tag
        self.training_started_at = trainingStartedAt
        self.training_completed_at = trainingCompletedAt
        self.evaluating_started_at = evaluatingStartedAt
        self.evaluating_completed_at = evaluatingCompletedAt
        self.created_at = createdAt

    def __repr__(self):
        return f"ModelInstance(model_instance_id={repr(self.model_instance_id)}, lifecycle={repr(self.lifecycle)}, lifecycle_msg={repr(self.lifecycle_msg)}, model_id={repr(self.model_id)}, tag={repr(self.tag)}, training_started_at={repr(self.training_started_at)}, training_completed_at={repr(self.training_completed_at)}, evaluating_started_at={repr(self.evaluating_started_at)}, evaluating_completed_at={repr(self.evaluating_completed_at)}, created_at={repr(self.created_at)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'model_instance_id': self.model_instance_id, 'lifecycle': self.lifecycle, 'lifecycle_msg': self.lifecycle_msg, 'model_id': self.model_id, 'tag': self.tag, 'training_started_at': self.training_started_at, 'training_completed_at': self.training_completed_at, 'evaluating_started_at': self.evaluating_started_at, 'evaluating_completed_at': self.evaluating_completed_at, 'created_at': self.created_at}

    def refresh(self):
        self = self.describe()
        return self
