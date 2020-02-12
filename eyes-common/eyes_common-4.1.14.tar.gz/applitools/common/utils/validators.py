import attr
from selenium.webdriver.remote.webelement import WebElement


def check_if_rectangle_protocol(instance, attribute, dct):
    if not isinstance(dct, dict):
        raise TypeError(
            "{class_name}.{name} Must be dict type".format(
                class_name=instance.__class__.__name__, name=attribute.name
            )
        )
    if set(dct.keys()) != {"width", "height"}:
        raise TypeError("Dict must contain `width` and `height`")


def is_list_or_tuple(elm):
    return isinstance(elm, list) or isinstance(elm, tuple)


def is_webelement(elm):
    return isinstance(elm, WebElement) or isinstance(
        getattr(elm, "_element", None), WebElement
    )


def optional(type):
    return attr.validators.optional(attr.validators.instance_of(type))
