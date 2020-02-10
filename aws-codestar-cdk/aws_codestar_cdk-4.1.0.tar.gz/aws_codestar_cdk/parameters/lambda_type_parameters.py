from aws_cdk.aws_iam import Role


class LambdaTypeParameters:
    """
    Parameters class.
    """
    def __init__(self, lambda_exec_role: Role, event_type: str, **kwargs):
        """
        Parameters, describing your function invocation event.

        :param lambda_exec_role: Execution role for the lambda function.
        :param event_type: The type of event, that invokes your function.
        Currently supported types are:
        Api - Creates an API gateway for your function with GET and POST requests.
        Schedule - Creates a schedule to invoke your lambda function at specific times.
        In this case, argument schedule_expression is also required
        None - No invocation event is created, your function can only be deployed in the AWS testing environment.
        :param kwargs: currently supported arguments:
        schedule_expression - a string, describing your lambda invocation schedule.

        Is can be either:
        rate(x units), meaning your function will be called every x units.
        e.g. rate(5 minutes), in which case the function will be invoked every 5 minutes.

        cron(Minutes Hours Day-of-month Month Day-of-week Year)
        e.g. cron(0 0 * * ? *), which would mean, that the function will be invoked every day at midnight.

        More info: https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html

        :return No return.
        """
        self.lambda_exec_role = lambda_exec_role

        assert event_type in ['Api', 'Schedule', 'None']

        self.event_type = event_type
        if event_type == 'Schedule':
            self.schedule_expression = kwargs['schedule_expression']
            assert self.schedule_expression.startswith('rate(') or self.schedule_expression.startswith('cron(')
