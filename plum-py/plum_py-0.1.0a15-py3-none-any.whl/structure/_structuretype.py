# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure type metaclass."""

import operator

from plum import boost
from plum._plumtype import PlumType
from plum.structure._member import Member
from plum.structure._methods import __pack__, __setattr__, asdict


class MemberInfo:

    """Structure member information."""

    def __init__(self, namespace):

        nbytes = 0
        annotations = namespace.get('__annotations__', {})

        members = {}

        for name, member in namespace.items():

            # may be a subclass with other class attributes besides member definitions
            if not isinstance(member, Member):
                continue

            members[name] = member.finish_initialization(len(members), name, annotations)

            try:
                nbytes += member.cls.__nbytes__
            except (TypeError, AttributeError):
                # set overall size as "varies"
                # TypeError -> one or the other is None
                # AttributeError -> variably typed member
                nbytes = None

        for member in members.values():
            member.adjust_members(members)

        for member in members.values():
            member.finalize(members)

        self.members = list(members.values())
        self.nbytes = nbytes if members else None

    @property
    def is_fast_candidate(self):
        """plum.boost acceleration support indication.

        :returns: indication if plum.boost supports member variations
        :rtype: bool

        """
        # FUTURE - support touchups in fast
        members = self.members
        return bool(members) and all(not member.touched_up for member in members)

    @property
    def parameters(self):
        """__init__ method parameters source.

        :returns: method parameters
        :rtype: str

        """
        parameters = []

        force_default = False

        for i, member in enumerate(self.members):
            if force_default or member.touched_up or member.default is not None:
                force_default = True
                parameters.append(f'{member.name}=__defaults__[{i}]')
            else:
                parameters.append(member.name)

        return ', '.join(parameters)

    def make_init(self):
        """Construct __init__ method.

        :return: method source code
        :rtype: str

        """
        lines = [f'def __init__(self, {self.parameters}):']

        if len(self.members) == 1:
            lines += [f'list.append(self, {self.members[0].name})']
        else:
            arg_names = ", ".join(member.name for member in self.members)
            lines += [
                f'list.extend(self, ({arg_names}))']

        lines += ['']

        ensure_arg_value = False

        for i, member in enumerate(self.members):
            if member.default is None:
                if not member.touched_up:
                    ensure_arg_value = True
            else:
                ensure_arg_value = True

            if ensure_arg_value and member.default is None and not member.touched_up:
                lines += [
                    f'if {member.name} is None:',
                    f'    raise TypeError("__init__() missing required argument {member.name!r}")',
                    '',
                ]

        if any(member.touched_up for member in self.members):
            lines += [
                'types = self.__plum_internals__[1]',
                'setitem = list.__setitem__',
                '']

            for i, member in enumerate(self.members):
                if member.touched_up:
                    lines += [
                        f'if {member.name} is None:',
                        f'    setitem(self, {i}, types[{i}].__touchup__(self))',
                        f'',
                    ]

        return '\n    '.join(lines)

    def make_compare(self, name):
        """Construct comparision method.

        :param str name: method name (__eq__ or __ne__)
        :return: method source code
        :rtype: str

        """
        indices = [i for i, member in enumerate(self.members) if not member.ignore]

        compare = EXAMPLE_COMPARE.replace('__eq__', name)

        unpack_expression = ', '.join(
            f's{i}' if i in indices else '_' for i in range(len(self.members)))

        compare = compare.replace('s0, _, s2, _', unpack_expression)
        compare = compare.replace('o0, _, o2, _', unpack_expression.replace('s', 'o'))

        if name == '__eq__':
            return_logic = ' and '.join(f'(s{i} == o{i})' for i in indices)
        else:
            return_logic = ' or '.join(f'(s{i} != o{i})' for i in indices)

        return compare.replace('(s0 == o0) and (s2 == o2)', return_logic)


# example for 4 items where 2nd and last items are ignored
EXAMPLE_COMPARE = """
def __eq__(self, other):
    if type(other) is type(self):
        s0, _, s2, _ = self
        o0, _, o2, _ = other
        return (s0 == o0) and (s2 == o2)
    else:    
        return list.__eq__(self, other)
    """.strip()


class StructureType(PlumType):

    """Structure type metaclass.

    Create custom |Structure| subclass. For example:

        >>> from plum.structure import Structure
        >>> from plum.int.little import UInt16, UInt8
        >>> class MyStruct(Structure):
        ...     m0: UInt16
        ...     m1: UInt8
        ...
        >>>

    """

    def __new__(mcs, name, bases, namespace):
        # pylint: disable=too-many-locals,too-many-branches
        member_info = MemberInfo(namespace)

        nbytes = member_info.nbytes
        names = tuple(member.name for member in member_info.members)
        types = tuple(member.cls for member in member_info.members)
        has_touchups = any(member.touched_up for member in member_info.members)

        namespace['__nbytes__'] = nbytes
        namespace['__plum_internals__'] = (names, types, has_touchups)
        namespace['__types__'] = types
        namespace['__defaults__'] = tuple(
            member.default for member in member_info.members)

        is_fast_candidate = boost and member_info.is_fast_candidate

        if member_info.members:
            # pylint: disable=exec-used

            # create custom __init__ within class namespace
            if '__init__' not in namespace:
                exec(member_info.make_init(), globals(), namespace)

            if any(member.ignore for member in member_info.members):
                # create custom __eq__ and __ne__ within class namespace
                if '__eq__' not in namespace:
                    exec(member_info.make_compare('__eq__'), globals(), namespace)
                if '__ne__' not in namespace:
                    exec(member_info.make_compare('__ne__'), globals(), namespace)

            # create member accessors
            for i, member in enumerate(member_info.members):
                if not hasattr(member, '__get__'):
                    def setitem(self, value, i=i):
                        self[i] = value
                    namespace[member.name] = property(operator.itemgetter(i)).setter(setitem)

            # calculate member offsets relative to the start of the structure
            if all([isinstance(member_cls.__nbytes__, int) for member_cls in types]):
                member_offsets = []
                cursor = 0

                for member_cls in types:
                    member_offsets.append(cursor)
                    cursor += member_cls.__nbytes__

                namespace["__offsets__"] = member_offsets

            if 'asdict' not in namespace:
                namespace['asdict'] = asdict

            if '__pack__' in namespace:
                is_fast_candidate = False
            else:
                namespace['__pack__'] = classmethod(__pack__)

            if '__unpack__' in namespace:
                is_fast_candidate = False
            else:
                namespace['__setattr__'] = __setattr__

            namespace['__plum_names__'] = names

        cls = super().__new__(mcs, name, bases, namespace)

        if is_fast_candidate:
            # attach binary string containing plum-c accelerator "C" structure
            # (so structure memory de-allocated when class deleted)
            cls.__plum_c_internals__ = boost.faststructure.add_c_acceleration(
                cls, -1 if nbytes is None else nbytes, len(types), types)

        return cls
