from ..core import base_client


class UserTaskClient(base_client.BaseClient):

    def __init__(self, url, session=None, identity=None):
        super(UserTaskClient, self).__init__(url, session, identity)

    async def finish_user_task(self, process_instance_id, correlation_id, user_task_instance_id, answer):
        path = f"/api/consumer/v1/processes/{process_instance_id}/correlations/{correlation_id}/usertasks/{user_task_instance_id}/finish"

        answer_payload = {"formFields": answer}

        result = await self.do_post(path, answer_payload)

        return result

    async def get_own_user_tasks(self):
        path = "/api/consumer/v1/user_tasks/own"

        result = await self.do_get(path)

        return result['userTasks']