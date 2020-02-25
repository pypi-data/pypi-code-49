# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure type metaclass."""

from types import FunctionType, MethodType

from plum import boost
from plum._plumtype import PlumType
from plum.structure._bitfield_member import BitFieldMember
from plum.structure._member import Member
from plum.structure._methods import __pack__, __setattr__, asdict


class MemberInfo:

    """Structure member information."""

    # pylint: disable=too-many-instance-attributes

    def __init__(self, namespace):
        annotations = namespace.get('__annotations__', {})

        self.bitfields = []
        self.member_definitions = []  # all but BitFieldMember
        self.required_parameter_names = []
        self.optional_parameter_names = []
        self.optional_parameter_defaults = []
        self.internal_parameters = []
        self.member_initializations = []
        self.default_factory_lines = []
        self.sizes = []
        self.members = {
            key: value for key, value in namespace.items() if isinstance(value, Member)}
        self.type_hints = {
            name: annotations.get(name, None) for name in self.members}

        names = [
            name for name, value in namespace.items() if isinstance(value, Member)]

        while names:
            name = names[0]
            member = self.members[name]

            if isinstance(member, BitFieldMember):
                for bitfield_name in self._process_bitfield_members(
                        names, member.cls, namespace):
                    names.remove(bitfield_name)
            else:
                self._process_member(name, member)
                names.remove(name)

        for member in self.member_definitions:
            member.adjust_members(self.members)

        for member in self.member_definitions:
            member.finalize(self.members)

        if self.sizes:
            try:
                self.nbytes = sum(self.sizes)
            except TypeError:
                # has variably sized member (member nbytes is None)
                self.nbytes = None
        else:
            # anonymous structure
            self.nbytes = None

    def _process_bitfield_members(self, names, bitfields_cls, namespace):
        actual_names = set()
        for name in names:
            member = self.members[name]
            if isinstance(member, BitFieldMember) and member.cls is bitfields_cls:
                actual_names.add(name)
            else:
                break

        if actual_names != set(bitfields_cls.__fields__):
            if len(actual_names) != len(bitfields_cls.__fields__):
                raise TypeError(
                    f'{bitfields_cls.__name__!r} bit fields must all be present '
                    f'and in one group')
            raise TypeError(
                f'{bitfields_cls.__name__!r} bit field names must match the following: '
                f'{", ".join(bitfields_cls.__fields__)}')

        bitfields_index = len(self.member_definitions)

        # add actual "hidden" member to implement the fields
        self._process_member('', Member(cls=bitfields_cls))

        for name in bitfields_cls.__fields__:
            member = self.members[name]
            member.finish_initialization(
                bitfields_index, name, self.type_hints)

            default = member.default

            if default is None:
                default = getattr(bitfields_cls, name).default

            if default is None:
                self.required_parameter_names.append(name)
            else:
                self.optional_parameter_names.append(name)
                self.optional_parameter_defaults.append(default)

            namespace[name] = member.get_accessor()

        return actual_names

    def _process_member(self, name, member):
        member_index = len(self.member_definitions)
        member.finish_initialization(member_index, name, self.type_hints)

        self.member_definitions.append(member)

        if name:
            self.member_initializations.append(name)
            if member.default is None:
                self.required_parameter_names.append(name)
            else:
                if isinstance(member.default, (FunctionType, MethodType)):
                    default_index = len(self.optional_parameter_defaults)
                    self.default_factory_lines += [
                        f'',
                        f'if {member.name} is None:',
                        f'    self[{member_index}] = _defaults[{default_index}](self)',
                    ]
                self.optional_parameter_names.append(name)
                self.optional_parameter_defaults.append(member.default)
        else:
            # must be a bitfields member where init has args for individual fields
            args = ', '.join(
                f'{name}={name}' for name in member.cls.__fields__)
            self.member_initializations.append(
                f'_{member.cls.__name__}({args})')
            self.internal_parameters.append(
                f'_{member.cls.__name__}=__bitfields__[{len(self.bitfields)}]')
            self.bitfields.append(member.cls)

        self.sizes.append(member.cls.__nbytes__)

    @property
    def is_fast_candidate(self):
        """plum.boost acceleration support indication.

        :returns: indication if plum.boost supports member variations
        :rtype: bool

        """
        return bool(self.member_definitions)

    def make_init(self):
        """Construct __init__ method.

        :return: method source code
        :rtype: str

        """
        parameters = list(self.required_parameter_names)

        for index, (name, default) in enumerate(zip(
                self.optional_parameter_names, self.optional_parameter_defaults)):

            if isinstance(default, (FunctionType, MethodType)):
                parameters.append(f'{name}=None')
            else:
                parameters.append(f'{name}=__defaults__[{index}]')

        parameters += self.internal_parameters

        if self.default_factory_lines:
            parameters += ['_defaults=__defaults__']

        lines = [f'def __init__(self, {", ".join(parameters)}):']

        if len(self.member_initializations) == 1:
            lines += [f'list.append(self, {self.member_initializations[0]})']
        else:
            init_values = ', '.join(self.member_initializations)
            lines += [f'list.extend(self, ({init_values}))']

        lines += self.default_factory_lines

        # print('\n    '.join(lines))
        return '\n    '.join(lines)

    def make_compare(self, name):
        """Construct comparision method.

        :param str name: method name ("__eq__" or "__ne__")
        :return: method source code
        :rtype: str

        """
        indices = [i for i, member in enumerate(self.member_definitions) if not member.ignore]

        compare = EXAMPLE_COMPARE.replace('__eq__', name)

        unpack_expression = ', '.join(
            f's{i}' if i in indices else '_' for i in range(len(self.member_definitions)))

        compare = compare.replace('s0, _, s2, _', unpack_expression)
        compare = compare.replace('o0, _, o2, _', unpack_expression.replace('s', 'o'))

        if name == '__eq__':
            return_logic = ' and '.join(
                ['len(self) == len(other)'] + [f'(s{i} == o{i})' for i in indices])
        else:
            return_logic = ' or '.join(
                ['len(self) != len(other)'] + [f'(s{i} != o{i})' for i in indices])

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
        names = tuple(member.name for member in member_info.member_definitions)
        types = tuple(member.cls for member in member_info.member_definitions)

        namespace['__nbytes__'] = nbytes
        namespace['__names_types__'] = (names, types)
        namespace['__defaults__'] = tuple(member_info.optional_parameter_defaults)
        namespace['__bitfields__'] = tuple(member_info.bitfields)

        is_fast_candidate = boost and member_info.is_fast_candidate

        if member_info.members:
            # pylint: disable=exec-used

            # create custom __init__ within class namespace
            if '__init__' not in namespace:
                exec(member_info.make_init(), globals(), namespace)

            if any(member.ignore for member in member_info.member_definitions):
                # create custom __eq__ and __ne__ within class namespace
                if '__eq__' not in namespace:
                    exec(member_info.make_compare('__eq__'), globals(), namespace)
                if '__ne__' not in namespace:
                    exec(member_info.make_compare('__ne__'), globals(), namespace)

            # install member accessors (in some cases its the same member definition, in
            # other cases member definition returns a custom accessor)
            for member in member_info.member_definitions:
                if member.name:
                    namespace[member.name] = member.get_accessor()

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

            if '__setattr__' not in namespace:
                namespace['__setattr__'] = __setattr__

            namespace['__plum_names__'] = names

        del namespace['__defaults__']
        del namespace['__bitfields__']

        cls = super().__new__(mcs, name, bases, namespace)

        if is_fast_candidate:
            # attach binary string containing plum-c accelerator "C" structure
            # (so structure memory de-allocated when class deleted)
            cls.__plum_c_internals__ = boost.faststructure.add_c_acceleration(
                cls, -1 if nbytes is None else nbytes, len(types), types)

        return cls
