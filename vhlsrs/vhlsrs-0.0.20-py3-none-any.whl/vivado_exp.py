"""
Create experimental environment for vivado HLS 
"""

import logging
from pathlib import Path

from . import compedit
from . import vivado_hls_tcl as vtcl
from . import vivado_report as vrpt
from .tmpdir import TmpDirManager
from .utils import run_script

def generate_script(vivado_script, clock_period, standard, comp_name, defines, includes, part):
    with vivado_script.open("w") as o:
        logger = logging.getLogger("vrs_log")
        logger.debug("Starting generation of tcl script")
        vtcl.create_project(o, "vivado_synthesis", "comp.cpp", comp_name, includes, defines, standard, "solution", part,
                            clock_period)
        vtcl.csynth_solution_script(o)


def experiment(comp_path,
               comp_name,
               exp_name,
               clock_period,
               part,
               standard,
               includes=None,
               defines=None,
               keep_env=False,
               depth_constraint=None
               ):
    logger = logging.getLogger("vrs_log")
    logger.info("Experiment: {}".format(exp_name))
    comp = Path(comp_path).resolve()
    if not comp.exists():
        raise FileNotFoundError("Error when starting experiment: component file"
                                "{} does not exist".format(comp))
    logger.info("Found component file {}".format(comp))
    with TmpDirManager(exp_name, not keep_env):
        comp_copy = Path("comp.cpp")
        compedit.decorate_comp(comp, comp_copy, depth_constraint)
        logger.debug("Adding pragma decoration")

        vivado_script = Path("vivado_script.tcl")
        generate_script(vivado_script,
                        clock_period,
                        standard,
                        comp_name,
                        defines,
                        includes,
                        part
                        )
        run_script(vivado_script)
        vivado_hls_rpt = Path(
            "./vivado_hls_synthesis/solution/syn/report/{}_csynth.xml".format(comp_name)
        ).resolve()
        syn_res = vrpt.parse_syn_report(vivado_hls_rpt)
        vivado_report = Path(
            "./vivado_hls_synthesis/solution/impl/report/vhdl/{}_export.xml".format(comp_name)
        ).resolve()
        impl_res = vrpt.parse_impl_report(vivado_report)
    return {"syn": syn_res, "impl": impl_res}
