import json
from datetime import datetime
from logging import Formatter

from c42eventextractor.maps import (
    AED_EVENT_TO_SIGNATURE_ID_MAP,
    CEF_CUSTOM_FIELD_NAME_MAP,
    JSON_TO_CEF_MAP,
)

CEF_TEMPLATE = u"CEF:0|Code42|{productName}|1|{signatureID}|{eventName}|{severity}|{extension}"
CEF_TIMESTAMP_FIELDS = ["end", "fileCreateTime", "fileModificationTime", "rt"]


class AEDDictToCEFFormatter(Formatter):
    """Formats AED dicts into CEF format. Attach to a logger via `setFormatter` to use.

    Args:
        default_product_name: The default value to use in the product name segment of the CEF message.
        default_severity_level: The default integer between 1 and 10 to assign to the severity segment of the CEF message.
    """

    def __init__(
        self, default_product_name="Advanced Exfiltration Detection", default_severity_level="5"
    ):
        # type: (str, str) -> None
        super(AEDDictToCEFFormatter, self).__init__()
        self._default_product_name = default_product_name
        self._default_severity_level = default_severity_level

    def format(self, record):
        aed_dict = record.msg
        # FED must convert to AED dict format before calling this.
        kvp_list = {
            JSON_TO_CEF_MAP[key]: aed_dict[key]
            for key in aed_dict
            if key in JSON_TO_CEF_MAP and (aed_dict[key] is not None and aed_dict[key] != [])
        }

        extension = u" ".join(_format_cef_kvp(key, kvp_list[key]) for key in kvp_list)

        event_name = aed_dict.get("eventType", "UNKNOWN")
        signature_id = AED_EVENT_TO_SIGNATURE_ID_MAP.get(event_name, "C42000")

        cef_log = CEF_TEMPLATE.format(
            productName=self._default_product_name,
            signatureID=signature_id,
            eventName=event_name,
            severity=self._default_severity_level,
            extension=extension,
        )
        return cef_log


class AEDDictToJSONFormatter(Formatter):
    """Formats AED dicts into JSON format. Attach to a logger via `setFormatter` to use.

    Items in the dictionary whose values are `None`, empty string, or empty lists will be excluded
    from the JSON conversion. 
    """

    def format(self, record):
        aed_dict = record.msg
        aed_dict = {key: aed_dict[key] for key in aed_dict if aed_dict[key] or aed_dict[key] == 0}
        return json.dumps(aed_dict)


def _format_cef_kvp(cef_field_key, cef_field_value):
    if cef_field_key + "Label" in CEF_CUSTOM_FIELD_NAME_MAP:
        return _format_custom_cef_kvp(cef_field_key, cef_field_value)

    cef_field_value = _handle_nested_json_fields(cef_field_key, cef_field_value)
    if isinstance(cef_field_value, list):
        cef_field_value = _convert_list_to_csv(cef_field_value)
    elif cef_field_key in CEF_TIMESTAMP_FIELDS:
        cef_field_value = _convert_aed_timestamp_to_cef_timestamp(cef_field_value)
    return u"{0}={1}".format(cef_field_key, cef_field_value)


def _handle_nested_json_fields(cef_field_key, cef_field_value):
    if cef_field_key == u"duser":
        cef_field_value = [user[u"cloudUsername"] for user in cef_field_value]

    return cef_field_value


def _format_custom_cef_kvp(custom_cef_field_key, custom_cef_field_value):
    custom_cef_label_key = "{0}Label".format(custom_cef_field_key)
    custom_cef_label_value = CEF_CUSTOM_FIELD_NAME_MAP[custom_cef_label_key]
    return u"{0}={1} {2}={3}".format(
        custom_cef_field_key, custom_cef_field_value, custom_cef_label_key, custom_cef_label_value
    )


def _convert_list_to_csv(_list):
    value = u",".join([val for val in _list])
    return value


def _convert_aed_timestamp_to_cef_timestamp(timestamp_value):
    try:
        _datetime = datetime.strptime(timestamp_value, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        _datetime = datetime.strptime(timestamp_value, "%Y-%m-%dT%H:%M:%SZ")
    value = "{:.0f}".format(_datetime_to_ms_since_epoch(_datetime))
    return value


def _datetime_to_ms_since_epoch(_datetime):
    epoch = datetime.utcfromtimestamp(0)
    total_seconds = (_datetime - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds * 1000
