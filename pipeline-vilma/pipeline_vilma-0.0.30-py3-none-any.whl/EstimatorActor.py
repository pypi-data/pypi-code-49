class EstimatorActor:
    def update_model(self):
        raise NotImplementedError("Should have implemented this")

    def estimate(self, message):
        raise NotImplementedError("Should have implemented this")
