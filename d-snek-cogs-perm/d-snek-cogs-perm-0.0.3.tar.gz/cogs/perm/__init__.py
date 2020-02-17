import json
from dataclasses import dataclass
from typing import Optional, Union, Type, List

from discord import Member, Guild, Role
from discord.ext.commands import command, group, guild_only, Cog
from pony.orm import Database, PrimaryKey, Required
from pony.orm.core import Entity, db_session
from ruamel.yaml import YAML, StringIO
from snek import SNEK, IPerm, SNEKContext, UsesDatabase

yaml = YAML()


def dump_yaml(obj):
    sio = StringIO()

    yaml.dump(obj, sio)

    return sio.getvalue()


class Perm(IPerm, UsesDatabase):
    def __init__(self, bot: SNEK):
        self.bot = bot
        self.PermGroup: Optional[Type[Entity]] = None

    async def do_db(self, db: Database) -> None:
        class PermGroup(db.Entity):
            name = Required(str)
            guild = Required(int, size=64)

            order = Required(int)
            perm = Required(bool, default=lambda: False)  # permanent

            roles = Required(str)
            data = Required(str)

            PrimaryKey(guild, name)

        self.PermGroup = PermGroup

    @dataclass
    class PGroup(IPerm.PGroup):
        @classmethod
        def from_db(cls, row: Entity) -> "Perm.PGroup":
            return cls(
                name=row.name,
                order=row.order,
                roles=json.loads(row.roles),
                data=json.loads(row.data),
                perm=row.perm,
                guild=row.guild,
            )

        def to_dict(self) -> dict:
            return {
                "name": self.name,
                "guild": self.guild,
                "order": self.order,
                "perm": self.perm,
                "data": json.dumps(self.data),
                "roles": json.dumps(self.roles),
            }

        def update(self, entity: Type[Entity]):
            with db_session:
                entity[self.guild, self.name].set(**self.to_dict())

    def get_user_pgroups(self, guild: Guild, member: Member) -> List[PGroup]:
        with db_session:
            applicable_pgroups = []
            for pgroup in (
                self.PGroup.from_db(r)
                for r in self.PermGroup.select(lambda pg: pg.guild == guild.id)
            ):
                roles = [
                    guild.get_role(role)
                    for role in pgroup.roles
                    if guild.get_role(role) is not None
                ]

                if (
                    len(set(roles).intersection(set(member.roles))) > 0
                    or pgroup.name == "everyone"
                ):
                    applicable_pgroups.append(pgroup)

            applicable_pgroups.sort(key=lambda v: v.order)

        return applicable_pgroups

    async def check_perm(self, guild: Guild, member: Member, perm: str):
        if await self.bot.is_owner(member):
            return True

        applicable_pgroups = self.get_user_pgroups(guild, member)
        perm_state = None
        for pgroup in applicable_pgroups:
            if pgroup.data.get(perm) is not None:
                perm_state = pgroup.data.get(perm)

        return perm_state

    def get_pgroup(self, guild: Guild, name: str) -> Optional["Perm.PGroup"]:
        with db_session:
            row = self.PermGroup.select(
                lambda pg: pg.guild == guild.id and pg.name == name
            ).first()

            if row is not None:
                return self.PGroup.from_db(row)
            else:
                return None

    @Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            self.ensure_perm_pgroups(guild)

    @Cog.listener()
    async def on_guild_join(self, guild: Guild):
        self.ensure_perm_pgroups(guild)

    def ensure_perm_pgroups(self, guild: Guild):
        with db_session:
            mod = self.get_pgroup(guild, "mod")
            everyone = self.get_pgroup(guild, "everyone")

            if mod is None:
                self.PermGroup(
                    name="mod",
                    guild=guild.id,
                    order=9999,
                    perm=True,
                    roles="[]",
                    data="{}",
                )
            else:
                if mod.perm is not True:
                    self.PermGroup[guild.id, "mod"].set(perm=True)

            if everyone is None:
                self.PermGroup(
                    name="everyone",
                    guild=guild.id,
                    order=0,
                    perm=True,
                    roles="[]",
                    data="{}",
                )
            else:
                if mod.perm is not True:
                    self.PermGroup[guild.id, "everyone"].set(perm=True)

    @command(hidden=True)
    @SNEK.is_mod()
    @guild_only()
    async def chmod(
        self, ctx: SNEKContext, perm: str, name: str, setting: Optional[bool]
    ):
        pgroup = self.get_pgroup(ctx.guild, name)
        if pgroup is None:
            await ctx.send("This permissions group does not exist!")

        if setting is None:
            if pgroup.data.get(perm) is not None:
                del pgroup.data[perm]
                await ctx.bot.log(
                    f"Deleted pgroup setting: {name}[{perm}]", _for="PERM"
                )

        else:
            pgroup.data[perm] = setting
            await ctx.bot.log(
                f"Set pgroup setting: {name}[{perm}] = {setting!r}", _for="PERM"
            )

        pgroup.update(self.PermGroup)

        await ctx.send("Set setting for group.")

    @group(hidden=True)
    @guild_only()
    @SNEK.is_mod()
    async def pgroup(self, ctx: SNEKContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("pgroup")

    @pgroup.command(name="new")
    @guild_only()
    async def pgroup_new(self, ctx: SNEKContext, name: str):
        with db_session:
            if self.PermGroup.exists(guild=ctx.guild.id, name=name):
                await ctx.send(
                    "Cannot create new group; Permission Group of this name already exists."
                )
            else:
                self.PermGroup(
                    name=name, guild=ctx.guild.id, order=1, roles="[]", data="{}"
                )

        await ctx.send("Group created.")
        await ctx.bot.log(f"New pgroup: {name}", _for="PERM")

    @pgroup.command(name="del")
    @guild_only()
    async def pgroup_del(self, ctx: SNEKContext, name: str):
        pg = self.get_pgroup(ctx.guild, name)

        if pg is None:
            await ctx.send("The group does not exist.")
        else:
            if pg.perm:
                await ctx.send("Cannot delete a permanent group!")
                return

            with db_session:
                self.PermGroup[pg.guild, pg.name].delete()

            await ctx.send("Group deleted")
            await ctx.bot.log(f"Deleted pgroup: {name}", _for="PERM")

    @pgroup.command(name="order")
    @guild_only()
    async def pgroup_order(self, ctx: SNEKContext, name: str, order: int):
        pg = self.get_pgroup(ctx.guild, name)
        if pg is None:
            await ctx.send("The group does not exist.")
        else:
            pg.order = order
            pg.update(self.PermGroup)

            await ctx.send("Set new order.")
            await ctx.bot.log(
                f"Set pgroup order: order {order} for pgroup {name}", _for="PERM"
            )

    @pgroup.command(name="append")
    @guild_only()
    async def pgroup_append(self, ctx: SNEKContext, name: str, role: Role):
        """Appends a role to the permission group"""
        pg = self.get_pgroup(ctx.guild, name)
        if pg is None:
            await ctx.send("The group does not exist.")
        else:
            pg.roles.append(role.id)
            pg.roles = list(set([r for r in pg.roles]))
            pg.update(self.PermGroup)

            await ctx.send("Appended role")
            await ctx.bot.log(f"Set pgroup roles for {name}: {pg.roles!r}", _for="PERM")

    @pgroup.command(name="remove")
    @guild_only()
    async def pgroup_remove(self, ctx: SNEKContext, name: str, role: Union[Role, int]):
        """Removes a role from the permission group"""
        pg = self.get_pgroup(ctx.guild, name)
        if pg is None:
            await ctx.send("The group does not exist.")
        else:
            if isinstance(role, Role):
                role = role.id

            pg.roles.remove(role)
            pg.update(self.PermGroup)

            await ctx.send("Removed role")
            await ctx.bot.log(f"Set pgroup roles for {name}: {pg.roles!r}", _for="PERM")

    @pgroup.command(name="info")
    @guild_only()
    async def pgroup_info(self, ctx: SNEKContext, name: str):
        pg = self.get_pgroup(ctx.guild, name)

        if pg is None:
            await ctx.send("The group does not exist.")
        else:
            await ctx.send(
                dump_yaml(
                    {
                        "Name": pg.name,
                        "Order": pg.order,
                        "Roles": pg.roles,
                        "Permissions": pg.data,
                        "Permanent": pg.perm,
                    }
                ),
                lang="yaml",
            )

    @command(hidden=True)
    @SNEK.is_mod()
    @guild_only()
    async def pgroups(self, ctx: SNEKContext):
        with db_session:
            groups = [
                self.PGroup.from_db(r).to_dict()
                for r in self.PermGroup.select(lambda pg: pg.guild == ctx.guild.id)
            ]

        await ctx.send(
            json.dumps(
                sorted(groups, key=lambda v: v["order"], reverse=True), indent=" "
            ),
            lang="json",
        )

    @command(hidden=True)
    @SNEK.is_mod()
    @guild_only()
    async def roleid(self, ctx: SNEKContext, name_or_role: Union[Role, str]):
        """Provide name in quotes, and output role ID."""
        roles = []
        if isinstance(name_or_role, Role):
            roles.append(name_or_role)
        else:
            for role in ctx.guild.roles:
                if role.name.lower() == name_or_role.lower():
                    roles.append(role)

        if len(roles) == 0:
            await ctx.send("A role with this name does not exist.")
        elif len(roles) == 1:
            role = roles[0]
            await ctx.send(f"Role {role.name!r} has ID {role.id}")
        else:
            role_list = "\n".join(
                f"Role {role.name!r} (with color {role.color!s}) has ID {role.id}"
                for role in roles
            )

            await ctx.send(f"There are multiple roles with this name:\n{role_list}")

    @command(hidden=True)
    @guild_only()
    async def whatamiin(self, ctx: SNEKContext):
        groups = self.get_user_pgroups(ctx.guild, ctx.author)

        await ctx.send(json.dumps([v.name for v in groups]), lang="json")

    @command(hidden=True)
    @guild_only()
    async def checkperm(self, ctx: SNEKContext, perm: str):
        await ctx.send(f"Perm result: {await ctx.check_perm(perm)!s}")


def setup(bot: SNEK):
    bot.add_cog(Perm(bot))
