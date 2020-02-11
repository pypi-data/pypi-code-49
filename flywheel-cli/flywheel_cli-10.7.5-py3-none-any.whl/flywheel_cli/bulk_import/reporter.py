"""Progress reporter for bulk import"""
import json
import logging
import os
import stat
import sys
import threading
from datetime import datetime

import crayons

from ..util import create_packfile_name, print_tree

log = logging.getLogger(__name__)

HIERARCHY = ["project", "subject", "session", "acquisition"]


class TerminalSpinnerThread:
    """Thread for terminal spinner"""

    def __init__(self, message):
        self._running = False
        self._thread = None
        self._shutdown_event = threading.Event()
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
        sys.stdout.write("\n\n")
        sys.stdout.flush()
        counter = 0
        while self._running:
            current_spin = str(crayons.magenta(spinner[counter]))
            message = str(crayons.blue(self.message, bold=True))
            sys.stdout.write(current_spin + " " + message + "\r")
            sys.stdout.flush()
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
            sys.stdout.write("\033[K")
            sys.stdout.write(str(crayons.blue(message, bold=True)) + "\n\n")
            sys.stdout.flush()


class BulkImportProgressReporter:
    """Thread that prints bulk import progress"""

    def __init__(self, context):
        self._suspended = False
        self._running = False
        self._thread = None
        self._shutdown_event = threading.Event()
        self._start_time = datetime.now()
        self.report_time = 1
        self.columns = 80

        self.context = context
        self.before_review = True
        self.mode = os.fstat(sys.stdout.fileno()).st_mode

    def start(self):
        """Starts progress report thread"""
        if not stat.S_ISREG(self.mode):
            log.debug("Starting progress reporter...")
            self._running = True
            self._suspended = False
            self._thread = threading.Thread(target=self.run, name="progress-report-thread")
            self._thread.daemon = True
            self._thread.start()

    def suspend(self):
        """Suspend progress report thread"""
        self._suspended = True

    def resume(self):
        """Resume suspended progress report thread"""
        if not self._running:
            self.start()
        self._suspended = False

    def shutdown(self):
        """Shut down progress report thread"""
        if self._running:
            self._running = False
            self._shutdown_event.set()
            self._thread.join()

    def run(self):
        """Report progress"""
        sys.stdout.write(f"Current import's Ingest ID: {self.context.current_ingest.ingest_id}\n")
        sys.stdout.flush()
        while self._running:
            if not self._suspended:
                if self.before_review:
                    self.report_before_review_stage()
                else:
                    self.report_after_review_stage()

    def report_before_review_stage(self):
        """Print report of scan stage"""
        headers = ["Folders", "Groups", "Projects", "Subjects", "Sessions", "Acquisitions"]
        self.print_headers(headers, stage="Scanning")
        while True:

            if not self.before_review:
                return

            if not self._running:
                return

            if not self._suspended:
                messages = []
                folder_count = self.context.items_mapper.get_unique_count_of_ingest("subdir", self.context.current_ingest.ingest_id)[0]
                messages.append(folder_count)
                messages.extend(self.container_status().values())

                message = self.format_table(messages, headers)

                sys.stdout.write(message)
                sys.stdout.flush()
            self._shutdown_event.wait(self.report_time)

    def report_after_review_stage(self):
        """Print report of process stage"""
        headers = ["Items", "Completed", "Failed", "Processing", "Waiting", "Time Remaining"]
        self.write_newline()
        self.print_headers(headers, stage="Processing")
        while True:
            if not self._running:
                return

            if not self._suspended:
                messages = []
                messages.append(self.context.items_mapper.get_count_of_ingest("item_id", self.context.current_ingest.ingest_id)[0])
                for value in self.process_status().values():
                    messages.append(value)
                messages.append(self.compute_eta())

                message = self.format_table(messages, headers)

                sys.stdout.write(message)
                sys.stdout.flush()
            self._shutdown_event.wait(self.report_time)

    def report_review_summary(self, container_factory):
        """Print summary report of review stage"""
        messages = []
        messages.extend(["Review Summary\n", "\n"])
        summary = {"groups": 0,
                   "projects": 0,
                   "subjects": 0,
                   "sessions": 0,
                   "acquisitions": 0,
                   "warnings": 0,
                   "errors": 0}

        containers = self.container_status()
        for key, value in containers.items():
            summary[key + "s"] = value

        summary["errors"] = self.context.items_mapper.get_count_of_ingest("errors", self.context.current_ingest.ingest_id)[0]
        summary["warnings"] = self.context.items_mapper.get_count_of_ingest("warnings", self.context.current_ingest.ingest_id)[0]

        for key, value in summary.items():
            messages.append(f"{key.capitalize()}: {value}\n")
        message = "".join(messages)
        sys.stdout.write(message + "\n")
        sys.stdout.flush()

        if self.context.config.verbose:
            self.hierarchy_printer(container_factory, verbose=True)

    def report_process_summary(self):
        """Print summary report of process stage"""
        messages = []
        if not stat.S_ISREG(self.mode):
            messages.extend(["\n", "\n"])
        messages.extend(["Process Summary\n", "\n"])

        summary = {"items": 0,
                   "completed": 0,
                   "failed": 0,
                   "time_taken": 0}
        ingest_operation = self.context.ingest_mapper.find(self.context.current_ingest.ingest_id)
        summary["items"] = self.context.items_mapper.get_count_of_ingest("item_id", self.context.current_ingest.ingest_id)[0]
        process_status = self.process_status()
        summary["completed"] = process_status["complete"]
        summary["failed"] = process_status["failed"]
        summary["time_taken"] = str(ingest_operation.processing_end - ingest_operation.processing_start).split(".")[0]

        for key, value in summary.items():
            messages.append(f"{key.replace('_', ' ').capitalize()}: {value}\n")
        message = "".join(messages)
        sys.stdout.write(message)
        sys.stdout.flush()

    def container_status(self):
        """Return the count of unique containers in contexts"""
        contexts = self.context.items_mapper.get_column_of_ingest("context", self.context.current_ingest.ingest_id)
        container_count = {"group": 0,
                           "project": 0,
                           "subject": 0,
                           "session": 0,
                           "acquisition":0}
        for key in container_count:
            if key == "group":
                key_set = {json.loads(context[0]).get(key, {}).get("_id") for context in contexts}
            else:
                key_set = {json.loads(context[0]).get(key, {}).get("label") for context in contexts}
            if None in key_set:
                key_set.remove(None)
            container_count[key] = len(key_set)

        return container_count

    def process_status(self):
        """Get information about item processing"""
        status_counter = {"complete": 0,
                          "failed": 0,
                          "processing": 0,
                          "waiting": 0}
        count_by_status = self.context.work_queue_mapper.get_count_by_status_of_ingest(self.context.current_ingest.ingest_id)
        status_counter.update(dict(count_by_status))

        return status_counter

    def hierarchy_printer(self, container_factory, verbose=False, fh=sys.stdout):
        """After converting files, prints hierarchy from ingested items"""
        spinner = TerminalSpinnerThread("Creating hierarchy")
        spinner.start()

        converted_files = []
        ingest_items = self.context.items_mapper.get_all_item_for_ingest(self.context.current_ingest.ingest_id)

        for item in ingest_items:
            group = item.context.get("group").get("_id", "")
            parts = [item.context[lvl]["label"] for lvl in HIERARCHY if lvl in item.context]
            container_node = container_factory.resolve(item.context)
            if item.item_type == "packfile":
                parts.append(create_packfile_name(item.context, container_node))
            else:
                parts.append(item.files[0])
            while container_node.container_type != "root":
                item.context[container_node.container_type]["status"] = "using" if container_node.exists else "creating"
                container_node = container_node.parent
            item.name = "/".join(parts)
            converted_files.append(item)

        spinner.stop("Created hierarchy")

        print_tree(converted_files, group, verbose=verbose, fh=fh)

    def compute_eta(self):
        """Compute ETA"""
        completed_size_sum = self.context.items_mapper.get_sum_of_completed_sizes(self.context.current_ingest.ingest_id)[0] or 0
        start_time = self.context.ingest_mapper.find(self.context.current_ingest.ingest_id).processing_start
        if completed_size_sum == 0:
            return []
        size_sum = self.context.items_mapper.get_sum_of_sizes(self.context.current_ingest.ingest_id)[0]
        elapsed_time = datetime.now() - start_time
        remaining_time = (elapsed_time *  (size_sum / completed_size_sum)) - elapsed_time
        remaining_time = str(remaining_time).split(".")[0]
        return remaining_time

    def is_running(self):
        """Reporter is running or not"""
        return self._running

    @staticmethod
    def format_table(messages, headers, space_between=2):
        """Format table from messages and headers"""
        formatted_table = "\r"
        for i, message in enumerate(messages):
            space_between = 0 if i == (len(headers) - 1) else space_between
            message = str(message)
            formatted_table += (len(headers[i]) - len(message)) * " " + message + " " * space_between
        return formatted_table

    @staticmethod
    def print_headers(headers, stage=None, space_between=2):
        """Prints the given headers"""
        if stage:
            sys.stdout.write(str(crayons.magenta(stage + "\n", bold=True)))
        message = (" " * space_between).join(headers) + "\n"
        sys.stdout.write(str(crayons.blue(message, bold=True)))
        sys.stdout.flush()

    @staticmethod
    def write_newline():
        """Print newline"""
        sys.stdout.write("\n")
        sys.stdout.flush()
