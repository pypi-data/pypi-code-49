from __future__ import print_function

import logging
import sys
import typing

from dbnd import dbnd_bootstrap
from dbnd_airflow.dbnd_task_executor.airflow_operator_as_dbnd import (
    AirflowOperatorAsDbndTask,
)
from dbnd_airflow_contrib.dbnd_operator import DbndOperator


if typing.TYPE_CHECKING:
    from dbnd._core.task_run.task_run import TaskRun

logger = logging.getLogger(__name__)


def dbnd_execute_airflow_operator(airflow_operator, context):
    """
    Airflow Operator execute function
    """
    dbnd_task_id = getattr(airflow_operator, "dbnd_task_id", None)
    if not dbnd_task_id:
        return airflow_operator.execute(context)

    # operator is wrapped/created by databand
    if isinstance(airflow_operator, DbndOperator):
        return airflow_operator.execute(context)

    from dbnd._core.current import get_databand_run

    # this is the Airflow native Operator
    # we will want to call it with Databand wrapper
    # we are at the airflow operator that is part of databand dag
    dbnd_task_run = get_databand_run().get_task_run_by_id(dbnd_task_id)
    if isinstance(dbnd_task_run.task, AirflowOperatorAsDbndTask):
        # we need to update it with latest, as we have "templated" and copy airflow operator object
        dbnd_task_run.task.airflow_op = airflow_operator
        return dbnd_task_run.runner.execute(context)
    else:
        logging.info(
            "Found airflow operator with dbnd_task_id that can not be run by dbnd: %s",
            airflow_operator,
        )
        return airflow_operator.execute(context)


# wrappers for DbndOperator


def _dbnd_operator_to_taskrun(operator):
    # type: (DbndOperator)-> TaskRun
    from dbnd._core.current import get_databand_run

    return get_databand_run().get_task_run_by_id(operator.dbnd_task_id)


def dbnd_operator__execute(dbnd_operator, context):
    from dbnd._core.current import try_get_databand_run
    from dbnd._core.run.databand_run import DatabandRun
    from targets import target

    run = try_get_databand_run()
    if not run:
        # we are not inside dbnd run, probably we are running from native airflow
        # let's try to load it:
        executor_config = dbnd_operator.executor_config
        logger.info("context: %s", context)

        logger.info("task.executor_config: %s", dbnd_operator.executor_config)
        logger.info("ti.executor_config: %s", context["ti"].executor_config)
        driver_dump = executor_config["DatabandExecutor"].get("dbnd_driver_dump")
        print(
            "Running dbnd task %s %s" % (dbnd_operator.dbnd_task_id, driver_dump),
            file=sys.__stderr__,
        )

        if executor_config["DatabandExecutor"].get(
            "remove_airflow_std_redirect", False
        ):
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

        dbnd_bootstrap()
        run = DatabandRun.load_run(
            dump_file=target(driver_dump), disable_tracking_api=False
        )

        with run.run_context() as dr:
            task_run = run.get_task_run_by_id(dbnd_operator.dbnd_task_id)
            ret_value = task_run.runner.execute(airflow_context=context)
    else:
        task_run = run.get_task_run_by_id(dbnd_operator.dbnd_task_id)
        ret_value = task_run.runner.execute(airflow_context=context)

    return ret_value


def dbnd_operator__kill(dbnd_operator):
    from dbnd._core.current import try_get_databand_run

    run = try_get_databand_run()
    if not run:
        return

    task_run = run.get_task_run_by_id(dbnd_operator.dbnd_task_id)
    return task_run.task.on_kill()
