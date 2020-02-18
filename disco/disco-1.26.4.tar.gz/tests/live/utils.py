from disco.core import constants


def get_non_running_tasks(m_tasks):
    non_running_tasks = []
    for m_task in m_tasks:
        print("{} with Status: {}".format(m_task, m_task.status))
        if m_task.status != constants.TaskStatus.running.value:
            non_running_tasks.append(m_task)
    return non_running_tasks
