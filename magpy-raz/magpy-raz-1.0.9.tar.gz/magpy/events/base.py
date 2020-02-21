import datetime
import gitlab as gl
import magpy.general as mg


class Event:
    '''
    '''
    TARGET_TYPE_GITLAB = 'GitLab'
    TARGET_TYPE_REPOSITOTY = 'Repository'

    def __init__(self, hub_name, project_name, user_name,
                 sprint_start_dates, gl_event_date):
        self.hub_name = hub_name
        self.project_name = project_name
        self.student_name = self.__user_name(user_name)
        event_datetime = self.__datetime(gl_event_date)
        self.date = event_datetime.date()
        self.time = event_datetime.time()
        self.week = self.__week(self.date, sprint_start_dates[0])
        self.sprint_number = self.__sprint_number(
            self.date, sprint_start_dates)
        self.sprint_week = self.__sprint_week(
            self.sprint_number, self.date, sprint_start_dates)

    def __user_name(self, user_name):
        '''
        Returns the name of the user
        '''
        name = user_name.strip().title().split()
        student_name = name[0]
        # Last name initial (if exists)
        if len(name) > 1:
            student_name += f' {name[1][0]}.'

        return student_name

    def __datetime(self, event_datetime):
        '''
        Returns the event date and time in local time-zone
        '''

        return mg.str_to_datetime(event_datetime)

    def __sprint_number(self, event_date, project_sprint_start_dates):
        '''
        Returns the event sprint number
        '''
        sprint_number = -1
        for sprint_start in project_sprint_start_dates:
            if event_date < sprint_start:
                break
            sprint_number += 1

        if sprint_number == -1:
            sprint_number = 0

        return sprint_number

    def __week(self, event_date, start_date):
        '''
        Returns the week number in the year (1 = week of first meeting)
        '''

        return (event_date - start_date).days // 7 + 1

    def __sprint_week(self, sprint_num, event_date, sprint_start_dates):
        '''
        Represent sprint-week as a decimal namber, where:
           sprint number is the integer part and
           week number is the fraction
        Example: 2.3 represents week 3 of sprint 2
        '''
        sprint_week = 0
        for sprint_start in sprint_start_dates:
            if event_date >= sprint_start:
                days_in_sprint = (event_date - sprint_start).days
                sprint_week = days_in_sprint // 7 + 1

        return sprint_num + sprint_week / 10
