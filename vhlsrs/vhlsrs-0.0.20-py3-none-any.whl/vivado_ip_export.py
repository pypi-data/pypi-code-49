"""
Create tcl script for exporting an IP
"""

import logging
import shutil
from pathlib import Path

from . import vivado_hls_tcl as vtcl
from .tmpdir import TmpDirManager
from .utils import run_script


def _generate_script(script_path, clock_period, standard, comp_name, defines, includes, part, ip_lib, version, descr):
    with script_path.open("w") as o:
        logger = logging.getLogger("vrs_log")
        logger.debug("Starting generation of tcl script")
        vtcl.create_project(o,
                            "vivado_export",
                            "comp.cpp",
                            comp_name,
                            includes,
                            defines,
                            standard,
                            "solution",
                            part,
                            clock_period
                            )
        vtcl.csynth_solution_script(o)
        vtcl.export_ip_script(o, comp_name, descr, version, ip_lib)


def export_ip(comp_path,
              comp_name,
              exp_name,
              clock_period,
              part,
              standard,
              ip_lib,
              version,
              descr,
              includes=None,
              defines=None,
              keep_env=False,
              ):
    logger = logging.getLogger("vrs_log")
    logger.info("Experiment: {}".format(exp_name))
    comp = Path(comp_path).resolve()
    if not comp.exists():
        raise FileNotFoundError("Error when starting experiment: component file"
                                "{} does not exist".format(comp))
    logger.info("Found component file {}".format(comp))
    pwd = Path().resolve()
    with TmpDirManager(not keep_env):
        comp_copy = Path("comp.cpp")
        shutil.copyfile(comp, comp_copy)

        vivado_script = Path("vivado_script.tcl")
        _generate_script(vivado_script,
                         clock_period,
                         standard,
                         comp_name,
                         defines,
                         includes,
                         part,
                         ip_lib,
                         version,
                         descr
                         )
        run_script(vivado_script)
        export_path = list(Path("./vivado_export/solution/impl/ip/").glob('*.zip'))[0]
        shutil.move(str(export_path.resolve()), str(pwd))
