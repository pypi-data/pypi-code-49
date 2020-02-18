"""Sync queue module"""
import datetime
import sys

import fs.filesize

from ..importers.work_queue import Task, WorkQueue
from ..importers.progress_reporter import ProgressReporter
from ..util import confirmation_prompt


class SyncQueue(WorkQueue):
    """Queue class"""

    def __init__(self, dst, jobs, assume_yes=False, dry_run=False):
        super().__init__({'store': jobs, 'delete': 1})
        self.dst = dst
        self.assume_yes = assume_yes
        self.dry_run = dry_run
        self.cleanup = False
        self.report = SyncProgressReporter(self)
        self.report.add_group('store', 'Syncing', 0)
        self.report.add_group('delete', 'Deleting', 0)

    def store(self, src_file):
        """Add a store task to queue for a source file"""
        self.enqueue(StoreTask(self, src_file))
        self.report.groups['store'].total_bytes += src_file.size

    def delete(self, dst_file):
        """Add a delete task to queue for a destination file"""
        self.enqueue(DeleteTask(self, dst_file))
        self.cleanup = True

    def enqueue(self, task, priority=10):
        super().enqueue(task, priority=priority)
        self.report.groups[task.group].total_count += 1

    def confirm_replace(self, filename):
        """Confirm file replacement"""
        if self.assume_yes or self.dry_run:
            return True
        with self._lock:
            self.report.suspend()
            message = f'Are you sure you want to replace "{filename}"?'
            confirm = confirmation_prompt(message)
            self.report.resume()
            return confirm

    def start(self):
        super().start()
        self.report.start()

    def shutdown(self):
        if self.cleanup:
            self.dst.cleanup()
        super().shutdown()
        self.report.shutdown()
        self.report.final_report()


class StoreTask(Task):
    """Store task class"""
    __slots__ = ('queue', 'src_file', 'bytes_read', 'event')

    def __init__(self, queue, src_file):
        super().__init__('store')
        self.queue = queue
        self.src_file = src_file
        self.bytes_read = 0
        self.event = None

    def execute(self):
        """Compare src and dst (if it exists) and create/update(prompt)/skip as appropriate"""
        dst_file = self.queue.dst.file(self.src_file.name)
        if not dst_file.stat():
            self.event = 'store/create'
            self.store(dst_file)
        elif self.src_file.size == dst_file.size and self.src_file.modified <= dst_file.modified:
            self.event = 'skip/stat'
            self.skip()
        elif self.queue.confirm_replace(self.src_file.name):
            self.event = 'store/update'
            self.store(dst_file)
        else:
            self.event = 'skip/user'
            self.skip()
        return None, None

    def store(self, dst_file):
        """Store source file contents to destination file"""
        if self.queue.dry_run:
            self.bytes_read = self.src_file.size
        else:
            dst_file.store(self.src_file)
            self.bytes_read = self.src_file.bytes_read
            self.src_file.cleanup()
        self.src_file = None

    def skip(self):
        """Skip task and notify queue"""
        self.skipped = True
        self.queue.skip_task(task=self)

    def get_bytes_processed(self):
        """Return number of bytes read from the source (equals bytes written to destination)"""
        return self.bytes_read

    def get_desc(self):
        """Return 'store path/to/file'"""
        return f'{self.group} {self.src_file.name}'


class DeleteTask(Task):
    """Delete task"""
    __slots__ = ('queue', 'dst_file')

    def __init__(self, queue, dst_file):
        super().__init__('delete')
        self.queue = queue
        self.dst_file = dst_file

    def execute(self):
        """Delete file on destination"""
        if not self.queue.dry_run:
            self.dst_file.delete()
        self.dst_file = None
        return None, None

    def get_bytes_processed(self):
        """Return one (representing a single file instead of bytes)"""
        return 1

    def get_desc(self):
        """Return 'delete path/to/file'"""
        return f'{self.group} {self.dst_file.name}'


class SyncProgressReporter(ProgressReporter):
    """Sync progress reporter class"""
    def report(self, newline='\r'):
        messages = []
        compare_total = compared_count = 0
        for name, group in self.groups.items():
            compare_total += group.total_count
            compared_count += group.completed
            unskipped_count = group.total_count - group.skipped
            if unskipped_count > 0:
                if group.completed == unskipped_count:
                    speed_str = 'DONE'
                elif name == 'store':
                    speed_str = fs.filesize.traditional(group.bytes_per_sec) + '/s'
                elif name == 'delete':
                    # NOTE reusing group.bytes_per_sec for tracking deleted / sec
                    # TODO in-depth subclassing of WorkQueue for appropriate attribute name
                    speed_str = f'{group.bytes_per_sec:.2f}/s'
                messages.append(f'{group.desc} {group.completed}/{group.total_count} - {speed_str}')
        if self.queue.dry_run:
            if compared_count == compare_total:
                status_str = 'DONE'
            else:
                status_str = f'{compared_count}/{compare_total}'
            message = f'Comparing source and destination - {status_str}'
        elif messages:
            message = ', '.join(messages)
        else:
            return
        sys.stdout.write(message.ljust(self.columns) + newline)
        sys.stdout.flush()

    def final_report(self):
        self.sample()
        self.report(newline='\n')

        create_count = update_count = 0
        for task in self.queue.completed:
            if isinstance(task, StoreTask) and task.event == 'store/create':
                create_count += 1
            elif isinstance(task, StoreTask) and task.event == 'store/update':
                update_count += 1
        delete_count = self.groups['delete'].completed
        skip_count = self.groups['store'].skipped
        cancel_count = (sum(group.total_count - group.completed for group in self.groups.values()))
        transfer_bytes = self.groups['store'].completed_bytes
        if transfer_bytes > 0:
            xfer_bytes = fs.filesize.traditional(transfer_bytes)
            xfer_files = create_count + update_count
            if self.queue.dry_run:
                xfer_msg = f'Would transfer {xfer_bytes} across {xfer_files} files'
            else:
                xfer_time = self.format_timedelta(datetime.datetime.now() - self._start_time)
                xfer_msg = f'Transferred {xfer_bytes} across {xfer_files} files in {xfer_time}'
            print(xfer_msg.ljust(self.columns))
        messages = []
        if create_count > 0:
            messages.append(f'create {create_count}')
        if update_count:
            messages.append(f'update {update_count}')
        if delete_count:
            messages.append(f'delete {delete_count}')
        if skip_count:
            messages.append(f'skip {skip_count}')
        if cancel_count:
            messages.append(f'cancel {cancel_count}')
        message = ', '.join(messages)
        print(f'Sync summary: {message}'.ljust(self.columns))

    @staticmethod
    def format_timedelta(timedelta):
        """Return human-readable str given a datetime.timedelta"""
        seconds = timedelta.total_seconds()
        if seconds < 60:
            return f'{seconds:.2f} seconds'
        return str(datetime.timedelta(seconds=int(seconds)))
