"""
    Name: compiler.py
    Author: Charles Zhang <694556046@qq.com>
    Propose: A module to compile source code in different languages.
    Coding: UTF-8

    Change Log:
        **2020.01.30**
        Update compile_c option from c90 to c99

        **2020.01.26**
        Create this file!
"""

import pygrading.general_test as gg
from typing import Tuple


def compile_c(source: str, target: str, compiler_type: str = "gcc", option: str = "-O2 -Wall -std=c99") -> Tuple:
    """Compile c source file

    Compile c source file using gcc.

    Args:
        source: c source file directory.
        target: target file path.
        compiler_type: (optional)compiler type, default gcc.
        option: (optional)addition options, default "-O2 -Wall -std=c90".

    Returns:
        status: compile status, 0 for success, 1 for fail.
        log: compile log
    """
    cmd = " ".join([str(compiler_type), str(option), str(source), "-o", str(target)])

    try:
        ret = gg.utils.bash(cmd)
    except Exception as e:
        status = 1
        output = str(e)
    else:
        status = ret[0]
        output = ret[1]

    return status, output


def compile_cpp(source: str, target: str, compiler_type: str = "g++", option: str = "-O2 -Wall -std=c++11") -> Tuple:
    """Compile cpp source file

    Compile cpp source file using gcc.

    Args:
        source: cpp source file directory.
        target: target file path.
        compiler_type: (optional)compiler type, default g++.
        option: (optional)addition options, default "-O2 -Wall -std=c++11".

    Returns:
        status: compile status, 0 for success, 1 for fail.
        log: compile log
    """
    cmd = " ".join([str(compiler_type), str(option), str(source), "-o", str(target)])

    try:
        ret = gg.utils.bash(cmd)
    except Exception as e:
        status = 1
        output = str(e)
    else:
        status = ret[0]
        output = ret[1]

    return status, output
