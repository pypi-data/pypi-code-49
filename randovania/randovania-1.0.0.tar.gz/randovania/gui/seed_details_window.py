from functools import partial
from typing import List

from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QRadioButton, QGroupBox, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, \
    QApplication, QDialog, QAction, QMenu

from randovania.game_description.default_database import default_prime2_game_description
from randovania.game_description.node import PickupNode
from randovania.gui.dialog.game_input_dialog import GameInputDialog
from randovania.gui.generated.seed_details_window_ui import Ui_SeedDetailsWindow
from randovania.gui.lib import preset_describer
from randovania.gui.lib.background_task_mixin import BackgroundTaskMixin
from randovania.gui.lib.common_qt_lib import set_default_window_icon, prompt_user_for_seed_log
from randovania.gui.lib.window_manager import WindowManager
from randovania.interface_common import simplified_patcher, status_update_lib
from randovania.interface_common.options import Options
from randovania.interface_common.status_update_lib import ProgressUpdateCallable
from randovania.layout.layout_description import LayoutDescription
from randovania.layout.preset import Preset


def _unique(iterable):
    seen = set()

    for item in iterable:
        if item in seen:
            continue
        seen.add(item)
        yield item


def _show_pickup_spoiler(button):
    button.setText(button.item_name)
    button.item_is_hidden = False


def _hide_pickup_spoiler(button):
    button.setText("Hidden")
    button.item_is_hidden = True


# TODO: this should not be a Window class
class SeedDetailsWindow(QMainWindow, Ui_SeedDetailsWindow):
    _on_bulk_change: bool = False
    _history_items: List[QRadioButton]
    pickup_spoiler_buttons: List[QPushButton]
    layout_description: LayoutDescription
    _options: Options
    _window_manager: WindowManager

    def __init__(self, background_processor: BackgroundTaskMixin, window_manager: WindowManager, options: Options):
        super().__init__()
        self.setupUi(self)
        set_default_window_icon(self)

        self._history_items = []
        self.pickup_spoiler_buttons = []
        self.background_processor = background_processor
        self._options = options
        self._window_manager = window_manager

        # Ui
        self._tool_button_menu = QMenu(self.tool_button)
        self.tool_button.setMenu(self._tool_button_menu)

        self._action_open_tracker = QAction(self)
        self._action_open_tracker.setText("Open map tracker")
        self._tool_button_menu.addAction(self._action_open_tracker)

        self._action_copy_permalink = QAction(self)
        self._action_copy_permalink.setText("Copy Permalink")
        self._tool_button_menu.addAction(self._action_copy_permalink)

        # Signals
        self.export_log_button.clicked.connect(self._export_log)
        self.export_iso_button.clicked.connect(self._export_iso)
        self._action_open_tracker.triggered.connect(self._open_map_tracker)
        self._action_copy_permalink.triggered.connect(self._copy_permalink)

        # Cosmetic
        self.remove_hud_popup_check.stateChanged.connect(self._persist_option_then_notify("hud_memo_popup_removal"))
        self.faster_credits_check.stateChanged.connect(self._persist_option_then_notify("speed_up_credits"))
        self.open_map_check.stateChanged.connect(self._persist_option_then_notify("open_map"))
        self.pickup_markers_check.stateChanged.connect(self._persist_option_then_notify("pickup_markers"))

        # Keep the Layout Description visualizer ready, but invisible.
        self._create_pickup_spoilers()

    # Operations
    def _copy_permalink(self):
        QApplication.clipboard().setText(self.layout_description.permalink.as_str)

    def _export_log(self):
        json_path = prompt_user_for_seed_log(self, new_file=True)
        if json_path is not None:
            self.layout_description.save_to_file(json_path)

    def _export_iso(self):
        layout = self.layout_description
        options = self._options

        dialog = GameInputDialog(options,
                                 "Echoes Randomizer - {}.iso".format(
                                     layout.shareable_word_hash
                                 ))
        result = dialog.exec_()

        if result != QDialog.Accepted:
            return

        input_file = dialog.input_file
        output_file = dialog.output_file

        def work(progress_update: ProgressUpdateCallable):
            num_updaters = 2
            if input_file is not None:
                num_updaters += 1
            updaters = status_update_lib.split_progress_update(progress_update, num_updaters)

            if input_file is not None:
                simplified_patcher.unpack_iso(input_iso=input_file,
                                              options=options,
                                              progress_update=updaters[0])

            # Apply Layout
            simplified_patcher.apply_layout(layout=layout,
                                            options=options,
                                            progress_update=updaters[-2])

            # Pack ISO
            simplified_patcher.pack_iso(output_iso=output_file,
                                        options=options,
                                        progress_update=updaters[-1])

            progress_update(f"Finished!", 1)

        self.background_processor.run_in_background_thread(work, "Exporting...")

    def _open_map_tracker(self):
        self._window_manager.open_map_tracker(self.layout_description.permalink.layout_configuration)

    # Layout Visualization
    def _create_pickup_spoiler_combobox(self):
        self.pickup_spoiler_pickup_combobox.currentTextChanged.connect(self._on_change_pickup_filter)

    def _create_pickup_spoilers(self):
        self.pickup_spoiler_show_all_button.clicked.connect(self._toggle_show_all_pickup_spoiler)
        self.pickup_spoiler_show_all_button.currently_show_all = True

        self._create_pickup_spoiler_combobox()

        game_description = default_prime2_game_description()
        world_to_group = {}

        for world in game_description.world_list.worlds:
            for is_dark_world in [False, True]:
                group_box = QGroupBox(self.pickup_spoiler_scroll_contents)
                group_box.setTitle(world.correct_name(is_dark_world))
                vertical_layout = QVBoxLayout(group_box)
                vertical_layout.setContentsMargins(8, 4, 8, 4)
                vertical_layout.setSpacing(2)
                group_box.vertical_layout = vertical_layout

                vertical_layout.horizontal_layouts = []
                world_to_group[world.correct_name(is_dark_world)] = group_box
                self.pickup_spoiler_scroll_content_layout.addWidget(group_box)

        for world, area, node in game_description.world_list.all_worlds_areas_nodes:
            if not isinstance(node, PickupNode):
                continue

            group_box = world_to_group[world.correct_name(area.in_dark_aether)]
            horizontal_layout = QHBoxLayout()
            horizontal_layout.setSpacing(2)

            label = QLabel(group_box)
            label.setText(game_description.world_list.node_name(node))
            horizontal_layout.addWidget(label)
            horizontal_layout.label = label

            push_button = QPushButton(group_box)
            push_button.setFlat(True)
            push_button.setText("Hidden")
            push_button.item_is_hidden = True
            push_button.pickup_index = node.pickup_index
            push_button.clicked.connect(partial(self._toggle_pickup_spoiler, push_button))
            push_button.item_name = "Nothing was Set, ohno"
            push_button.row = horizontal_layout
            horizontal_layout.addWidget(push_button)
            horizontal_layout.button = push_button
            self.pickup_spoiler_buttons.append(push_button)

            group_box.vertical_layout.addLayout(horizontal_layout)
            group_box.vertical_layout.horizontal_layouts.append(horizontal_layout)

    def create_history_item(self, node):
        button = QRadioButton(self.layout_history_content)
        button.toggled.connect(self.on_select_node)
        button.setText(node)
        self.layout_history_content_layout.addWidget(button)
        self._history_items.append(button)
        return button

    def update_layout_description(self, description: LayoutDescription):
        self.layout_description = description
        self.layout_info_tab.show()

        self.export_log_button.setEnabled(description.permalink.spoiler)

        title_text = """
        <p>
            Permalink: <span style='font-weight:600;'>{description.permalink.as_str}</span><br/>
            Seed Hash: {description.shareable_word_hash} ({description.shareable_hash})<br/>
            Preset Name: {description.permalink.preset.name}
        </p>
        """.format(description=description)
        self.layout_title_label.setText(title_text)

        categories = list(preset_describer.describe(description.permalink.preset))
        self.layout_description_left_label.setText(preset_describer.merge_categories(categories[::2]))
        self.layout_description_right_label.setText(preset_describer.merge_categories(categories[1::2]))

        # Game Spoiler
        has_spoiler = description.permalink.spoiler
        self.pickup_tab.setEnabled(has_spoiler)

        if has_spoiler:
            pickup_names = {
                pickup.name
                for pickup in description.patches.pickup_assignment.values()
            }
        else:
            pickup_names = {}
            self.layout_info_tab.removeTab(self.layout_info_tab.indexOf(self.pickup_tab))

        self.pickup_spoiler_pickup_combobox.clear()
        self.pickup_spoiler_pickup_combobox.addItem("None")
        for pickup_name in sorted(pickup_names):
            self.pickup_spoiler_pickup_combobox.addItem(pickup_name)

        for pickup_button in self.pickup_spoiler_buttons:
            pickup = description.patches.pickup_assignment.get(pickup_button.pickup_index)
            if pickup is not None:
                pickup_button.item_name = pickup.name if has_spoiler else "????"
            else:
                pickup_button.item_name = "Nothing"

            if not pickup_button.item_is_hidden:
                pickup_button.setText(pickup_button.item_name)

    def _toggle_pickup_spoiler(self, button):
        if button.item_is_hidden:
            _show_pickup_spoiler(button)
        else:
            _hide_pickup_spoiler(button)
        self._update_show_all_button_state()

    def _toggle_show_all_pickup_spoiler(self):
        if self.pickup_spoiler_show_all_button.currently_show_all:
            action = _show_pickup_spoiler
        else:
            action = _hide_pickup_spoiler

        for button in self.pickup_spoiler_buttons:
            action(button)

        self._update_show_all_button_state()

    def _update_show_all_button_state(self):
        self.pickup_spoiler_show_all_button.currently_show_all = all(
            button.item_is_hidden for button in self.pickup_spoiler_buttons
        )
        if self.pickup_spoiler_show_all_button.currently_show_all:
            self.pickup_spoiler_show_all_button.setText(QtCore.QCoreApplication.translate("HistoryWindow", "Show All"))
        else:
            self.pickup_spoiler_show_all_button.setText(QtCore.QCoreApplication.translate("HistoryWindow", "Hide All"))

    def _on_change_pickup_filter(self, text):
        for button in self.pickup_spoiler_buttons:
            visible = text == "None" or text == button.item_name
            button.setVisible(visible)
            button.row.label.setVisible(visible)

    def _persist_option_then_notify(self, attribute_name: str):
        def persist(value: int):
            with self._options as options:
                setattr(options, attribute_name, bool(value))

        return persist

    def on_options_changed(self, options: Options):
        self.remove_hud_popup_check.setChecked(options.hud_memo_popup_removal)
        self.faster_credits_check.setChecked(options.speed_up_credits)
        self.open_map_check.setChecked(options.open_map)
        self.pickup_markers_check.setChecked(options.pickup_markers)
