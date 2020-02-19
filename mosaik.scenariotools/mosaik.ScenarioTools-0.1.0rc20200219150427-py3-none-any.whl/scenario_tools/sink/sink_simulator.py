from mosaik_api import Simulator

from mosaik_scenario_tools.scenario_tools.sink.sink_model import SinkModel


class SinkSimulator(Simulator):
    def __init__(self):
        meta = {
            'models': {
                SinkModel.__name__: {
                    'public': True,
                    'params': [],
                    'attrs': [
                        'my_attribute',  # input
                    ],
                },
            },
        }
        super().__init__(meta)

        self._models = []

    def create(self, num, model, **model_params):
        if num != 1:
            raise NotImplementedError()

        if model != SinkModel.__name__:
            raise NotImplementedError()

        if len(model_params) != 0:
            print(model_params)
            raise NotImplementedError()

        if len(self._models) != 0:
            raise NotImplementedError()

        eid = SinkModel.__name__ + '-0'
        self._models.append(SinkModel(eid=eid))

        return [{'eid': eid, 'type': model}]

    def get_data(self, outputs):
        for model in self._models:
            assert model.eid in outputs.keys()

        outputs = {model.eid: model.get_data() for model in self._models}

        return outputs

    def step(self, time, inputs):
        for model in self._models:
            model.step(inputs[model.eid])

        # Request being scheduled for every time step
        return time + 1
