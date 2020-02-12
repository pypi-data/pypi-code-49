import nanome
import os
import re

MENU_PATH = os.path.join(os.path.dirname(__file__), 'json/Settings.json')
OFF_ICON_PATH = os.path.join(os.path.dirname(__file__), 'assets/off.png')
ON_ICON_PATH = os.path.join(os.path.dirname(__file__), 'assets/on.png')

class Settings():
    def __init__(self, plugin, on_close):
        self.__plugin = plugin
        self.__menu = nanome.ui.Menu.io.from_json(MENU_PATH)
        self.__menu.register_closed_callback(on_close)

        # layout node setup (bonds)
        self.__ln_btn_bonds   = self.__menu.root.find_node('Bonds Button')
        self.__img_bonds  = self.__ln_btn_bonds.create_child_node('Image')
        self.__img_bonds.forward_dist = -0.003
        self.__img_bonds.add_new_image(ON_ICON_PATH)
        self.__btn_bonds = self.__ln_btn_bonds.get_content()
        self.__btn_bonds.img = self.__img_bonds

        # button config (bonds)
        self.__btn_bonds.outline.active = False
        self.__btn_bonds.name = self.__ln_btn_bonds.name
        self.__btn_bonds.register_pressed_callback(self.set_option)

        # layout node setup (dssp)
        self.__ln_btn_dssp   = self.__menu.root.find_node('DSSP Button')
        self.__img_dssp  = self.__ln_btn_dssp.create_child_node('Image')
        self.__img_dssp.forward_dist = -0.003
        self.__img_dssp.add_new_image(OFF_ICON_PATH)
        self.__btn_dssp = self.__ln_btn_dssp.get_content()
        self.__btn_dssp.img = self.__img_dssp

        # button config (dssp)
        self.__btn_dssp.outline.active = False
        self.__btn_dssp.name = self.__ln_btn_dssp.name
        self.__btn_dssp.register_pressed_callback(self.set_option)

        self.use_bonds = True
        self.use_dssp  = True

        self.__btn_bonds.selected = self.use_bonds
        self.__btn_dssp.selected = self.use_dssp

    def open_menu(self):
        self.__menu.enabled = True
        self.__plugin.menu = self.__menu
        self.__plugin.update_menu(self.__plugin.menu)

    def set_option(self, button):
        button.selected = not button.selected
        button.img.get_content().file_path = ON_ICON_PATH if button.selected else OFF_ICON_PATH
        option_name = 'bonds' if 'bonds' in button.name.lower() else 'dssp'
        setattr(self, "use_"+option_name, button.selected)
        self.__plugin.update_menu(self.__menu)