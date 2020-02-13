# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.


from collections import OrderedDict, defaultdict
from typing import Union, List, ValuesView, Optional, Dict, Any

import networkx
import numpy as np
from numpy.random import RandomState

from textworld import g_rng
from textworld.utils import uniquify
from textworld.generator.data import KnowledgeBase
from textworld.generator.vtypes import get_new

from textworld.generator.graph_networks import direction
from textworld.generator.graph_networks import DIRECTIONS, reverse_direction
from textworld.logic import Proposition, State, Variable


class NoFreeExitError(Exception):
    pass


def connect(room1: Variable, direction: str, room2: Variable,
            door: Optional[Variable] = None) -> List[Proposition]:
    """ Generate predicates that connect two rooms.

    Args:
        room1: A room variable.
        direction: Direction that we need to travel to go from
                   room1 to room2.
        room2: A room variable.
        door: The door separating the two rooms. If `None`, there is no
              door between the rooms.
    """
    r_direction = reverse_direction(direction) + "_of"
    direction += "_of"
    facts = [Proposition(direction, [room2, room1]),
             Proposition(r_direction, [room1, room2]),
             Proposition("free", [room1, room2]),
             Proposition("free", [room2, room1])]

    if door is not None:
        facts += [Proposition("link", [room1, door, room2]),
                  Proposition("link", [room2, door, room1])]

    return facts


def graph2state(G: networkx.Graph, rooms: Dict[str, Variable]) -> List[Proposition]:
    """ Convert Graph object to a list of `Proposition`.

    Args:
        G: Graph defining the structure of the world.
        rooms: information about the rooms in the world.
    """
    state = []
    for src, dest in G.edges():
        d = direction(src, dest)

        d_r = direction(dest, src)
        e = G[src][dest]

        room_src = rooms[src]
        room_dest = rooms[dest]
        if e["has_door"]:
            door = Variable(e['door_name'], "d")
            pred1 = Proposition("{}_of".format(d), [room_dest, room_src])
            pred2 = Proposition("{}_of".format(d_r), [room_src, room_dest])
            state.append(Proposition(e["door_state"], [door]))
            state.append(Proposition("link", [room_src, door, room_dest]))
            state.append(Proposition("link", [room_dest, door, room_src]))
            if e["door_state"] == "open":
                state.append(Proposition("free", [room_dest, room_src]))
                state.append(Proposition("free", [room_src, room_dest]))
        else:
            pred1 = Proposition("{}_of".format(d), [room_dest, room_src])
            pred2 = Proposition("{}_of".format(d_r), [room_src, room_dest])
            state.append(Proposition("free", [room_dest, room_src]))
            state.append(Proposition("free", [room_src, room_dest]))

        state.append(pred1)
        state.append(pred2)

    return state


class WorldEntity(Variable):
    """
    A WorldEntity is an abstract concept representing anything with a name and a type.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.content = []
        self.related_facts = []
        self.properties = []
        self.matching_entity_id = None

    @classmethod
    def create(cls, var: Variable) -> Union["WorldRoom", "WorldObject"]:
        # TODO: make a small factory instead of classmethod.
        if var.type == "r":
            return WorldRoom(var.name, var.type)

        return WorldObject(var.name, var.type)

    @property
    def id(self) -> str:
        return self.name

    def add_related_fact(self, fact: Proposition) -> None:
        if len(fact.arguments) == 1:
            # Fact considered as an object's property.
            self.properties.append(fact.name)

        self.related_facts.append(fact)

    def get_attributes(self) -> List[Proposition]:
        return self.related_facts


class WorldObject(WorldEntity):
    """
    A WorldObject is anything we can directly interact with.
    """
    pass


class WorldRoom(WorldEntity):
    """
    WorldRooms can be linked with each other through exits.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.exits = OrderedDict()
        self.doors = OrderedDict()


class World:
    def __init__(self):
        self._facts = []
        self._entities_infos = {}


class Maker:
    def __init__(self, kb: KnowledgeBase = None):
        self.kb = kb or KnowledgeBase.default()

    def new(self, type: str, name: Optional[str] = None,
            desc: Optional[str] = None) -> World:
        """ Creates new entity given its type.

        Args:
            type: The type of the entity.
            name: The name of the entity.
            desc: The description of the entity.

        Returns:
            The newly created entity.

            * If the `type` is `'r'`, then a `WorldRoom` object is returned.
            * Otherwise, a `WorldEntity` is returned.
        """
        var_id = type
        if not self.kb.types.is_constant(type):
            var_id = self.get_new(type, self._types_counts)

        var = Variable(var_id, type)
        if type == "r":
            entity = WorldRoom(var, name, desc)
            self.rooms.append(entity)
        else:
            entity = WorldEntity(var, name, desc)

        self._entities[var_id] = entity
        if entity.name:
            self._named_entities[entity.name] = entity

        return entity



class World:

    @classmethod
    def from_facts(cls, facts: List[Proposition]) -> "World":
        world = cls()
        world.add_facts(facts)
        return world

    @classmethod
    def deserialize(cls, serialized_facts: List) -> "World":
        return cls.from_facts([Proposition.deserialize(f) for f in serialized_facts])

    def serialize(self) -> List:
        return [f.serialize() for f in self.facts]

    @classmethod
    def from_map(cls, map: networkx.Graph) -> "World":
        """
        Args:
            map: Graph defining the structure of the world.
        """
        world = cls()
        names = [d.get("name", "r_{}".format(i)) for i, (n, d) in enumerate(map.nodes.items())]
        rooms = OrderedDict((n, Variable(names[i], "r")) for i, n in enumerate(map.nodes()))
        world.add_facts(graph2state(map, rooms))
        return world

    @property
    def player_room(self) -> WorldRoom:
        return self._player_room

    @property
    def rooms(self) -> List[WorldRoom]:
        return self._rooms

    @property
    def objects(self) -> List[WorldObject]:
        return self._objects

    @property
    def entities(self) -> ValuesView[WorldEntity]:
        return self._entities.values()

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, state: State) -> None:
        self._state = State()
        self.add_facts(state.facts)

    @property
    def facts(self) -> List[Proposition]:
        # Sort the facts for deterministic world generation
        return sorted(self._state.facts)

    def add_fact(self, fact: Proposition) -> None:
        self.add_facts([fact])

    def add_facts(self, facts: List[Proposition]) -> None:
        self._state.add_facts(facts)
        self._update()  # Update the internal representation of the world.

    def _get_entity(self, var: Variable) -> WorldEntity:
        if var.name not in self._entities:
            self._entities[var.name] = WorldEntity.create(var)

        return self._entities[var.name]

    def _get_room(self, var: Variable) -> WorldRoom:
        entity = self._get_entity(var)
        assert isinstance(entity, WorldRoom)
        return entity

    def _get_object(self, var: Variable) -> WorldObject:
        entity = self._get_entity(var)
        assert isinstance(entity, WorldObject)
        return entity

    def _update(self) -> None:
        """ Update the internal representation of the world.

        This method will create new entities based on facts. It should be called whenever
        backing facts are changed.
        """
        self._entities = OrderedDict()  # Clear entities.
        self.player = self._get_entity(Variable("P"))
        self.inventory = self._get_entity(Variable("I"))
        self._player_room = None
        self._process_rooms()
        self._process_objects()
        self._rooms = [entity for entity in self._entities.values() if isinstance(entity, WorldRoom)]
        self._objects = [entity for entity in self._entities.values() if isinstance(entity, WorldObject)]

        self._entities_per_type = defaultdict(list)
        for entity in self._entities.values():
            self._entities_per_type[entity.type].append(entity)

    def _process_rooms(self) -> None:
        for fact in self.facts:
            if not KnowledgeBase.default().types.is_descendant_of(fact.arguments[0].type, 'r'):
                continue  # Skip non room facts.

            room = self._get_room(fact.arguments[0])
            room.add_related_fact(fact)

            if fact.name.endswith("_of"):
                # Handle room positioning facts.
                exit = reverse_direction(fact.name.split("_of")[0])
                dest = self._get_room(fact.arguments[1])
                dest.add_related_fact(fact)
                assert exit not in room.exits
                room.exits[exit] = dest

        # Handle door link facts.
        for fact in self.facts:
            if fact.name != "link":
                continue

            src = self._get_room(fact.arguments[0])
            door = self._get_object(fact.arguments[1])
            dest = self._get_room(fact.arguments[2])
            door.add_related_fact(fact)
            src.content.append(door)

            exit_found = False
            for exit, room in src.exits.items():
                if dest == room:
                    src.doors[exit] = door
                    exit_found = True
                    break

            if not exit_found:
                # Need to position both rooms w.r.t. each other.
                src_free_exits = [exit for exit in DIRECTIONS if exit not in src.exits]
                for exit in src_free_exits:
                    r_exit = reverse_direction(exit)
                    if r_exit not in dest.exits:
                        src.exits[exit] = dest
                        dest.exits[r_exit] = src
                        src.doors[exit] = door
                        exit_found = True
                        break

            # Relax the Cartesian grid constraint.
            if not exit_found:
                # Need to position both rooms w.r.t. each other.
                src_free_exits = [exit for exit in DIRECTIONS if exit not in src.exits]
                dest_free_exits = [exit for exit in DIRECTIONS if exit not in dest.exits]
                if len(src_free_exits) > 0 and len(dest_free_exits) > 0:
                    exit = src_free_exits[0]
                    r_exit = dest_free_exits[0]
                    src.exits[exit] = dest
                    dest.exits[r_exit] = src
                    src.doors[exit] = door
                    exit_found = True

            if not exit_found:  # If there is still no exit found.
                raise NoFreeExitError("Cannot connect {} and {}.".format(src, dest))

    def _process_objects(self) -> None:
        for fact in self.facts:
            if KnowledgeBase.default().types.is_descendant_of(fact.arguments[0].type, 'r'):
                continue  # Skip room facts.

            obj = self._get_entity(fact.arguments[0])
            obj.add_related_fact(fact)

            if fact.name == "match":
                other_obj = self._get_entity(fact.arguments[1])
                obj.matching_entity_id = fact.arguments[1].name
                other_obj.matching_entity_id = fact.arguments[0].name

            if fact.name in ["in", "on", "at"]:
                holder = self._get_entity(fact.arguments[1])
                holder.content.append(obj)

                if fact.arguments[0].type == "P":
                    self._player_room = holder

    def get_facts_in_scope(self) -> List[Proposition]:
        facts = []
        facts += [fact for exit in self.player_room.exits.values() for fact in exit.related_facts]
        facts += [fact for door in self.player_room.doors.values() for fact in door.related_facts]
        facts += [fact for obj in self.get_visible_objects_in(self.player_room) for fact in obj.related_facts]
        facts += [fact for obj in self.get_objects_in_inventory() for fact in obj.related_facts]

        return uniquify(facts)

    def get_visible_objects_in(self, obj: WorldObject) -> List[WorldObject]:
        if "locked" in obj.properties or "closed" in obj.properties:
            return []

        objects = list(obj.content)
        for obj in obj.content:
            objects += self.get_visible_objects_in(obj)

        return objects

    def get_all_objects_in(self, obj: WorldObject) -> List[WorldObject]:
        objects = list(obj.content)
        for obj in obj.content:
            objects += self.get_all_objects_in(obj)

        return objects

    def get_objects_in_inventory(self) -> List[WorldObject]:
        return self.inventory.content

    def get_entities_per_type(self, type: str) -> List[WorldEntity]:
        """ Get all entities of a certain type. """
        return self._entities_per_type.get(type, [])

    def find_object_by_id(self, id: str) -> Optional[WorldObject]:
        return self._entities.get(id)

    def find_room_by_id(self, id: str) -> Optional[WorldRoom]:
        return self._entities.get(id)

    def set_player_room(self, start_room: Union[None, WorldRoom, str] = None) -> None:
        if start_room is None:
            if len(self.rooms) == 0:
                start_room = WorldRoom("r_0", "r")
            else:
                start_room = self.rooms[0]

        elif start_room in self._entities:
            start_room = self._entities[start_room]
        elif isinstance(start_room, Variable) and start_room.name in self._entities:
            start_room = self._entities[start_room.name]
        else:
            raise ValueError("Unknown room: {}".format(start_room))

        self.add_fact(Proposition("at", [self.player, start_room]))

    def __eq__(self, other: Any) -> bool:
        return (isinstance(other, World) and
                self.state == other.state)

    def __hash__(self) -> int:
        return hash(frozenset(self.facts))
