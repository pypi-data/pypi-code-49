import socket
import threading
import time
import math

import datetime

from ..models import Schedule

"""
The scheduler has a resolution of 0.1 seconds

The scheduler reads from the database and calculates the jobs depending on overrides etc.
After the calculations the job is headed over to the Taskrunner wich triggers the events.
"""


class TaskRunner(object):
    """Class to run a periodic job"""

    def __init__(self):
        self.jobs = []

    def return_10th_second(self, act_time=None):
        if not act_time:
            act_time = self.return_clean_now()
        return int((act_time - datetime.datetime(1970, 1, 1)).total_seconds() * 10)

    def return_clean_now(self):
        act_time = datetime.datetime.now()
        return act_time.replace(microsecond=math.trunc(act_time.microsecond / 100000.0) * 100000)

    def check_execution(self, job_times, act_thread, **job):
        for job_time in job_times:
            # print(job)
            # kill old
            if job_time.date() > job['job_end_date']:
                if not act_thread.stopped:
                    act_thread.stopped = True

            # is job in date range?
            elif job_time.date() >= job['job_start_date']:
                # does weekday match?
                if not job['weekdays'] or job_time.weekday() in job['weekdays']:
                    # is job in time range?
                    if job['job_start_time'] <= job_time.time() <= job['job_end_time']:
                        # repeated or not..?
                        if job['duration'].total_seconds() == 0:
                            if job['job_start_time'] == job_time.time():
                                print(job_time, job['name'], 'on time per day..')
                        else:
                            start_time = job_time.replace(
                                hour=job['job_start_time'].hour,
                                minute=job['job_start_time'].minute,
                                second=job['job_start_time'].second,
                                microsecond=job['job_start_time'].microsecond,
                            )
                            time_from_start_time_10th = math.trunc((job_time - start_time).total_seconds() * 10)
                            duration_10th = math.trunc(job['duration'].total_seconds() * 10)

                            if time_from_start_time_10th % duration_10th == 0:
                                print(job_time, job['name'])

    def job_timer(self, **job):
        old_10th_second = self.return_10th_second()
        errors = 0
        while not getattr(threading.current_thread(), 'stopped', False):
            act_time = self.return_clean_now()

            act_10th_second = self.return_10th_second(act_time)
            if act_10th_second != old_10th_second:
                job_times = [
                    datetime.datetime.fromtimestamp(missed / 10.0)
                    for missed in range(
                        max(old_10th_second, act_10th_second - 100),
                        act_10th_second
                    )[1:]
                ]
                job_times.append(act_time)
                if len(job_times) > 1:
                    errors += 1
                    print(errors, job_times)

                # check for execution
                check_dic = {
                    'job_times': job_times,
                    'act_thread': threading.current_thread(),
                }
                check_dic.update(job)

                check_thread = threading.Thread(
                    target=self.check_execution,
                    kwargs=check_dic
                )
                check_thread.daemon = True
                check_thread.start()

                old_10th_second = act_10th_second
            time.sleep(.05)

    def add_job(self, threaded=False, **job):
        if not threaded:
            job.update({'threaded': True})
            t0 = threading.Thread(
                target=self.add_job,
                kwargs=job
            )
            t0.daemon = True
            t0.stopped = False
            t0.start()

            self.jobs.append(t0)

        else:
            self.job_timer(**job)

    def reload_tasks(self):
        while self.jobs:
            setattr(self.jobs.pop(), 'stopped', True)

        print('TaskRunner reload jobs.')


class Scheduler(object):
    """Class to schedule a task"""

    def __init__(self):
        self.socket = None
        self.task_runner = None

        t0 = threading.Thread(target=self.block_socket)
        t0.daemon = True
        t0.start()

    def block_socket(self):
        # NOTE Can be called multiple times: Only the first instance which blocks the socket will be executed.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)

        try:
            self.socket.bind(('127.0.0.1', 40000))
            self.socket.listen(1)

            self.task_runner = TaskRunner()
            self.get_jobs_from_database()

            self.socket_listener()
        except socket.error:
            pass

    def socket_listener(self):
        # NOTE this is local - maybe a reload is unnecessary
        while True:
            conn, addr = self.socket.accept()
            while True:
                data = conn.recv(1024)
                if data.strip() == b'reload_jobs':
                    self.get_jobs_from_database()
                if not data:
                    break

            conn.close()

    def get_jobs_from_database(self):

        self.task_runner.reload_tasks()

        override_jobs = Schedule.objects.filter(override_day=True, active=True)
        excluded_dates = [x.start_date for x in override_jobs] + [datetime.date.max]
        excluded_dates.sort()

        intervals = [x for x in Schedule.objects.filter(override_day=False, active=True)]

        for interval in intervals:
            if not interval.last_date:
                interval.last_date = datetime.date.max

            if interval.last_time == datetime.time.min:
                interval.last_time = datetime.time.max

            self.analyze_job(interval, excluded_dates)

        for override in override_jobs:
            override.last_date = override.start_date

            if override.last_time == datetime.time.min:
                override.last_time = datetime.time.max

            self.analyze_job(override, [datetime.date.max])

    def analyze_job(self, job, excluded_dates):
        job_start_date = job.start_date
        for (i, excluded_date) in enumerate(excluded_dates):
            if job_start_date < excluded_date:
                pass
            # excluded does not affect
            elif job_start_date > excluded_date:
                continue
            # add + 1 to start..
            elif job_start_date == excluded_date:
                job_start_date += datetime.timedelta(days=1)

            # exluded does not affect
            if job.last_date < excluded_date:
                job_end_date = job.last_date

            # job.last_date > excluded_date
            else:
                job_end_date = excluded_date - datetime.timedelta(days=1)

            if job_start_date <= job_end_date:
                # print( 'RUN:', i + 1, job_start_date.strftime('%d.%m.%Y'), '>>', job_end_date.strftime('%d.%m.%Y'))
                weekdays = [i for i in range(7) if getattr(job, 'd_{}'.format(i))]
                self.task_runner.add_job(
                    **{
                        'job_start_date': job_start_date,
                        'job_end_date': job_end_date,
                        'job_start_time': job.start_time,
                        'job_end_time': job.last_time,
                        'duration': job.repeat_duration,
                        'weekdays': weekdays,
                        'name': job.name,
                    }
                )

            try:
                job_start_date = excluded_date + datetime.timedelta(days=1)
            except OverflowError:
                pass

        # print('Running threads:', len(self.task_runner.jobs))
