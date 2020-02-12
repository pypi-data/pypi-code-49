import pangeamt_tea
import pangeamt_nlp
from pangeamt_tea.project.workflow.stage.base_stage import BaseStage
from pangeamt_nlp.multilingual_resource.dataset.dataset import Dataset


class InitStage(BaseStage):
    NAME = "init"

    def __init__(self, workflow):
        super().__init__(workflow, self.NAME)

    async def run(self):
        project = self.workflow.project
        project_dir = project.config.project_dir
        dataset = Dataset(str(project.config.data_dir))
        resources = dataset.get_resources()
        resource_array = []

        for resource in resources:
            resource_array.append(
                {
                    "file": resource.file,
                    "num_trans_units": resource.get_num_trans_units(),
                }
            )

        versions_dir = {
            "pangeamt_nlp": pangeamt_nlp.__version__,
            "pangeamt_tea": pangeamt_tea.__version__,
        }
        output = {"resources": resource_array, "version": versions_dir}
        print(output)
        return output
