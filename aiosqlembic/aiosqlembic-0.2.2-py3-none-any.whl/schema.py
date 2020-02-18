import asyncio
import logging
from collections import OrderedDict
from itertools import groupby
from pathlib import Path
from typing import Tuple, Dict, Optional, List

import aiosql
from asyncpg.pool import Pool
from migra import Statements, Changes
from schemainspect import ColumnInfo
from schemainspect.misc import quoted_identifier
from schemainspect.pg.obj import (
    InspectedSchema,
    InspectedRowPolicy,
    InspectedCollation,
    InspectedPrivilege,
    InspectedEnum,
    InspectedSelectable,
    InspectedIndex,
    InspectedSequence,
    InspectedConstraint,
    InspectedExtension,
    InspectedFunction,
    InspectedTrigger,
    InspectedDomain,
    InspectedType,
)

from aiosqlembic.models.inspector import (
    Schema,
    Enum,
    Relation,
    Index,
    Sequence,
    Constraint,
    Extension,
    Function,
    Dep,
    Privilege,
    Trigger,
    Collation,
    RlsPolicy,
    Type,
    Domain,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s:%(filename)s.%(funcName)s:%(lineno)d %(message)s"
)


class AsyncSchemaInspector:
    def __init__(self, pool: Pool):
        self.current_path = Path(__file__).parent
        self.queries = aiosql.from_path(
            self.current_path / "./sql/metadata",
            "asyncpg",
            record_classes={
                "Schema": Schema,
                "Enum": Enum,
                "Relation": Relation,
                "Index": Index,
                "Sequence": Sequence,
                "Constraint": Constraint,
                "Extension": Extension,
                "Function": Function,
                "Dep": Dep,
                "Privilege": Privilege,
                "Trigger": Trigger,
                "Collation": Collation,
                "RlsPolicy": RlsPolicy,
                "Type": Type,
                "Domain": Domain,
            },
        )
        self.pool = pool

    async def load_all(self) -> None:
        task_schemas = asyncio.create_task(self.load_schemas())
        task_relations = asyncio.create_task(self.load_all_relations())
        task_functions = asyncio.create_task(self.load_functions())
        await asyncio.gather(task_schemas, task_relations, task_functions)
        self.selectables: OrderedDict[str, InspectedSelectable] = OrderedDict()
        self.selectables.update(self.relations)
        self.selectables.update(self.functions)

        task_deps = asyncio.create_task(self.load_deps())
        task_deps_all = asyncio.create_task(self.load_deps_all())
        task_privileges = asyncio.create_task(self.load_privileges())
        task_triggers = asyncio.create_task(self.load_triggers())
        task_collations = asyncio.create_task(self.load_collations())
        task_rlspolicies = asyncio.create_task(self.load_rlspolicies())
        task_types = asyncio.create_task(self.load_types())
        task_domains = asyncio.create_task(self.load_domains())
        await asyncio.gather(
            task_deps,
            task_deps_all,
            task_privileges,
            task_triggers,
            task_collations,
            task_rlspolicies,
            task_types,
            task_domains,
        )
        pass

    async def load_schemas(self) -> None:
        q: List[Schema] = await self.queries.get_all_schemas(self.pool)
        logger.debug(f"schemas loaded: {q}")

        schemas: List[InspectedSchema] = [
            InspectedSchema(schema=each.schemaname) for each in q
        ]
        self.schemas: OrderedDict[str, InspectedSchema] = OrderedDict(
            (schema.schema, schema) for schema in schemas
        )

    async def load_all_relations(self) -> None:
        self.tables: OrderedDict[str, InspectedSelectable] = OrderedDict()
        self.views: OrderedDict[str, InspectedSelectable] = OrderedDict()
        self.materialized_views: OrderedDict[str, InspectedSelectable] = OrderedDict()
        self.composite_types: OrderedDict[str, InspectedSelectable] = OrderedDict()

        q = await self.queries.get_all_enums(self.pool)
        logger.debug(f"enums loaded: {q}")

        enumlist = [
            InspectedEnum(name=i.name, schema=i.schemaname, elements=i.elements)
            for i in q
        ]
        self.enums: OrderedDict[str, InspectedEnum] = OrderedDict(
            (i.quoted_full_name, i) for i in enumlist
        )
        q = await self.queries.get_all_relations(self.pool)
        logger.debug(f"relations loaded: {q}")

        for _, g in groupby(q, lambda x: (x.relationtype, x.schemaname, x.name)):
            clist = list(g)
            f = clist[0]

            def get_enum(name: str, schema: str) -> Optional[InspectedEnum]:
                if not name and not schema:
                    return None

                quoted_full_name = "{}.{}".format(
                    quoted_identifier(schema), quoted_identifier(name)
                )
                return self.enums[quoted_full_name]

            columns = [
                ColumnInfo(
                    name=c.attname,
                    dbtype=c.datatype,
                    dbtypestr=c.datatypestring,
                    # pytype=self.to_pytype(c.datatype),
                    pytype=c.datatype,
                    default=c.defaultdef,
                    not_null=c.not_null,
                    is_enum=c.is_enum,
                    enum=get_enum(c.enum_name, c.enum_schema),
                    collation=c.collation,
                )
                for c in clist
                if c.position_number
            ]

            s = InspectedSelectable(
                name=f.name,
                schema=f.schemaname,
                columns=OrderedDict((c.name, c) for c in columns),
                relationtype=f.relationtype,
                definition=f.definition,
                comment=f.comment,
                parent_table=f.parent_table,
                partition_def=f.partition_def,
                rowsecurity=f.rowsecurity,
                forcerowsecurity=f.forcerowsecurity,
            )
            RELATIONTYPES = {
                "r": "tables",
                "v": "views",
                "m": "materialized_views",
                "c": "composite_types",
                "p": "tables",
            }
            att = getattr(self, RELATIONTYPES[f.relationtype])
            att[s.quoted_full_name] = s
        self.relations: OrderedDict[str, InspectedSelectable] = OrderedDict()
        for x in (self.tables, self.views, self.materialized_views):
            self.relations.update(x)
        q = await self.queries.get_all_indexes(self.pool)
        logger.debug(f"indexes loaded: {q}")

        indexlist = [
            InspectedIndex(
                name=i.name,
                schema=i.schemaname,
                definition=i.definition,
                table_name=i.table_name,
                key_columns=i.key_columns,
                key_options=i.key_options,
                num_att=i.num_att,
                is_unique=i.is_unique,
                is_pk=i.is_pk,
                is_exclusion=i.is_exclusion,
                is_immediate=i.is_immediate,
                is_clustered=i.is_clustered,
                key_collations=i.key_collations,
                key_expressions=i.key_expressions,
                partial_predicate=i.partial_predicate,
            )
            for i in q
        ]
        self.indexes: OrderedDict[str, InspectedIndex] = OrderedDict(
            (i.quoted_full_name, i) for i in indexlist
        )
        q = await self.queries.get_all_sequences(self.pool)
        logger.debug(f"sequences loaded: {q}")

        sequencelist = [InspectedSequence(name=i.name, schema=i.schemaname) for i in q]
        self.sequences: OrderedDict[str, InspectedSequence] = OrderedDict(
            (i.quoted_full_name, i) for i in sequencelist
        )
        q = await self.queries.get_all_constraints(self.pool)

        constraintlist = []

        for i in q:
            constraint = InspectedConstraint(
                name=i.name,
                schema=i.schemaname,
                constraint_type=i.constraint_type,
                table_name=i.table_name,
                definition=i.definition,
                index=i.index,
            )
            if constraint.index:
                index_name = quoted_identifier(i.index, schema=i.schemaname)
                index = self.indexes[index_name]
                index.constraint = constraint
                constraint.index = index

            constraintlist.append(constraint)

        self.constraints: OrderedDict[str, InspectedConstraint] = OrderedDict(
            (i.quoted_full_name, i) for i in constraintlist
        )

        q = await self.queries.get_all_extensions(self.pool)
        logger.debug(f"extensions loaded: {q}")

        extensionlist = [
            InspectedExtension(name=i.name, schema=i.schemaname, version=i.version)
            for i in q
        ]
        # extension names are unique per-database rather than per-schema like other things (even though extensions are assigned to a particular schema)
        self.extensions: OrderedDict[str, InspectedExtension] = OrderedDict(
            (i.name, i) for i in extensionlist
        )
        # add indexes and constraints to each table
        for each in self.indexes.values():
            t = each.quoted_full_table_name
            n = each.quoted_full_name
            self.relations[t].indexes[n] = each
        for each in self.constraints.values():
            t = each.quoted_full_table_name
            n = each.quoted_full_name
            self.relations[t].constraints[n] = each

    async def load_functions(self) -> None:
        self.functions = OrderedDict()
        q = await self.queries.get_all_functions(self.pool)
        logger.debug(f"functions loaded: {q}")

        for _, g in groupby(q, lambda x: (x.schemaname, x.name, x.identity_arguments)):
            clist = list(g)
            f = clist[0]
            outs = [c for c in clist if c.parameter_mode == "OUT"]
            columns = [
                ColumnInfo(
                    name=c.parameter_name,
                    dbtype=c.data_type,
                    pytype=c.data_type,
                    # pytype=self.to_pytype(c.data_type),
                )
                for c in outs
            ]
            if outs:
                columns = [
                    ColumnInfo(
                        name=c.parameter_name,
                        dbtype=c.data_type,
                        pytype=c.data_type,
                        # pytype=self.to_pytype(c.data_type),
                    )
                    for c in outs
                ]
            else:
                columns = [
                    ColumnInfo(
                        name=f.name,
                        dbtype=f.data_type,
                        pytype=f.returntype,
                        # pytype=self.to_pytype(f.returntype),
                        default=f.parameter_default,
                    )
                ]
            plist = [
                ColumnInfo(
                    name=c.parameter_name,
                    dbtype=c.data_type,
                    pytype=c.data_type,
                    # pytype=self.to_pytype(c.data_type),
                    default=c.parameter_default,
                )
                for c in clist
                if c.parameter_mode == "IN"
            ]
            s = InspectedFunction(
                schema=f.schemaname,
                name=f.name,
                columns=OrderedDict((c.name, c) for c in columns),
                inputs=plist,
                identity_arguments=f.identity_arguments,
                result_string=f.result_string,
                language=f.language,
                definition=f.definition,
                strictness=f.strictness,
                security_type=f.security_type,
                volatility=f.volatility,
                full_definition=f.full_definition,
                comment=f.comment,
                returntype=f.returntype,
            )

            identity_arguments = "({})".format(s.identity_arguments)
            self.functions[s.quoted_full_name + identity_arguments] = s

    async def load_deps(self) -> None:
        q = await self.queries.get_all_deps(self.pool)
        logger.debug(f"deps loaded: {q}")

        for dep in q:
            x = quoted_identifier(dep.name, dep.schemaname)
            x_dependent_on = quoted_identifier(
                dep.name_dependent_on,
                dep.schema_dependent_on,
                dep.identity_arguments_dependent_on,
            )
            self.selectables[x].dependent_on.append(x_dependent_on)
            self.selectables[x].dependent_on.sort()
            self.selectables[x_dependent_on].dependents.append(x)
            self.selectables[x_dependent_on].dependents.sort()

    async def load_deps_all(self) -> None:
        def get_related_for_item(
            item: InspectedSelectable, att: str
        ) -> List[InspectedSelectable]:
            related = [self.selectables[_] for _ in getattr(item, att)]
            return [item.signature] + [
                _ for d in related for _ in get_related_for_item(d, att)
            ]

        for k, x in self.selectables.items():
            d_all = get_related_for_item(x, "dependent_on")[1:]
            d_all.sort()
            x.dependent_on_all = d_all
            d_all = get_related_for_item(x, "dependents")[1:]
            d_all.sort()
            x.dependents_all = d_all

    async def load_privileges(self) -> None:
        q = await self.queries.get_all_privileges(self.pool)
        logger.debug(f"privileges loaded: {q}")

        privileges = [
            InspectedPrivilege(
                object_type=i.object_type,
                schema=i.schemaname,
                name=i.name,
                privilege=i.privilege,
                target_user=i.user,
            )
            for i in q
        ]
        self.privileges: OrderedDict[str, InspectedPrivilege] = OrderedDict(
            (i.key, i) for i in privileges
        )

    async def load_triggers(self) -> None:
        q = await self.queries.get_all_triggers(self.pool)
        logger.debug(f"triggers loaded: {q}")

        triggers = [
            InspectedTrigger(
                i.name,
                i.schemaname,
                i.table_name,
                i.proc_schema,
                i.proc_name,
                i.enabled,
                i.full_definition,
            )
            for i in q
        ]
        self.triggers = OrderedDict((t.signature, t) for t in triggers)

    async def load_collations(self) -> None:
        q = await self.queries.get_all_collations(self.pool)
        logger.debug(f"collations loaded: {q}")

        collations = [
            InspectedCollation(
                schema=i.schemaname,
                name=i.name,
                provider=i.provider,
                encoding=i.encoding,
                lc_collate=i.lc_collate,
                lc_ctype=i.lc_ctype,
                version=i.version,
            )
            for i in q
        ]
        self.collations: OrderedDict[str, InspectedCollation] = OrderedDict(
            (i.quoted_full_name, i) for i in collations
        )

    async def load_rlspolicies(self) -> None:
        q = await self.queries.get_all_rlspolicies(self.pool)
        logger.debug(f"rlspolicies loaded: {q}")
        rlspolicies = [
            InspectedRowPolicy(
                name=p.name,
                schema=p.schemaname,
                table_name=p.table_name,
                commandtype=p.commandtype,
                permissive=p.permissive,
                roles=p.roles,
                qual=p.qual,
                withcheck=p.withcheck,
            )
            for p in q
        ]

        self.rlspolicies: OrderedDict[str, InspectedRowPolicy] = OrderedDict(
            (p.key, p) for p in rlspolicies
        )

    async def load_types(self) -> None:
        q = await self.queries.get_all_types(self.pool)
        logger.debug(f"types loaded: {q}")

        def col(defn: Dict[str, str]) -> Tuple[str, str]:
            return defn["attribute"], defn["type"]

        types = [
            InspectedType(i.name, i.schemaname, dict(col(_) for _ in i.columns))
            for i in q
        ]
        self.types = OrderedDict((t.signature, t) for t in types)

    async def load_domains(self) -> None:
        q = await self.queries.get_all_domains(self.pool)
        logger.debug(f"domains loaded: {q}")

        def col(defn: Dict[str, str]) -> Tuple[str, str]:
            return defn["attribute"], defn["type"]

        domains = [
            InspectedDomain(
                i.name,
                i.schemaname,
                i.data_type,
                i.collation,
                i.constraint_name,
                i.not_null,
                i.default,
                i.check,
            )
            for i in q
        ]
        self.domains = OrderedDict((t.signature, t) for t in domains)

    # @property
    # def partitioned_tables(self) -> "OrderedDict[str, InspectedSelectable]":
    #     return OrderedDict((k, v) for k, v in self.tables.items() if v.is_partitioned)
    #
    # @property
    # def alterable_tables(
    #     self,
    # ) -> "OrderedDict[str, InspectedSelectable]":  # ordinary tables and parent tables
    #     return OrderedDict((k, v) for k, v in self.tables.items() if v.is_alterable)
    #
    # @property
    # def data_tables(
    #     self,
    # ) -> "OrderedDict[str, InspectedSelectable]":  # ordinary tables and child tables
    #     return OrderedDict((k, v) for k, v in self.tables.items() if v.contains_data)
    #
    # @property
    # def partitioning_child_tables(self) -> "OrderedDict[str, InspectedSelectable]":
    #     return OrderedDict(
    #         (k, v) for k, v in self.tables.items() if v.is_partitioning_child_table
    #     )
    #
    # @property
    # def tables_using_partitioning(self) -> "OrderedDict[str, InspectedSelectable]":
    #     return OrderedDict(
    #         (k, v) for k, v in self.tables.items() if v.uses_partitioning
    #     )
    #
    # @property
    # def tables_not_using_partitioning(self) -> "OrderedDict[str, InspectedSelectable]":
    #     return OrderedDict(
    #         (k, v) for k, v in self.tables.items() if not v.uses_partitioning
    #     )

    def one_schema(self, schema: str) -> None:
        props = "schemas relations tables views functions selectables sequences constraints indexes enums extensions privileges collations triggers"
        for prop in props.split():
            att = getattr(self, prop)
            filtered = {k: v for k, v in att.items() if v.schema == schema}
            setattr(self, prop, filtered)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AsyncSchemaInspector):
            return NotImplemented
        else:
            return (
                type(self) == type(other)
                and self.schemas == other.schemas
                and self.relations == other.relations
                and self.sequences == other.sequences
                and self.enums == other.enums
                and self.constraints == other.constraints
                and self.extensions == other.extensions
                and self.functions == other.functions
                and self.triggers == other.triggers
                and self.collations == other.collations
                and self.rlspolicies == other.rlspolicies
            )


class Amigration:
    def __init__(self, schema: str = None) -> None:
        self.statements = Statements()
        self.changes = Changes(None, None)
        self.schema = schema

    @classmethod
    async def create(cls, x_from: Pool, x_target: Pool) -> "Amigration":
        self = Amigration()
        self.changes.i_from = AsyncSchemaInspector(pool=x_from)
        self.changes.i_target = AsyncSchemaInspector(pool=x_target)
        await self.load_all()
        return self

    async def load_all(self) -> None:
        logger.debug("loading migration")
        task_ifrom = self.changes.i_from.load_all()
        task_itarget = self.changes.i_target.load_all()
        await asyncio.gather(task_ifrom, task_itarget)

    def clear(self) -> None:
        self.statements = Statements()

    # def apply(self):
    #     for stmt in self.statements:
    #         raw_execute(self.s_from, stmt)
    #     self.changes.i_from = get_inspector(self.s_from, schema=self.schema)
    #     safety_on = self.statements.safe
    #     self.clear()
    #     self.set_safety(safety_on)

    def add(self, statements: Statements) -> None:
        self.statements += statements

    def add_sql(self, sql: str) -> None:
        self.statements += Statements([sql])

    def set_safety(self, safety_on: bool) -> None:
        self.statements.safe = safety_on

    def add_extension_changes(self, creates: bool = True, drops: bool = True) -> None:
        if creates:
            self.add(self.changes.extensions(creations_only=True))
        if drops:
            self.add(self.changes.extensions(drops_only=True))

    def add_all_changes(self, privileges: bool = False) -> None:
        self.add(self.changes.schemas(creations_only=True))

        self.add(self.changes.extensions(creations_only=True))
        self.add(self.changes.collations(creations_only=True))
        self.add(self.changes.enums(creations_only=True, modifications=False))
        self.add(self.changes.sequences(creations_only=True))
        self.add(self.changes.triggers(drops_only=True))
        self.add(self.changes.rlspolicies(drops_only=True))
        if privileges:
            self.add(self.changes.privileges(drops_only=True))
        self.add(self.changes.non_pk_constraints(drops_only=True))
        self.add(self.changes.pk_constraints(drops_only=True))
        self.add(self.changes.indexes(drops_only=True))

        self.add(self.changes.selectables())

        self.add(self.changes.sequences(drops_only=True))
        self.add(self.changes.enums(drops_only=True, modifications=False))
        self.add(self.changes.extensions(drops_only=True))
        self.add(self.changes.indexes(creations_only=True))
        self.add(self.changes.pk_constraints(creations_only=True))
        self.add(self.changes.non_pk_constraints(creations_only=True))
        if privileges:
            self.add(self.changes.privileges(creations_only=True))
        self.add(self.changes.rlspolicies(creations_only=True))
        self.add(self.changes.triggers(creations_only=True))
        self.add(self.changes.collations(drops_only=True))
        self.add(self.changes.schemas(drops_only=True))

    @property
    def sql(self) -> str:
        s: str = self.statements.sql
        return s
