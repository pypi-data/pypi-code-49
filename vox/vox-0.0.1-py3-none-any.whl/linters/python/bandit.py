import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Bandit(BaseLinter):
    COMMAND = vox.FlagsBuilder(
        flags={"--config": flaggy.Options(name="--configfile", sep=" ")}
    ).sugar(
        program="bandit",
        r=None,
        format="custom",
        **{
            "msg-template": '"{relpath}:{line}:{test_id}:{severity}:{msg}:{confidence}:{range}"'
        }
    )
    DEPENDENCIES = ["bandit"]
    FORMAT = linty.to_str.BANDIT_MAM_CUSTOM
    NAME = "bandit"
    extract_errors = linty.from_str.bandit_mam_custom
