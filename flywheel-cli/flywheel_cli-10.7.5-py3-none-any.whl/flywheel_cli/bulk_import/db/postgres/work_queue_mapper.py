"""Provides WorkQueueMapper class."""

from ..mappers import AbstractWorkQueueMapper


class WorkQueueMapper(AbstractWorkQueueMapper):
    """Creating and contolling work queue items."""

    get_next_sql = (
        "UPDATE work_queue SET status='processing', actor_id=? WHERE item_id = "
        "(SELECT item_id FROM work_queue WHERE status='waiting' "
        "ORDER BY item_id LIMIT 1 FOR UPDATE SKIP LOCKED) "
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
