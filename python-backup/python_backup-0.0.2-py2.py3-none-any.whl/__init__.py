import contextlib
import os
import platform
import psutil
import shlex
import subprocess
import sys
import time
import yaml

from glob import glob
from slugify import slugify


def term():
    """Get the Terminal reference to make output pretty

    Returns:
        (blessings.Terminal): Returns
        a `blessings <https://blessings.readthedocs.io/en/latest>`_ terminal
        instance. If running in windows and not cygwin it will return an
        `intercessions <https://pypi.org/project/intercessions>`_ terminal
        instance instead
    """
    if not hasattr(term, '_handle'):
        if sys.platform != "cygwin" and platform.system() == 'Windows':
            from intercessions import Terminal

        else:
            from blessings import Terminal

        term._handle = Terminal()

    return term._handle


@contextlib.contextmanager
def pushd(newDir):
    previousDir = os.getcwd()
    os.chdir(newDir)
    try:
        yield

    finally:
        os.chdir(previousDir)


class StateException(Exception):
    pass


class BackupException(Exception):
    pass


class Job(object):
    pool = []
    maxthreads = 4
    verbosity = 3
    logTransitions = False
    READY = 0
    QUEUED = 1
    RUNNING = 2
    FAILED = 3
    SUCCESSFUL = 4

    @staticmethod
    def initPool():
        if Job.pool:
            maxthreads = Job.maxthreads
            running = len(Job.running())
            if maxthreads > running:
                queued = Job.queued()
                if len(queued) < maxthreads - running:
                    maxthreads = len(queued)

                if maxthreads:
                    for i in range(0, maxthreads):
                        if len(queued) > i:
                            queued[i].start()

    @staticmethod
    def finished():
        return [x for x in Job.pool if x.state in (Job.FAILED, Job.SUCCESSFUL)]

    @staticmethod
    def pending():
        return [x for x in Job.pool
                if x.state not in (Job.FAILED, Job.SUCCESSFUL)]

    @staticmethod
    def running():
        return [x for x in Job.pool
                if x.state is Job.RUNNING]

    @staticmethod
    def queued():
        return [x for x in Job.pending() if x.state is Job.QUEUED]

    def __init__(self, backup, config):
        self._config = config
        self._backup = backup
        self._state = Job.READY

    def __str__(self):
        return 'Backup {0} Job #{1} ({2})'.format(
                self._backup.name, self.index, self.getState())

    @property
    def config(self):
        return self._config

    @property
    def state(self):
        if self._state is Job.READY and self in Job.pool:
            self.setState(Job.QUEUED)

        elif self._state is Job.RUNNING:
            code = self._process.poll() or self._process.returncode
            if code is None and not psutil.pid_exists(self._process.pid):
                code = -1

            if code is not None:
                self.setState(Job.FAILED if code else Job.SUCCESSFUL)
                Job.initPool()

        return self._state

    def queue(self):
        if self.state is not Job.READY:
            raise StateException('{} not in state to queue'.format(self))

        if self in Job.pool:
            raise StateException('{} already in queued pool'.format(self))

        self.setState(Job.QUEUED)
        Job.pool.append(self)

    @property
    def args(self):
        if not hasattr(self, '_args'):
            if Backup.engine == "rdiff-backup":
                args = ['rdiff-backup', '-v{}'.format(Backup.verbosity)]
                if 'filters' in self.config:
                    for item in self.config['filters']:
                        if 'include' in item:
                            args += ['--include', item['include']]

                        elif 'exclude' in item:
                            args += ['--exclude', item['exclude']]

                        else:
                            raise BackupException(
                                '{0} has an invalid filter {1}'.format(self, item))

                self._args = args + [self.fromPath, self.toPath]

            else:
                raise StateException(
                    'Invalid backup engine {}'.format(Backup.engine))

        return self._args

    @property
    def logfile(self):
        if not hasattr(self, '_logfile'):
            path = os.path.dirname(self.logpath)
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)

            self._logfile = open(self.logpath, 'w')

        return self._logfile

    @property
    def logpath(self):
        if not hasattr(self, '_logpath'):
            self._logpath = os.path.join(os.path.dirname(
                self._backup.logpath), 'job{}.log'.format(self.index))

        return self._logpath

    @property
    def fromPath(self):
        if not hasattr(self, '_fromPath'):
            fromPath = self.config['from']
            if 'roots' in self._backup.config:
                roots = self._backup.config['roots']
                if 'from' in roots:
                    if '::' in roots['from']:
                        if roots['from'].endswith('::'):
                            fromPath = roots['from'] + fromPath

                        else:
                            fromPath = roots['from'] + os.sep + fromPath

                    else:
                        fromPath = os.path.join(roots['from'], fromPath)

            self._fromPath = fromPath

        return self._fromPath

    @property
    def toPath(self):
        if not hasattr(self, '_toPath'):
            toPath = self.config['to']
            if 'roots' in self._backup.config:
                roots = self._backup.config['roots']
                if 'to' in roots:
                    if '::' in roots['to']:
                        if roots['to'].endswith('::'):
                            toPath = roots['to'] + toPath

                        else:
                            toPath = roots['to'] + os.sep + toPath

                    else:
                        toPath = os.path.join(roots['to'], toPath)

            self._toPath = toPath

        return self._toPath

    @property
    def process(self):
        return self._process

    @property
    def index(self):
        if not hasattr(self, '_index'):
            self._index = self._backup.jobs.index(self)

        return self._index

    def log(self, text):
        text = '[Backup {0} Job #{1}] {2}\n'.format(
                self._backup.name, self.index, text)
        print(text, end='')
        self._backup.logfile.write(text)
        self._backup.logfile.flush()

    def start(self):
        if self.state is not Job.QUEUED:
            raise StateException('Invalid state to start {}'.format(self))

        self._backup.setStatus(Backup.RUNNING)
        self.setState(Job.RUNNING)
        self.logfile.write(' '.join([shlex.quote(x) for x in self.args]) + '\n')
        self.logfile.flush()
        self._process = subprocess.Popen(
                self.args, stdout=self.logfile, stderr=subprocess.STDOUT,
                stdin=subprocess.DEVNULL, universal_newlines=True, bufsize=1)

    def setState(self, state):
        if self._state != state:
            self.log('{0} -> {1}'.format(
                    self.getState(self._state), self.getState(state)))
            self._state = state
            if state in (Job.SUCCESSFUL, Job.FAILED):
                self.logfile.close()

    def getState(self, state=None):
        return {
            Job.READY: 'ready',
            Job.QUEUED: 'queued',
            Job.RUNNING: 'running',
            Job.FAILED: 'failed',
            Job.SUCCESSFUL: 'successful',
        }[self.state if state is None else state]


class Backup(object):
    instances = {}
    _queue = []
    logTransitions = False
    engine = 'rdiff-backup'
    logdir = '/var/log/backup.d'
    BLOCKED = 0
    READY = 1
    QUEUED = 2
    RUNNING = 3
    FAILED = 4
    SUCCESSFUL = 5

    @staticmethod
    def _log():
        print('Backup status:')
        for backup in Backup.instances.values():
            print(' {}'.format(backup))
            for job in backup.pending:
                print('  {}'.format(job))

    @staticmethod
    def load(paths):
        for path in paths:
            Backup.get(path)

    @staticmethod
    def blocked():
        return [x for x in Backup.instances.values()
                if x.status is Backup.BLOCKED]

    @staticmethod
    def get(path):
        if path not in Backup.instances:
            Backup(sources()[path])

        return Backup.instances[path]

    @staticmethod
    def start():
        for backup in Backup.instances.values():
            backup.queue()

        Job.initPool()

    @staticmethod
    def wait(log=False):
        while Backup._queue:
            for backup in Backup._queue:
                if backup.status is Backup.BLOCKED:
                    for dependency in backup.blocking:
                        if dependency.status is Backup.READY:
                            dependency.queue()

            if log:
                Backup._log()

            time.sleep(1)

    def __init__(self, config):
        self._config = config
        self._path = self._config['path']
        self._name = slugify(self._path, max_length=255)
        self._logpath = os.path.realpath(os.path.join(
                Backup.logdir, self.name, 'backup.log'))
        self._status = Backup.READY
        if self.blocking:
            self.setStatus(Backup.BLOCKED)

        Backup.instances[self._path] = self

    def __str__(self):
        return 'Backup {0} ({1}, {2} jobs)'.format(
                self.name, self.getStatus(), len([x for x in self.jobs
                    if x.state not in (Job.FAILED, Job.SUCCESSFUL)]))

    @property
    def config(self):
        return self._config

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path

    @property
    def logpath(self):
        return self._logpath

    @property
    def logfile(self):
        if not hasattr(self, '_logfile'):
            path = os.path.dirname(self.logpath)
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)

            self._logfile = open(self.logpath, 'w+')

        return self._logfile

    def log(self, text):
        text = '[Backup {0}] {1}\n'.format(self.name, text)
        print(text, end='')
        self.logfile.write(text)
        self.logfile.flush()

    @property
    def status(self):
        if self.blocking:
            if [x for x in self.blocking if x.status is Backup.FAILED]:
                self.setStatus(Backup.FAILED)

            elif self._status is not Backup.BLOCKED:
                self.setStatus(Backup.BLOCKED)

        elif self._status is Backup.BLOCKED:
            if self not in Backup._queue:
                self.setStatus(Backup.READY)

            else:
                self.setStatus(Backup.QUEUED)
                for job in self.ready:
                    job.queue()

                Job.initPool()

        elif self._status is Backup.QUEUED and self not in Backup._queue:
            self.setStatus(Backup.READY)

        if self._status in (Backup.RUNNING, Backup.QUEUED) and not self.pending:
            self.setStatus(Backup.FAILED if self.failed else Backup.SUCCESSFUL)

        if self._status in (Backup.FAILED, Backup.SUCCESSFUL) \
                and self in Backup._queue:
            Backup._queue.remove(self)

        return self._status

    @property
    def blocking(self):
        return [x for x in self.depends
                if x.status is not Backup.SUCCESSFUL]

    @property
    def depends(self):
        if not hasattr(self, '_depends'):
            self._depends = []
            for path in self.config["depends"]:
                if path not in Backup.instances:
                    Backup(sources()[path])

                self._depends.append(Backup.instances[path])

        return self._depends

    @property
    def jobs(self):
        if not hasattr(self, '_jobs'):
            self._jobs = []
            if 'jobs' in self.config:
                for job in self.config['jobs']:
                    self._jobs.append(Job(self, job))

        return self._jobs

    @property
    def pending(self):
        return [x for x in self.jobs if x.state not in (Job.FAILED, Job.SUCCESSFUL)]

    @property
    def ready(self):
        return [x for x in self.jobs if x.state is Job.READY]

    @property
    def failed(self):
        return [x for x in self.jobs if x.state is Job.FAILED]

    def setStatus(self, status):
        if self._status != status:
            self.log('{0} -> {1}'.format(
                self.getStatus(self._status), self.getStatus(status)))
            self._status = status
            if status in (Backup.SUCCESSFUL, Backup.FAILED):
                self.logfile.close()

    def getStatus(self, status=None):
        return {
            Backup.BLOCKED: 'blocked',
            Backup.READY: 'ready',
            Backup.QUEUED: 'queued',
            Backup.RUNNING: 'running',
            Backup.FAILED: 'failed',
            Backup.SUCCESSFUL: 'successful'
        }[self.status if status is None else status]

    def queue(self):
        if self in Backup._queue:
            raise StateException('Backup already queued')

        Backup._queue.append(self)
        self.setStatus(Backup.QUEUED)
        if self.status is not Backup.BLOCKED:
            for job in self.ready:
                job.queue()

            Job.initPool()


def config():
    if hasattr(config, '_handle'):
        return config._handle

    with pushd(config._root):
        with open("backup.yml") as f:
            config._handle = yaml.load(f, Loader=yaml.SafeLoader)

    return config._handle


def sources():
    if hasattr(sources, '_handle'):
        return sources._handle

    sources._handle = {}
    with pushd(config._root):
        for source in config()['sources']:
            source = os.path.realpath(source)
            for path in glob('{}/*.yml'.format(source)) + \
                    glob('{}/*.yaml'.format(source)):
                path = os.path.realpath(path)
                with pushd(os.path.dirname(path)), open(path) as f:
                    data = yaml.load(f, Loader=yaml.SafeLoader)
                    if "active" in data and data["active"]:
                        data['path'] = path
                        if "depends" not in data:
                            data["depends"] = []

                        for i in range(0, len(data["depends"])):
                            data["depends"][i] = os.path.realpath(
                                    '{}.yml'.format(data["depends"][i]))

                        sources._handle[path] = data

    return sources._handle


def main(args):
    config._root = args[0] if len(args) else '/etc/backup.d'
    if not os.path.exists(config._root):
        raise BackupException(
            'Configuration files missing from {}'.format(config._root))

    if 'engine' in config():
        engine = config()["engine"]
        if engine not in ("rdiff-backup"):
            raise BackupException('Unknown backup engine: {}'.format(engine))

        Backup.engine = engine

    if 'logdir' in config():
        logdir = config()['logdir']
        os.makedirs(logdir, exist_ok=True)
        if not os.path.exists(logdir):
            raise BackupException(
                'Unable to create logging directory: {}'.format(logdir))

        Backup.logdir = logdir

    if 'maxthreads' in config():
        Job.maxthreads = config()['maxthreads']

    if 'verbosity' in config():
        Backup.verbosity = config()['verbosity']

    Backup.logTransitions = Job.logTransitions = True
    Backup.load(sources().keys())
    Backup.start()
    Backup.wait()


if __name__ == '__main__':
    try:
        main(sys.argv[1:])

    except BackupException as ex:
        print(ex)
        sys.exit(1)

    except Exception:
        from traceback import format_exc
        msg = "Error encountered:\n" + format_exc().strip()
        print(msg)
        sys.exit(1)
