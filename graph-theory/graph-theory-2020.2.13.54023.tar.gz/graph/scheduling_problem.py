from itertools import count
from matplotlib import pyplot as plt
from graph import Graph
from graph.hash import graph_hash


# __all__ = ['Machine', 'Job', 'minimise_makespan', 'gantt']


class Process(object):
    __slots__ = ['id', 'run', 'setup', 'teardown']

    def __init__(self, id, run, setup, teardown):
        """
        :param run: int or float: runtime of the process.
        :param setup: int or float: setup time of the process.
        :param teardown: int or float: teardown time of the process.

        Note that consecutive executions of an already set-up process does
        not require to be set-up again hereby if: p = Process(2,3,5), then
        the makespan of  2 * p : 2 + 3 + 3 + 5 = 13 units of time.

        """
        self.id = id
        assert isinstance(run, (int, float)) and run >= 0
        self.run = run
        assert isinstance(setup, (int, float)) and setup >= 0
        self.setup = setup
        assert isinstance(teardown, (int, float)) and teardown >= 0
        self.teardown = teardown

    def copy(self):
        return Process(self.id, self.run, self.setup, self.teardown)


class Task(object):
    def __init__(self, process, job):
        self.process = process
        self.job = job

    def __lt__(self, other):
        return self.process.id < other.process.id

    def __repr__(self):
        return "{},{}".format(self.process, self.job)


class AppointmentError(Exception):
    pass


class Appointment(object):
    __slots__ = ['machine', 'job', 'process', 'earliest_start', 'start', 'finish']

    def __init__(self, machine, job, process, earliest_start, start=float('inf'), finish=float('inf')):
        """ An appointment between a machine and a job.
        :param machine: machine id
        :param job: job id
        :param process: process id
        :param earlist_start: estimated start
        :param start: start
        :param finish: finish
        """
        self.machine = machine
        self.job = job
        self.process = process
        self.earliest_start = earliest_start
        self.start = start
        self.finish = finish

    def copy(self):
        return Appointment(self.machine, self.job, self.process, self.earliest_start, self.start, self.finish)


class Machine(object):
    ids = count()

    def __init__(self):
        self.id = next(Machine.ids)
        self.processes = {}
        self.jobs = []
        self.schedule = []
        self.appointments = Graph()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{}-{}".format(self.__class__.__name__, self.id)

    def __hash__(self):
        return self.id

    def add_process(self, process_id, run_time, setup_time=0, teardown_time=0):
        self.processes[process_id] = Process(id=process_id, run=run_time, setup=setup_time, teardown=teardown_time)

    def makespan_finish(self):
        if not self.schedule:
            return 0
        return max([s.f for s in self.schedule])

    def evaluate(self, schedule):
        """ Machine selects jobs until all jobs have a machine """
        raise NotImplementedError


class Job(object):
    ids = count()

    def __init__(self):
        self.id = next(Job.ids)
        self.paths = Graph()
        self.candidate_machines = []
        self.schedule = []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{}-{}".format(self.__class__.__name__, self.id)

    def __hash__(self):
        return self.id

    def add_appointment(self, appointment):
        self.schedule.append(appointment)

    def is_scheduled(self):
        if len(self.paths.nodes()) == 0:
            raise ValueError("add process first.")

        if len(self.paths.nodes()) == 1:
            proc_id = self.paths.nodes()[0]
            if len(self.schedule) == 1:
                appointment = self.schedule[0]
                if appointment.process == proc_id:
                    return True

        path = [app.process for app in self.schedule]
        if path[0] not in self.paths.nodes(in_degree=0):  # starts
            return False
        if path[-1] not in self.paths.nodes(out_degree=0):  # ends
            return False
        if not self.paths.has_path(path):
            return False
        item_1 = self.schedule[0]
        for item_2 in self.schedule[1:]:
            if item_1.finish > item_2.start:
                raise AppointmentError(f"{item_2.start} start before {item_1.finish} ends")
            item_1 = item_2
        return True

    def add_process(self, steps):
        """
        :param: steps: a list of required processing steps.

        minimum: [1] interpreted as "one step" process.

        to provide multiple paths, for example [1,2,3] or [1,4,3]
        simply add processes twice, as the job creates a graph of
        options as:

        [1] ---> [2] ---> [3]
           +             /
            ---> [4] -->
        """
        assert isinstance(steps, list)
        if len(steps) == 1:
            self.paths.add_node(steps[0])
        for idx in range(len(steps) - 1):
            self.paths.add_edge(steps[idx], steps[idx + 1])

    def evaluate(self, schedule):
        """ Job selets machines until all process steps have a machine """
        raise NotImplementedError


def minimise_makespan(machines, jobs):
    """
    Minimises the makespan of the scheduling problem
    :param machines: list of machines
    :param jobs: list of jobs
    :return list of schedules.  # :return: tuple(list of machines, list of jobs)

    by returning the same output, as given as input,
    multiple iterations can be performed.
    """
    assert isinstance(machines, list)
    assert all(isinstance(i, Machine) for i in machines)
    assert isinstance(jobs, list)
    assert all(isinstance(i, Job) for i in jobs)

    makespan_min = float('inf')  # the default value for an unsolved scheduling problem.
    solutions = set()  # collection of graph-hashes for explored solutions.
    best_solution = None  # the solution with the smallest makespan.
    compatibility = Graph()  # bi-directional di-graph with machines and jobs based on processes.
    for m in machines:
        m_proc = set(m.processes.keys())  # processes that the machine supports.
        for j in jobs:
            j_procs = set(j.paths.nodes())  # processes that the job requires.
            if j_procs.intersection(m_proc):
                compatibility.add_edge(m, j)
                compatibility.add_edge(j, m)

    # check that all jobs can be processed.
    all_procs = set([m.processes.keys() for m in machines])
    all_jobs = set([j.paths.nodes() for j in jobs])
    if all_jobs.issuperset(all_procs):
        missing = all_jobs.difference(all_procs)
        raise ValueError("machines do not support processes: {}".format(missing))

    # machines offer services to jobs.
    #     candidates = compatibility.nodes(from_node=m)
    #     m.candidate_jobs()

    while True:
        # 1. let jobs book time with machines.
        # 2. let machines move jobs around to reduce idle time.
        # 3. evaluate current performance...
        ms = makespan(machines, jobs)  # evaluate the performance.
        if ms == float('inf'):  # means that there are still unassigned jobs.
            continue

        if ms < makespan_min:  # remember the solution if the performance is better than best previously known solution.
            makespan_min = ms
            best_solution = [m.schedule.copy() for m in machines]

        gh = graph_hash(solution(machines, jobs))
        if gh in solutions:  # the solution search is cyclic: abort with best known solution.
            return best_solution
        else:
            solutions.add(gh)


def makespan(machines, jobs):  # todo
    """ calculates the makespan of the schedule.
    :param: machines: list of machines
    :param: jobs: list of jobs
    :return: float: the makespan of the assignment.
    If all jobs are not assigned, float('inf') is returned.

    """
    # 1. make a set of all jobs and check if they're scheduled.
    if not all(job.is_scheduled() for job in jobs):
        return float('inf')
    # 2. find the max finish time of all machines
    return max((m.makespan_finish() for m in machines))


def solution(machines, jobs):
    """
    :param machines: list of machines
    :param jobs: list of jobs
    :return: graph of assignments
    """
    raise NotImplementedError


def gantt(machines, jobs):
    """ creates a gantt chart of the machines and their assigned jobs. """
    assert isinstance(machines, list), 'expected list of Machines'
    assert all(isinstance(i, Machine) for i in machines), 'expected list of Machines'
    assert isinstance(jobs, list), 'expected list of Jobs'
    assert all(isinstance(i, Job) for i in jobs), 'Expected list of Jobs'

    fig, ax = plt.subplots()

    # to debug see: https://matplotlib.org/examples/pylab_examples/broken_barh.html
    x_max = 0
    for m in machines:
        xs = []
        for s in m.schedule:
            xs.append((s.start, s.end - s.start))
            x_max = max(x_max, s.end)
        ys = (m.id * 10, 8)  # y offset, y height
        ax.broken_barh(xs, ys)

        for s in m.schedule:
            ax.annotate('J{}.{}'.format(s.job, s.proc), (s.start, m.id * 10),
                        fontsize=8,
                        horizontalalignment='right', verticalalignment='top')

    ax.set_ylim(0, len(machines) * 10 + 10)
    ax.set_xlim(0, x_max)
    ax.set_xlabel('time')
    ax.set_yticks([(m.id * 10) - 5 for m in machines])
    ax.set_yticklabels([m.id for m in machines])
    ax.grid(True)

    plt.show()


