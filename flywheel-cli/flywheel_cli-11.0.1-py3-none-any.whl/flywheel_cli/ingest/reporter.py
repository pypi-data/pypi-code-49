"""Ingest progress reporter"""
import datetime
import logging
import os
import stat
import sys
import threading
import time

import crayons
import fs
import tzlocal

from .. import util, config as root_config
from .schemas import IngestStatus
from .container_tree import ContainerTree

log = logging.getLogger(__name__)

END_STATUSES = [IngestStatus.finished, IngestStatus.failed, IngestStatus.aborted]


class TerminalSpinnerThread:
    """Thread for terminal spinner"""

    def __init__(self, message):
        self._running = False
        self._thread = None
        self._shutdown_event = threading.Event()
        self._fh = sys.stdout
        self.mode = os.fstat(sys.stdout.fileno()).st_mode
        self.message = message

    def start(self):
        """Start terminal spinner"""
        if not stat.S_ISREG(self.mode):
            log.debug("Starting terminal spinner reporter...")
            self._running = True
            self._thread = threading.Thread(target=self.run, name="terminal-spinner-thread")
            self._thread.daemon = True
            self._thread.start()

    def run(self):
        """Run terminal spinner"""
        spinner = ["[   ]", "[=  ]", "[== ]", "[===]", "[ ==]", "[  =]", "[   ]"]
        counter = 0
        while self._running:
            current_spin = str(crayons.magenta(spinner[counter]))
            message = str(crayons.blue(self.message, bold=True))
            self.print(current_spin + " " + message + "\r")
            counter = (counter + 1) % len(spinner)
            if counter == 0:
                spinner.reverse()
            self._shutdown_event.wait(0.2)

    def stop(self, message):
        """Stop terminal spinner"""
        if self._running:
            self._running = False
            self._shutdown_event.set()
            self._thread.join()
            sys.stdout.write("")
            formatted_msg = str(crayons.blue(message, bold=True))
            self.print(f"\033[K{formatted_msg}\n")

    def print(self, msg):
        """Print"""
        self._fh.write(msg)
        self._fh.flush()

class IngestFollower:
    """Follow the progress on an ingest operation"""

    def __init__(self, ingest_manager):
        self._fh = sys.stdout
        self.ingest_manager = ingest_manager
        self.mode = os.fstat(sys.stdout.fileno()).st_mode

    def run(self):
        """Report progress"""
        last_status_idx = -1
        ingest = None
        status = None
        while status not in END_STATUSES:
            ingest = self.ingest_manager.get_ingest()
            status = ingest.status
            status_idx = self.print_status_history(ingest.history, last_status_idx)
            if status_idx == last_status_idx:
                time.sleep(1)
            else:
                last_status_idx = status_idx

        self.print_final_report()
        log.debug("Ingest done, collecting logs...")
        self.save_log("audit")
        self.save_log("deid")
        self.save_subjects()

    def print_status_history(self, history, last=-1):
        """Print report of every status since previous status"""
        for idx, status in enumerate(history):
            if last >= idx:
                continue
            last = idx
            st_name, timestamp = status
            timestamp = datetime.datetime.fromtimestamp(timestamp, tz=tzlocal.get_localzone())
            self.print_status_header(st_name, timestamp)
            follow_method = getattr(self, f"follow_{st_name}_status", None)
            if follow_method:
                follow_method()
            self.print("")  # start new line
        return last

    def follow_scanning_status(self):
        """Follow scanning status"""
        status = self.ingest_manager.get_ingest().status
        while status == IngestStatus.scanning:
            self.print_scan_progress()
            status = self.ingest_manager.get_ingest().status
            time.sleep(1)
        self.print_scan_progress()
        self.print("")  # start new line

    def print_scan_progress(self):
        """Print scan progress"""
        progress = self.ingest_manager.get_ingest_progress()
        size = fs.filesize.traditional(progress.bytes.total)
        file_str = "files" if progress.files.total > 1 else "file"
        finished_scan = progress.scans.finished
        total_scan = progress.scans.total
        msg = f"{finished_scan} / {total_scan}, {progress.files.total} {file_str}, {size}"
        self.print(msg, replace=True)

    def follow_resolving_status(self):
        """Show resolve progress"""
        spinner = TerminalSpinnerThread("Resolving containers")
        spinner.start()
        status = self.ingest_manager.get_ingest().status
        while status == IngestStatus.resolving:
            time.sleep(1)
            status = self.ingest_manager.get_ingest().status
        spinner.stop("Resolved containers")

    def follow_in_review_status(self):
        """Print summary report of review stage"""
        if self.ingest_manager.config.verbose:
            self.print("Hierarchy sample:\n")
            container_factory = ContainerTree()
            for container in self.ingest_manager.get_ingest_tree():
                container_factory.add_node(
                    container.id,
                    container.parent_id,
                    container.level,
                    src_context=container.src_context,
                    dst_context=container.dst_context,
                    bytes_sum=container.bytes_sum,
                    files_cnt=container.files_cnt,
                )
            container_factory.print_tree()

        self.print("Summary:")
        summary = self.ingest_manager.get_ingest_summary().dict()
        for k, v in summary.items():
            self.print(f"  {k.capitalize()}: {v}")

        status = self.ingest_manager.get_ingest().status
        if status != IngestStatus.in_review:
            # do not prompt if status is not in_review
            return
        if self.ingest_manager.config.assume_yes or util.confirmation_prompt("Confirm upload?"):
            self.ingest_manager.review_ingest()
        else:
            self.ingest_manager.abort_ingest()

    def follow_preparing_status(self):
        """Show preparing progress"""
        spinner = TerminalSpinnerThread("Preparing for ingest")
        spinner.start()
        status = self.ingest_manager.get_ingest().status
        while status == IngestStatus.preparing:
            time.sleep(1)
            status = self.ingest_manager.get_ingest().status
        spinner.stop("Preparing complete")

    def follow_uploading_status(self):
        """Print report of uploading stage"""
        ingest = self.ingest_manager.get_ingest()
        prev_eta = {}
        while ingest.status == IngestStatus.uploading:
            progress = self.ingest_manager.get_ingest_progress()
            self.print_upload_progress(progress, ingest, prev_eta)
            time.sleep(1)
            ingest = self.ingest_manager.get_ingest()

        progress = self.ingest_manager.get_ingest_progress()
        ingest = self.ingest_manager.get_ingest()
        self.print_upload_progress(progress, ingest, prev_eta)
        self.print("")  # start a new line
        self.print_upload_summary(progress)

    def print_upload_progress(self, progress, ingest, prev_eta):
        """Print upload progress"""
        finished = progress.items.finished + progress.items.skipped
        failed = progress.items.failed
        total = progress.items.total
        eta = self.compute_eta(ingest, progress.items, prev_eta)
        if eta:
            eta = str(eta["eta"]).split(".")[0]
        else:
            eta = "~"
        msg = f"{finished} / {total} ({failed} failed), ETA: {eta}"
        self.print(msg, replace=True)

    def print_upload_summary(self, progress):
        """Print upload summary"""
        exclude = ["finished"]
        for status, count in progress.items.dict().items():
            if count > 0 and status not in exclude:
                self.print(f"{status.capitalize()}: {count}")

    def print_final_report(self):
        """Print final report of the ingest"""
        self.print(str(crayons.magenta("Final report", bold=True)))
        report = self.ingest_manager.get_ingest_report()
        if report.errors:
            self.print("The following errors happend:")
            for error in report.errors:
                self.print(f"{error.type}: {error.message}")

        for status, elapsed in report.elapsed.items():
            elapsed = str(datetime.timedelta(seconds=elapsed))
            cap_status = status.replace('_', ' ').capitalize()
            self.print(f"{cap_status} took: {elapsed}")

        total_elapsed = 0
        for st_elapsed in report.elapsed.values():
            total_elapsed += st_elapsed

        elapsed = str(datetime.timedelta(seconds=total_elapsed))
        self.print(f"Total elapsed time: {elapsed}")

    def print(self, msg, replace=False):
        """Print"""
        if replace:
            msg = f"\r{msg}\033[K"
        else:
            msg = f"{msg}\n"
        self._fh.write(msg)
        self._fh.flush()

    def print_status_header(self, status, timestamp):
        """Print status header"""
        status_name = status.replace("_", " ").capitalize().ljust(15)
        status_name = str(crayons.magenta(status_name, bold=True))
        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        self.print(f"{status_name}[{timestamp}]")

    def save_log(self, log_type):
        """Save audit log if it was requested."""
        path = getattr(self.ingest_manager.config, f"save_{log_type}_log")
        if path:
            log_fn = getattr(self.ingest_manager, f"get_{log_type}_logs")
            final_path = self.save_stream_to_file(
                log_fn(),
                path,
                f"{log_type}_log"
            )
            self.print(f"Saved {log_type} log to {final_path}")

    def save_subjects(self):
        """Save subjects to a file"""
        path = self.ingest_manager.config.save_subjects
        if path:
            final_path = self.save_stream_to_file(
                self.ingest_manager.get_subjects_csv(),
                path,
                "subjects"
            )
            self.print(f"Saved subjects to {final_path}")

    @staticmethod
    def save_stream_to_file(stream, path, prefix, extension="csv"):
        """Save stream to file"""
        error = None
        try:
            path = util.get_filepath(path, prefix=prefix, extension=extension)
        except FileNotFoundError as exc:
            error = str(exc)
            path = util.get_filepath(root_config.LOG_FILE_DIRPATH, prefix=prefix)
        except FileExistsError as exc:
            error = f"File already exists: {path}"
            path = util.get_incremental_filename(path)

        with open(path, "w") as fp:
            for line in stream:
                fp.write(line)

        if error:
            msg = f"{error}. Fallback to: {path}"
            log.error(msg)

        return path

    @classmethod
    def compute_eta(cls, ingest, item_stats, prev_eta):
        """Compute ETA"""
        if item_stats.finished == 0:
            return None
        if prev_eta and item_stats.finished == prev_eta["finished"]:
            report_time = datetime.datetime.utcnow()
            new_eta = prev_eta["eta"] - (report_time - prev_eta["report_time"])
            prev_eta["eta"] = max(new_eta, datetime.timedelta(0))
            prev_eta["report_time"] = report_time
        else:
            upload_started = cls.get_upload_start_time(ingest.history)
            report_time = datetime.datetime.utcnow()
            elapsed_time = report_time - upload_started
            remaining_time = (elapsed_time / item_stats.finished) * (item_stats.pending + item_stats.running)
            prev_eta.update({
                "eta": remaining_time,
                "report_time": report_time,
                "pending": item_stats.pending,
                "finished": item_stats.finished,
            })
        return prev_eta

    @staticmethod
    def get_upload_start_time(status_history):
        """Return when upload started"""
        for st_name, timestamp in status_history:
            if st_name == IngestStatus.uploading:
                return datetime.datetime.utcfromtimestamp(timestamp)
        return None
