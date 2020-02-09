from collections import UserDict, OrderedDict


class Type:
    __types__ = (
        (int, float, str, bool),
        (list, tuple, set, frozenset)
    )

    @staticmethod
    def is_type(item: any) -> type:
        return item if isinstance(item, type) else type(item)

    @staticmethod
    def is_list(item: any) -> bool:
        if isinstance(item, Type.__types__[1]):
            return True
        else:
            return False


class Item(Type):
    """ Converting an item type to type from a related subset of types. """
    __mempty__ = None

    def __init__(self, item: any):
        if item != self.__mempty__:
            self._type = self.is_type(item)
            self._set = [s for s in self.__types__ if self._type in s][0]
        self.data = item

    def __add__(self, operand: any) -> any:
        """ Converting operand to type(self). """
        if self.data == self.__mempty__:
            return operand
        elif operand == self.__mempty__ or isinstance(operand, type):
            return self.data
        elif self.is_list(self.data) and self.data:
            return self._type(
                [
                    self._type_by_index(index)(i)
                    if not isinstance(i, type) else i
                    for index,i in enumerate(list(operand))
                ]
            )
        elif not self.is_type(operand) in self._set:
            raise TypeError
        else:
            return self._type(operand)

    def _type_by_index(self, index: int) -> type:
        if index >= len(self.data):
            return self.is_type(list(self.data)[0])
        return self.is_type(list(self.data)[index])


class Dict(Type, UserDict):
    """ Wrapper to build a dictionary processing chain.

    (+) - atomic update values ​​of the first dictionary
    to values ​​from second dictionary with support recursive processing
    nested dictionaries.
    """

    __mempty__ = dict()
    __supported_classes__ = (dict, OrderedDict, UserDict)

    def fmap(self, f: type) -> dict:
        """ Applies function to each pair of key values ​​in dict. """
        return Dict([f(k,v) for k,v in self.items()])

    def bind(self, f: type) -> dict:
        """ Applies function to object. """
        return f(self)

    def do(self, *args: [type]) -> dict:
        acc = args[0](self)
        for obj in args[1:]:
            acc = acc.bind(obj)
        return acc

    def __add__(self, operand: dict) -> dict:
        if operand == self.__mempty__:
            return self.data
        elif self.data == self.__mempty__:
            return operand

        return self.fmap(lambda k,v:
            (k, Dict(v) + operand.get(k, self.__mempty__))
            if self.is_dict(v) else
            (k, Item(v) + operand.get(k, Item.__mempty__))
        )

    @staticmethod
    def is_dict(obj: any) -> bool:
        return isinstance(obj, Dict.__supported_classes__ + (Dict,))
