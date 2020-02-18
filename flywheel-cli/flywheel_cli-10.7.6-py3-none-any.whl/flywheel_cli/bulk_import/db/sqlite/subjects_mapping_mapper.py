"""Provides SubjectsMappingMapper class."""

from ..models import SubjectMap
from ..mappers import AbstractSubjectMappingMapper


class SubjectsMappingMapper(AbstractSubjectMappingMapper):
    """Sqlite specific implementation of AbstractSubjectMappingMapper class."""
    select_match_sql = "SELECT * FROM subjects_mapping WHERE ingest_id=? AND field_values=? ORDER BY subject_id DESC LIMIT 1"
    select_last_sql = "SELECT * FROM subjects_mapping WHERE ingest_id=? ORDER BY subject_id DESC LIMIT 1"

    def _get(self, ingest_id, field_values, format_code=None):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("BEGIN IMMEDIATE")
            cursor.execute(self.select_match_sql, (ingest_id, field_values))
            try:
                row = next(cursor)
                record = self.deserialize(row)
            except StopIteration:
                # No subject code for the given field values
                row = None

            if not row:
                cursor.execute(self.select_last_sql, (ingest_id,))
                try:
                    row = next(cursor)
                    result = self.deserialize(row)
                    last_id = result.subject_id
                except StopIteration:
                    last_id = 0
                insert_keys = list(self.columns.keys())
                insert_keys_str = ','.join(insert_keys)
                placeholders = ','.join(['?'] * len(insert_keys))
                command = 'INSERT INTO subjects_mapping({}) VALUES({})'.format(insert_keys_str, placeholders)
                record = SubjectMap(
                    ingest_id=ingest_id,
                    subject_id=last_id + 1,
                    subject_code=format_code(last_id) if format_code else last_id,
                    field_values=field_values,
                )
                params = [SubjectMap.map_field(key, getattr(record, key, None)) for key in insert_keys]
                cursor.execute(command, tuple(params))

            return record
