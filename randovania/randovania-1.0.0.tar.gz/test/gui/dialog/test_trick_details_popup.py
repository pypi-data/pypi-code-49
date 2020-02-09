from unittest.mock import MagicMock

from PySide2.QtWidgets import QWidget

from randovania.game_description.resources.simple_resource_info import SimpleResourceInfo
from randovania.gui.dialog import trick_details_popup
from randovania.layout.trick_level import LayoutTrickLevel


def test_click_on_link(echoes_game_description,
                       skip_qtbot):
    # Setup
    main_window = QWidget()
    main_window.open_data_visualizer_at = MagicMock()
    skip_qtbot.add_widget(main_window)
    world_name = "World"
    area_name = "Area"

    # Run
    popup = trick_details_popup.TrickDetailsPopup(
        main_window,
        main_window,
        echoes_game_description,
        SimpleResourceInfo(-1, "Nothing", "Nothing", None),
        LayoutTrickLevel.HARD
    )
    popup._on_click_link_to_data_editor(f"data-editor://{world_name}/{area_name}")

    # Assert
    main_window.open_data_visualizer_at.assert_called_once_with(world_name, area_name)
