from pangeamt_tea.project.workflow.stage.base_stage import BaseStage


class EvalStage(BaseStage):
    NAME = 'eval'

    def __init__(self, workflow):
        super().__init__(workflow, self.NAME)

    async def run(self):
        return {

        }