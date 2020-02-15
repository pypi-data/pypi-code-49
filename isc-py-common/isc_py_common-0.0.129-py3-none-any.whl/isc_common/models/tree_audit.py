import logging

from django.db.models.query import RawQuerySet

from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditManager, AuditQuerySet

logger = logging.getLogger(__name__)


class TreeAuditModelQuerySet(AuditQuerySet):
    def _check(self, **kwargs):
        from kaf_pas.ckk.models.item import Item
        if isinstance(kwargs.get('parent'), Item):
            parent = kwargs.get('parent').id
        else:
            parent = kwargs.get('parent')

        if parent == None and isinstance(kwargs.get('parent_id'), int):
            parent = Item.objects.get(id=kwargs.get('parent_id'))

        if isinstance(kwargs.get('child'), Item):
            child = kwargs.get('child').id
        else:
            child = kwargs.get('child')

        if child == None and isinstance(kwargs.get('child_id'), int):
            child = Item.objects.get(id=kwargs.get('child_id'))

        if parent == child:
            raise Exception(f'Attempt to write circular reference id ({parent})')

    def create(self, **kwargs):
        self._check(**kwargs)
        return super().create(**kwargs)

    def update(self, **kwargs):
        self._check(**kwargs)
        return super().update(**kwargs)

    def get_or_create(self, defaults=None, **kwargs):
        self._check(**kwargs)
        return super().get_or_create(defaults, **kwargs)

    def update_or_create(self, defaults=None, **kwargs):
        self._check(**kwargs)
        return super().update_or_create(defaults, **kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)

    def get_descendants(self, id=None, start=None, end=None, child_id='child_id', parent_id='parent_id', child_parent_value=None, include_self=True, where_clause='', order_by_clause='', fields='*') -> RawQuerySet:
        db_name = self.model._meta.db_table

        if id != None:
            if isinstance(id, int):
                id = tuple([id])
            elif not isinstance(id, tuple):
                raise Exception(f'id must be list or int')

        if id != None:
            sql_text = f'''WITH RECURSIVE r AS (
                                SELECT *, 1 AS level
                                FROM {db_name}
                                WHERE {child_id if include_self else parent_id} IN %s
                                      {"and " + where_clause.replace("where", "") if where_clause else ""}  
    
                                union all
    
                                SELECT {db_name}.*, r.level + 1 AS level
                                FROM {db_name}
                                    JOIN r
                                ON {db_name}.{parent_id} = r.{child_id})
    
                            select {fields} from r {where_clause} {order_by_clause} limit %s offset %s
                        '''
            logger.debug(f'sql: {sql_text}')
            res = super().raw(sql_text, params=((id,), end, start))
        else:
            child_parent_value_str = f' = {child_parent_value}'
            sql_text = f'''WITH RECURSIVE r AS (
                                            SELECT *, 1 AS level
                                            FROM {db_name}
                                            WHERE {child_id if include_self else parent_id} {"IS NULL" if child_parent_value == None else child_parent_value_str}
                                                  {"and " + where_clause.replace("where", "") if where_clause else ""}  

                                            union all

                                            SELECT {db_name}.*, r.level + 1 AS level
                                            FROM {db_name}
                                                JOIN r
                                            ON {db_name}.{parent_id} = r.{child_id})

                                        select {fields} from r {where_clause} {order_by_clause} limit %s offset %s
                                    '''
            logger.debug(f'sql: {sql_text}')
            res = super().raw(sql_text, params=(end, start))

        return res

    def get_parents(self, id=None, start=None, end=None, child_id='child_id', parent_id='parent_id', include_self=True, where_clause='', order_by_clause='', fields='*') -> RawQuerySet:
        db_name = self.model._meta.db_table

        if isinstance(id, int):
            id = tuple([id])
        elif not isinstance(id, tuple):
            raise Exception(f'id must be list or int')

        sql = f'''WITH RECURSIVE r AS (
                            SELECT *, 1 AS level
                            FROM {db_name}
                            WHERE {parent_id if include_self else child_id} IN %s

                            union all

                            SELECT {db_name}.*, r.level + 1 AS level
                            FROM {db_name}
                                JOIN r
                            ON {db_name}.{child_id} = r.{parent_id})

                        select {fields} from r {where_clause} {order_by_clause} limit %s offset %s
                        '''

        logger.debug(f'sql: {sql}')
        res = super().raw(sql, params=((id,), end, start))

        return res

    def get_descendants_count(self, id='id', limit=None, offset=None, child_id='child_id', parent_id='parent_id', child_parent_value=None, include_self=True, where_clause='') -> int:
        return len(self.get_descendants(id=id, start=offset, end=limit, child_id=child_id, parent_id=parent_id, child_parent_value=child_parent_value, include_self=include_self, where_clause=where_clause))

    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class TreeAuditModelManager(AuditManager):
    def get_range_rows1(self, request, function=None, distinct_field_names=None):
        request = DSRequest(request=request)
        self.alive_only = request.alive_only
        self.enabledAll = request.enabledAll
        res = self.get_queryset().get_range_rows(start=request.startRow, end=request.endRow, function=function, distinct_field_names=distinct_field_names, json=request.json)
        return res

    def get_descendants(self, id=None, limit=None, offset=None, child_id='child_id', parent_id='parent_id', child_parent_value=None, include_self=True, where_clause='', order_by_clause='', fields='*') -> RawQuerySet:
        return self.get_queryset().get_descendants(id=id, start=offset, end=limit, child_id=child_id, parent_id=parent_id, child_parent_value=child_parent_value, include_self=include_self, where_clause=where_clause, order_by_clause=order_by_clause, fields=fields)

    def get_parents(self, id=None, limit=None, offset=None, child_id='child_id', parent_id='parent_id', include_self=True, where_clause='', order_by_clause='', fields='*') -> RawQuerySet:
        return self.get_queryset().get_parents(id=id, start=offset, end=limit, child_id=child_id, parent_id=parent_id, include_self=include_self, where_clause=where_clause, order_by_clause=order_by_clause, fields=fields)

    def get_descendants_count(self, id=None, limit=None, offset=None, child_id='child_id', parent_id='parent_id', child_parent_value=None, include_self=True, where_clause='') -> int:
        return self.get_queryset().get_descendants_count(id=id, limit=limit, offset=offset, child_id=child_id, parent_id=parent_id, child_parent_value=child_parent_value, include_self=include_self, where_clause=where_clause)

    def get_queryset(self):
        return TreeAuditModelQuerySet(self.model, using=self._db)
