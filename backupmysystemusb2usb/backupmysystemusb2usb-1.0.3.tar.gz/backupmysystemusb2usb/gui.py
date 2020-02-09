"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib  # noqa: E402
from subprocess import Popen, CalledProcessError  # noqa: E402
from . import const  # noqa: E402

GUI_TITLE = const.GUI_TITLE
GUI_HBOX_SPACING = 5
GUI_BUTTON_CANCEL = const.GUI_BUTTON_CANCEL
GUI_BUTTON_QUIT = const.GUI_BUTTON_QUIT
GUI_FILE_NOT_FOUND = const.GUI_FILE_NOT_FOUND
GUI_FILE_NONE = const.GUI_FILE_NONE

"""
https://python-gtk-3-tutorial.readthedocs.io/en/latest/treeview.html#the-view
"""


class LogWindow(Gtk.Window):
    def __init__(self, log_file, service):
        self.log_file = log_file
        self.service = service
        self.log_list = self.__read_log_file()
        self.window = Gtk.Window.__init__(self, title=GUI_TITLE)
        self.set_border_width(10)

        # Setting up the self.grid in wich the element are to be positione
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        # Creating the ListStore model
        self.log_list_liststore = Gtk.ListStore(str)
        for l in self.log_list:
            # self.log_list_liststore.append(list(l))
            self.log_list_liststore.append([l])
        self.current_filter = None

        # Creating the treeview, making it use the filter as a model,
        # and adding the columns
        self.filter = self.log_list_liststore.filter_new()
        # Setting the filter
        self.filter.set_visible_func(self.filter_func)

        # Crating the treeview, making it use the filter as a model, and adding
        # columns
        self.treeview = Gtk.TreeView.new_with_model(self.filter)
        for i, column_title in enumerate(['Log']):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        hbox = Gtk.Box(spacing=GUI_HBOX_SPACING)

        button = Gtk.Button.new_with_label(GUI_BUTTON_CANCEL)
        button.connect('clicked', self.on_click_cancel)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label(GUI_BUTTON_QUIT)
        button.connect('clicked', self.on_quit)
        hbox.add(button)

        # Setting up the layout, putting the treeview in scrollwindow, and
        # the button in
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 3, 15)
        self.grid.attach_next_to(hbox, self.scrollable_treelist,
                                 Gtk.PositionType.BOTTOM, 1, 1)
        self.scrollable_treelist.add(self.treeview)

        # Scroll at bottom
        self.__scroll_bottom()

        # Events
        self.grid.connect('key-release-event', self.on_key_release)
        self.timeout_id = GLib.timeout_add(1000, self.on_timeout, None)

        self.show_all()

    def filter_func(self, model, iter, data):
        return True

    def on_timeout(self, user_data):
        """
        Event: read file every 10 sec
        """
        new_log_list = self.__read_log_file()
        if not new_log_list == self.log_list:
            self.log_list = new_log_list
            self.log_list_liststore.clear()
            for l in self.log_list:
                self.log_list_liststore.append([l])
                self.__scroll_bottom()
        return True

    def on_click_cancel(self, button):
        """
        Cancel execution
        """
        self.__cancel_execution()

    def on_quit(self, button):
        """
        Quit execution
        """
        self.__quit_execution()

    def on_key_release(self, widget, ev, data=None):
        """
        Key release
        """
        if ev.keyval in [Gdk.KEY_Control_L, Gdk.KEY_c]:
            self.__quit_execution()
        if ev.keyval in [Gdk.KEY_Control_R, Gdk.KEY_c]:
            self.__quit_execution()
        if ev.keyval in [Gdk.KEY_F10]:
            self.__cancel_execution()

    def __cancel_execution(self):
        """
        Cancel execution
        """
        self.__cmd_root()

    def __quit_execution(self):
        """
        Exit
        """
        Gtk.main_quit()

    def __read_log_file(self):
        """
        Read the log file
        """
        try:
            open_fd = open(self.log_file, 'r')
            read_file = []
            lines = open_fd.readlines()
            if lines is None:
                read_file = [(GUI_FILE_NONE % (self.log_file))]
            else:
                for l in lines:
                    read_file.append((l.rstrip()))
            return read_file
            open_fd.close()
        except FileNotFoundError:
            return [(GUI_FILE_NOT_FOUND % (self.log_file))]
        except IOError as err:
            return [(err)]

    def __scroll_bottom(self):
        self.treeview.scroll_to_cell(len(self.log_list), column=None,
                                     use_align=True, row_align=0.0,
                                     col_align=0.0)

    def __cmd_root(self):
        """
        systemctl stop self.service
        killall -9 dd
        """
        global KILLSERVICE
        try:
            cmd_list = ['systemctl', 'stop', self.service]
            cmd = Popen(cmd_list)
            KILLSERVICE = cmd.communicate()[0]
            print(KILLSERVICE)
        except CalledProcessError:
            print(const.ERR_CMD % ('systemctl stop' + self.service))
        global KILLALLOUTPUT
        try:
            cmd_list = ['killall', '-9', 'dd']
            cmd = Popen(cmd_list)
            cmd.wait()
            KILLALLOUTPUT = cmd.communicate()[0]
            print(KILLALLOUTPUT)
        except CalledProcessError:
            print(const.ERR_CMD % ('sudo killall -9 dd'))


class gui:
    def __init__(self, log_file, service):
        self.log_file = log_file
        self.service = service

    def run(self):
        """
        Run gui
        """
        win = LogWindow(self.log_file, self.service)
        win.connect('destroy', Gtk.main_quit)
        win.show_all()
        Gtk.main()
