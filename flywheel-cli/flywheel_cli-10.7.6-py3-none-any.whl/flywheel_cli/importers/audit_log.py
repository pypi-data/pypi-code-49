"""Provides audit logging class"""
import csv
import logging
import os

log = logging.getLogger(__name__)

class AuditLog:
    """AuditLog class"""
    def __init__(self, audit_log_path):
        """Initialize audit logging"""
        self.headers = ['Source Path', 'Flywheel Path', 'Failed', 'Message']
        self.path = audit_log_path

        if self.path and not os.path.exists(self.path):
            with open(self.path, 'w') as log_file:
                csv_writer = csv.DictWriter(log_file, fieldnames=self.headers)
                csv_writer.writeheader()

    def log_root_dir(self, rootdir):
        """Log root dir"""
        if self.path:
            self._write_entry(src_path=rootdir, message='Begin import scan')

    def add_log(self, src_path, container, file_name, failed=False, message=None):
        """Add log message"""
        if self.path:
            resolver_path = self.get_container_resolver_path(container, file_name)
            self._write_entry(src_path=src_path, flywheel_path=resolver_path,
                              failed='true' if failed else 'false', message=message or '')

    def _write_entry(self, src_path='', flywheel_path='', failed='', message=''):
        with open(self.path, 'a') as log_file:
            csv_writer = csv.DictWriter(log_file, fieldnames=self.headers)
            csv_writer.writerow({
                'Source Path': src_path,
                'Flywheel Path': flywheel_path,
                'Failed': failed,
                'Message': message
            })

    def finalize(self, container_factory):
        """Upload audit log to target project"""
        if not self.path:
            return

        # Upload the audit log to the target project
        project = container_factory.get_first_project()
        if not project:
            log.info('No project found for import, skipping audit-log upload')
            return

        if not hasattr(container_factory.resolver, 'upload'):
            log.warning('Cannot upload audit-log -- no upload function available')
            return

        try:
            log_name = os.path.basename(self.path)
            with open(self.path, 'rb') as f:
                container_factory.resolver.upload(project, log_name, f)
        except Exception:  # pylint: disable=broad-except
            log.error('Error uploading audit-log', exc_info=True)
        else:
            print(f'{log_name} uploaded to the "{project.label}" project.')

    @staticmethod
    def get_container_resolver_path(container, file_name=None):
        """Utility function for getting container's resolver path"""
        path = []
        if container is None:
            return ''
        while container.container_type != 'root':
            if container.container_type == 'group':
                path = [container.id] + path
            else:
                path = [container.label] + path
            container = container.parent
        if file_name is not None:
            path += ['files', file_name]
        return '/'.join(path)
