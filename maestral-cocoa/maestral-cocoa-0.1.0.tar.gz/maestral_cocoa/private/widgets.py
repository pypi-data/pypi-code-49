# -*- coding: utf-8 -*-
"""
@author: Sam Schott  (ss2151@cam.ac.uk)

(c) Sam Schott; This work is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivs 2.0 UK: England & Wales License.

"""

import click

import toga
from toga.handlers import wrapped_handler
from toga.widgets.base import Widget
from toga.icons import Icon
from toga.style.pack import Pack
from toga.constants import ROW, RIGHT
from toga_cocoa.libs import at

from maestral_cocoa.utils import clear_background
from . import factory as private_factory
from .constants import (
    ON, MIXED,
    TRUNCATE_TAIL, VisualEffectMaterial,
    NSWindowAnimationBehaviorDefault, NSWindowAnimationBehaviorAlertPanel,
)


# ==== layout widgets ====================================================================

class Spacer(toga.Box):
    """A widget to take up space and push others to the side."""

    def __init__(self, direction=ROW):
        style = Pack(flex=1, direction=direction)
        super().__init__(style=style)
        clear_background(self)


class VibrantBox(Widget):
    """A macOS style vibrant box, to be used as translucent window background."""

    def __init__(self, id=None, style=None, children=None, material=VisualEffectMaterial.UnderWindowBackground, factory=private_factory):
        super().__init__(id=id, style=style, factory=factory)
        self._children = []
        if children:
            for child in children:
                self.add(child)

        self._material = material
        self._impl = self.factory.VibrantBox(interface=self)

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, matertial):
        self._matrial = matertial
        self._impl.set_material(matertial)


# ==== buttons ===========================================================================

class DialogButtons(toga.Box):
    """
    A dialog button box. Buttons will be created from the given list of labels (defualts
    to ['Ok', 'Cancel']). If a callback ``on_press`` is provided, will be executed if any
    button is pressed, with the label of the respective button as an argument.

    :param labels: An iterable of label strings.
    :param str default: A default button to select. Value must match one of the labels
    :param on_press: Callback when any button is pressed. Takes the button
        label as argument.
    """

    MIN_BUTTON_WIDTH = 80

    def __init__(self, labels=('Ok', 'Cancel'), default='Ok', on_press=None, id=None, style=None, factory=None):
        super().__init__(id=id, style=style, factory=factory)

        self.on_press = on_press
        self._buttons = []

        # always display buttons in a row, to the right
        self.style.update(direction=ROW)
        self.add(Spacer())

        for label in labels[::-1]:
            style = Pack(padding_left=10, alignment=RIGHT)
            btn = toga.Button(label=label, on_press=self._on_press, style=style)
            self.add(btn)
            self._buttons.insert(0, btn)

            btn.style.width = max(self.MIN_BUTTON_WIDTH, btn.intrinsic.width.value)

        if default:
            try:
                default_index = labels.index(default)
                self._buttons[default_index]._impl.native.keyEquivalent = at('\r')
            except ValueError:
                pass

        clear_background(self)

    def _on_press(self, widget):
        if self.on_press:
            self.on_press(widget.label)

    def __getitem__(self, item):
        return next(btn for btn in self._buttons if btn.label == item)

    @property
    def enabled(self):
        return any(btn.enabled for btn in self)

    @enabled.setter
    def enabled(self, yes):
        for btn in self._buttons:
            btn.enabled = yes


class Switch(toga.Switch):
    """Reimplements toga.Switch to allow *programmatic* setting of
    an intermediate state."""

    def __init__(self, label, id=None, style=None, on_toggle=None, is_on=False, enabled=True, factory=private_factory):
        super().__init__(label, id, style, on_toggle, is_on, enabled, factory)

    @property
    def state(self):
        """Button state: 0 = off, 1 = mixed, 2 = on."""
        return self._impl.get_state()

    @state.setter
    def state(self, value):
        """Setter: Button state: 0 = off, 1 = mixed, 2 = on."""
        self._impl.set_state(value)

    @property
    def on_toggle(self):
        return self._on_toggle

    @on_toggle.setter
    def on_toggle(self, handler):

        def new_handler(*args, **kwargs):
            if self.state == MIXED:
                self.state = ON
            if handler:
                handler(*args, **kwargs)

        self._on_toggle = wrapped_handler(self, new_handler)
        self._impl.set_on_toggle(self._on_toggle)


class FollowLinkButton(Widget):
    """A macOS style 'follow link' button that takes you to a file or web URL."""

    def __init__(self, label, url=None, locate=False, id=None, style=None, enabled=True, factory=private_factory):
        super().__init__(id=id, enabled=enabled, style=style, factory=factory)

        # Create a platform specific implementation of a Button
        self._impl = self.factory.FollowLinkButton(interface=self)

        # Set all the properties
        self.locate = locate
        self.label = label
        self.url = url

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        if value is None:
            self._label = ''
        else:
            self._label = str(value)
        self._impl.set_label(value)
        self._impl.rehint()

    def on_press(self, handler):
        click.launch(self.url, locate=self.locate)


class Selection(toga.Selection):

    def __init__(self, id=None, style=None, items=None, on_select=None, enabled=True, factory=private_factory):
        super().__init__(id, style, items, on_select, enabled, factory)


# ==== labels ============================================================================

class Label(toga.Label):
    """Reimplements toga.Label with text wrapping."""

    def __init__(self, text, linebreak_mode=TRUNCATE_TAIL, id=None, style=None, factory=private_factory):
        self._linebreak_mode = linebreak_mode
        super().__init__(text, id=id, style=style, factory=factory)
        self.linebreak_mode = linebreak_mode

    @property
    def linebreak_mode(self):
        return self._linebreak_mode

    @linebreak_mode.setter
    def linebreak_mode(self, value):
        self._linebreak_mode = value
        self._impl.set_linebreak_mode(value)


class RichMultilineTextInput(toga.MultilineTextInput):
    """A multiline text view with html support."""

    MIN_HEIGHT = 100
    MIN_WIDTH = 100

    def __init__(self, id=None, style=None, factory=private_factory,
                 html='', readonly=False, placeholder=None):
        super().__init__(id=id, style=style, readonly=readonly,
                         placeholder=placeholder, factory=factory)

        # Create a platform specific implementation of a Label
        self._impl = self.factory.RichMultilineTextInput(interface=self)
        self.html = html

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._html = value
        self._impl.set_html(value)


class RichLabel(Widget):
    """A label with html support."""

    MIN_HEIGHT = 17
    MIN_WIDTH = 50

    def __init__(self, html, id=None, style=None, factory=private_factory):
        super().__init__(id=id, style=style, factory=factory)

        # Create a platform specific implementation of a Label
        self._impl = self.factory.RichLabel(interface=self)
        self.html = html

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._html = value
        self._impl.set_html(value)


# ==== icons =============================================================================

class IconForPath(toga.Icon):
    """
    Reimplements toga.Icon to provide the icon for the file / folder type
    instead of loading an icon from the file content.

    :param path: File to path.
    """

    def __init__(self, path, system=False):
        super().__init__(path, system)

    def bind(self, factory):
        if self._impl is None:
            self._impl = private_factory.IconForPath(interface=self, path=self.path)

        return self._impl


# ==== menus and menu items ==============================================================

class MenuItem:
    """
    A menu item to be used in a Menu.

    Args:
        label: A label for the item.
        icon: (optional) a path to an icon resource to decorate the item.
        action: (optional) a function to invoke when the item is clicked.
        submenu: A Menu to use as a submenu. It will become visible when this item is clicked.
        factory: A python module that is capable to return a implementation of this class with the same name. (optional & normally not needed).
    """
    def __init__(self, label, icon=None, cheackable=False, action=None, submenu=None, factory=private_factory):
        self.factory = factory
        self._impl = self.factory.MenuItem(interface=self)

        self._cheackable = cheackable
        self.action = action
        self.label = label
        self.icon = icon
        self.enabled = self.action is not None
        self.submenu = submenu

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value
        if self._impl is not None:
            self._impl.set_enabled(value)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon_or_name):
        if isinstance(icon_or_name, Icon) or icon_or_name is None:
            self._icon = icon_or_name
        else:
            self._icon = Icon(icon_or_name)

        self._impl.set_icon(self._icon)

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label
        self._impl.set_label(label)

    @property
    def submenu(self):
        return self._submenu

    @submenu.setter
    def submenu(self, submenu):
        self._submenu = submenu
        if submenu:
            self._impl.set_submenu(submenu._impl)
        else:
            self._impl.set_submenu(None)

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):

        if self._cheackable:
            def new_action(*args):
                self.checked = not self.checked
                action(args)
        else:
            new_action = action

        self._action = wrapped_handler(self, new_action)
        self._impl.set_action(self._action)

    @property
    def checked(self):
        return self._checked

    @checked.setter
    def checked(self, yes):
        if self._cheackable:
            self._checked = yes
            self._impl.set_checked(yes)


class MenuItemSeparator:
    """A horizontal separator between menu items."""
    def __init__(self, factory=private_factory):
        self.factory = factory
        self._impl = self.factory.MenuItemSeparator(self)


class Menu:
    """
    A menu, to be used as context menu, status bar menu or in the menu bar.

    Args:
        items: A list of MenuItem.
    """

    def __init__(self, items=None, factory=private_factory):
        self.factory = factory
        self._items = []

        self._impl = self.factory.Menu(self)

        if items:
            self.add(*items)

    def add(self, *items):
        """Add in MenuItems to the menu."""
        self._items += items
        for item in items:
            self._impl.add_item(item._impl)

    def insert(self, index, item):
        """Add in MenuItems to the menu."""
        if item not in self._items:
            self._items.insert(index, item)
            self._impl.insert_item(index, item._impl)

    def remove(self, *items):
        """Remove MenuItems from the menu."""
        for item in items:
            try:
                self._items.remove(item)
            except ValueError:
                pass
            else:
                self._impl.remove_item(item._impl)

    def clear(self):
        """Clear the menu (removes all items)"""
        for item in self.items:
            self._impl.remove_item(item._impl)
        self._items.clear()

    @property
    def items(self):
        """All MenuItems in the menu."""
        return self._items

    @property
    def visible(self):
        """True if the menu is currently visible."""
        return self._impl.visible


# ==== StatusBarItem =====================================================================

class StatusBarItem:
    """A status bar item which can have an icon and a menu."""

    def __init__(self, icon, menu=None, factory=private_factory):
        self.factory = factory
        self._impl = self.factory.StatusBarItem(self)

        self.icon = icon
        self.menu = menu

    @property
    def menu(self):
        return self._menu

    @menu.setter
    def menu(self, menu):
        self._menu = menu
        if menu:
            self._impl.set_menu(menu._impl)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon_or_name):
        if isinstance(icon_or_name, Icon) or icon_or_name is None:
            self._icon = icon_or_name
        else:
            self._icon = Icon(icon_or_name)

        self._impl.set_icon(self._icon)


# ==== Custom Window =====================================================================

class Window(toga.Window):

    def __init__(self, id=None, title=None, position=None, size=(640, 480),
                 toolbar=None, resizeable=True, closeable=True, minimizable=True, release_on_close=True, app=None, factory=None):
        intial_position = position or (100, 100)
        super().__init__(id, title, intial_position, size, toolbar, resizeable, closeable, minimizable, factory)
        if app:
            self.app = app

        self._impl.native.releasedWhenClosed = release_on_close
        self.is_dialog = False

        if not position:
            self.center()

    # visibility and positioning
    @property
    def visible(self):
        return bool(self._impl.native.isVisible)

    def center(self):
        self._impl.native.center()

    def raise_(self):
        self.show()
        self._impl.native.orderFrontRegardless()
        if self.app:
            self.app._impl.native.activateIgnoringOtherApps(True)

    def hide(self):
        self._impl.native.orderOut(None)

    # sheet support

    def show_as_sheet(self, window):
        window._impl.native.beginSheet(self._impl.native, completionHandler=None)

    # application modal support

    def runModal(self):
        self.raise_()
        return self.app._impl.native.runModalForWindow(self._impl.native)

    def stopModal(self, res=0):
        if self.app._impl.native.modalWindow == self._impl.native:
            self.app._impl.native.stopModalWithCode(res)

    # close with handling sheet session

    def close(self):
        if self._impl.native.sheetParent:
            self._impl.native.sheetParent.endSheet(self._impl.native)

        self._impl.native.close()

    @property
    def release_on_close(self):
        return self._impl.native.releasedWhenClosed

    @release_on_close.setter
    def release_on_close(self, value):
        self._impl.native.releasedWhenClosed = value

    @property
    def is_dialog(self):
        return self._is_dialog

    @is_dialog.setter
    def is_dialog(self, yes):
        self._is_dialog = yes
        animation = NSWindowAnimationBehaviorAlertPanel if yes else NSWindowAnimationBehaviorDefault
        self._impl.native.animationBehavior = animation


# ==== Application =======================================================================

class SystemTrayApp(toga.App):

    def __init__(self, formal_name=None, app_id=None, app_name=None, id=None, icon=None,
                 author=None, version=None, home_page=None, description=None, startup=None,
                 on_exit=None, factory=private_factory):
        super().__init__(formal_name, app_id, app_name, id, icon, author, version,
                         home_page, description, startup, on_exit, factory)

    def _create_impl(self):
        return self.factory.SystemTrayApp(interface=self)
