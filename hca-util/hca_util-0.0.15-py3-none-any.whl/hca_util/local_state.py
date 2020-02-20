class LocalState:

    def __init__(self):
        self.known_dirs = []
        self.selected_dir = None

    def add_dir(self, dir):
        if dir not in self.known_dirs:
            self.known_dirs.append(dir)

    def del_dir(self, dir):
        if dir in self.known_dirs:
            self.known_dirs.remove(dir)

    def reset_dirs(self):
        self.known_dirs = []

    def select_dir(self, dir):
        self.selected_dir = dir
        self.addDir(dir)

    def unselect_dir(self):
        self.selected_dir = None
