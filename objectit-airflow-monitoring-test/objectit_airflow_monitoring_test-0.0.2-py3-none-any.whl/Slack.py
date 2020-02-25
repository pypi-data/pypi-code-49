from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator

class Slack:
    def __init__(self):
        self.slack_conn_id = 'slack'
 
    def notify_slack_channel(self, context):
        if context is not None:
            slack_webhook_token = BaseHook.get_connection(self.slack_conn_id).password
            slack_msg = """
                    :red_circle: Task Failed. 
                    *Task*: {task}  
                    *Dag*: {dag} 
                    *Execution Time*: {exec_date}
                    *Log Url*: {log_url} 
                    """.format(
                    task=context.get('task_instance').task_id,
                    dag=context.get('task_instance').dag_id,
                    ti=context.get('task_instance'),
                    exec_date=context.get('execution_date').strftime("%d-%m-%Y %H:%M:%S"),
                    log_url=context.get('task_instance').log_url,
                )
            failed_alert = SlackWebhookOperator(
                task_id='slack_test',
                http_conn_id='slack',
                webhook_token=slack_webhook_token,
                message=slack_msg,
                username='airflow')
        
            return failed_alert.execute(context=context)