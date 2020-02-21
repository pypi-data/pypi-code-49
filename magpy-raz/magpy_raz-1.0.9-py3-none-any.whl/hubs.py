'''
'''
import threading
import magpy.project as mp
import magpy.general as mg
from magpy.csv_files.backlog_file import BacklogFile
from magpy.csv_files.event_file import EventFile
from magpy.csv_files.sprint_file import SprintFile


class Hubs:
    '''
    Represents a Magshimim list of hubs, and all of their projects
    '''

    def __init__(self, gl, hubs):
        self.events = []
        self.backlog = []
        self.sprint_items = []

        print('Loading projects:')
        print('=================')
        for hub in hubs:
            try:
                group = gl.gitlab.groups.get(hub.group_id)

            except BaseException:
                print(f'Gitlab hub group not found: id = {hub.group_id}')
                exit(1)

            # Projects
            hub_projects = group.projects.list(include_subgroups=True,
                                               simple=True,
                                               all=True)

            threads = []
            events = [[] for i in range(len(hub_projects))]
            backlog = [[] for i in range(len(hub_projects))]
            sprints = [[] for i in range(len(hub_projects))]

            # Each project data extraction id done ina seperate thread
            for i, p in enumerate(hub_projects):
                gl_project = gl.gitlab.projects.get(p.id)
                thread_args = [gl, hub.name, hub.start_date, hub.end_date,
                               gl_project, i, events, backlog, sprints]
                thread = threading.Thread(target=self.get_project_data,
                                          args=thread_args)
                thread.start()
                threads.append(thread)

            # wait for all threads to end
            for thread in threads:
                thread.join()

            # collect thread results
            self.events += [e for p_events in events for e in p_events]
            self.backlog += [i for p_issues in backlog for i in p_issues]
            self.sprint_items += [
                i for p_sprints in sprints for s in p_sprints for i in s.items]

    def write_csv_files(self):
        '''
        Generate hubs csv data files
        '''
        print()
        print('Writing CSV files:')
        print('==================')
        BacklogFile(self.backlog).write()
        EventFile(self.events).write()
        SprintFile(self.sprint_items).write()

    def get_project_data(self, gl, hub_name, start_date, end_date,
                         gl_project, i, events, backlog, sprints):
        '''
        Extracts project data from Gitlab
        '''
        project = mp.Project(gl, hub_name, start_date, end_date, gl_project)

        # Extracted data is kept in a list to avoid thread colissions
        events[i] = project.events
        backlog[i] = project.backlog
        sprints[i] = project.sprints
