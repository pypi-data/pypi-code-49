import os
from pangeamt_tea.project.workflow.stage.base_stage import BaseStage
from pangeamt_tea.project.workflow.stage.stage_factory import StageFactory
from pangeamt_nlp.translation_model.translation_model_factory import (
    TranslationModelFactory,
)


class TrainStage(BaseStage):
    NAME = "train"
    DIR = "03_trained"

    def __init__(self, workflow):
        super().__init__(workflow, self.NAME)

    async def run(self, gpu=None):
        project = self.workflow.project
        config = project.config
        project_dir = config.project_dir

        name = config.translation_model["name"]
        args = config.translation_model["args"].split(" ")
        translation_model = TranslationModelFactory.get_class(name)

        workflow_dir = self.workflow.get_dir(project_dir)
        model_dir = os.path.join(workflow_dir, TrainStage.DIR)
        os.mkdir(model_dir)
        prepare_stage = StageFactory.new("prepare", self.workflow)
        prepared_dir = os.path.join(workflow_dir, prepare_stage.DIR)
        data_dir = os.path.join(prepared_dir, "05_batched")

        if gpu is not None:
            gpu = str(gpu)

        translation_model.train(data_dir, model_dir, *args, gpu=gpu)
        return {}
