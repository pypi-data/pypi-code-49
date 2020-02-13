"""
Task Objects
"""
from pathlib import Path
from disco.core.utils import shorten_string


class TaskResult:
    """
    Task Result
    """
    def __init__(self, task_id, raw_result):
        self.task_id = task_id
        self.raw_result = raw_result

    @property
    def stdout(self):
        """The standard output produced by the script."""
        for file_name, content in self.raw_result:
            if file_name.startswith('IqoqoTask.stdout.'):
                return content.strip()

        return None

    def __repr__(self):
        return f"<{type(self).__name__}: " \
            f"job={self.task_id} " \
            f"stdout={shorten_string(self.stdout)}"

    def write_files(self, path):
        """Write all the files created by the job to the local filesystem.

        Args:
            path (str): The path to write the files in.
        """
        path = Path(str(path))
        if path.exists():
            assert path.is_dir()
        for relative_file_path, content in self.raw_result:
            absolute_file_path = path / relative_file_path
            if relative_file_path[-1] == '/':
                absolute_file_path.mkdir(parents=True)
            else:
                absolute_file_path.write_bytes(content)

    def get_raw_result(self):
        """Returns the raw result (file->binary data) of a task"""
        return self.raw_result
