import itertools
import json
from pathlib import Path
from typing import List
from unittest.mock import patch, MagicMock, call

import pytest

import randovania.interface_common.options
import randovania.interface_common.persisted_options
from randovania.interface_common import update_checker
from randovania.interface_common.options import Options, DecodeFailedException


@pytest.fixture(name="option")
def _option() -> Options:
    return Options(MagicMock())


def test_migrate_from_v11(option):
    old_data = {"version": 11,
                "options": {
                    "cosmetic_patches": {
                        "disable_hud_popup": True,
                        "speed_up_credits": True,
                        "open_map": True,
                        "pickup_markers": True,
                    }}}

    # Run
    new_data = randovania.interface_common.persisted_options.get_persisted_options_from_data(old_data)
    option.load_from_persisted(new_data, False)

    # Assert
    expected_data = {
        "cosmetic_patches": {
            "disable_hud_popup": True,
            "speed_up_credits": True,
            "open_map": True,
            "pickup_markers": True,
        }
    }
    assert new_data == expected_data


@patch("randovania.interface_common.options.Options._save_to_disk", autospec=True)
def test_context_manager_with_no_changes_doesnt_save(mock_save_to_disk: MagicMock,
                                                     option: Options):
    # Setup
    settings_changed = MagicMock()
    option.on_options_changed = settings_changed

    # Run
    with option:
        pass

    # Assert
    mock_save_to_disk.assert_not_called()
    settings_changed.assert_not_called()


@patch("randovania.interface_common.options.Options._save_to_disk", autospec=True)
def test_save_with_context_manager(mock_save_to_disk: MagicMock,
                                   option: Options):
    # Setup
    settings_changed = MagicMock()
    option._output_directory = Path("start")
    option.on_options_changed = settings_changed

    # Run
    with option:
        option.output_directory = Path("end")

    # Assert
    mock_save_to_disk.assert_called_once_with(option)
    settings_changed.assert_called_once_with()


@patch("randovania.interface_common.options.Options._save_to_disk", autospec=True)
def test_single_save_with_nested_context_manager(mock_save_to_disk: MagicMock,
                                                 option: Options):
    # Setup
    option._output_directory = Path("start")

    # Run
    with option:
        option.output_directory = Path("end")
        with option:
            pass

    # Assert
    mock_save_to_disk.assert_called_once_with(option)


def test_changing_field_without_context_manager_should_error(option: Options):
    # Run
    with pytest.raises(AssertionError) as exception:
        option.output_directory = Path("start")

    # Assert
    assert str(exception.value) == "Attempting to edit an Options, but it wasn't made editable"


@patch("randovania.interface_common.options.get_persisted_options_from_data", autospec=True)
@patch("randovania.interface_common.options.Options._read_persisted_options", return_value=None, autospec=True)
def test_load_from_disk_no_data(mock_read_persisted_options: MagicMock,
                                mock_get_persisted_options_from_data: MagicMock,
                                option: Options):
    # Run
    option.load_from_disk()

    # Assert
    mock_read_persisted_options.assert_called_once_with(option)
    mock_get_persisted_options_from_data.assert_not_called()


@pytest.mark.parametrize("fields_to_test",
                         itertools.combinations(randovania.interface_common.options._SERIALIZER_FOR_FIELD.keys(), 2))
@patch("randovania.interface_common.options.Options._set_field", autospec=True)
@patch("randovania.interface_common.options.get_persisted_options_from_data", autospec=True)
@patch("randovania.interface_common.options.Options._read_persisted_options", autospec=True)
def test_load_from_disk_with_data(mock_read_persisted_options: MagicMock,
                                  mock_get_persisted_options_from_data: MagicMock,
                                  mock_set_field: MagicMock,
                                  fields_to_test: List[str],
                                  option: Options):
    # Setup
    persisted_options = {
        field_name: MagicMock()
        for field_name in fields_to_test
    }
    new_serializers = {
        field_name: MagicMock()
        for field_name in fields_to_test
    }
    mock_get_persisted_options_from_data.return_value = persisted_options

    # Run
    with patch.dict(randovania.interface_common.options._SERIALIZER_FOR_FIELD, new_serializers):
        option.load_from_disk()

    # Assert
    mock_read_persisted_options.assert_called_once_with(option)
    mock_get_persisted_options_from_data.assert_called_once_with(mock_read_persisted_options.return_value)
    for field_name, serializer in new_serializers.items():
        serializer.decode.assert_called_once_with(persisted_options[field_name])

    mock_set_field.assert_has_calls(
        call(option, field_name, new_serializers[field_name].decode.return_value)
        for field_name in fields_to_test
    )


# TODO: test with an actual field as well
def test_serialize_fields(option: Options):
    # Setup

    # Run
    result = option._serialize_fields()

    # Assert
    assert result == {
        "version": randovania.interface_common.persisted_options._CURRENT_OPTIONS_FILE_VERSION,
        "options": {
            "last_changelog_displayed": str(update_checker.strict_current_version()),
        }
    }


def test_edit_during_options_changed(tmpdir):
    # Setup
    option = Options(Path(tmpdir))
    option._output_directory = Path("start")

    def on_changed():
        with option:
            option.output_directory = Path("final")

    option.on_options_changed = on_changed

    # Run
    with option:
        option.output_directory = Path("middle")

    second_option = Options(Path(tmpdir))
    second_option.load_from_disk()

    # Assert
    assert option.output_directory == Path("final")
    assert option.output_directory == second_option.output_directory


@pytest.mark.parametrize("ignore_decode_errors", [False, True])
def test_load_from_disk_missing_json(ignore_decode_errors: bool,
                                     tmpdir):
    # Setup
    option = Options(Path(tmpdir))
    tmpdir.join("config.json").write_text("", "utf-8")

    if ignore_decode_errors:
        result = option.load_from_disk(ignore_decode_errors)
        assert result != ignore_decode_errors
    else:
        with pytest.raises(DecodeFailedException):
            option.load_from_disk(ignore_decode_errors)


@pytest.mark.parametrize("ignore_decode_errors", [False])
def test_load_from_disk_invalid_json(ignore_decode_errors: bool,
                                     tmpdir):
    # Setup
    option = Options(Path(tmpdir))
    tmpdir.join("config.json").write_text(
        json.dumps(randovania.interface_common.persisted_options.serialized_data_for_options({
            "cosmetic_patches": {
                "pickup_model_style": "invalid-value"
            }
        })),
        "utf-8")

    if ignore_decode_errors:
        result = option.load_from_disk(ignore_decode_errors)
        assert result != ignore_decode_errors
    else:
        with pytest.raises(DecodeFailedException):
            option.load_from_disk(ignore_decode_errors)
