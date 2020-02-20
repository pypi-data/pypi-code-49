"""
General purpose tcl script creation modules
"""


def create_project(file, project_name, filename, comp_name, includes, defines, standard, solution_name, part, period):
    """
    Generate a tcl script for an HLS component creation
    :param filename: name of the file containing hls code
    :param period: clock period in ns
    :param part: part code to use
    :param solution_name: name of the solution to create inside the project
    :param file: the file on which the script will be written
    :param project_name: the name of the vivado project to generate
    :param comp_name: the name of the high level component
    :param includes: list of include directories
    :param defines: list of defines
    :param standard: c++ standard code to use
    """
    file.write("open_project {}\n".format(project_name))
    file.write("set_top {}\n".format(comp_name))
    includes_str = "" if includes is None else " ".join(
        ["-I{}".format(s) for s in includes]
    )
    if defines is None:
        def_str = ""
    else:
        def_str = " ".join(["-D{}={}".format(k, v) for k, v in defines.items()])
    file.write('add_files {} -cflags "-std={} {} {}"\n'.format(
        filename,
        standard,
        includes_str,
        def_str
    )
    )
    file.write('open_solution "{}"\n'.format(solution_name))
    file.write('set_part {{{}}} -tool vivado\n'.format(part))
    file.write('create_clock -period {} -name default\n'.format(
        period
    ))


def csynth_solution_script(file):
    """Generate a script in file for synthetizing solution solution_name of project project_name"""
    file.write('csynth_design\n')


def export_ip_script(file, comp_name, descr, version, ip_lib):
    """Generate a script in file for exporting solution solution_name of project project_name"""
    file.write(
        'export_design -flow syn -display_name {} -vendor someone -description "{}" -rtl vhdl -version "{}" -library "{}" -format ip_catalog\n'.format(
            comp_name,
            descr,
            version,
            ip_lib)
    )
