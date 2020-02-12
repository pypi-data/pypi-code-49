import nanome
from nanome.util import Logs

from .Settings import Settings

class StructurePrep(nanome.PluginInstance):
    def start(self):
        self.settings = Settings(self, lambda b: None)

    def on_run(self):
        self.request_complex_list(self.get_complexes_deep)

    def get_complexes_deep(self, complex_list):
        selected = [c.index for c in complex_list if c._selected]
        if not selected:
            self.send_notification(nanome.util.enums.NotificationTypes.error, "Please select an entry")
            return
        self.set_plugin_list_button(self.PluginListButtonType.run, "Running...", False)
        self.request_complexes(selected, self.step1)

    def step1(self, complex_list):
        if self.settings.use_bonds:
            # remove bonds first
            for complex in complex_list:
                for atom in complex.atoms:
                    atom._bonds.clear()
                for residue in complex.residues:
                    residue._bonds.clear()
            self.update_structures_deep(complex_list)
            # readd bonds
            self.add_bonds(complex_list, self.step2)
        else:
            self.step2(complex_list)

    def step2(self, complex_list):
        if self.settings.use_dssp:
            self.add_dssp(complex_list, self.done)
        else:
            self.done(complex_list)

    def done(self, complex_list):
        self.send_notification(nanome.util.enums.NotificationTypes.success, "Structures prepped")
        self.set_plugin_list_button(self.PluginListButtonType.run, "Run", True)
        self.update_structures_deep(complex_list)

    def on_advanced_settings(self):
        self.settings.open_menu()

def main():
    plugin = nanome.Plugin("Structure Prep", "Select your structures from the Entry List, then press Run to regenerate bonds and secondary structure.", "Structure", True)
    plugin.set_plugin_class(StructurePrep)
    plugin.run('127.0.0.1', 8888)

if __name__ == "__main__":
    main()