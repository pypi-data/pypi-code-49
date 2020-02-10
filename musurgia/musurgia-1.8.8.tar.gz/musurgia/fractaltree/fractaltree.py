import itertools

from quicktions import Fraction

from musurgia.permutation import LimitedPermutation, permute
from musurgia.tree import Tree


class FractalTreeException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ValueCannotBeChanged(FractalTreeException):
    def __init__(self, *args):
        super().__init__(*args)


class SetValueFirst(FractalTreeException):
    def __init__(self, *args):
        super().__init__('FractalTree().value must be set before add_layer()', *args)


class FractalTree(Tree):
    def __init__(self, value=None, proportions=None, tree_permutation_order=None, multi=None, fertile=True,
                 reading_direction='horizontal', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = None
        self._proportions = None
        self._tree_permutation_order = None
        self._multi = None
        self._permutation_order = None
        self._fertile = None
        self._reading_direction = None
        self._fractal_order = None
        self._children_fractal_values = None
        self._name = None

        self.proportions = proportions
        self.tree_permutation_order = tree_permutation_order
        self.value = value
        self.multi = multi
        self.fertile = fertile
        self.reading_direction = reading_direction

    @property
    def proportions(self):
        return self._proportions

    @proportions.setter
    def proportions(self, values):
        if values is None:
            values = [1, 2, 3]
        self._proportions = [Fraction(Fraction(value) / Fraction(sum(values))) for value in values]

    @property
    def tree_permutation_order(self):
        return self._tree_permutation_order

    @tree_permutation_order.setter
    def tree_permutation_order(self, values):
        if values is None:
            values = [3, 1, 2]
        self._tree_permutation_order = values
        self._permutation_order = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if val:
            val = Fraction(val)
        if self._value:
            if self.is_root and not self.get_children():
                self._value = val
            else:
                raise ValueCannotBeChanged(
                    'FractalTree().value can only be changed for the root with no children. Use change_value() for other cases.'
                )
        else:
            self._value = val

        if self._value == 0:
            self.fertile = False

    @property
    def multi(self):
        return self._multi

    @multi.setter
    def multi(self, vals):
        if vals is None:
            vals = (1, 1)

        elif not isinstance(vals, tuple) or len(vals) != 2:
            raise TypeError('multi has to be a tuple with a length of 2')

        m_1 = vals[0]
        m_2 = vals[1]
        m_1, m_2 = (((m_1 - 1) % self.size) + 1 + ((m_2 - 1) // self.size)) % self.size, (
                (m_2 - 1) % self.size) + 1
        if m_1 == 0:
            m_1 = self.size
        self._multi = (m_1, m_2)

        self._permutation_order = None

    @property
    def fertile(self):
        return self._fertile

    @fertile.setter
    def fertile(self, val):
        if not isinstance(val, bool):
            raise TypeError('fertile.value must be of type bool not{}'.format(type(val)))
        self._fertile = val

    @property
    def reading_direction(self):
        return self._reading_direction

    @reading_direction.setter
    def reading_direction(self, val):
        if self._reading_direction:
            raise FractalTreeException('reading_direction can only be set during initialisation')
        permitted = ['horizontal', 'vertical']
        if val not in permitted:
            raise ValueError('reading_direction.value {} must be in {}'.format(val, permitted))
        self._reading_direction = val

    @property
    def permutation_order(self):
        def _calculate_permutation_order():
            if self.tree_permutation_order:
                permutation = LimitedPermutation(input_list=list(range(1, self.size + 1)),
                                                 main_permutation_order=self.tree_permutation_order, multi=self.multi,
                                                 reading_direction=self.reading_direction)

                return permutation.permutation_order
            else:
                raise FractalTreeException('tree_permutation_order must be set')

        if self._permutation_order is None:
            self._permutation_order = _calculate_permutation_order()
        return self._permutation_order

    @property
    def fractal_order(self):
        return self._fractal_order

    def calculate_position_in_tree(self):
        parent = self.up
        if self.is_root:
            return 0
        else:
            index = parent.get_children().index(self)
            if index == 0:
                return parent.position_in_tree
            else:
                return parent.get_children()[index - 1].position_in_tree + parent.get_children()[index - 1].value

    @property
    def position_in_tree(self):
        return self.calculate_position_in_tree()

    @property
    def number_of_layers(self):
        if self.get_leaves() == [self]:
            return 0
        else:
            return self.get_farthest_leaf().get_distance(self)

    @property
    def name(self):
        if self._name is None:
            if self.is_root:
                self._name = '0'
            elif self.up.is_root:
                self._name = str(self.up.get_children().index(self) + 1)
            else:
                self._name = self.up.name + '.' + str(self.up.get_children().index(self) + 1)
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def __name__(self):
        return self.name

    @__name__.setter
    def __name__(self, val):
        self.name = val

    @property
    def position(self):
        if self.is_root():
            # return self.first_position
            return 0
        else:
            siblings = self.up.children
            index = siblings.index(self)
            previous_siblings = siblings[:index]
            position_in_parent = 0
            for child in previous_siblings: position_in_parent += child.value
            return position_in_parent + self.up.position

    @property
    def children_fractal_values(self):
        if not self._children_fractal_values:
            self._children_fractal_values = self._calculate_children_fractal_values()
        return self._children_fractal_values

    def _calculate_children_fractal_orders(self):
        if self.value and self.proportions:
            children_fractal_orders = range(1, self.size + 1)
            permutation_order = self.permutation_order
            if permutation_order:
                children_fractal_orders = permute(children_fractal_orders, permutation_order)
            return children_fractal_orders

    @property
    def children_fractal_orders(self):
        return self._calculate_children_fractal_orders()

    def _calculate_children_fractal_values(self):
        value = self.value
        if value and self.proportions:
            children_fractal_values = [value * prop for prop in self.proportions]
            if self.permutation_order:
                try:
                    children_fractal_values = permute(children_fractal_values, self.permutation_order)
                except ValueError:
                    raise ValueError('proportions and tree_permutation_order should have the same length')
            return children_fractal_values

    @property
    def size(self):
        return len(self.proportions)

    def _child_multi(self, parent, index):
        number_of_children = self.size
        multi_first = sum(parent.multi) % number_of_children
        if multi_first == 0:
            multi_first = number_of_children
        ch_multi = (multi_first, index + 1)
        return ch_multi

    def add_self(self):
        leaves = self.get_leaves()
        for leaf in leaves:
            new_node = self.copy()
            new_node._up = self
            new_node._fractal_order = self.fractal_order
            leaf.add_child(new_node)

    def add_layer(self, *conditions):
        if self.value is None:
            raise SetValueFirst()

        leaves = list(self.traverse_leaves())
        if not leaves:
            leaves = [self]

        if conditions:
            for leaf in leaves:
                for condition in conditions:
                    if not condition(leaf):
                        leaf.fertile = False
                        break

        for leaf in leaves:
            if leaf.fertile is True:
                for i in range(leaf.size):
                    new_node = leaf.copy()
                    new_node.value = leaf.children_fractal_values[i]
                    new_node.multi = self._child_multi(leaf, i)
                    leaf.add_child(new_node)
                    new_node._fractal_order = leaf.children_fractal_orders[i]

            else:
                pass

    def get_layer(self, layer, key=None):
        if layer <= self.get_root().number_of_layers:
            branch_distances = []
            for child in self.get_children():
                branch_distances.append(child.get_farthest_leaf().get_distance())
            if layer == 0:
                if key:
                    return [getattr(self, key)]
                else:
                    return [self]

            if layer >= 1:
                output = []
                if not branch_distances:
                    output.extend(self.get_layer(layer=layer - 1, key=key))
                for i in range(len(self.get_children())):
                    child = self.get_children()[i]
                    if branch_distances[i] == 1:
                        if key:
                            output.append(getattr(child, key))
                        else:
                            output.append(child)
                    else:
                        if layer == 1:
                            output.extend(child.get_layer(layer - 1, key))
                        else:
                            output.append(child.get_layer(layer - 1, key))

                return output
        else:
            err = 'max layer number=' + str(self.number_of_layers)
            raise ValueError(err)

    def _change_children_value(self, factor):
        for child in self.get_children():
            # child_delta = Fraction(delta, len(self.get_children()))
            child._value *= factor
            child._change_children_value(factor)

    def change_value(self, new_value):
        if not new_value:
            new_value = Fraction(new_value)
        if not self.value:
            self.value = new_value
        else:
            factor = Fraction(new_value, self.value)
            self._value = new_value
            for node in reversed(self.get_branch()[:-1]):
                node._value = sum([child.value for child in node.get_children()])

            self._change_children_value(factor)

    @property
    def layers(self):
        return [self.get_layer(i) for i in range(self.number_of_layers + 1)]

    @property
    def next(self):
        if not self.is_leaf():
            raise Exception('FractalTree().next property can only be used for leaves')
        else:
            try:

                parent = self.up
                while parent is not None:
                    parent_leaves = list(parent.traverse_leaves())
                    index = parent_leaves.index(self)
                    try:
                        return parent_leaves[index + 1]
                    except IndexError:
                        parent = parent.up
                raise IndexError()
            except IndexError:
                return None

    def get_previous_leaf(self):
        if not self.is_leaf():
            raise Exception('FractalTree().get_previous_leaf  can only be applied to leaves')
        try:
            parent = self.up
            while parent is not None:
                parent_leaves = list(parent.traverse_leaves())
                index = parent_leaves.index(self)
                try:
                    return parent_leaves[index - 1]
                except IndexError:
                    parent = parent.up
            raise IndexError()
        except IndexError:
            return None

    def get_previous_sibling(self):
        try:
            siblings = self.up.get_children()
            index = siblings.index(self)
            if index == 0:
                return None
            return siblings[index - 1]
        except AttributeError:
            return None

    def get_next_sibling(self):
        try:
            siblings = self.up.get_children()
            index = siblings.index(self)
            return siblings[index + 1]
        except (IndexError, AttributeError):
            return None

    def split(self, *proportions):

        for prop in proportions:
            self.add_self()
            self.get_children()[-1].value = self.value * prop / sum(proportions)

    def _reduce(self):
        sisters = self.get_siblings()

        if not sisters:
            raise Exception('no reduction possible without sisters')
        else:

            non_zero_sisters = [sister for sister in sisters if sister.value != 0]

            if non_zero_sisters:
                addition = self.value / len(non_zero_sisters)
                for sister in non_zero_sisters:
                    if sister.value != 0:
                        sister._value += addition
                self._value = 0

    def reduce_children(self, condition):

        for child in self.get_children():
            if condition(child):
                child._reduce()

        to_be_detached = [child for child in self.get_children() if condition(child)]
        for child in to_be_detached:
            child.detach()

        self._children_fractal_values = [child.value for child in self.get_children()]

    def _check_merge_nodes(self, nodes):
        return True

    def merge_children(self, *lengths):
        children = self.get_children()
        if not children:
            raise Exception('there are no children to be merged')
        if sum(lengths) != len(children):
            raise ValueError(
                'sum of lengths {} must be the same as length of children {}'.format(sum(lengths), len(children)))

        def _merge(nodes):
            self._check_merge_nodes(nodes)

            node_values = [node.value for node in nodes]

            nodes[0]._value = sum(node_values)
            for node in nodes[1:]:
                self.remove_child(node)

        iter_children = iter(children)
        chunks = [list(itertools.islice(iter_children, l)) for l in lengths]

        for chunk in chunks:
            _merge(chunk)

    def _get_merge_lengths(self, number_of_children, merge_index):
        if 0 > merge_index > self.size - 1:
            raise ValueError('generate_children.merge_index {} not valid'.format(merge_index))
        if number_of_children > self.size or number_of_children < 0:
            raise ValueError(
                'generate_children.number_of_children {} must be a positive int'.format(number_of_children))
        if number_of_children == 1:
            return [self.size]

        lengths = self.size * [1]
        pointer = merge_index
        sliced_lengths = [lengths[:pointer], lengths[pointer:]]

        if not sliced_lengths[0]:
            sliced_lengths = sliced_lengths[1:]

        while len(sliced_lengths) < number_of_children and len(sliced_lengths[0]) > 1:
            temp = sliced_lengths[0]
            sliced_lengths[0] = temp[:-1]
            sliced_lengths.insert(1, temp[-1:])

        while len(sliced_lengths) < number_of_children and len(sliced_lengths[pointer]) > 1:
            temp = sliced_lengths[pointer]
            sliced_lengths[pointer] = temp[:-1]
            sliced_lengths.insert(pointer + 1, temp[-1:])

        sliced_lengths = [len(x) for x in sliced_lengths]

        return sliced_lengths

    def generate_children(self, number_of_children, mode='reduce', merge_index=0):

        permitted_modes = ['reduce', 'merge']
        if mode not in permitted_modes:
            raise ValueError('generate_children.mode {} must be in{}'.format(mode, permitted_modes))
        if isinstance(number_of_children, int):
            if number_of_children == 0:
                pass
            if number_of_children > self.size or number_of_children < 0:
                raise ValueError(
                    'generate_children.number_of_children {} must be a positive int'.format(number_of_children))
            else:
                self.add_layer()
                if mode == 'reduce':
                    self.reduce_children(
                        lambda child: child.fractal_order < self.size - number_of_children + 1)
                else:
                    merge_lengths = self._get_merge_lengths(number_of_children, merge_index)
                    self.merge_children(*merge_lengths)

        elif isinstance(number_of_children, tuple):
            self.generate_children(len(number_of_children), mode=mode, merge_index=merge_index)

            for index, child in enumerate(self.get_children()):
                if mode == 'reduce':
                    number_of_grand_children = number_of_children[
                        child.fractal_order - child.size + len(number_of_children) - 1]
                else:
                    number_of_grand_children = number_of_children[index]
                child.generate_children(number_of_grand_children, mode=mode, merge_index=merge_index)

        else:
            raise TypeError()

    def copy(self):
        return self.__class__(value=self.value, proportions=self.proportions,
                              tree_permutation_order=self.tree_permutation_order, multi=self.multi,
                              reading_direction=self.reading_direction, fertile=self.fertile)

    # def copy_without_children(self):

    def __deepcopy__(self, memodict={}):
        copied = self.__class__(value=self.value, proportions=self.proportions,
                                tree_permutation_order=self.tree_permutation_order, multi=self.multi,
                                reading_direction=self.reading_direction, fertile=self.fertile)
        copied._fractal_order = self.fractal_order
        copied._name = self._name
        for child in self.get_children():
            copied.add_child(child.__deepcopy__())
        return copied
