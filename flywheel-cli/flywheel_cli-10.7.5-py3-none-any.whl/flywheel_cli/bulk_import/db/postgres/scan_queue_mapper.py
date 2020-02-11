"""Provides ScanQueueMapper class."""

from ..mappers import AbstractScanQueueMapper


class ScanQueueMapper(AbstractScanQueueMapper):
    """Creating and contolling scan queue items."""

    get_next_sql = (
        "UPDATE scan_queue SET status='processing', actor_id=? WHERE task_id = "
        "(SELECT task_id FROM scan_queue WHERE status='waiting' "
        "ORDER BY task_id LIMIT 1 FOR UPDATE SKIP LOCKED) "
        "RETURNING *;"
    )

    def _get(self, actor_id):
        """Get the next item from the queue"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(self.get_next_sql, (actor_id,))

            try:
                row = next(cursor)
            except StopIteration:
                # No ready items
                row = None

            return self.deserialize(row)
