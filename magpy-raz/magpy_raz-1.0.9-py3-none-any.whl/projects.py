'''
'''
import threading
import magpy.project as mp
import magpy.general as mg
from magpy.csv_files.backlog_file import BacklogFile
from magpy.csv_files.event_file import EventFile
from magpy.csv_files.sprint_file import SprintFile


class Projects:
    '''
    Represents a Magshimim list of projects
    '''

    def __init__(self, gl, project_list):
        self.events = []
        self.backlog = []
        self.sprint_items = []

        print('Loading projects:')
        print('=================')

        threads = []
        events = [[] for i in range(len(project_list))]
        backlog = [[] for i in range(len(project_list))]
        sprints = [[] for i in range(len(project_list))]

        # Each project data extraction id done ina seperate thread
        for i, p in enumerate(project_list):
            hub_name, project_id, start_date, end_date = p
            thread_args = [gl, hub_name, start_date, end_date,
                           project_id, i, events, backlog, sprints]
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
        Generate projects csv data files
        '''
        print()
        print('Writing CSV files:')
        print('==================')
        BacklogFile(self.backlog).write()
        EventFile(self.events).write()
        SprintFile(self.sprint_items).write()

    def get_project_data(self, gl, hub_name, start_date, end_date,
                         project_id, i, events, backlog, sprints):
        '''
        Extracts project data from Gitlab
        '''
        project = mp.Project(
            gl,
            hub_name,
            project_id,
            start_date,
            end_date)

        # Extracted data is kept in a list to avoid thread colissions
        events[i] = project.events
        backlog[i] = project.backlog
        sprints[i] = project.sprints
