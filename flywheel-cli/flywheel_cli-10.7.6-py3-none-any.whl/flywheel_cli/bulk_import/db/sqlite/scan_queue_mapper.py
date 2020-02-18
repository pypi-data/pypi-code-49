"""Provides ScanQueueMapper class."""

from ..models import TaskStatus
from ..mappers import AbstractScanQueueMapper


class ScanQueueMapper(AbstractScanQueueMapper):
    """Creating and contolling scan queue items."""

    select_next_sql = "SELECT * FROM scan_queue WHERE status='waiting' ORDER BY task_id LIMIT 1"
    update_next_sql = "UPDATE scan_queue SET status='processing', actor_id=? WHERE task_id=?"

    def _get(self, actor_id):
        """Get the next item from the queue"""
        # Exclusive write lock
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('BEGIN IMMEDIATE')
            cursor.execute(self.select_next_sql)
            try:
                row = next(cursor)
                # Update the selected item
                cursor.execute(self.update_next_sql, (actor_id, row[0]))
            except StopIteration:
                # No ready items
                row = None

            if row:
                # Update modified fields
                result = self.deserialize(row)
                result.actor_id = actor_id
                result.status = TaskStatus.processing
                return result

            return None
