import time
from datetime import datetime
from autoclass import autoclass


@autoclass
class BaseStage:
    START = "start"
    END = "end"
    REPORT = "report"

    def __init__(self, workflow, name):
        pass

    async def run_with_time_report(self, *args, **kwargs):
        start = time.ctime(int(time.time()))
        workflow_config = self.workflow.config
        getattr(workflow_config, self.name)
        workflow_config.set_stage(
            self.name,
            {
                BaseStage.START: start,
                BaseStage.END: None,
                BaseStage.REPORT: None,
            },
        )
        workflow_config.save()

        report = await self.run(*args, **kwargs)
        end = time.ctime(int(time.time()))
        workflow_config.set_stage(
            self.name,
            {
                BaseStage.START: start,
                BaseStage.END: end,
                BaseStage.REPORT: report,
            },
        )
        workflow_config.save()

    async def run(self, *args, **kwargs):
        raise ValueError("This method should be implemented")
