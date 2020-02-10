import types
from copy import copy
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncIterator,
    Callable,
    Dict,
    Generator,
    Generic,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
)

from pypika import JoinType, Order, Table
from pypika.functions import Count
from pypika.queries import QueryBuilder
from typing_extensions import Protocol

from tortoise.backends.base.client import BaseDBAsyncClient, Capabilities
from tortoise.exceptions import DoesNotExist, FieldError, IntegrityError, MultipleObjectsReturned
from tortoise.fields.relational import (
    ForeignKeyFieldInstance,
    OneToOneFieldInstance,
    RelationalField,
)
from tortoise.functions import Function
from tortoise.query_utils import Prefetch, Q, QueryModifier, _get_joins_for_related_field

# Empty placeholder - Should never be edited.
QUERY: QueryBuilder = QueryBuilder()

if TYPE_CHECKING:  # pragma: nocoverage
    from tortoise.models import Model

MODEL = TypeVar("MODEL", bound="Model")
T_co = TypeVar("T_co", covariant=True)


class QuerySetSingle(Protocol[T_co]):
    """
    Awaiting on this will resolve a single instance of the Model object, and not a sequence.
    """

    # pylint: disable=W0104
    def __await__(self) -> Generator[Any, None, T_co]:
        ...  # pragma: nocoverage


class AwaitableQuery(Generic[MODEL]):
    __slots__ = ("_joined_tables", "query", "model", "_db", "capabilities")

    def __init__(self, model: Type[MODEL]) -> None:
        self._joined_tables: List[Table] = []
        self.model: "Type[Model]" = model
        self.query: QueryBuilder = QUERY
        self._db: BaseDBAsyncClient = None  # type: ignore
        self.capabilities: Capabilities = model._meta.db.capabilities

    def resolve_filters(
        self,
        model: "Type[Model]",
        q_objects: List[Q],
        annotations: Dict[str, Any],
        custom_filters: Dict[str, Dict[str, Any]],
    ) -> None:
        """
        Builds the common filters for a QuerySet.

        :param model: The Model this querysit is based on.
        :param q_objects: The Q expressions to apply.
        :param annotations: Extra annotations to add.
        :param custom_filters:
        """
        modifier = QueryModifier()
        for node in q_objects:
            modifier &= node.resolve(model, annotations, custom_filters, model._meta.basetable)

        where_criterion, joins, having_criterion = modifier.get_query_modifiers()
        for join in joins:
            if join[0] not in self._joined_tables:
                self.query = self.query.join(join[0], how=JoinType.left_outer).on(join[1])
                self._joined_tables.append(join[0])

        self.query._wheres = where_criterion
        self.query._havings = having_criterion

    def _join_table_by_field(
        self, table: Table, related_field_name: str, related_field: RelationalField
    ) -> Table:
        joins = _get_joins_for_related_field(table, related_field, related_field_name)
        for join in joins:
            if join[0] not in self._joined_tables:
                self.query = self.query.join(join[0], how=JoinType.left_outer).on(join[1])
                self._joined_tables.append(join[0])
        return joins[-1][0]

    def resolve_ordering(
        self,
        model: "Type[Model]",
        table: Table,
        orderings: List[Tuple[str, str]],
        annotations: Dict[str, Any],
    ) -> None:
        """
        Applies standard ordering to QuerySet.

        :param model: The Model this querysit is based on.
        :param table: ``pypika.Table`` to keep track of the virtual SQL table
            (to allow self referential joins)
        :param orderings: What columns/order to order by
        :param annotations:  Annotations that may be ordered on
        """
        for ordering in orderings:
            field_name = ordering[0]
            if field_name in model._meta.fetch_fields:
                raise FieldError(
                    "Filtering by relation is not possible. Filter by nested field of related model"
                )
            if field_name.split("__")[0] in model._meta.fetch_fields:
                related_field_name = field_name.split("__")[0]
                related_field = cast(RelationalField, model._meta.fields_map[related_field_name])
                related_table = self._join_table_by_field(table, related_field_name, related_field)
                self.resolve_ordering(
                    related_field.model_class,
                    related_table,
                    [("__".join(field_name.split("__")[1:]), ordering[1])],
                    {},
                )
            elif field_name in annotations:
                annotation = annotations[field_name]
                annotation_info = annotation.resolve(self.model, table)
                self.query = self.query.orderby(annotation_info["field"], order=ordering[1])
            else:
                field_object = self.model._meta.fields_map.get(field_name)
                if not field_object:
                    raise FieldError(f"Unknown field {field_name} for model {self.model.__name__}")
                field_name = field_object.source_field or field_name
                field = getattr(table, field_name)

                func = field_object.get_for_dialect(
                    model._meta.db.capabilities.dialect, "function_cast"
                )
                if func:
                    field = func(field_object, field)

                self.query = self.query.orderby(field, order=ordering[1])

    def _make_query(self) -> None:
        raise NotImplementedError()  # pragma: nocoverage

    async def _execute(self) -> Any:
        raise NotImplementedError()  # pragma: nocoverage


class QuerySet(AwaitableQuery[MODEL]):
    __slots__ = (
        "fields",
        "_prefetch_map",
        "_prefetch_queries",
        "_single",
        "_get",
        "_count",
        "_db",
        "_limit",
        "_offset",
        "_filter_kwargs",
        "_orderings",
        "_q_objects",
        "_distinct",
        "_annotations",
        "_having",
        "_custom_filters",
    )

    def __init__(self, model: Type[MODEL]) -> None:
        super().__init__(model)
        self.fields: Set[str] = model._meta.db_fields

        self._prefetch_map: Dict[str, Set[Union[str, Prefetch]]] = {}
        self._prefetch_queries: Dict[str, QuerySet] = {}
        self._single: bool = False
        self._get: bool = False
        self._count: bool = False
        self._limit: Optional[int] = None
        self._offset: Optional[int] = None
        self._filter_kwargs: Dict[str, Any] = {}
        self._orderings: List[Tuple[str, Any]] = []
        self._q_objects: List[Q] = []
        self._distinct: bool = False
        self._annotations: Dict[str, Function] = {}
        self._having: Dict[str, Any] = {}
        self._custom_filters: Dict[str, dict] = {}

    def _clone(self) -> "QuerySet[MODEL]":
        queryset = QuerySet.__new__(QuerySet)
        queryset.fields = self.fields
        queryset.model = self.model
        queryset.query = self.query
        queryset.capabilities = self.capabilities
        queryset._prefetch_map = copy(self._prefetch_map)
        queryset._prefetch_queries = copy(self._prefetch_queries)
        queryset._single = self._single
        queryset._get = self._get
        queryset._count = self._count
        queryset._db = self._db
        queryset._limit = self._limit
        queryset._offset = self._offset
        queryset._filter_kwargs = copy(self._filter_kwargs)
        queryset._orderings = copy(self._orderings)
        queryset._joined_tables = copy(self._joined_tables)
        queryset._q_objects = copy(self._q_objects)
        queryset._distinct = self._distinct
        queryset._annotations = copy(self._annotations)
        queryset._having = copy(self._having)
        queryset._custom_filters = copy(self._custom_filters)
        return queryset

    def _filter_or_exclude(self, *args: Q, negate: bool, **kwargs: Any) -> "QuerySet[MODEL]":
        queryset = self._clone()
        for arg in args:
            if not isinstance(arg, Q):
                raise TypeError("expected Q objects as args")
            if negate:
                queryset._q_objects.append(~arg)
            else:
                queryset._q_objects.append(arg)

        for key, value in kwargs.items():
            if negate:
                queryset._q_objects.append(~Q(**{key: value}))
            else:
                queryset._q_objects.append(Q(**{key: value}))

        return queryset

    def filter(self, *args: Q, **kwargs: Any) -> "QuerySet[MODEL]":
        """
        Filters QuerySet by given kwargs. You can filter by related objects like this:

        .. code-block:: python3

            Team.filter(events__tournament__name='Test')

        You can also pass Q objects to filters as args.
        """
        return self._filter_or_exclude(negate=False, *args, **kwargs)

    def exclude(self, *args: Q, **kwargs: Any) -> "QuerySet[MODEL]":
        """
        Same as .filter(), but with appends all args with NOT
        """
        return self._filter_or_exclude(negate=True, *args, **kwargs)

    def order_by(self, *orderings: str) -> "QuerySet[MODEL]":
        """
        Accept args to filter by in format like this:

        .. code-block:: python3

            .order_by('name', '-tournament__name')

        Supports ordering by related models too.
        """
        queryset = self._clone()
        new_ordering = []
        for ordering in orderings:
            order_type = Order.asc
            if ordering[0] == "-":
                field_name = ordering[1:]
                order_type = Order.desc
            else:
                field_name = ordering

            if not (
                field_name.split("__")[0] in self.model._meta.fields
                or field_name in self._annotations
            ):
                raise FieldError(f"Unknown field {field_name} for model {self.model.__name__}")
            new_ordering.append((field_name, order_type))
        queryset._orderings = new_ordering
        return queryset

    def limit(self, limit: int) -> "QuerySet[MODEL]":
        """
        Limits QuerySet to given length.
        """
        queryset = self._clone()
        queryset._limit = limit
        return queryset

    def offset(self, offset: int) -> "QuerySet[MODEL]":
        """
        Query offset for QuerySet.
        """
        queryset = self._clone()
        queryset._offset = offset
        if self.capabilities.requires_limit and queryset._limit is None:
            queryset._limit = 1000000
        return queryset

    def distinct(self) -> "QuerySet[MODEL]":
        """
        Make QuerySet distinct.

        Only makes sense in combination with a ``.values()`` or ``.values_list()`` as it
        precedes all the fetched fields with a distinct.
        """
        queryset = self._clone()
        queryset._distinct = True
        return queryset

    def annotate(self, **kwargs: Function) -> "QuerySet[MODEL]":
        """
        Annotate result with aggregation or function result.
        """
        queryset = self._clone()
        for key, annotation in kwargs.items():
            if not isinstance(annotation, Function):
                raise TypeError("value is expected to be Function instance")
            queryset._annotations[key] = annotation
            from tortoise.models import get_filters_for_field

            queryset._custom_filters.update(get_filters_for_field(key, None, key))
        return queryset

    def values_list(self, *fields_: str, flat: bool = False) -> "ValuesListQuery":
        """
        Make QuerySet returns list of tuples for given args instead of objects.

        If ```flat=True`` and only one arg is passed can return flat list.

        If no arguments are passed it will default to a tuple containing all fields
        in order of declaration.
        """
        return ValuesListQuery(
            db=self._db,
            model=self.model,
            q_objects=self._q_objects,
            flat=flat,
            fields_for_select_list=fields_  # type: ignore
            or [
                field
                for field in self.model._meta.fields_map.keys()
                if field in self.model._meta.db_fields
            ],
            distinct=self._distinct,
            limit=self._limit,
            offset=self._offset,
            orderings=self._orderings,
            annotations=self._annotations,
            custom_filters=self._custom_filters,
        )

    def values(self, *args: str, **kwargs: str) -> "ValuesQuery":
        """
        Make QuerySet return dicts instead of objects.

        Can pass names of fields to fetch, or as a ``field_name='name_in_dict'`` kwarg.

        If no arguments are passed it will default to a dict containing all fields.
        """
        if args or kwargs:
            fields_for_select: Dict[str, str] = {}
            for field in args:
                if field in fields_for_select:
                    raise FieldError(f"Duplicate key {field}")
                fields_for_select[field] = field

            for return_as, field in kwargs.items():
                if return_as in fields_for_select:
                    raise FieldError(f"Duplicate key {return_as}")
                fields_for_select[return_as] = field
        else:
            fields_for_select = {
                field: field
                for field in self.model._meta.fields_map.keys()
                if field in self.model._meta.db_fields
            }

        return ValuesQuery(
            db=self._db,
            model=self.model,
            q_objects=self._q_objects,
            fields_for_select=fields_for_select,
            distinct=self._distinct,
            limit=self._limit,
            offset=self._offset,
            orderings=self._orderings,
            annotations=self._annotations,
            custom_filters=self._custom_filters,
        )

    def delete(self) -> "DeleteQuery":
        """
        Delete all objects in QuerySet.
        """
        return DeleteQuery(
            db=self._db,
            model=self.model,
            q_objects=self._q_objects,
            annotations=self._annotations,
            custom_filters=self._custom_filters,
        )

    def update(self, **kwargs: Any) -> "UpdateQuery":
        """
        Update all objects in QuerySet with given kwargs.

        A usage example:

        .. code-block:: py3

            await Employee.filter(occupation='developer').update(salary=5000)

        Will instead of returning a resultset, update the data in the DB itself.
        """
        return UpdateQuery(
            db=self._db,
            model=self.model,
            update_kwargs=kwargs,
            q_objects=self._q_objects,
            annotations=self._annotations,
            custom_filters=self._custom_filters,
        )

    def count(self) -> "CountQuery":
        """
        Return count of objects in queryset instead of objects.
        """
        return CountQuery(
            db=self._db,
            model=self.model,
            q_objects=self._q_objects,
            annotations=self._annotations,
            custom_filters=self._custom_filters,
            limit=self._limit,
            offset=self._offset,
        )

    def all(self) -> "QuerySet[MODEL]":
        """
        Return the whole QuerySet.
        Essentially a no-op except as the only operation.
        """
        return self._clone()

    def first(self) -> QuerySetSingle[Optional[MODEL]]:
        """
        Limit queryset to one object and return one object instead of list.
        """
        queryset = self._clone()
        queryset._limit = 1
        queryset._single = True
        return queryset  # type: ignore

    def get(self, *args: Q, **kwargs: Any) -> QuerySetSingle[MODEL]:
        """
        Fetch exactly one object matching the parameters.
        """
        queryset = self.filter(*args, **kwargs)
        queryset._limit = 2
        queryset._get = True
        return queryset  # type: ignore

    def get_or_none(self, *args: Q, **kwargs: Any) -> QuerySetSingle[MODEL]:
        """
        Fetch exactly one object matching the parameters.
        """
        queryset = self.filter(*args, **kwargs)
        queryset._limit = 1
        queryset._single = True
        return queryset  # type: ignore

    def prefetch_related(self, *args: Union[str, Prefetch]) -> "QuerySet[MODEL]":
        """
        Like ``.fetch_related()`` on instance, but works on all objects in QuerySet.
        """
        queryset = self._clone()
        queryset._prefetch_map = {}

        for relation in args:
            if isinstance(relation, Prefetch):
                relation.resolve_for_queryset(queryset)
                continue
            relation_split = relation.split("__")
            first_level_field = relation_split[0]
            if first_level_field not in self.model._meta.fetch_fields:
                if first_level_field in self.model._meta.fields:
                    raise FieldError(
                        f"Field {first_level_field} on {self.model._meta.table} is not a relation"
                    )
                raise FieldError(
                    f"Relation {first_level_field} for {self.model._meta.table} not found"
                )
            if first_level_field not in queryset._prefetch_map.keys():
                queryset._prefetch_map[first_level_field] = set()
            forwarded_prefetch = "__".join(relation_split[1:])
            if forwarded_prefetch:
                queryset._prefetch_map[first_level_field].add(forwarded_prefetch)
        return queryset

    async def explain(self) -> Any:
        """Fetch and return information about the query execution plan.

        This is done by executing an ``EXPLAIN`` query whose exact prefix depends
        on the database backend, as documented below.

        - PostgreSQL: ``EXPLAIN (FORMAT JSON, VERBOSE) ...``
        - SQLite: ``EXPLAIN QUERY PLAN ...``
        - MySQL: ``EXPLAIN FORMAT=JSON ...``

        .. note::
            This is only meant to be used in an interactive environment for debugging
            and query optimization.
            **The output format may (and will) vary greatly depending on the database backend.**
        """
        if self._db is None:
            self._db = self.model._meta.db  # type: ignore
        self._make_query()
        return await self._db.executor_class(model=self.model, db=self._db).execute_explain(
            self.query
        )

    def using_db(self, _db: BaseDBAsyncClient) -> "QuerySet[MODEL]":
        """
        Executes query in provided db client.
        Useful for transactions workaround.
        """
        queryset = self._clone()
        queryset._db = _db
        return queryset

    def _resolve_annotate(self) -> None:
        if not self._annotations:
            return
        table = self.model._meta.basetable
        if any(
            annotation.resolve(self.model, table)["field"].is_aggregate
            for annotation in self._annotations.values()
        ):
            self.query = self.query.groupby(table.id)
        for key, annotation in self._annotations.items():
            annotation_info = annotation.resolve(self.model, table)
            for join in annotation_info["joins"]:
                table = self._join_table_by_field(*join)
            self.query._select_other(annotation_info["field"].as_(key))

    def _make_query(self) -> None:
        self.query = copy(self.model._meta.basequery_all_fields)
        self._resolve_annotate()
        self.resolve_filters(
            model=self.model,
            q_objects=self._q_objects,
            annotations=self._annotations,
            custom_filters=self._custom_filters,
        )
        if self._limit:
            self.query._limit = self._limit
        if self._offset:
            self.query._offset = self._offset
        if self._distinct:
            self.query._distinct = True
        self.resolve_ordering(
            self.model, self.model._meta.basetable, self._orderings, self._annotations
        )

    def __await__(self) -> Generator[Any, None, List[MODEL]]:
        if self._db is None:
            self._db = self.model._meta.db  # type: ignore
        self._make_query()
        return self._execute().__await__()

    async def __aiter__(self) -> AsyncIterator[MODEL]:
        for val in await self:
            yield val

    async def _execute(self) -> List[MODEL]:
        instance_list = await self._db.executor_class(
            model=self.model,
            db=self._db,
            prefetch_map=self._prefetch_map,
            prefetch_queries=self._prefetch_queries,
        ).execute_select(self.query, custom_fields=list(self._annotations.keys()))
        if self._get:
            if len(instance_list) == 1:
                return instance_list[0]
            if not instance_list:
                raise DoesNotExist("Object does not exist")
            raise MultipleObjectsReturned("Multiple objects returned, expected exactly one")
        if self._single:
            if not instance_list:
                return None  # type: ignore
            return instance_list[0]
        return instance_list


class UpdateQuery(AwaitableQuery):
    __slots__ = ("update_kwargs", "q_objects", "annotations", "custom_filters")

    def __init__(
        self,
        model: Type[MODEL],
        update_kwargs: Dict[str, Any],
        db: BaseDBAsyncClient,
        q_objects: List[Q],
        annotations: Dict[str, Any],
        custom_filters: Dict[str, Dict[str, Any]],
    ) -> None:
        super().__init__(model)
        self.update_kwargs = update_kwargs
        self.q_objects = q_objects
        self.annotations = annotations
        self.custom_filters = custom_filters
        self._db = db

    def _make_query(self) -> None:
        table = self.model._meta.basetable
        self.query = self._db.query_class.update(table)
        self.resolve_filters(
            model=self.model,
            q_objects=self.q_objects,
            annotations=self.annotations,
            custom_filters=self.custom_filters,
        )
        # Need to get executor to get correct column_map
        executor = self._db.executor_class(model=self.model, db=self._db)

        for key, value in self.update_kwargs.items():
            field_object = self.model._meta.fields_map.get(key)
            if not field_object:
                raise FieldError(f"Unknown keyword argument {key} for model {self.model}")
            if field_object.pk:
                raise IntegrityError(f"Field {key} is PK and can not be updated")
            if isinstance(field_object, (ForeignKeyFieldInstance, OneToOneFieldInstance)):
                fk_field: str = field_object.source_field  # type: ignore
                db_field = self.model._meta.fields_map[fk_field].source_field
                value = executor.column_map[fk_field](value.pk, None)
            else:
                try:
                    db_field = self.model._meta.fields_db_projection[key]
                except KeyError:
                    raise FieldError(f"Field {key} is virtual and can not be updated")
                value = executor.column_map[key](value, None)

            self.query = self.query.set(db_field, value)

    def __await__(self) -> Generator[Any, None, int]:
        if self._db is None:
            self._db = self.model._meta.db  # type: ignore
        self._make_query()
        return self._execute().__await__()

    async def _execute(self) -> int:
        return (await self._db.execute_query(str(self.query)))[0]


class DeleteQuery(AwaitableQuery):
    __slots__ = ("q_objects", "annotations", "custom_filters")

    def __init__(
        self,
        model: Type[MODEL],
        db: BaseDBAsyncClient,
        q_objects: List[Q],
        annotations: Dict[str, Any],
        custom_filters: Dict[str, Dict[str, Any]],
    ) -> None:
        super().__init__(model)
        self.q_objects = q_objects
        self.annotations = annotations
        self.custom_filters = custom_filters
        self._db = db

    def _make_query(self) -> None:
        self.query = copy(self.model._meta.basequery)
        self.resolve_filters(
            model=self.model,
            q_objects=self.q_objects,
            annotations=self.annotations,
            custom_filters=self.custom_filters,
        )
        self.query._delete_from = True

    def __await__(self) -> Generator[Any, None, int]:
        if self._db is None:
            self._db = self.model._meta.db  # type: ignore
        self._make_query()
        return self._execute().__await__()

    async def _execute(self) -> int:
        return (await self._db.execute_query(str(self.query)))[0]


class CountQuery(AwaitableQuery):
    __slots__ = ("q_objects", "annotations", "custom_filters", "limit", "offset")

    def __init__(
        self,
        model: Type[MODEL],
        db: BaseDBAsyncClient,
        q_objects: List[Q],
        annotations: Dict[str, Any],
        custom_filters: Dict[str, Dict[str, Any]],
        limit: Optional[int],
        offset: Optional[int],
    ) -> None:
        super().__init__(model)
        self.q_objects = q_objects
        self.annotations = annotations
        self.custom_filters = custom_filters
        self.limit = limit
        self.offset = offset or 0
        self._db = db

    def _make_query(self) -> None:
        self.query = copy(self.model._meta.basequery)
        self.resolve_filters(
            model=self.model,
            q_objects=self.q_objects,
            annotations=self.annotations,
            custom_filters=self.custom_filters,
        )
        self.query._select_other(Count("*"))

    def __await__(self) -> Generator[Any, None, int]:
        if self._db is None:
            self._db = self.model._meta.db  # type: ignore
        self._make_query()
        return self._execute().__await__()

    async def _execute(self) -> int:
        _, result = await self._db.execute_query(str(self.query))
        count = list(dict(result[0]).values())[0] - self.offset
        if self.limit and count > self.limit:
            return self.limit
        return count


class FieldSelectQuery(AwaitableQuery):
    # pylint: disable=W0223
    __slots__ = ("annotations",)

    def __init__(self, model: Type[MODEL], annotations: Dict[str, Any]) -> None:
        super().__init__(model)
        self.annotations = annotations

    def _join_table_with_forwarded_fields(
        self, model: Type[MODEL], table: Table, field: str, forwarded_fields: str
    ) -> Tuple[Table, str]:
        if field in model._meta.fields_db_projection and not forwarded_fields:
            return table, model._meta.fields_db_projection[field]

        if field in model._meta.fields_db_projection and forwarded_fields:
            raise FieldError(f'Field "{field}" for model "{model.__name__}" is not relation')

        if field in self.model._meta.fetch_fields and not forwarded_fields:
            raise ValueError(
                'Selecting relation "{}" is not possible, select concrete '
                "field on related model".format(field)
            )

        field_object = cast(RelationalField, model._meta.fields_map.get(field))
        if not field_object:
            raise FieldError(f'Unknown field "{field}" for model "{model.__name__}"')

        table = self._join_table_by_field(table, field, field_object)
        forwarded_fields_split = forwarded_fields.split("__")

        return self._join_table_with_forwarded_fields(
            model=field_object.model_class,
            table=table,
            field=forwarded_fields_split[0],
            forwarded_fields="__".join(forwarded_fields_split[1:]),
        )

    def add_field_to_select_query(self, field: str, return_as: str) -> None:
        table = self.model._meta.basetable
        if field in self.model._meta.fields_db_projection:
            db_field = self.model._meta.fields_db_projection[field]
            self.query._select_field(getattr(table, db_field).as_(return_as))
            return

        if field in self.model._meta.fetch_fields:
            raise ValueError(
                'Selecting relation "{}" is not possible, select '
                "concrete field on related model".format(field)
            )

        if field in self.annotations:
            annotation = self.annotations[field]
            annotation_info = annotation.resolve(self.model, table)
            self.query._select_other(annotation_info["field"].as_(return_as))
            return

        field_split = field.split("__")
        if field_split[0] in self.model._meta.fetch_fields:
            related_table, related_db_field = self._join_table_with_forwarded_fields(
                model=self.model,
                table=table,
                field=field_split[0],
                forwarded_fields="__".join(field_split[1:]),
            )
            self.query._select_field(getattr(related_table, related_db_field).as_(return_as))
            return

        raise FieldError(f'Unknown field "{field}" for model "{self.model.__name__}"')

    def resolve_to_python_value(self, model: Type[MODEL], field: str) -> Callable:
        if field in model._meta.fetch_fields:
            # return as is to get whole model objects
            return lambda x: x

        if field in [x[1] for x in model._meta.db_native_fields]:
            return lambda x: x

        if field in self.annotations:
            field_object = self.annotations[field].field_object
            if field_object:
                return field_object.to_python_value
            return lambda x: x

        if field in model._meta.fields_map:
            return model._meta.fields_map[field].to_python_value

        field_split = field.split("__")
        if field_split[0] in model._meta.fetch_fields:
            new_model = model._meta.fields_map[field_split[0]].model_class  # type: ignore
            return self.resolve_to_python_value(new_model, "__".join(field_split[1:]))

        raise FieldError(f'Unknown field "{field}" for model "{model}"')


class ValuesListQuery(FieldSelectQuery):
    __slots__ = (
        "flat",
        "fields",
        "limit",
        "offset",
        "distinct",
        "orderings",
        "annotations",
        "custom_filters",
        "q_objects",
        "fields_for_select_list",
    )

    def __init__(
        self,
        model: Type[MODEL],
        db: BaseDBAsyncClient,
        q_objects: List[Q],
        fields_for_select_list: List[str],
        limit: Optional[int],
        offset: Optional[int],
        distinct: bool,
        orderings: List[Tuple[str, str]],
        flat: bool,
        annotations: Dict[str, Any],
        custom_filters: Dict[str, Dict[str, Any]],
    ) -> None:
        super().__init__(model, annotations)
        if flat and (len(fields_for_select_list) != 1):
            raise TypeError("You can flat value_list only if contains one field")

        fields_for_select = {str(i): field for i, field in enumerate(fields_for_select_list)}
        self.fields = fields_for_select
        self.limit = limit
        self.offset = offset
        self.distinct = distinct
        self.orderings = orderings
        self.custom_filters = custom_filters
        self.q_objects = q_objects
        self.fields_for_select_list = fields_for_select_list
        self.flat = flat
        self._db = db

    def _make_query(self) -> None:
        self.query = copy(self.model._meta.basequery)
        for positional_number, field in self.fields.items():
            self.add_field_to_select_query(field, positional_number)

        self.resolve_filters(
            model=self.model,
            q_objects=self.q_objects,
            annotations=self.annotations,
            custom_filters=self.custom_filters,
        )
        if self.limit:
            self.query._limit = self.limit
        if self.offset:
            self.query._offset = self.offset
        if self.distinct:
            self.query._distinct = True
        self.resolve_ordering(
            self.model, self.model._meta.basetable, self.orderings, self.annotations
        )

    def __await__(self) -> Generator[Any, None, List[Any]]:
        if self._db is None:
            self._db = self.model._meta.db  # type: ignore
        self._make_query()
        return self._execute().__await__()  # pylint: disable=E1101

    async def __aiter__(self) -> AsyncIterator[Any]:
        for val in await self:
            yield val

    async def _execute(self) -> List[Any]:
        _, result = await self._db.execute_query(str(self.query))
        columns = [
            (key, self.resolve_to_python_value(self.model, name))
            for key, name in sorted(list(self.fields.items()))
        ]
        if self.flat:
            func = columns[0][1]
            flatmap = lambda entry: func(entry["0"])  # noqa
            return list(map(flatmap, result))

        listmap = lambda entry: tuple(func(entry[column]) for column, func in columns)  # noqa
        return list(map(listmap, result))


class ValuesQuery(FieldSelectQuery):
    __slots__ = (
        "fields_for_select",
        "limit",
        "offset",
        "distinct",
        "orderings",
        "annotations",
        "custom_filters",
        "q_objects",
    )

    def __init__(
        self,
        model: Type[MODEL],
        db: BaseDBAsyncClient,
        q_objects: List[Q],
        fields_for_select: Dict[str, str],
        limit: Optional[int],
        offset: Optional[int],
        distinct: bool,
        orderings: List[Tuple[str, str]],
        annotations: Dict[str, Any],
        custom_filters: Dict[str, Dict[str, Any]],
    ) -> None:
        super().__init__(model, annotations)
        self.fields_for_select = fields_for_select
        self.limit = limit
        self.offset = offset
        self.distinct = distinct
        self.orderings = orderings
        self.custom_filters = custom_filters
        self.q_objects = q_objects
        self._db = db

    def _make_query(self) -> None:
        self.query = copy(self.model._meta.basequery)
        for return_as, field in self.fields_for_select.items():
            self.add_field_to_select_query(field, return_as)

        self.resolve_filters(
            model=self.model,
            q_objects=self.q_objects,
            annotations=self.annotations,
            custom_filters=self.custom_filters,
        )
        if self.limit:
            self.query._limit = self.limit
        if self.offset:
            self.query._offset = self.offset
        if self.distinct:
            self.query._distinct = True
        self.resolve_ordering(
            self.model, self.model._meta.basetable, self.orderings, self.annotations
        )

    def __await__(self) -> Generator[Any, None, List[dict]]:
        if self._db is None:
            self._db = self.model._meta.db  # type: ignore
        self._make_query()
        return self._execute().__await__()  # pylint: disable=E1101

    async def __aiter__(self) -> AsyncIterator[dict]:
        for val in await self:
            yield val

    async def _execute(self) -> List[dict]:
        result = await self._db.execute_query_dict(str(self.query))
        columns = [
            val
            for val in [
                (alias, self.resolve_to_python_value(self.model, field_name))
                for alias, field_name in self.fields_for_select.items()
            ]
            if not isinstance(val[1], types.LambdaType)
        ]

        if columns:
            for row in result:
                for col, func in columns:
                    row[col] = func(row[col])

        return result
