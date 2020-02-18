"""Useful objects that help solve common problems for yeahyeah_plugins, such as generating lists of actions and persisting
these lists

Anything above core yeahyeah functionality that can potentially be used by multiple yeahyeah_plugins
"""
import collections
import yaml


class YeahYeahMenuItem:
    """Something you can add to the base yeahyeah menu and then launch"""

    def __init__(self, name, help_text=None):
        """

        Parameters
        ----------
        name: str
            Name to launch this item with, probably you want to keep this short.
        help_text: str, optional
            Short help message for this item. Defaults to empty string
        """
        self.name = name
        self._help_text = help_text

    @property
    def help_text(self):
        if self._help_text is None:
            return ""
        else:
            return self._help_text

    def to_click_command(self):
        """Return a click command representation of this action

        Returns
        -------
        func
            A function that has been processed by the @click.command() decorator.
            <click_group>.add_command(test) should work

        """
        raise NotImplementedError()


class SerialisableMenuItem(YeahYeahMenuItem):
    """A menu item that you can serialise to and from a dict"""

    def get_parameters(self):
        """ Any extra parameters as dict. These are saved along with item name and help_text

        Overwrite this in child classes

        Returns
        -------
        Dict[param_name:param_value]
            Parameters for this menu item that need to be persisted
        """
        return {}

    def to_dict(self):
        """

        Returns
        -------
        Dict[str:Dict[param1,param2, etc..]]:
            [menu item key: [parameters that need to be saved]]

        """
        values = self.get_parameters()
        if self._help_text is not None:
            values["text"] = self._help_text
        return {self.name: values}

    @classmethod
    def from_dict(cls, dict_in):
        """Create an instance of this object from given dict.

        """
        name = list(dict_in.keys()).pop()
        values = dict_in[name]
        help_text = values.pop("text", None)

        return cls(name=name, help_text=help_text, **values)


class MenuItemList(collections.UserList):
    """A list-like list of menu items that can be saved to and loaded from a file"""

    # The type of objects that this list can contain
    item_classes = [SerialisableMenuItem]

    def __init__(self, items):
        """

        Parameters
        ----------
        items: List[SerialisableMenuItem]
            The items to put in this list
        """
        self.data = items

    @property
    def items(self):
        """I find 'items' more descriptive then 'data' """
        return self.data

    def save(self, file):
        """Save list to file

        Parameters
        ----------
        file: Open file handle
            save to this file

        Returns
        -------

        """
        yaml.dump(self.to_dict(), file, default_flow_style=False)

    @classmethod
    def load(cls, file):
        """Try to parse the given file's content into any of the classes in cls.item_classes.

        Parameters
        ----------
        file: open file handle

        Returns
        -------
        MenuItemList
            List of items represented in file

        Raises
        ------
        MenuItemLoadError:
            When object loaded is not a list or when contents could not be parsed as any of the item_classes


        """

        loaded = yaml.load(file, Loader=yaml.loader.Loader)

        if type(loaded) is not dict:
            msg = f"Expected to load a dictionary, but found {type(loaded)} instead"
            raise MenuItemLoadError(msg)
        # flatten to list of dicts
        item_list = []
        for key, values in loaded.items():
            item_as_dict = {key: values}
            for ItemClass in cls.item_classes:
                try:
                    item_instance = ItemClass.from_dict(item_as_dict)
                    break
                except TypeError:
                    item_instance = None
                    continue
            if not item_instance:
                msg = f"Could not create any object from {item_as_dict}. Tried {[str(x) for x in cls.item_classes]}.."
                raise MenuItemLoadError(msg)
            else:
                item_list.append(item_instance)

        return cls(items=item_list)

    def to_dict(self):
        """This list as dict, as terse as possible:

        {pattern_name1: {param1: value1,...},
         pattern_name2: {param2: value2,...},

         Notes
         -----
         This function is mainly to make yaml dump something readable to file. Dict of dict renders quite well
        """
        result = {}
        for item in self.data:
            pattern_dict = item.to_dict()
            result.update(pattern_dict)

        return result


class MenuItemLoadError(Exception):
    pass
