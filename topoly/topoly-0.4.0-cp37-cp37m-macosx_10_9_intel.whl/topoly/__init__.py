#!/usr/bin/python3
"""
The main Topoly module collecting the functions designed for the users.

Pawel Dabrowski-Tumanski
p.dabrowski at cent.uw.edu.pl
04.09.2019

Docs:
https://realpython.com/documenting-python-code/#docstring-types

The type used here: Google

Support in PyCharm:
https://www.jetbrains.com/help/pycharm/settings-tools-python-integrated-tools.html
- change default reStructuredText to Google

Docs will be published in: https://readthedocs.org/
"""

from .manipulation import *
from .invariants import *
from topoly.topoly_knot import *
from topoly.topoly_preprocess import *
from .codes import *
from .plotting import KnotMap, Reader
from .params import *
from .polygongen import Polygon_lasso, Polygon_loop, Polygon_walk
from .lasso import Lasso
from .gln import GLN
from .convert import convert_xyz2vmd


def alexander(input_data, closure=Closure.TWO_POINTS, tries=200, boundaries=None, reduce_method=ReduceMethod.KMT,
              max_cross=15, poly_reduce=True, translate=False, external_dictionary='', hide_trivial=True,
              matrix=False, density=1, level=0, matrix_plot=False, plot_ofile="KnotFingerPrintMap",
              plot_format=PlotFormat.PNG, output_file='', output_format=OutputFormat.Dictionary, cuda=True,
              run_parallel=False, parallel_workers=None, debug=False):
    """
    Calculates the Alexander polynomial of the given structure.

    Args:
        input_data (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str, optional): the method to close the chain. Viable options are the parameters of the Closure
                            closure. Default: Closure.TWO_POINTS
        tries (int, optional): the number of tries for stochastic closure methods. Default: 200
        boundaries (list of [int, int]): the boundaries of the subchains to be checked. The subchains are specified as
                            a list of subchain beginning and ending index. If empty, the whole chain is calculated.
                            Default: []
        reduce_method (str, optional): the method of chain reduction. Viable options are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT
        max_cross (int, optional): the maximal number of crossings after reduction to start the polynomial calculation.
                            Default: 15
        poly_reduce (bool, optional): if the polynomial should be presented in the reduced form. Default: False
        translate (bool, optional): if translate the polynomial to the structure topology using the dictionary.
                            Default: False
        external_dictionary (str, optional): the path to the file with the external dictionary of the polynomials.
                            Default: ''
        hide_trivial (bool, optional): if to suppress printing out the trivial results. Default: True
        matrix (bool, optional): if to calculate the whole matrix i.e. the polynomial for each subchain. Default: False
        density (int, optional): the inverse of resolution of matrix calculation. Higher number speeds up calculation,
                            but may result in omitting some non-trivial subchains. Default: 1
        level (float, optional): the cutoff of the non-trivial structure probability. If 0, all the subchains with at
                            least one non-trivial closure are treated as non-trivial. Default: 0
        matrix_plot (bool, optional): if to plot a figure of a matrix (knot fingerprint). Default: False
        plot_ofile (str, optional): the name of the matrix figure plot. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the matrix figure plot. Viable formats are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        output_file (str, optional): the name of the file with the matrix results. If empty, the resulting matrix is
                            returned to source. Default: ''
        output_format (str, optional): the format of the matrix output. The viable formats are the parameters of the
                            OutputFormat class. Default: OutputFormat.DICTIONARY
        cuda (bool, optional): if to use the cuda-provided acceleration if possible. Default: True
        run_parallel (bool, optional): if to use the Python-provided parallelization of calculation. Default: True
        parallel_workers (int, optional): number of parallel workers. If 0, all the available processors will be used.
                            Default: 0
        debug (bool, optional): the debug mode. Default: False

    Returns:
        The dictionary with the Alexander polynomial results. For each subchain a separate dictionary with different
        polynomial probabilities is created.
    """
    result = Invariant(input_data)
    return result.calculate(AlexanderGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            boundaries=boundaries, poly_reduce=poly_reduce, translate=translate, max_cross=max_cross,
                            external_dictionary=external_dictionary, hide_trivial=hide_trivial, matrix=matrix,
                            density=density, level=level, cuda=cuda, matrix_plot=matrix_plot, plot_ofile=plot_ofile,
                            plot_format=plot_format, output_file=output_file, output_format=output_format,
                            run_parallel=run_parallel, parallel_workers=parallel_workers, debug=debug)


def jones(input_data, closure=Closure.TWO_POINTS, tries=200, reduce_method=ReduceMethod.KMT, boundaries=None,
          max_cross=15, poly_reduce=True, translate=False, external_dictionary='', chiral=False, hide_trivial=True,
          matrix=False, density=1, level=0, matrix_plot=False, plot_ofile="KnotFingerPrintMap",
          plot_format=PlotFormat.PNG, output_file='', output_format=OutputFormat.Dictionary, cuda=True,
          run_parallel=False, parallel_workers=None, debug=False):
    """
    Calculates the Jones polynomial of the given structure.

    Args:
        input_data (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str, optional): the method to close the chain. Viable options are the parameters of the Closure
                            closure. Default: Closure.TWO_POINTS
        tries (int, optional): the number of tries for stochastic closure methods. Default: 200
        reduce_method (str, optional): the method of chain reduction. Viable options are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT
        boundaries (list of [int, int]): the boundaries of the subchains to be checked. The subchains are specified as
                            a list of subchain beginning and ending index. If empty, the whole chain is calculated.
                            Default: []
        max_cross (int, optional): the maximal number of crossings after reduction to start the polynomial calculation.
                            Default: 15
        poly_reduce (bool, optional): if the polynomial should be presented in the reduced form. Default: False
        translate (bool, optional): if translate the polynomial to the structure topology using the dictionary.
                            Default: False
        external_dictionary (str, optional): the path to the file with the external dictionary of the polynomials.
                            Default: ''
        chiral (bool, optional): if to take into account the structure chirality. Default: False
        hide_trivial (bool, optional): if to suppress printing out the trivial results. Default: True
        matrix (bool, optional): if to calculate the whole matrix i.e. the polynomial for each subchain. Default: False
        density (int, optional): the inverse of resolution of matrix calculation. Higher number speeds up calculation,
                            but may result in omitting some non-trivial subchains. Default: 1
        level (float, optional): the cutoff of the non-trivial structure probability. If 0, all the subchains with at
                            least one non-trivial closure are treated as non-trivial. Default: 0
        matrix_plot (bool, optional): if to plot a figure of a matrix (knot fingerprint). Default: False
        plot_ofile (str, optional): the name of the matrix figure plot. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the matrix figure plot. Viable formats are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        output_file (str, optional): the name of the file with the matrix results. If empty, the resulting matrix is
                            returned to source. Default: ''
        output_format (str, optional): the format of the matrix output. The viable formats are the parameters of the
                            OutputFormat class. Default: OutputFormat.DICTIONARY
        cuda (bool, optional): if to use the cuda-provided acceleration if possible. Default: True
        run_parallel (bool, optional): if to use the Python-provided parallelization of calculation. Default: True
        parallel_workers (int, optional): number of parallel workers. If 0, all the available processors will be used.
                            Default: 0
        debug (bool, optional): the debug mode. Default: False

    Returns:
        The dictionary with the Jones polynomial results. For each subchain a separate dictionary with different
        polynomial probabilities is created.
    """
    result = Invariant(input_data)
    return result.calculate(JonesGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            poly_reduce=poly_reduce, translate=translate, chiral=chiral, boundaries=boundaries,
                            hide_trivial=hide_trivial, external_dictionary=external_dictionary, max_cross=max_cross,
                            matrix=matrix, density=density, level=level, cuda=cuda, matrix_plot=matrix_plot,
                            plot_ofile=plot_ofile, plot_format=plot_format, output_file=output_file,
                            output_format=output_format, run_parallel=run_parallel, parallel_workers=parallel_workers,
                            debug=debug)


def conway(input_data, closure=Closure.TWO_POINTS, tries=200, reduce_method=ReduceMethod.KMT, poly_reduce=True,
           translate=False, external_dictionary='', boundaries=None, hide_trivial=True, max_cross=15, matrix=False,
           density=1, level=0, matrix_plot=False, plot_ofile="KnotFingerPrintMap", plot_format=PlotFormat.PNG,
           output_file='', output_format=OutputFormat.Dictionary, cuda=True, run_parallel=False, parallel_workers=None,
           debug=False):
    """
    Calculates the Conway polynomial of the given structure.

    Args:
        input_data (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str, optional): the method to close the chain. Viable options are the parameters of the Closure
                            closure. Default: Closure.TWO_POINTS
        tries (int, optional): the number of tries for stochastic closure methods. Default: 200
        reduce_method (str, optional): the method of chain reduction. Viable options are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT
        boundaries (list of [int, int]): the boundaries of the subchains to be checked. The subchains are specified as
                            a list of subchain beginning and ending index. If empty, the whole chain is calculated.
                            Default: []
        max_cross (int, optional): the maximal number of crossings after reduction to start the polynomial calculation.
                            Default: 15
        poly_reduce (bool, optional): if the polynomial should be presented in the reduced form. Default: False
        translate (bool, optional): if translate the polynomial to the structure topology using the dictionary.
                            Default: False
        external_dictionary (str, optional): the path to the file with the external dictionary of the polynomials.
                            Default: ''
        hide_trivial (bool, optional): if to suppress printing out the trivial results. Default: True
        matrix (bool, optional): if to calculate the whole matrix i.e. the polynomial for each subchain. Default: False
        density (int, optional): the inverse of resolution of matrix calculation. Higher number speeds up calculation,
                            but may result in omitting some non-trivial subchains. Default: 1
        level (float, optional): the cutoff of the non-trivial structure probability. If 0, all the subchains with at
                            least one non-trivial closure are treated as non-trivial. Default: 0
        matrix_plot (bool, optional): if to plot a figure of a matrix (knot fingerprint). Default: False
        plot_ofile (str, optional): the name of the matrix figure plot. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the matrix figure plot. Viable formats are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        output_file (str, optional): the name of the file with the matrix results. If empty, the resulting matrix is
                            returned to source. Default: ''
        output_format (str, optional): the format of the matrix output. The viable formats are the parameters of the
                            OutputFormat class. Default: OutputFormat.DICTIONARY
        cuda (bool, optional): if to use the cuda-provided acceleration if possible. Default: True
        run_parallel (bool, optional): if to use the Python-provided parallelization of calculation. Default: True
        parallel_workers (int, optional): number of parallel workers. If 0, all the available processors will be used.
                            Default: 0
        debug (bool, optional): the debug mode. Default: False

    Returns:
        The dictionary with the Conway polynomial results. For each subchain a separate dictionary with different
        polynomial probabilities is created.
    """
    result = Invariant(input_data)
    return result.calculate(ConwayGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            poly_reduce=poly_reduce, translate=translate, boundaries=boundaries,
                            hide_trivial=hide_trivial, external_dictionary=external_dictionary, max_cross=max_cross,
                            matrix=matrix, density=density, level=level, cuda=cuda, matrix_plot=matrix_plot,
                            plot_ofile=plot_ofile, plot_format=plot_format, output_file=output_file,
                            output_format=output_format, run_parallel=run_parallel, parallel_workers=parallel_workers,
                            debug=debug)


def homfly(input_data, closure=Closure.TWO_POINTS, tries=200, reduce_method=ReduceMethod.KMT, poly_reduce=True,
           translate=False, external_dictionary='', chiral=False, boundaries=None, hide_trivial=True, max_cross=15,
           matrix=False, density=1, level=0, matrix_plot=False, plot_ofile="KnotFingerPrintMap",
           plot_format=PlotFormat.PNG, output_file='', output_format=OutputFormat.Dictionary, cuda=True,
           run_parallel=False, parallel_workers=None, debug=False):
    """
    Calculates the HOMFLY-PT polynomial of the given structure.

    Args:
        input_data (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str, optional): the method to close the chain. Viable options are the parameters of the Closure
                            closure. Default: Closure.TWO_POINTS
        tries (int, optional): the number of tries for stochastic closure methods. Default: 200
        reduce_method (str, optional): the method of chain reduction. Viable options are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT
        boundaries (list of [int, int]): the boundaries of the subchains to be checked. The subchains are specified as
                            a list of subchain beginning and ending index. If empty, the whole chain is calculated.
                            Default: []
        max_cross (int, optional): the maximal number of crossings after reduction to start the polynomial calculation.
                            Default: 15
        poly_reduce (bool, optional): if the polynomial should be presented in the reduced form. Default: False
        translate (bool, optional): if translate the polynomial to the structure topology using the dictionary.
                            Default: False
        external_dictionary (str, optional): the path to the file with the external dictionary of the polynomials.
                            Default: ''
        chiral (bool, optional): if to take into account the structure chirality. Default: False
        hide_trivial (bool, optional): if to suppress printing out the trivial results. Default: True
        matrix (bool, optional): if to calculate the whole matrix i.e. the polynomial for each subchain. Default: False
        density (int, optional): the inverse of resolution of matrix calculation. Higher number speeds up calculation,
                            but may result in omitting some non-trivial subchains. Default: 1
        level (float, optional): the cutoff of the non-trivial structure probability. If 0, all the subchains with at
                            least one non-trivial closure are treated as non-trivial. Default: 0
        matrix_plot (bool, optional): if to plot a figure of a matrix (knot fingerprint). Default: False
        plot_ofile (str, optional): the name of the matrix figure plot. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the matrix figure plot. Viable formats are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        output_file (str, optional): the name of the file with the matrix results. If empty, the resulting matrix is
                            returned to source. Default: ''
        output_format (str, optional): the format of the matrix output. The viable formats are the parameters of the
                            OutputFormat class. Default: OutputFormat.DICTIONARY
        cuda (bool, optional): if to use the cuda-provided acceleration if possible. Default: True
        run_parallel (bool, optional): if to use the Python-provided parallelization of calculation. Default: True
        parallel_workers (int, optional): number of parallel workers. If 0, all the available processors will be used.
                            Default: 0
        debug (bool, optional): the debug mode. Default: False

    Returns:
        The dictionary with the HOMFLY-PT polynomial results. For each subchain a separate dictionary with different
        polynomial probabilities is created.
    """
    result = Invariant(input_data)
    return result.calculate(HomflyGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            poly_reduce=poly_reduce, translate=translate, chiral=chiral, boundaries=boundaries,
                            hide_trivial=hide_trivial, external_dictionary=external_dictionary, max_cross=max_cross,
                            matrix=matrix, density=density, level=level, cuda=cuda, matrix_plot=matrix_plot,
                            plot_ofile=plot_ofile, plot_format=plot_format, output_file=output_file,
                            output_format=output_format, run_parallel=run_parallel, parallel_workers=parallel_workers,
                            debug=debug)


def yamada(input_data, closure=Closure.TWO_POINTS, tries=200, reduce_method=ReduceMethod.KMT, poly_reduce=True,
           translate=False, external_dictionary='', chiral=False, boundaries=None, hide_trivial=True, max_cross=15,
           matrix=False, density=1, level=0, matrix_plot=False, plot_ofile="KnotFingerPrintMap",
           plot_format=PlotFormat.PNG, output_file='', output_format=OutputFormat.Dictionary, cuda=True,
           run_parallel=False, parallel_workers=None, debug=False):
    """
    Calculates the Yamada polynomial of the given structure.

    Args:
        input_data (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str, optional): the method to close the chain. Viable options are the parameters of the Closure
                            closure. Default: Closure.TWO_POINTS
        tries (int, optional): the number of tries for stochastic closure methods. Default: 200
        reduce_method (str, optional): the method of chain reduction. Viable options are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT
        boundaries (list of [int, int]): the boundaries of the subchains to be checked. The subchains are specified as
                            a list of subchain beginning and ending index. If empty, the whole chain is calculated.
                            Default: []
        max_cross (int, optional): the maximal number of crossings after reduction to start the polynomial calculation.
                            Default: 15
        poly_reduce (bool, optional): if the polynomial should be presented in the reduced form. Default: False
        translate (bool, optional): if translate the polynomial to the structure topology using the dictionary.
                            Default: False
        external_dictionary (str, optional): the path to the file with the external dictionary of the polynomials.
                            Default: ''
        chiral (bool, optional): if to take into account the structure chirality. Default: False
        hide_trivial (bool, optional): if to suppress printing out the trivial results. Default: True
        matrix (bool, optional): if to calculate the whole matrix i.e. the polynomial for each subchain. Default: False
        density (int, optional): the inverse of resolution of matrix calculation. Higher number speeds up calculation,
                            but may result in omitting some non-trivial subchains. Default: 1
        level (float, optional): the cutoff of the non-trivial structure probability. If 0, all the subchains with at
                            least one non-trivial closure are treated as non-trivial. Default: 0
        matrix_plot (bool, optional): if to plot a figure of a matrix (knot fingerprint). Default: False
        plot_ofile (str, optional): the name of the matrix figure plot. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the matrix figure plot. Viable formats are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        output_file (str, optional): the name of the file with the matrix results. If empty, the resulting matrix is
                            returned to source. Default: ''
        output_format (str, optional): the format of the matrix output. The viable formats are the parameters of the
                            OutputFormat class. Default: OutputFormat.DICTIONARY
        cuda (bool, optional): if to use the cuda-provided acceleration if possible. Default: True
        run_parallel (bool, optional): if to use the Python-provided parallelization of calculation. Default: True
        parallel_workers (int, optional): number of parallel workers. If 0, all the available processors will be used.
                            Default: 0
        debug (bool, optional): the debug mode. Default: False

    Returns:
        The dictionary with the Yamada polynomial results. For each subchain a separate dictionary with different
        polynomial probabilities is created.
    """
    result = Invariant(input_data)
    return result.calculate(YamadaGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            poly_reduce=poly_reduce, translate=translate, chiral=chiral, boundaries=boundaries,
                            hide_trivial=hide_trivial, external_dictionary=external_dictionary, max_cross=max_cross,
                            matrix=matrix, density=density, level=level, cuda=cuda, matrix_plot=matrix_plot,
                            plot_ofile=plot_ofile, plot_format=plot_format, output_file=output_file,
                            output_format=output_format, run_parallel=run_parallel, parallel_workers=parallel_workers,
                            debug=debug)


def kauffman_bracket(input_data, closure=Closure.TWO_POINTS, tries=200, reduce_method=ReduceMethod.KMT,
                     poly_reduce=True, translate=False, external_dictionary='', chiral=False, boundaries=None,
                     hide_trivial=True, max_cross=15, matrix=False, density=1, level=0, matrix_plot=False,
                     plot_ofile="KnotFingerPrintMap", plot_format=PlotFormat.PNG, output_file='',
                     output_format=OutputFormat.Dictionary, cuda=True, run_parallel=False, parallel_workers=None,
                     debug=False):
    """
    Calculates the Kauffman bracket of the given structure.

    Args:
        input_data (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str, optional): the method to close the chain. Viable options are the parameters of the Closure
                            closure. Default: Closure.TWO_POINTS
        tries (int, optional): the number of tries for stochastic closure methods. Default: 200
        reduce_method (str, optional): the method of chain reduction. Viable options are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT
        boundaries (list of [int, int]): the boundaries of the subchains to be checked. The subchains are specified as
                            a list of subchain beginning and ending index. If empty, the whole chain is calculated.
                            Default: []
        max_cross (int, optional): the maximal number of crossings after reduction to start the polynomial calculation.
                            Default: 15
        poly_reduce (bool, optional): if the polynomial should be presented in the reduced form. Default: False
        translate (bool, optional): if translate the polynomial to the structure topology using the dictionary.
                            Default: False
        external_dictionary (str, optional): the path to the file with the external dictionary of the polynomials.
                            Default: ''
        chiral (bool, optional): if to take into account the structure chirality. Default: False
        hide_trivial (bool, optional): if to suppress printing out the trivial results. Default: True
        matrix (bool, optional): if to calculate the whole matrix i.e. the polynomial for each subchain. Default: False
        density (int, optional): the inverse of resolution of matrix calculation. Higher number speeds up calculation,
                            but may result in omitting some non-trivial subchains. Default: 1
        level (float, optional): the cutoff of the non-trivial structure probability. If 0, all the subchains with at
                            least one non-trivial closure are treated as non-trivial. Default: 0
        matrix_plot (bool, optional): if to plot a figure of a matrix (knot fingerprint). Default: False
        plot_ofile (str, optional): the name of the matrix figure plot. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the matrix figure plot. Viable formats are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        output_file (str, optional): the name of the file with the matrix results. If empty, the resulting matrix is
                            returned to source. Default: ''
        output_format (str, optional): the format of the matrix output. The viable formats are the parameters of the
                            OutputFormat class. Default: OutputFormat.DICTIONARY
        cuda (bool, optional): if to use the cuda-provided acceleration if possible. Default: True
        run_parallel (bool, optional): if to use the Python-provided parallelization of calculation. Default: True
        parallel_workers (int, optional): number of parallel workers. If 0, all the available processors will be used.
                            Default: 0
        debug (bool, optional): the debug mode. Default: False

    Returns:
        The dictionary with the Kauffman bracket results. For each subchain a separate dictionary with different
        polynomial probabilities is created.
    """
    result = Invariant(input_data)
    return result.calculate(KauffmanBracketGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            poly_reduce=poly_reduce, translate=translate, chiral=chiral, boundaries=boundaries,
                            hide_trivial=hide_trivial, external_dictionary=external_dictionary, max_cross=max_cross,
                            matrix=matrix, density=density, level=level, cuda=cuda, matrix_plot=matrix_plot,
                            plot_ofile=plot_ofile, plot_format=plot_format, output_file=output_file,
                            output_format=output_format, run_parallel=run_parallel, parallel_workers=parallel_workers,
                            debug=debug)


def kauffman_polynomial(input_data, closure=Closure.TWO_POINTS, tries=200, reduce_method=ReduceMethod.KMT,
                        poly_reduce=True, translate=False, external_dictionary='', chiral=False, boundaries=None,
                        hide_trivial=True, max_cross=15, matrix=False, density=1, level=0, matrix_plot=False,
                        plot_ofile="KnotFingerPrintMap", plot_format=PlotFormat.PNG, output_file='',
                        output_format=OutputFormat.Dictionary, cuda=True, run_parallel=False, parallel_workers=None,
                        debug=False):
    """
    Calculates the Kauffman two-variable polynomial of the given structure.

    Args:
        input_data (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str, optional): the method to close the chain. Viable options are the parameters of the Closure
                            closure. Default: Closure.TWO_POINTS
        tries (int, optional): the number of tries for stochastic closure methods. Default: 200
        reduce_method (str, optional): the method of chain reduction. Viable options are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT
        boundaries (list of [int, int]): the boundaries of the subchains to be checked. The subchains are specified as
                            a list of subchain beginning and ending index. If empty, the whole chain is calculated.
                            Default: []
        max_cross (int, optional): the maximal number of crossings after reduction to start the polynomial calculation.
                            Default: 15
        poly_reduce (bool, optional): if the polynomial should be presented in the reduced form. Default: False
        translate (bool, optional): if translate the polynomial to the structure topology using the dictionary.
                            Default: False
        external_dictionary (str, optional): the path to the file with the external dictionary of the polynomials.
                            Default: ''
        chiral (bool, optional): if to take into account the structure chirality. Default: False
        hide_trivial (bool, optional): if to suppress printing out the trivial results. Default: True
        matrix (bool, optional): if to calculate the whole matrix i.e. the polynomial for each subchain. Default: False
        density (int, optional): the inverse of resolution of matrix calculation. Higher number speeds up calculation,
                            but may result in omitting some non-trivial subchains. Default: 1
        level (float, optional): the cutoff of the non-trivial structure probability. If 0, all the subchains with at
                            least one non-trivial closure are treated as non-trivial. Default: 0
        matrix_plot (bool, optional): if to plot a figure of a matrix (knot fingerprint). Default: False
        plot_ofile (str, optional): the name of the matrix figure plot. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the matrix figure plot. Viable formats are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        output_file (str, optional): the name of the file with the matrix results. If empty, the resulting matrix is
                            returned to source. Default: ''
        output_format (str, optional): the format of the matrix output. The viable formats are the parameters of the
                            OutputFormat class. Default: OutputFormat.DICTIONARY
        cuda (bool, optional): if to use the cuda-provided acceleration if possible. Default: True
        run_parallel (bool, optional): if to use the Python-provided parallelization of calculation. Default: True
        parallel_workers (int, optional): number of parallel workers. If 0, all the available processors will be used.
                            Default: 0
        debug (bool, optional): the debug mode. Default: False

    Returns:
        The dictionary with the Kauffman two-variable polynomial results. For each subchain a separate dictionary with
        different polynomial probabilities is created.
    """
    result = Invariant(input_data)
    return result.calculate(KauffmanPolynomialGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            poly_reduce=poly_reduce, translate=translate, chiral=chiral, boundaries=boundaries,
                            hide_trivial=hide_trivial, external_dictionary=external_dictionary, max_cross=max_cross,
                            matrix=matrix, density=density, level=level, cuda=cuda, matrix_plot=matrix_plot,
                            plot_ofile=plot_ofile, plot_format=plot_format, output_file=output_file,
                            output_format=output_format, run_parallel=run_parallel, parallel_workers=parallel_workers,
                            debug=debug)


def blmho(input_data, closure=Closure.TWO_POINTS, tries=200, reduce_method=ReduceMethod.KMT, poly_reduce=True,
          translate=False, external_dictionary='', boundaries=None, hide_trivial=True, max_cross=15, matrix=False,
          density=1, level=0, matrix_plot=False, plot_ofile="KnotFingerPrintMap", plot_format=PlotFormat.PNG,
          output_file='', output_format=OutputFormat.Dictionary, cuda=True, run_parallel=False, parallel_workers=None,
          debug=False):
    """
    Calculates the BLM/Ho polynomial of the given structure.

    Args:
        input_data (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str, optional): the method to close the chain. Viable options are the parameters of the Closure
                            closure. Default: Closure.TWO_POINTS
        tries (int, optional): the number of tries for stochastic closure methods. Default: 200
        reduce_method (str, optional): the method of chain reduction. Viable options are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT
        boundaries (list of [int, int]): the boundaries of the subchains to be checked. The subchains are specified as
                            a list of subchain beginning and ending index. If empty, the whole chain is calculated.
                            Default: []
        max_cross (int, optional): the maximal number of crossings after reduction to start the polynomial calculation.
                            Default: 15
        poly_reduce (bool, optional): if the polynomial should be presented in the reduced form. Default: False
        translate (bool, optional): if translate the polynomial to the structure topology using the dictionary.
                            Default: False
        external_dictionary (str, optional): the path to the file with the external dictionary of the polynomials.
                            Default: ''
        hide_trivial (bool, optional): if to suppress printing out the trivial results. Default: True
        matrix (bool, optional): if to calculate the whole matrix i.e. the polynomial for each subchain. Default: False
        density (int, optional): the inverse of resolution of matrix calculation. Higher number speeds up calculation,
                            but may result in omitting some non-trivial subchains. Default: 1
        level (float, optional): the cutoff of the non-trivial structure probability. If 0, all the subchains with at
                            least one non-trivial closure are treated as non-trivial. Default: 0
        matrix_plot (bool, optional): if to plot a figure of a matrix (knot fingerprint). Default: False
        plot_ofile (str, optional): the name of the matrix figure plot. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the matrix figure plot. Viable formats are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        output_file (str, optional): the name of the file with the matrix results. If empty, the resulting matrix is
                            returned to source. Default: ''
        output_format (str, optional): the format of the matrix output. The viable formats are the parameters of the
                            OutputFormat class. Default: OutputFormat.DICTIONARY
        cuda (bool, optional): if to use the cuda-provided acceleration if possible. Default: True
        run_parallel (bool, optional): if to use the Python-provided parallelization of calculation. Default: True
        parallel_workers (int, optional): number of parallel workers. If 0, all the available processors will be used.
                            Default: 0
        debug (bool, optional): the debug mode. Default: False

    Returns:
        The dictionary with the BLM/Ho polynomial results. For each subchain a separate dictionary with different
        polynomial probabilities is created.
    """
    result = Invariant(input_data)
    return result.calculate(BlmhoGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            poly_reduce=poly_reduce, translate=translate, boundaries=boundaries,
                            hide_trivial=hide_trivial, external_dictionary=external_dictionary, max_cross=max_cross,
                            matrix=matrix, density=density, level=level, cuda=cuda, matrix_plot=matrix_plot,
                            plot_ofile=plot_ofile, plot_format=plot_format, output_file=output_file,
                            output_format=output_format, run_parallel=run_parallel, parallel_workers=parallel_workers,
                            debug=debug)


def aps(input_data, closure=Closure.TWO_POINTS, tries=200, reduce_method=ReduceMethod.KMT, poly_reduce=True,
        translate=False, external_dictionary='', chiral=False, boundaries=None, hide_trivial=True, max_cross=15,
        matrix=False, density=1, level=0, matrix_plot=False, plot_ofile="KnotFingerPrintMap",
        plot_format=PlotFormat.PNG, output_file='', output_format=OutputFormat.Dictionary, cuda=True,
        run_parallel=False, parallel_workers=None, debug=False):
    """
    Calculates the APS bracket of the given structure.

    Args:
        input_data (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str, optional): the method to close the chain. Viable options are the parameters of the Closure
                            closure. Default: Closure.TWO_POINTS
        tries (int, optional): the number of tries for stochastic closure methods. Default: 200
        reduce_method (str, optional): the method of chain reduction. Viable options are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT
        boundaries (list of [int, int]): the boundaries of the subchains to be checked. The subchains are specified as
                            a list of subchain beginning and ending index. If empty, the whole chain is calculated.
                            Default: []
        max_cross (int, optional): the maximal number of crossings after reduction to start the polynomial calculation.
                            Default: 15
        poly_reduce (bool, optional): if the polynomial should be presented in the reduced form. Default: False
        translate (bool, optional): if translate the polynomial to the structure topology using the dictionary.
                            Default: False
        external_dictionary (str, optional): the path to the file with the external dictionary of the polynomials.
                            Default: ''
        chiral (bool, optional): if to take into account the structure chirality. Default: False
        hide_trivial (bool, optional): if to suppress printing out the trivial results. Default: True
        matrix (bool, optional): if to calculate the whole matrix i.e. the polynomial for each subchain. Default: False
        density (int, optional): the inverse of resolution of matrix calculation. Higher number speeds up calculation,
                            but may result in omitting some non-trivial subchains. Default: 1
        level (float, optional): the cutoff of the non-trivial structure probability. If 0, all the subchains with at
                            least one non-trivial closure are treated as non-trivial. Default: 0
        matrix_plot (bool, optional): if to plot a figure of a matrix (knot fingerprint). Default: False
        plot_ofile (str, optional): the name of the matrix figure plot. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the matrix figure plot. Viable formats are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        output_file (str, optional): the name of the file with the matrix results. If empty, the resulting matrix is
                            returned to source. Default: ''
        output_format (str, optional): the format of the matrix output. The viable formats are the parameters of the
                            OutputFormat class. Default: OutputFormat.DICTIONARY
        cuda (bool, optional): if to use the cuda-provided acceleration if possible. Default: True
        run_parallel (bool, optional): if to use the Python-provided parallelization of calculation. Default: True
        parallel_workers (int, optional): number of parallel workers. If 0, all the available processors will be used.
                            Default: 0
        debug (bool, optional): the debug mode. Default: False

    Returns:
        The dictionary with the APS bracket results. For each subchain a separate dictionary with different
        polynomial probabilities is created.
    """
    result = Invariant(input_data)
    return result.calculate(ApsGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            poly_reduce=poly_reduce, translate=translate, chiral=chiral, boundaries=boundaries,
                            hide_trivial=hide_trivial, external_dictionary=external_dictionary, max_cross=max_cross,
                            matrix=matrix, density=density, level=level, cuda=cuda, matrix_plot=matrix_plot,
                            plot_ofile=plot_ofile, plot_format=plot_format, output_file=output_file,
                            output_format=output_format, run_parallel=run_parallel, parallel_workers=parallel_workers,
                            debug=debug)


def writhe(input_data, closure=Closure.TWO_POINTS, tries=200, reduce_method=ReduceMethod.KMT, poly_reduce=True,
           translate=False, boundaries=None, hide_trivial=True, max_cross=15, matrix=False, density=1, level=0,
           matrix_plot=False, plot_ofile="KnotFingerPrintMap", plot_format=PlotFormat.PNG, output_file='', cuda=True,
           run_parallel=False, parallel_workers=None, debug=False):
    result = Invariant(input_data)
    return result.calculate(WritheGraph, closure=closure, tries=tries, reduce_method=reduce_method,
                            poly_reduce=poly_reduce, translate=translate, boundaries=boundaries,
                            hide_trivial=hide_trivial, max_cross=max_cross, matrix=matrix, density=density, level=level,
                            cuda=cuda, matrix_plot=matrix_plot, plot_ofile=plot_ofile, plot_format=plot_format,
                            output_file=output_file, run_parallel=run_parallel, parallel_workers=parallel_workers,
                            debug=debug)


# TODO - test it! - Wanda!
def generate_walk(length, no_of_structures, bond_length=1, print_with_index=True,
                  file_prefix='walk', folder_prefix='', out_fmt=(3, 5)):
    """
    Generates polygonal lasso structure with vertices of equal lengths and saves
    in .xyz file. Each structures is saved in distinct file named
    <file_prefix>_<num>.xyz in folder l<looplength>_t<taillength>.

    Args:
        length (int): number of sides of polygonal random walk
        no_of_structures (int): quantity of created walks
        bond_length (int, optional): length of each side of created walks, 
                                     default: 1.
        print_with_index (bool, optional): if True, then created .xyz file has 
                              4 columns, first with index, rest for coordinates.
                              If False then there are only 3 coordinate columns.
                              Default: True.
        file_prefix (str, optional): prefix of each created file, default: "walk".
        folder_prefix (str, optional): prefix of created file folder,
                              default: no prefix.
        out_fmt ((int,int,int), optional): numbers on file and folder format
                              <num>, <looplength>, <taillength> are padded with
                              maximally these number of zeros respectively.

    Returns:
        Polygon_walk object

    """
    return Polygon_walk(length, no_of_structures, bond_length, print_with_index,
                        file_prefix, folder_prefix, out_fmt)


def generate_loop(length, no_of_structures, bond_length=1, is_loop_closed=False,
                  print_with_index=True, file_prefix='loop',
                  folder_prefix='', out_fmt=(3, 5)):
    """
    Generates polygonal loop structure with vertices of equal lengths and saves
    in .xyz file. Each structures is saved in distinct file named
    <file_prefix>_<num>.xyz in folder w<length>.

    Args:
        length (int): number of sides of polygonal loops
        no_of_structures (int): quantity of created loops
        bond_length (int, optional): length of each side of created loops, 
                                     default: 1.
        is_loop_closed (bool, optional): if True, then last creates one extra
                              node for loop with is same as it's first node,
                              default: False.
        print_with_index (bool, optional): if True, then created .xyz file has 
                              4 columns, first with index, rest for coordinates.
                              If False then there are only 3 coordinate columns.
                              Default: True.
        file_prefix (str, optional): prefix of each created file, default: "loop".
        folder_prefix (str, optional): prefix of created file folder,
                              default: no prefix.
        out_fmt ((int,int), optional): numbers on file and folder format
                              <num>, <looplength> are padded with maximally
                              these number of zeros respectively.

    Returns:
        Polygon_loop object

    """
    return Polygon_loop(length, no_of_structures, bond_length, is_loop_closed,
                        print_with_index, file_prefix, folder_prefix, out_fmt)


def generate_lasso(looplength, taillength, no_of_structures, bond_length=1,
                   is_loop_closed=False, print_with_index=True,
                   file_prefix='lasso', folder_prefix='', out_fmt=(3, 3, 5)):
    """
    Generates polygonal lasso structure with vertices of equal lengths and saves
    in .xyz file. Each structures is saved in distinct file named
    <file_prefix>_<num>.xyz in folder l<looplength>_t<taillength>.

    Args:
        looplength (int): number of sides of polygonal loop
        taillength (int): number of sides of polygonal tail
        no_of_structures (int): quantity of created loops
        bond_length (int, optional): length of each side of created lassos, 
                                     default: 1.
        is_loop_closed (bool, optional): if True, then last creates one extra
                              node for loop with is same as it's first node,
                              default: False.
        print_with_index (bool, optional): if True, then created .xyz file has 
                              4 columns, first with index, rest for coordinates.
                              If False then there are only 3 coordinate columns.
                              Default: True.
        file_prefix (str, optional): prefix of each created file,
                              default: "lasso".
        folder_prefix (str, optional): prefix of created file folder, 
                              default: no prefix.
        out_fmt ((int,int,int), optional): numbers on file and folder format
                              <num>, <looplength>, <taillength> are padded with
                              maximally these number of zeros respectively.

    Returns:
        Polygon_lasso object

    """
    return Polygon_lasso(looplength, taillength, no_of_structures, bond_length,
                         is_loop_closed, print_with_index, file_prefix,
                         folder_prefix, out_fmt)


# //

# def generate_handcuff(looplengths, taillength, no_of_structures,
#                   is_loop_closed = False, print_with_index = True,
#                   file_prefix = 'hdcf', folder_prefix = '', out_fmt= (3,3,3,5)):
#    return Polygon_handcuff(looplengths, taillength, no_of_structures,
#                            is_loop_closed, print_with_index, file_prefix,
#                            folder_prefix, out_fmt)

## /


def find_loops(structure, output_type=OutputType.PDcode):
    """
    Finds all loops in a given structure.

    Args:
        structure (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        output_type (str, optional): the output format of the loops. The viable formats are parameters of the
                            OutputType class. Default: OutputType.PDcode.

    Returns:
        The generator object of the loops in a chosen format.
    """
    g = Graph(structure)
    return g.find_loops(output_type=output_type)


def find_thetas(structure, output_type=OutputType.PDcode):
    """
    Finds all theta-curves in a given structure.

    Args:
        structure (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        output_type (str, optional): the output format of the loops. The viable formats are parameters of the
                            OutputType class. Default: OutputType.PDcode.

    Returns:
        The generator object of the loops in a chosen format.
    """
    g = Graph(structure)
    return g.find_thetas(output_type=output_type)


def find_handcuffs(structure, output_type=OutputType.PDcode):
    """
    Finds all theta-curves in a given structure.

    Args:
        structure (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        output_type (str, optional): the output format of the loops. The viable formats are parameters of the
                            OutputType class. Default: OutputType.PDcode.

    Returns:
        The generator object of the loops in a chosen format.
    """
    g = Graph(structure)
    return g.find_handcuffs(output_type=output_type)


def gln(chain1, chain2, indices1=(-1, -1), indices2=(-1, -1)):
    """
    Calculates gaussian linking number between two chains.

    Args:
        chain1: coordinates in of chain1 in one of a variety of possible formats
        chain2: coordinates in of chain1 in one of a variety of possible formats
        indices1 ([int,int], optional): first and last index of desired chain1
        indices2 ([int,int], optional): first and last index of desired chain2

    Returns:
        lala

    """
    obj = GLN(chain1, chain2, indices1, indices2)
    return obj.gln()


def gln_max(chain1, chain2, indices1=(-1, -1), indices2=(-1, -1), density=-1, precision_out=3):
    """
    Calculates maximal possible gaussian linking number between all possible subchains of two chains.

    Args:
        chain1: coordinates in of chain1 in one of a variety of possible formats
        chain2: coordinates in of chain1 in one of a variety of possible formats
        indices1 ([int,int], optional): first and last index of desired chain1
        indices2 ([int,int], optional): first and last index of desired chain2
        density (int, optional):
        precision_out (int, optional): 

    Returns:
        lala

    """
    obj = GLN(chain1, chain2, indices1, indices2)
    return obj.gln_max(density, precision_out)


def gln_average(chain1, chain2, indices1=(-1, -1), indices2=(-1, -1), tryamount=200):
    """
    Calculates average gaussian linking number between all possible subchains of two chains.

    Args:
        chain1: coordinates in of chain1 in one of a variety of possible formats
        chain2: coordinates in of chain1 in one of a variety of possible formats
        indices1 ([int,int], optional): first and last index of desired chain1
        indices2 ([int,int], optional): first and last index of desired chain2
        tryamount (int, optional): 

    Returns:
        lala

    """
    obj = GLN(chain1, chain2, indices1, indices2)
    return obj.gln_average(tryamount)


def gln_matrix(chain1, chain2, indices1=(-1, -1), indices2=(-1, -1)):
    """
    Finds gaussian linking number between chain1 and all possible subchains of chain2 and returns as matrix.

    Args:
        chain1: coordinates in of chain1 in one of a variety of possible formats
        chain2: coordinates in of chain1 in one of a variety of possible formats
        indices1 ([int,int], optional): first and last index of desired chain1
        indices2 ([int,int], optional): first and last index of desired chain2

    Returns:
        lala

    """
    obj = GLN(chain1, chain2, indices1, indices2)
    return obj.gln_matrix()


def make_surface(coordinates, loop_indices=None, precision=0, density=1):
    """
    Calculates minimals surface spanned on a given loop.

    Args:
        coordinates:
        loop_indices (list, optional):
        precision (int, optional):
        density (int, optional):

    Returns:
        lalalala

    """
    obj = Lasso(coordinates, loop_indices)
    return obj.make_surface(precision, density)


# Dla pustej listy mostkow trzeba zrobic petle po wszystkich mostkach w self.bridges
# musi byc tez dodatkowy parametr bridges=Bridges.SSBOND


def lasso_type(coordinates, loop_indices=None, smoothing=0, step=1, precision=PrecisionSurface.HIGH,
               density=DensitySurface.MEDIUM, min_dist=(10, 3, 10), pic_files=SurfacePlotFormat.DONTPLOT,
               output_prefix='', output_type=1):
    """
    Calculates minimals surface spanned on a given loop and checks if remaining part of chain crosses the surface and
    how many times. Returns corresponding topoly type of lasso.

    Args:
        coordinates:
        loop_indices (list):
        smoothing (int, optional):
        step (int, optional):
        precision (int, optional):
        density (int, optional):
        min_dist ((int, int, int), optional): min_dist, min_bridge_dist_min_tail_dist
        pic_files (int, optional):
        output_prefix (str, optional):
        output_type (int, optional):

    Returns:

    """
    obj = Lasso(coordinates, loop_indices)
    return obj.lasso_type(smoothing, step, precision, density, min_dist,
                          pic_files, output_prefix, output_type)


def translate(structure, output_type=OutputType.PDcode):
    """
    Translates between the abstract codes.

    Args:
        structure (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        output_type (str, optional): the output format of the loops. The viable formats are parameters of the
                            OutputType class. Default: OutputType.PDcode.

    Returns:
        The structure in a given format.
    """
    g = Graph(structure)
    return g.print(output_type=output_type)


def find_matching(data, invariant, chiral=False, external_dictionary=''):
    """
    Finds the matching structure for a given polynomial. Searches either the built-in, or user-defined dictionary

    Args:
        data: the polynomial given either in string of coefficients (e.g. '1 -1 1'),
            the dictionary of polynomials with their probabilities (e.g. {'1 -1 1': 0.8, '1 -3 1': 0.2},
            or dictionary of probabilities for each subchain (e.g.  {(0, 100): {'1 -1 1': 0.8, '1 -3 1': 0.2},
                                                                    (50, 100): {'1 -1 1': 0.3, '1': 0.7}}.
        invariant (string): the name of the invariant, e.g. 'Alexander', of 'Jones'.
        chiral (bool, optional): if the chirality should be taken into account. By default False.
        external_dictionary (string, optional): The absolute path to the user-defined dictionary of polynomials.
            The dictionary must be compliant with the template which can be obtained on the Topoly website
            (https://topoly.cent.uw.edu.pl).

    Returns:
        Either the string with matching structure name (e.g. '3_1'),
            or the dictionary with the structure name and respective probability (e.g. {'3_1': 0.8, '4_1': 0.2}),
            or the dictionary with data for each subchain, e.g. {(0, 100): {'3_1': 0.8, '4_1': 0.2},
                                                                (50, 100): {'3_1': 0.3, '0_1': 0.7}}.
    """
    return find_matching_structure(data, invariant, chiral=chiral, external_dictionary=external_dictionary)


def plot_matrix(matrix, plot_ofile="KnotFingerPrintMap", plot_format=PlotFormat.PNG, level=0.48, palette='',
                debug=False):
    """
    Plotting the figure for a given fingerprint matrix.

    Args:
        matrix (str): the matrix with information about the topology of each subchain of the structure. Can be given
                            either in dictionary, or KnotProt format. The matrix can be given directly,
                            or as a path to the file.
        plot_ofile (str, optional): the name of the output file with the matrix figure. Default: KnotFingerPrintMap
        plot_format (str, optional): the format of the output matrix figure. Viable options are the parameters of the
                            PlotFormat class. Default: PlotFormat.PNG
        level (float, optional): the cutoff of the non-trivial structure probability. All structures with probability
                            below the cutoff will be regarded as trivial, and therefore not marked in the figure.
                            Default: 0.48
        palette (str, optional): the palette of colors for matrix plot. Viable options are parameters of the Palette
                            class. Default: Palette.KNOT
        debug (bool, optional): the debug mode.

    Returns:
        Communicate about the figure creation.
    """
    return manipulation.plot_matrix(matrix, plot_ofile=plot_ofile, plot_format=plot_format, palette=palette,
                                    cutoff=level, debug=debug)


def plot_graph(structure, palette=None):
    """
    Plotting the 3D rotable presentation of the structure with each arc colored differently.

    Args:
        structure (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        palette (list, optional): the palette of colors for matrix plot. Viable options are parameters of the Palette
                            class. Default: Palette.RAINBOW

    Returns:
        Communicate about the figure creation.
    """
    g = Graph(structure)
    g.plot(palette)
    return


def import_structure(structure_name):
    """
    Finds a PDcode of the structure required and creates a corresponding graph.

    Args:
        structure_name (str): the name of the structure to create.

    Returns:
        The graph of the corresponding structure defined by the PDcode.
    """
    if structure_name in PD.keys():
        return Graph(PD[structure_name])
    else:
        raise TopolyException('The structure chosen is not available in the local library.')


def close_curve(structure, closure=Closure.TWO_POINTS, output_type=OutputType.XYZ):
    """
    Closing the structure (connecting loose ends) with a chosen method.

    Args:
        structure (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        closure (str): the method used to close the structure. Viable methods are the parameters of the Closure class.
                            Default: Closure.TWO_POINTS.
        output_type (str): the format of the reduced chain. Default: OutputType.XYZ.

    Returns:
        The abstract code or the coordinates of the closed structure.
    """
    return chain_close(structure, closure=closure, output_type=output_type)


def reduce(structure, reduce_method=ReduceMethod.KMT, output_type=OutputType.XYZ):
    """
    Reducing the structure to a form with less crossing in a planar projection.

    Args:
        structure (str/list): the structure to calculate the polynomial for, given in abstract code, coordinates,
                            or the path to the file containing the data.
        reduce_method (str): the method used to reduce the structure. Viable methods are the parameters of the
                            ReduceMethod class. Default: ReduceMethod.KMT.
        output_type (str): the format of the reduced chain. The abstract codes are possible only for closed structure.
                            Default: OutputType.XYZ.

    Returns:
        The abstract code or the coordinates of the reduced structure.
    """
    return chain_reduce(structure, reduce_method=reduce_method, output_type=output_type)


def xyz2vmd(xyz_file):
    """
    Converts .xyz file into .pdb file and creates .psf topoly file with same name.
    Then you can open your structure in vmd typing "vmd file.pdb -psf file.psf"
    
    .xyz file format:
            4 columns (id, x, y, z), atoms in neighboring rows are treated as
            bonded, lines with single letter (e.g. X) separate different arcs.
    
    Args:
            xyz_file (str): name of xyz file

    """
    return convert_xyz2vmd(xyz_file)
