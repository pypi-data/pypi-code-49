"""
The module containing the functions for calculating the isotopy invariants starting from graphs. In particular,
it contains functions to calculate knot invariants (Jones, Alexander, HOMFLY-PT) and spatial graph invariants.

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

import array
from topoly.topoly_homfly import *
from topoly.topoly_preprocess import *
from topoly.topoly_knot import *
from topoly.topoly_lmpoly import *
from .graph import Graph
from .polvalues import polvalues
from . import plot_matrix, data2knotprot, data2string
from .params import Closure, ReduceMethod, PlotFormat, TopolyException, OutputFormat
from .polynomial import polynomial as Poly
from itertools import product
import re


def find_matching_structure(data, invariant, chiral=False, external_dictionary=''):
    if not data:
        return data
    if type(data) is str or type(data) is Poly:
        return find_matching_knot(data, invariant, chiral=chiral, external_dictionary=external_dictionary)
    elif type(data) is dict and type(list(data.keys())[0]) is str:
        return find_point_matching(data, invariant, chiral=chiral, external_dictionary=external_dictionary)
    elif type(data) is dict and type(list(data.keys())[0]) is tuple:
        for subchain in data.keys():
            data[subchain] = find_point_matching(data[subchain], invariant, chiral=chiral, external_dictionary=external_dictionary)
    else:
        raise TopolyException("Unknown format of the data to identify the matching structure")
    return data


def find_matching_knot(data, invariant, chiral=False, external_dictionary=''):
    data = str(data)
    inverted = -1
    if '{' not in data and '|' not in data and '[' not in data and 'Too' not in data:
        inverted = ' '.join([str(-int(_)) for _ in data.strip().split()])
    result = polvalues[invariant].get(data, 'Unknown')
    if not chiral:
        result = re.sub('\.[1-9]*', '', re.sub('[\-\+]', '', result))
    if result == 'Unknown':
        result = polvalues[invariant].get(inverted, 'Unknown')
    if result == 'Unknown' and external_dictionary:
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("topoly_dictionary", external_dictionary)
            topoly_dictionary = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(topoly_dictionary)
            user_dictionary = topoly_dictionary.user_dictionary
            result = user_dictionary[invariant].get(data, 'Unknown')
        except ImportError:
            raise TopolyException("Cannot import the user defined dictionary")
    return result


def find_point_matching(data, invariant, chiral=False, external_dictionary=''):
    result = {}
    for key in data.keys():
        translated = find_matching_knot(key, invariant, chiral=chiral, external_dictionary=external_dictionary)
        if translated in result.keys():
            result[translated] += data[key]
        else:
            result[translated] = data[key]
    return result


def analyze_statistics(statistics, level=0):
    counter = {}
    if len(statistics) == 0:
        counter[0] = 1
    else:
        for polynomial in statistics:
            if polynomial not in counter.keys():
                counter[polynomial] = 0
            counter[polynomial] += 1
        for polynomial in counter.keys():
            counter[polynomial] = float(counter[polynomial])/len(statistics)
    return counter


def generate_identifier(subgraph):
    # TODO generalize on many arcs (theta-curves for example)
    return subgraph[0][0], subgraph[-1][0]


class Invariant(Graph):
    name = 'Invariant'
    known = {}
    communicate = ''

    def calculate(self, invariant, closure=Closure.TWO_POINTS, tries=200, direction=0, reduce_method=ReduceMethod.KMT,
                  poly_reduce=True, translate=False, external_dictionary='', chiral=False, boundaries=None,
                  hide_trivial=True, max_cross=15, matrix=True, density=1, level=0, cuda=True, matrix_plot=False,
                  plot_ofile="KnotFingerPrintMap", plot_format=PlotFormat.PNG, output_file='',
                  output_format=OutputFormat.Dictionary, run_parallel=False, parallel_workers=None, debug=False):

        if not boundaries:
            boundaries = []
        if output_file:
            matrix = True
        if translate:
            poly_reduce = True
        if matrix_plot:
            matrix = True
        if closure == Closure.CLOSED:
            tries = 1
        if len(boundaries) > 1 and matrix:
            matrix = False
            # TODO add Topoly warning:
            # With more than one subchain specified with the boundary variable the matrix cannot be calculated.
            # Calculating only the subchains specified.
        if matrix and len(self.arcs) > 1:
            raise TopolyException("The matrix can be calculated only for one arc for now.")

        matrix_result = {}

        if matrix and cuda and isinstance(invariant, AlexanderGraph):
            g = Invariant([[key] + self.coordinates[key] for key in self.coordinates.keys()])
            matrix_result = g.calc_cuda(closure=closure, tries=tries, direction=direction, reduce=reduce_method,
                       density=density, level=level, debug=debug)

        if run_parallel:
            print('parallel')
            # run_invarian_subgraph_part = partial(self.run_invariant_subgraph, tries, closure, direction, reduce_method, debug, level)
            # if not parallel_workers:
            #     parallel_workers = os.cpu_count() or 1
            # pool = Pool(processes=parallel_workers)
            # for ident, res in pool.imap_unordered(run_invarian_subgraph_part, self.generate_subchain(matrix=matrix, density=density, beg=beg, end=end), chunksize=4):
            #     if res != 0:
            #         additional.append(ident)
            #         result[ident] = res
            #         print(str(ident) + ': ' + str(res))
        else:
            subgraphs = self.generate_subchain(matrix=matrix, density=density, boundaries=boundaries)
            matrix_result = self.analyze_points(invariant, subgraphs, matrix_result, closure=closure,
                    reduce_method=reduce_method, direction=direction, max_cross=max_cross, tries=tries, hide_trivial=hide_trivial, poly_reduce=poly_reduce, debug=debug)

            additional = self.find_additional(matrix_result, density, level)

            if additional:
                matrix_result = self.analyze_points(invariant, additional, matrix_result, closure=closure,
                    reduce_method=reduce_method, direction=direction, max_cross=max_cross, tries=tries, hide_trivial=hide_trivial, debug=debug)

        # single chain calculation and non-empty result
        if not matrix and len(boundaries) < 2 and matrix_result:
            matrix_result = matrix_result[list(matrix_result.keys())[0]]

        if type(matrix_result) is dict:
            if translate:
                matrix_result = find_matching_structure(matrix_result, invariant.name, chiral=chiral,
                                                        external_dictionary=external_dictionary)

        if matrix_plot:
            plot_matrix(matrix_result, plot_ofile=plot_ofile, plot_format=plot_format)

        if output_file:
            if output_format == 'knotprot':
                with open(output_file, 'w') as myfile:
                    myfile.write(data2knotprot(matrix_result, 1, -1))
            elif output_format == 'dict':
                with open(output_file, 'w') as myfile:
                    myfile.write(data2string(matrix_result))
        return matrix_result

    def generate_subchain(self, matrix=False, density=1, boundaries=[], debug=False):
        if not self.coordinates and self.pdcode:
            return [self.pdcode]

        chain_beg = min(list(self.coordinates.keys()))
        chain_end = max(list(self.coordinates.keys()))
        subgraphs = []

        if boundaries:
            subgraphs = [(max(chain_beg, x), min(chain_end, y)) for x, y in boundaries]
        elif not matrix:
            subgraphs = [(chain_beg, chain_end)]
        else:
            for subchain_end in range(chain_beg, chain_end + 1, density):
                for subchain_beg in range(chain_beg, subchain_end - 5, density):
                    subgraphs.append((subchain_beg, subchain_end))
        return subgraphs

    def find_additional(self, matrix_results, density=1, level=0):
        additional = []
        central_points = []

        # trivial case
        if density == 1:
            return additional

        chain_beg = min(list(self.coordinates.keys()))
        chain_end = max(list(self.coordinates.keys()))

        # searching for subchains, which were identified as non-trivial
        for subchain in matrix_results.keys():
            knots = matrix_results[subchain]
            if type(knots) is not dict:
                continue
            for knot in knots.keys():
                if knot == '0_1':
                    continue
                elif knots[knot] > level:
                    central_points.append(subchain)
                    break

        # for each non-trivial point calculate its surrounding
        for point in central_points:
            horizontal = [k for k in range(max(point[0] - int(density / 2), chain_beg),
                                           min(point[0] + int(density / 2), chain_end))]
            vertical = [k for k in
                        range(max(point[1] - int(density / 2), chain_beg), min(point[1] + int(density / 2), chain_end))]
            for subchain in product(horizontal, vertical):
                additional.append(subchain)

        return additional

    def analyze_points(self, invariant, subgraphs, matrix_result, closure=Closure.TWO_POINTS,
                       reduce_method=ReduceMethod.KMT, direction=0, max_cross=15, tries=200, poly_reduce=True, hide_trivial=True, debug=False):
        for subchain_beg, subchain_end in subgraphs:
            results = []
            subchain = super().cut_chain(beg=subchain_beg, end=subchain_end)
            ident = generate_identifier(subchain)

            for k in range(tries):
                if debug:
                    print('Subchain: ' + str(ident) + '; Try: ' + str(k + 1))
                g = invariant(subchain)
                g.close(method=closure, direction=direction, debug=debug)
                g.reduce(method=reduce_method, debug=debug)
                g.parse_closed()
                results.append(g.calc_point(max_cross=max_cross, poly_reduce=poly_reduce, debug=debug))
                if debug:
                    print(results[-1] + '\n---')
            result = analyze_statistics(results)

            # removing trivial
            if not hide_trivial or (hide_trivial and result != {'1': 1.0}):
                matrix_result[ident] = result
                if debug:
                    print(ident, ": Statistics after " + str(tries) + " tries", matrix_result[ident], '\n===')
        return matrix_result


    def print_communicate(self):
        com1 = ''
        com2 = ''
        if self.level > 0:
            for _ in range(self.level - 1):
                com1 += '|  '
                com2 += '|  '
            com1 += '|->'
            com2 += '|  '
        com1 += self.communicate + self.pdcode
        print(com1)
        return com2


class AlexanderGraph(Invariant):
    name = 'Alexander'

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if poly_reduce:
            result = result.print_short().split('|')[1].strip()
        return str(result)

    def point(self, max_cross=15, debug=False):
        code = self.pdcode
        if len(code.split(';')) >  max_cross:
            raise TopolyException("Too many crossings.")

        # Analyzing known
        if code in super().known[__class__.name].keys():
            coefs = super().known[__class__.name][code]
            if debug:
                print(self.shift + 'Known case.\n' + self.shift + "Result " + self.communicate + str(coefs))

        else:
            p_red = calc_alexander_poly(self.coordinates_c[0])
            if debug:
                print("Coefficients obtained: " + str(p_red))
            # TODO is it the right condition?
            if not p_red:
                p_red = '1'
            coefs = p_red.split()
            if int(coefs[0]) < 0:
                coefs = [str(-int(_)) for _ in coefs]
            super().known[__class__.name][code] = coefs

        p = Poly('0')
        for k in range(len(coefs)):
            power = k - int((len(coefs)-1)/2)
            p += Poly(coefs[k]) * Poly('x**' + str(power))
        return p

    def calc_cuda(self, closure=Closure.TWO_POINTS, tries=200, direction=0, reduce=ReduceMethod.KMT,
                       density=1, level=0, debug=False):
        matrix = find_alexander_fingerprint_cuda(self.coordinates_W[0], density, level, closure, tries)
        return matrix


class JonesGraph(Invariant):
    name = 'Jones'
    level = 0
    communicate = ''
    shift = ''

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if poly_reduce:
            result = result.print_short()
        return str(result)

    def point(self, max_cross=15, debug=False):
        """ The basic method to calculate the Jones polynomial for closed structure. Its input data is the PD code."""

        # simplifying the graph, returns the number of 1st Reidemeister moves performed
        n = self.simplify(debug=False)
        if len(self.crossings) > max_cross:
            raise TopolyException("Too many crossings.")

        # TODO moze te funkcje mozna gdzies wywalic?
        self.generate_orientation()
        self.check_crossings_vs_orientation()

        if debug:
            self.shift = super().print_communicate()
            print(self.shift + "After simplification: " + self.pdcode + '\tn=' + str(n))

        # Check if the structure is in the known cases
        known_case = self.analyze_known(debug=debug)
        if known_case:
            return known_case

        # Treating split sum
        subgraphs = self.find_disjoined_components()
        if len(subgraphs) > 1:
            return self.analyze_split_graphs(subgraphs, n, debug=debug)

        # Reducing crossing by skein relation
        if len(self.crossings) > 0:
            return self.make_skein(n, debug=debug)

        # No crossing, no vertex = empty graph
        super().known[__class__.name][self.pdcode] = Poly('1')
        res = Poly('1')
        if debug:
            print(self.shift + "Empty graph. Result " + str(res))
        return res

    def make_skein(self, n, debug=False):
        """Performing the Jones skein relation on a random crossing k."""
        k = random.randint(0, len(self.crossings) - 1)
        sign = self.find_crossing_sign(k)

        # The coefficients in skein relation. The exact coefficients depend on the sign of the crossing.
        smoothing_coefficient = Poly(str(sign)) * Poly('t**0.5-t**-0.5') * Poly('t**' + str(sign))
        invert_coefficient = Poly('t**' + str(2 * sign))

        if debug:
            print(self.shift + "Reducing crossing " + str(self.crossings[k]) + " by skein relation. It is " +
                  str(sign) + " crossing.")

        # smoothing the crossing
        smoothed_graph = JonesGraph(self.smooth_crossing(k, sign))
        smoothed_graph.communicate = '(' + str(smoothing_coefficient) + ')*'
        smoothed_graph.level = self.level + 1
        smoothed_result = smoothed_graph.point(debug=debug)

        # inverting the crossing
        inverted_graph = JonesGraph(self.invert_crossing(k))
        inverted_graph.communicate = '(' + str(invert_coefficient) + ')*'
        inverted_graph.level = self.level + 1
        inverted_result = inverted_graph.point(debug=debug)

        super().known[__class__.name][self.pdcode] = smoothing_coefficient * smoothed_result + \
                                                     invert_coefficient * inverted_result
        res = super().known[__class__.name][self.pdcode]

        if debug:
            print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
        return res

    def analyze_split_graphs(self, subgraphs, n, debug=False):
        """Iteration over the subgraphs."""
        if debug:
            print(self.shift + "It's a split graph: " + '; '.join(subgraphs))

        super().known[__class__.name][self.pdcode] = Poly('1')
        for subgraph in subgraphs:
            partial_graph = JonesGraph(subgraph)
            partial_graph.level = self.level + 1
            partial_graph.communicate = ' * '
            partial_result = partial_graph.point(debug=debug)
            super().known[__class__.name][self.pdcode] *= partial_result

        super().known[__class__.name][self.pdcode] *= Poly('-t**0.5-t**-0.5')
        res = super().known[__class__.name][self.pdcode]

        if debug:
            print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
        return res

    def analyze_known(self, debug=False):
        """Analyzing known structures."""
        result = ''

        # Checking in the dictionary known:
        if self.pdcode in super().known[__class__.name].keys() and super().known[__class__.name][self.pdcode]:
            res = super().known[__class__.name][self.pdcode]
            if debug:
                print(self.shift + 'Known case.\n' + self.shift + "Result " + self.communicate + str(res))
            result = res

        # Checking if its a circle
        elif len(self.vertices) == 1 and not self.crossings:
            super().known[__class__.name][self.pdcode] = Poly('1')
            res = super().known[__class__.name][self.pdcode]
            if debug:
                print(self.shift + "It's a circle.")
            result = res

        # Checking if its a split sum of two circles
        if len(self.vertices) == 2 and not self.crossings:
            super().known[__class__.name][self.pdcode] = Poly('-t**0.5-t**-0.5')
            res = super().known[__class__.name][self.pdcode]
            if debug:
                print(self.shift + "It's a split sum of two circles.")
            result = res

        return result


class YamadaGraph(Invariant):
    name = 'Yamada'
    level = 0
    communicate = ''
    shift = ''

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if poly_reduce:
            result = result.print_short().split('|')[1].strip()
        return str(result)

    def point(self, max_cross=15, debug=False):
        """ The basic method to calculate the Yamada polynomial for closed structure. Its input data is the PD code."""

        # simplifying the graph, returns the number of 1st Reidemeister moves performed
        n = self.simplify(debug=False)
        if len(self.crossings) > max_cross:
            raise TopolyException("Too many crossings.")

        # TODO moze te funkcje mozna gdzies wywalic?
        self.generate_orientation()
        self.check_crossings_vs_orientation()

        if debug:
            self.shift = super().print_communicate()
            print(self.shift + "After simplification: " + self.pdcode + '\tn=' + str(n))

        # Check if the structure is in the known cases
        known_case = self.analyze_known(n, debug=debug)
        if known_case:
            return known_case

        # Treating split sum
        subgraphs = self.find_disjoined_components()
        if len(subgraphs) > 1:
            return self.analyze_split_graphs(subgraphs, n, debug=debug)

        # Reducing crossing - there are two ways, first better in terms of efficiency than the second
        if len(self.crossings) > 0:
            for k in range(len(self.crossings)):
                inverted_graph = YamadaGraph(self.invert_crossing(k))
                inverted_graph.simplify()
                if len(inverted_graph.crossings) < len(self.crossings):
                    # the skein-like relation
                    return self.make_skein(k, n, debug=debug)
            else:
                # removing of the first (0) crossing
                return self.remove_crossing(0, n, debug=debug)

        # Edges reduction:
        edges = self.get_noloop_edges()
        if len(edges) > 0:  # than len(self.vertices) >= 2
            return self.reduce_edges(n, edges, debug=debug)

        # No crossing, no vertex = empty graph
        super().known[__class__.name][self.pdcode] = Poly('1')
        res = Poly('1')
        if debug:
            print(self.shift + "Empty graph. Result " + str(res))
        return res

    def analyze_known(self, n, debug=False):
        """Analyzing known structures."""
        result = ''
        factor = Poly(str((-1) ** (n % 2)) + 'x^' + str(n))     # factor coming from the Reidemeister I and V moves

        # checking the dictionary of already calculated polynomials
        if self.pdcode in super().known[__class__.name].keys() and super().known[__class__.name][self.pdcode]:
            res = super().known[__class__.name][self.pdcode] * factor
            if debug:
                print(self.shift + 'Known case.\n' + self.shift + "Result " + self.communicate + '(' + str(res) + ')')
            result = res

        # bouquet of circles - number of circles in bouquet = len(set(graph.vertices[0]))
        elif len(self.vertices) == 1 and not self.crossings:
            n_circles = len(set(self.vertices[0]))
            super().known[__class__.name][self.pdcode] = Poly(-1) * Poly('-x-1-x^-1') ** n_circles
            res = super().known[__class__.name][self.pdcode] * factor
            if debug:
                print(self.shift + "It's a bouquet of " + str(n_circles) + " circles.\n" +
                      self.shift + "Result " + self.communicate + '(' + str(res) + ')')
            result = res

        # trivial theta or trivial handcuff
        elif len(self.vertices) == 2 and not self.crossings and len(self.vertices[1]) == 3:
            if set(self.vertices[0]) == set(self.vertices[1]):  # trivial theta
                super().known[__class__.name][self.pdcode] = Poly('-x^2-x-2-x^-1-x^-2')
                res = super().known[__class__.name][self.pdcode] * factor
                if debug:
                    print(self.shift + "It's a trivial theta.\n" + self.shift + "Result " + self.communicate +
                          '(' + str(res) + ')')
                result = res

            elif len(set(self.vertices[0]) & set(self.vertices[1])) == 1:  # trivial handcuff
                super().known[__class__.name][self.pdcode] = Poly('0')
                res = super().known[__class__.name][self.pdcode]
                if debug:
                    print(self.shift + "It's a trivial handcuff graph.\n" + self.shift + "Result " +
                          '(' + str(res) + ')')
                result = res

        else:    # other simplifying cases
            for v in range(len(self.vertices)):
                vert = self.vertices[v]
                if len(vert) > 3:
                    for k in range(len(vert)):
                        if vert[k] == vert[k - 1]:
                            # bouquet with one loop
                            if debug:
                                print(self.shift + "Removing loop.")
                            removed_loop_graph = YamadaGraph(self.remove_loop(v, k))
                            removed_loop_graph.level = self.level + 1
                            removed_loop_graph.communicate = ' * '
                            removed_loop_result = removed_loop_graph.point(debug=debug)

                            super().known[__class__.name][self.pdcode] = Poly('-1') * Poly('x+1+x^-1') * removed_loop_result
                            res = super().known[__class__.name][self.pdcode] * factor
                            if debug:
                                print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
                            result = res
        return result

    def analyze_split_graphs(self, subgraphs, n, debug=False):
        """Iteration over the subgraphs."""

        factor = Poly(str((-1) ** (n % 2)) + 'x^' + str(n))     # factor coming from the Reidemeister I and V moves

        if debug:
            print(self.shift + "It's a split graph: " + '; '.join(subgraphs))

        super().known[__class__.name][self.pdcode] = Poly('1')
        for subgraph in subgraphs:
            partial_graph = YamadaGraph(subgraph)
            partial_graph.level = self.level + 1
            partial_graph.communicate = ' * '
            partial_result = partial_graph.point(debug=debug)
            super().known[__class__.name][self.pdcode] *= partial_result

        res = super().known[__class__.name][self.pdcode] * factor

        if debug:
            print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
        return res

    def make_skein(self, k, n, debug=False):
        """Performing the Yamada skein-like relation on a crossing k."""

        # The coefficients in skein relation.
        smooth_positive_coefficient = Poly('x-x^-1')
        smooth_negative_coefficient = -Poly('x-x^-1')
        factor = Poly(str((-1) ** (n % 2)) + 'x^' + str(n))     # factor coming from the Reidemeister I and V moves

        if debug:
            print(self.shift + "Reducing crossing " + str(self.crossings[k]) + " by skein relation.")

        # "positive" smooth of the crossing
        smoothed_positive = YamadaGraph(self.smooth_crossing(k, 1))
        smoothed_positive.communicate = '(' + str(smooth_positive_coefficient) + ')*'
        smoothed_positive.level = self.level + 1
        smoothed_positive_result = smoothed_positive.point(debug=debug)

        # "negative" smooth of the crossing
        smoothed_negative = YamadaGraph(self.smooth_crossing(k, -1))
        smoothed_negative.communicate = '(' + str(smooth_negative_coefficient) + ')*'
        smoothed_negative.level = self.level + 1
        smoothed_negative_result = smoothed_negative.point(debug=debug)

        # inverting the crossing
        inverted_graph = YamadaGraph(self.invert_crossing(k))
        inverted_graph.communicate = ' + '
        inverted_graph.level = self.level + 1
        inverted_result = inverted_graph.point(debug=debug)

        super().known[__class__.name][self.pdcode] = smooth_positive_coefficient * smoothed_positive_result + \
                                       smooth_negative_coefficient * smoothed_negative_result + \
                                       inverted_result
        res = factor * super().known[__class__.name][self.pdcode]

        if debug:
            print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
        return res

    def remove_crossing(self, crossing_index, n, debug=False):
        """Removing the crossing crossing_index with introduction of new vertex."""

        # The coefficients in skein relation.
        smooth_positive_coefficient = Poly('x')
        smooth_negative_coefficient = Poly('x^-1')
        factor = Poly(str((-1) ** (n % 2)) + 'x^' + str(n))     # factor coming from the Reidemeister I and V moves

        if debug:
            print(self.shift + "Reducing crossing " + str(self.crossings[k]) + " by skein relation.")

        # "positive" smooth of the crossing
        smoothed_positive = YamadaGraph(self.smooth_crossing(crossing_index, 1))
        smoothed_positive.communicate = '(' + str(smooth_positive_coefficient) + ')*'
        smoothed_positive.level = self.level + 1
        smoothed_positive_result = smoothed_positive.point(debug=debug)

        # "negative" smooth of the crossing
        smoothed_negative = YamadaGraph(self.smooth_crossing(crossing_index, -1))
        smoothed_negative.communicate = '(' + str(smooth_negative_coefficient) + ')*'
        smoothed_negative.level = self.level + 1
        smoothed_negative_result = smoothed_negative.point(debug=debug)

        # vertex introduction
        new_vertex = YamadaGraph(self.smooth_crossing(crossing_index, 0))
        new_vertex.communicate = ' + '
        new_vertex.level = self.level + 1
        new_vertex_result = new_vertex.point(debug=debug)

        super().known[__class__.name][self.pdcode] = smooth_positive_coefficient * smoothed_positive_result + \
                                     smooth_negative_coefficient * smoothed_negative_result + \
                                     new_vertex_result
        res = super().known[__class__.name][self.pdcode] * factor

        if debug:
            print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
        return res

    def reduce_edges(self, n, edges, debug=False):
        """Reducing the first no-loop edge."""
        factor = Poly(str((-1) ** (n % 2)) + 'x^' + str(n))     # factor coming from the Reidemeister I and V moves

        if debug:
            print(com2 + "Reducing noloop edge " + str(edges[0]) + ".")

        # graph with removed no-loop edge
        removed_edge = YamadaGraph(self.reduce_edges(edges[0]))
        removed_edge.level = self.level + 1
        removed_edge_result = removed_edge.point(debug=debug)

        # graph with contracted edge
        contracted_edge = YamadaGraph(self.contract_edge(edges[0]))
        contracted_edge.level = self.level + 1
        contracted_edge.communicate = ' + '
        contracted_edge_result = contracted_edge.point(debug=debug)

        super().known[__class__.name][self.pdcode] = removed_edge_result + contracted_edge_result
        res = super().known[__class__.name][self.pdcode] * factor

        if debug:
            print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
        return res


class HomflyGraph(Invariant):
    name = 'HOMFLY-PT'

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if not poly_reduce:
            result = self.make_poly_explicit(result)
        return str(result)

    def truncate_bytes(s, maxlen=128, suffix=b'...'):
        # type: (bytes, int, bytes) -> bytes
        if maxlen and len(s) >= maxlen:
            return s[:maxlen].rsplit(b' ', 1)[0] + suffix
        return s

    def point(self, max_cross=15, debug=False):
        code = self.emcode.replace(';', '\n')
        if len(code.split('\n')) > max_cross:
            raise TopolyException("Too many crossings.")

        # Analyzing known structures
        if code in super().known[__class__.name].keys():
            result = super().known[__class__.name][code]
            if debug:
                print(self.shift + 'Known case.\n' + self.shift + "Result " + self.communicate + str(res))
        else:
            result = lmpoly(code).replace('\n', '|')
            super().known[__class__.name][code] = result
        return result

    def make_poly_explicit(self, poly):
        # the method is not strictly static, as it depends on the implicit variables (l,m) of the HOMFLY-PT polynomial
        result = Poly(0)
        rows = poly.split('|')
        m0 = len(rows)
        for m in range(len(rows)):
            row = rows[m]
            if row[0] == '[' and row[-1] == ']' and (len(row.split()) > 1 or row[1] == '['):
                m0 = m
                row = row[1:-1]
            terms = row.split()
            row_poly = Poly(0)
            l0 = len(terms)
            for l in range(len(terms)):
                term = terms[l]
                if '[' in term:
                    l0 = l
                    term = term[1:-1]
                row_poly += Poly(term) * Poly('l**' + str(l))
            result += row_poly * Poly('l**-' + str(l0) + 'm**' + str(m))
        result = result * Poly('m**-' + str(m0))
        return result


class ConwayGraph(Invariant):
    name = 'Conway'
    level = 0
    communicate = ''
    shift = ''

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if poly_reduce:
            result = result.print_short().split('|')[1].strip()
        return str(result)

    def point(self, max_cross=15, debug=False):
        """ The basic method to calculate the Conway polynomial for closed structure, using the skein relation.
        The methods input is the PD code."""

        # simplifying the graph, returns the number of 1st Reidemeister moves performed
        n = self.simplify(debug=False)
        if len(self.crossings) > max_cross:
            raise TopolyException("Too many crossings.")

        # TODO moze te funkcje mozna gdzies wywalic?
        self.generate_orientation()
        self.check_crossings_vs_orientation()

        if debug:
            self.shift = super().print_communicate()
            print(self.shift + "After simplification: " + self.pdcode + '\tn=' + str(n))

        # Check if the structure is in the known cases
        known_case = self.analyze_known(debug=debug)
        if known_case:
            return known_case

        # Treating split sum
        subgraphs = self.find_disjoined_components()
        if len(subgraphs) > 1:
            return Poly(0)

        # Reducing crossing by skein relation
        if len(self.crossings) > 0:
            return self.make_skein(n, debug=debug)

        # No crossing, no vertex = empty graph
        super().known[__class__.name][self.pdcode] = Poly('1')
        res = Poly('1')
        if debug:
            print(self.shift + "Empty graph. Result " + str(res))
        return res

    def analyze_known(self, debug=False):
        """Analyzing known structures."""
        result = ''

        # Checking in the dictionary known:
        if self.pdcode in super().known[__class__.name].keys() and super().known[__class__.name][self.pdcode]:
            res = super().known[__class__.name][self.pdcode]
            if debug:
                print(self.shift + 'Known case.\n' + self.shift + "Result " + self.communicate + str(res))
            result = res

        # Checking if its a circle
        elif len(self.vertices) == 1 and not self.crossings:
            super().known[__class__.name][self.pdcode] = Poly('1')
            res = super().known[__class__.name][self.pdcode]
            if debug:
                print(self.shift + "It's a circle.")
            result = res

        # Checking if its a split sum of two circles
        if len(self.vertices) == 2 and not self.crossings:
            super().known[__class__.name][self.pdcode] = Poly(0)
            res = super().known[__class__.name][self.pdcode]
            if debug:
                print(self.shift + "It's a split sum of two circles.")
            result = res

        return result

    def make_skein(self, n, debug=False):
        """Performing the Conway skein relation on a random crossing k."""
        k = random.randint(0, len(self.crossings) - 1)
        sign = self.find_crossing_sign(k)

        # The coefficients in skein relation. The exact coefficients depend on the sign of the crossing.
        smoothing_coefficient = Poly(str(sign)) * Poly('z')

        if debug:
            print(self.shift + "Reducing crossing " + str(self.crossings[k]) + " by skein relation. It is " +
                  str(sign) + " crossing.")

        # smoothing the crossing
        smoothed_graph = ConwayGraph(self.smooth_crossing(k, sign))
        smoothed_graph.communicate = '(' + str(smoothing_coefficient) + ')*'
        smoothed_graph.level = self.level + 1
        smoothed_result = smoothed_graph.point(debug=debug)

        # inverting the crossing
        inverted_graph = ConwayGraph(self.invert_crossing(k))
        inverted_graph.communicate = ' + '
        inverted_graph.level = self.level + 1
        inverted_result = inverted_graph.point(debug=debug)

        super().known[__class__.name][self.pdcode] = smoothing_coefficient * smoothed_result + inverted_result
        res = super().known[__class__.name][self.pdcode]

        if debug:
            print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
        return res


class KauffmanBracketGraph(Invariant):
    name = 'Kauffman bracket'

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if poly_reduce:
            result = result.print_short().split('|')[1].strip()
        return str(result)

    def point(self, max_cross=15, b='A**-1', d='-A**2-A**-2', debug=False):
        """ The basic method to calculate the Kauffman bracket for closed structure. Its input data is the PD code.
        The user may substitute different value of the parameters b and d in the Kauffman Bracket definition
        instead of the regular ones."""

        res = Poly('0')
        n = len(self.crossings)
        if n > max_cross:
            raise TopolyException("Too many crossings.")

        # calculating the polynomial value as the iteration of smoothings.
        for state in product([-1, 1], repeat=n):
            g = KauffmanBracketGraph(self.pdcode)
            for smooth in state:
                g = KauffmanBracketGraph(g.smooth_crossing(0, smooth))
            smooth_a = Poly('A**' + str(int((n + sum(state))/2)))
            smooth_b = Poly('B**' + str(int((n - sum(state))/2)))
            separate_parts = Poly('d**' + str(len(g.vertices)-1))
            term_res = smooth_a * smooth_b * separate_parts
            if debug:
                print("State: " + str(state) + ". Result: " + str(term_res))
            res += term_res
        res = res({'B': b, 'd': d})
        return res


class WritheGraph(Invariant):
    name = 'Writhe'

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        return str(self.point(debug=debug))

    def point(self, debug=False):
        res = sum([self.find_crossing_sign(k) for k in range(len(self.crossings))])
        return res


class KauffmanPolynomialGraph(Invariant):
    name = 'Kauffman polynomial'
    level = 0
    communicate = ''
    shift = ''

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if poly_reduce:
            result = result.print_short()
        return str(result)

    def point(self, max_cross=15, debug=False):
        self.simplify(debug=debug)
        if len(self.crossings) > max_cross:
            raise TopolyException("Too many crossings.")

        writhe = WritheGraph(self.pdcode).point()
        res = Poly('a**' + str(-writhe))
        g = Kauffman2VariableGraph(self.pdcode)
        res *= g.point(max_cross=max_cross, debug=debug)
        return res


class Kauffman2VariableGraph(WritheGraph):
    name = 'Kauffman two variable polynomial'
    level = 0
    communicate = ''
    shift = ''

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if poly_reduce:
            result = result.print_short()
        return str(result)

    def point(self, max_cross=15, debug=False):
        """ The basic method to calculate the Kauffman two-variable Polynomial polynomial for closed structure.
        Its input data is the PD code."""

        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}

        # simplifying the graph, returns the number of 1st Reidemeister moves performed
        n = int(self.simplify(debug=False)/2)
        if len(self.crossings) > max_cross:
            raise TopolyException("Too many crossings.")

        # TODO moze te funkcje mozna gdzies wywalic?
        self.generate_orientation()
        self.check_crossings_vs_orientation()

        if debug:
            self.shift = super().print_communicate()
            print(self.shift + "After simplification: " + self.pdcode + '\tn=' + str(n))

        # Check if the structure is in the known cases
        known_case = self.analyze_known(n, debug=debug)
        if known_case:
            return known_case

        # Treating split sum
        subgraphs = self.find_disjoined_components()
        if len(subgraphs) > 1:
            return self.analyze_split_graphs(subgraphs, n, debug=debug)

        # Reducing crossing by skein relation
        if len(self.crossings) > 0:
            return self.make_skein(n, debug=debug)

        # No crossing, no vertex = empty graph
        super().known[__class__.name][self.pdcode] = Poly('1')
        res = Poly('1')
        if debug:
            print(self.shift + "Empty graph. Result " + str(res))
        return res

    def analyze_known(self, n, debug=False):
        """Analyzing known structures."""
        result = ''
        factor = Poly('a^' + str(n))    # factor coming from the Reidemeister I move

        # Checking in the dictionary known:
        if self.pdcode in super().known[__class__.name].keys() and super().known[__class__.name][self.pdcode]:
            res = super().known[__class__.name][self.pdcode] * factor
            if debug:
                print(self.shift + 'Known case.\n' + self.shift + "Result " + self.communicate + str(res))
            result = res

        # Checking if its a circle
        elif len(self.vertices) == 1 and not self.crossings:
            super().known[__class__.name][self.pdcode] = Poly('1')
            res = super().known[__class__.name][self.pdcode] * factor
            if debug:
                print(self.shift + "It's a circle.")
            result = res

        # Checking if its a split sum of two circles
        if len(self.vertices) == 2 and not self.crossings:
            super().known[__class__.name][self.pdcode] = Poly('a+a**-1-z') * Poly('z**-1')
            res = super().known[__class__.name][self.pdcode] * factor
            if debug:
                print(self.shift + "It's a split sum of two circles.")
            result = res

        return result

    def analyze_split_graphs(self, subgraphs, n, debug=False):
        """Iteration over the subgraphs."""
        if debug:
            print(self.shift + "It's a split graph: " + '; '.join(subgraphs))

        factor = Poly('a^' + str(n))    # factor coming from the Reidemeister I move

        super().known[__class__.name][self.pdcode] = Poly('1')
        for subgraph in subgraphs:
            partial_graph = JonesGraph(subgraph)
            partial_graph.level = self.level + 1
            partial_graph.communicate = ' * '
            partial_result = partial_graph.point(debug=debug)
            super().known[__class__.name][self.pdcode] *= partial_result

        super().known[__class__.name][self.pdcode] *= Poly('a+a**-1-z')*Poly('z**-1')
        res = super().known[__class__.name][self.pdcode] * factor

        if debug:
            print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
        return res

    def make_skein(self, n, debug=False):
        """Performing the two variable Kauffman Polynomial skein relation on a random crossing k."""
        k = random.randint(0, len(self.crossings) - 1)
        sign = self.find_crossing_sign(k)
        factor = Poly('a^' + str(n))    # factor coming from the Reidemeister I move

        # The coefficients in skein relation. The exact coefficients depend on the sign of the crossing.
        positive_smooth_coefficient = Poly('z')
        negative_smooth_coefficient = Poly('z')

        if debug:
            print(self.shift + "Reducing crossing " + str(self.crossings[k]) + " by skein relation. It is " +
                  str(sign) + " crossing.")

        # positive smoothing
        positive_smooth = Kauffman2VariableGraph(self.smooth_crossing(k, 1))
        positive_smooth.communicate = '(' + str(positive_smooth_coefficient) + ')*'
        positive_smooth.level = self.level + 1
        positive_smooth_result = positive_smooth.point(debug=debug)

        # negative smoothing
        negative_smooth = Kauffman2VariableGraph(self.smooth_crossing(k, -1))
        negative_smooth.communicate = '(' + str(negative_smooth_coefficient) + ')*'
        negative_smooth.level = self.level + 1
        negative_smooth_result = negative_smooth.point(debug=debug)

        # inverting the crossing
        inverted_graph = Kauffman2VariableGraph(self.invert_crossing(k))
        inverted_graph.communicate = ' - '
        inverted_graph.level = self.level + 1
        inverted_result = inverted_graph.point(debug=debug)

        super().known[__class__.name][self.pdcode] = positive_smooth_coefficient * positive_smooth_result + \
                                     negative_smooth_coefficient * negative_smooth_result - \
                                     inverted_result

        res = super().known[__class__.name][self.pdcode] * factor

        if debug:
            print(self.shift + 'Result ' + str(res) + '\t(n=' + str(n) + ').')
        return res


class BlmhoGraph(Invariant):
    name = 'BLM/Ho'

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if poly_reduce:
            result = result.print_short()
        return str(result)

    def point(self, max_cross=15, debug=False):
        g = Kauffman2VariableGraph(self.pdcode)
        res = g.point(max_cross=max_cross, debug=debug)
        res = res({'a': 1, 'z': 'x'})
        if debug:
            print('After substitution: ' + str(res))
        return res


class ApsGraph(Invariant):
    name = 'APS'

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        result = self.point(max_cross=max_cross, debug=debug)
        if poly_reduce:
            result = result.print_short()
        return str(result)

    def point(self, max_cross=15, debug=False):
        raise NotImplementedError('APS not implemented yet!')


class GlnGraph(Invariant):
    name = 'GLN'

    def calc_point(self, max_cross=15, poly_reduce=True, debug=False):
        if __class__.name not in super().known.keys():
            super().known[__class__.name] = {}
        return str(self.point(debug=debug).print_short())

    def point(self, debug=False):
        raise NotImplementedError('GLN not implemented yet!')
