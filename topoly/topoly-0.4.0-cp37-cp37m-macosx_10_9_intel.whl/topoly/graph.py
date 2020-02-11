"""
The graph class containing the methods to calculate the graph (and knot) polynomials.
The graphs are stored as extended PD codes, including the information on vertices and crossings in planar projection.

Pawel Dabrowski-Tumanski
p.dabrowski at cent.uw.edu.pl
27.06.2019

Docs:
https://realpython.com/documenting-python-code/#docstring-types

The type used here: Google


Support in PyCharm:
https://www.jetbrains.com/help/pycharm/settings-tools-python-integrated-tools.html
- change default reStructuredText to Google

Docs will be published in: https://readthedocs.org/

"""
import os
import re
import random
from concurrent.futures.process import ProcessPoolExecutor
from functools import partial
from itertools import combinations, product
from copy import deepcopy
from multiprocessing.pool import Pool

import matplotlib as plt
import numpy as np

from .params import ReduceMethod, OutputType
from topoly.topoly_knot import *
from topoly.topoly_homfly import *
from topoly.topoly_lmpoly import *
from .manipulation import *

plot_colors = ['blue', 'red', 'green', 'yellow', 'cyan', 'magenta']


class Graph:
    def __init__(self, init_data='', chain=None, bridges=[], breaks=[], debug=False):
        # TODO ogarnac przypadek, kiedy uzytkownik daje plik, ktory nie istnieje
        # TODO a takze pusta liste
        self.orig_input = init_data
        if type(init_data) is str and os.path.isfile(init_data):
            with open(init_data, 'r') as myfile:
                init_data = myfile.read()
        self.init_data = init_data

        data = DataParser.read_format(self.init_data, self.orig_input, chain, bridges, breaks, debug)
        # real, coordinate-based properties of the graph:
        self.coordinates = data['coordinates']
        self.coordinates_c = []
        self.closed = data['closed']
        self.arcs = data['arcs']
        self.breaks = data['breaks']
        self.bridges = data['bridges']
        self.spatial_graph = self.generate_spatial_graph()
        self.identifier = ()

        # abstract, code-based properties of the graph
        self.pdcode = data['pdcode']
        self.emcode = data['emcode']
        self.vertices = []
        self.crossings = []
        self.abstract_graph = {}
        self.edges = set()
        self.orientation = []

        if self.closed:
            self.parse_closed()

    def get_coords(self):
        return self.coords2list(self.coordinates)

    @staticmethod
    def coords2list(coords): 
        keys = list(coords.keys())
        vals = list(coords.values())
        for i in range(len(keys)):
            vals[i].insert(0,keys[i])
        return vals

    def parse_closed(self):
        if self.coordinates and not self.coordinates_c:
            self.generate_coordinates_c()
        if self.coordinates_c and not self.emcode:
            self.generate_em_from_coords()
        if self.emcode and not self.pdcode:
            self.generate_pd_from_em()
        if self.pdcode and not self.emcode:
            self.generate_em_from_pd()
        self.generate_crossings()
        self.generate_vertices()
        self.generate_edges()
        self.generate_orientation()
        self.check_crossings_vs_orientation()
        self.generate_abstract_graph()
        return

    ''' Methods for generating, finding, and checking '''
    def check_crossings_vs_orientation(self):
        for k in range(len(self.crossings)):
            for arc in self.orientation:
                if self.crossings[k][0] in arc:     # TODO - to jakas tragedia. Moze mozna prosciej?
                    if arc.index(self.crossings[k][2]) < arc.index(self.crossings[k][0]) or arc.index(self.crossings[k][2]) == 0:
                        self.crossings[k] = self.crossings[k][2:] + self.crossings[k][:2]
        return

    def generate_coordinates_c(self):
        for arc in self.arcs:
            chain = ''
            for atom in arc:
                chain += str(atom) + ' ' + ' '.join([str(x) for x in self.coordinates[atom]]) + '\n'
            chain_c, unable = chain_read_from_string(chain.encode('utf-8'))
            self.coordinates_c.append(chain_c)
        return

    def generate_em_from_coords(self):
        # TODO polaczyc przypadki w programie Wandy
        if len(self.coordinates_c) == 1:
            code = find_link_homfly_code(self.coordinates_c)
        else:
            code = find_link_yamada_code(self.coordinates_c)
        code = code.decode('utf-8').strip().replace('\n', ';')
        self.emcode = code
        return

    def generate_pd_from_em(self):
        result = ''
        letters = 'abcd'
        intervals = []
        for cross in self.emcode.split(';'):
            if not cross:
                continue
            number, rest = re.sub('[-+V]', ' ', cross, count=1).split()
            typ = cross.strip(number)[0]
            code_tmp = []
            tmp = re.split(r'(\d+)', rest)[1:]
            for k in range(0, len(tmp), 2):
                end = tmp[k] + tmp[k + 1]
                if typ == 'V':
                    start = number + 'V'
                else:
                    start = number + letters[int(k / 2)]
                interval = [start, end]
                interval_rev = list(reversed(interval))
                if interval_rev in intervals:
                    code_tmp.append(str(intervals.index(interval_rev)))
                    intervals[intervals.index(interval_rev)] = 0
                else:
                    intervals.append(interval)
                    code_tmp.append(str(len(intervals) - 1))
            if typ == '-':
                code_tmp = list(reversed(code_tmp))
            if typ == '+':
                code_tmp = [code_tmp[1], code_tmp[0], code_tmp[3], code_tmp[2]]
            result += re.sub('[-+]', 'X', typ) + '[' + ','.join(code_tmp) + '];'
        self.pdcode = result[:-1].strip()
        return

    def generate_em_from_pd(self):
        # TODO ten kod trzeba poprawic
        # emcode = ''
        # arcs = {}
        # letters = ['c','b','a','d']
        # crosses = self.pdcode.split(';')
        # for k in range(len(crosses)):
        #     cross = crosses[k]
        #     typ = cross[0]
        #     edges = cross.strip('XV[]').split(',')
        #     for l in range(len(edges)):
        #         edge = edges[l]
        #         if edge not in arcs:
        #             arcs[edge] = []
        #         if typ == 'V':
        #             arcs[edge].append('V' + str(k))
        #         else:
        #             arcs[edge].append(str(k)+letters[l])
        # for k in range(len(crosses)):
        #     cross = crosses[k]
        #     edges = cross.strip('XV[]').split(',')
        #     orient = '+'
        #     emcross = str(k) + orient
        #     for edge in edges:
        #         for a in arcs[edge]:
        #             if int(a.strip('Vabcd')) != k:
        #                 emcross += a
        #     emcode += emcross + ';'
        # self.emcode = emcode
        return

    def generate_vertices(self):
        self.vertices = []
        for element in self.pdcode.split(';'):
            if element[0] == 'V':
                self.vertices.append([int(x) for x in element.strip('V[]').split(',')])
        if not self.vertices and self.crossings:
            # inserting a base vertex of valency 2
            max_ind = max([edge for cross in self.crossings for edge in cross])
            self.vertices.append([self.crossings[0][0], max_ind + 1])
            self.crossings[0][0] = max_ind + 1
        self.update_pdcode()
        return

    def generate_crossings(self):
        self.crossings = []
        for element in self.pdcode.split(';'):
            if element[0] == 'X':
                self.crossings.append([int(x) for x in element.strip('X[]').split(',')])
        return

    def generate_edges(self):
        self.edges = set()
        for cross in self.crossings:
            self.edges |= set(cross)
        for vert in self.vertices:
            self.edges |= set(vert)
        return

    def generate_spatial_graph(self):
        graph = {}
        for arc in self.arcs:
            if arc[0] not in graph.keys():
                graph[arc[0]] = []
            graph[arc[0]].append([arc[-1], arc[1:]])

            if arc[-1] not in graph.keys():
                graph[arc[-1]] = []
            graph[arc[-1]].append([arc[0], list(reversed(arc[:-1]))])
        return graph


    def generate_abstract_graph(self):
        graph = {}
        graph_edges = []    # the edges comming out of vertices
        for k in range(len(self.vertices)):
            graph[k] = []
            graph_edges += self.vertices[k]
        self.abstract_graph = graph
        for arc in self.orientation:
            beg, end = (-1, -1)
            for k in range(len(self.vertices)):
                if arc[-1] in self.vertices[k]:
                    if arc[-1] != arc[0] or beg >= 0 or arc[-1] in self.vertices[k][self.vertices[k].index(arc[-1])+1:]:
                        end = k
                if arc[0] in self.vertices[k] and beg < 0:
                    beg = k
            graph[beg].append([end, arc])
            if beg != end:
                graph[end].append([beg, list(reversed(arc))])
        return

    def generate_subchain_detailed(self, additional, density=1):
        # TODO - something is missing here !!!!
        if not additional:
            return []

    def generate_coords_from_c(self):
        self.coordinates = {}
        last_id = 0
        for arc in self.coordinates_c:
            id = 0
            for atom in arc:
                id = int(atom['id']) + last_id
                chains = [x for x in atom.keys() if x != 'id']
                coord_dict = atom[chains[0]]
                coords = [coord_dict[k] for k in ['x', 'y', 'z']]
                self.coordinates[id] = coords
            last_id = id
        return

    def generate_coords_from_atom_list(self, atoms):
        result = ''
        for arc in atoms:
            for atom in arc:
                result += str(atom) + ' ' + ' '.join([str(_) for _ in self.coordinates[atom]]) + '\n'
            result += 'X\n'
        return result[:-2]

    def generate_code_from_edges(self, edges):
        code = ''
        crossings = []
        vertices = []
        trans = {}

        # choosing appropriate crossings and vertices
        for cross in self.crossings:
            if all([c in edges for c in cross]):
                crossings.append(cross)
            else:
                trans[cross[0]] = cross[2]
                trans[cross[1]] = cross[3]
        for v in self.vertices:
            codev = []
            for e in edges:
                if e in v:
                    codev.append(e)
            if codev:
                vertices.append(codev)

        # simplifying the dictionary
        changed = True
        while changed:
            changed = False
            keys = list(trans.keys())
            for key in keys:
                if trans[key] in keys:
                    val = trans[trans[key]]
                    trans.pop(trans[key])
                    trans[key] = val
                    changed = True
                    break

        # making a PD code
        for cross in crossings:
            for k in range(len(cross)):
                if cross[k] in trans.keys():
                    cross[k] = trans[cross[k]]
            code += 'X[' + ','.join([str(x) for x in cross]) + '];'
        for vert in vertices:
            for k in range(len(vert)):
                if vert[k] in trans.keys():
                    vert[k] = trans[vert[k]]
            code += 'V[' + ','.join([str(x) for x in vert]) + '];'
        return code[:-1]

    def generate_orientation(self):
        # TODO uproscic
        edges_num = len(self.crossings) * 2 + len(self.vertices)
        vertex_edges = [edge for vertex in self.vertices for edge in vertex]
        crossing_edges = [edge for cross in self.crossings for edge in cross]
        paths = [[x] for x in list(set(vertex_edges) - set(crossing_edges))]
        checked = []
        while len(checked) < edges_num:
            for vert in self.vertices:
                if len(vert) == 2 and vert[0] == vert[1]:
                    paths.append([vert[0]])
            # searching for starting crossing
            path = []
            cross = []
            for cross in self.crossings:
                if cross[0] not in checked:
                    path += [cross[0], cross[2]]
                    break
            if not path:
                for cross in self.crossings:
                    if cross[1] not in checked:
                        path += [cross[1], cross[3]]
                        break
            while path and cross:
                b = False
                for c in self.crossings:
                    if path[-1] in c and c[c.index(path[-1]) - 2] not in path:
                        path.append(c[c.index(path[-1]) - 2])
                        break
                    if path[0] in c and c[c.index(path[0]) - 2] not in path:
                        path = [c[c.index(path[0]) - 2]] + path
                        break
                    if path[-1] in c and path[-1] in c[c.index(path[-1])+1:]:
                        ind = c.index(path[-1]) + c[c.index(path[-1])+1:].index(path[-1]) + 1
                        path.append(c[ind-2])
                    if path[0] in c and path[0] in c[c.index(path[0])+1:]:
                        ind = c.index(path[0]) + c[c.index(path[0])+1:].index(path[0]) + 1
                        path = [c[ind-2]] + path
                    if path[-1] in c and c[c.index(path[-1]) - 2] == path[0] and c != cross:
                        b = True
                        break
                if path[-1] in vertex_edges and path[0] in vertex_edges:
                    b = True
                    break
                if b:
                    break
            if path:
                paths.append(path)
            checked = [item for sublist in paths for item in sublist]
        self.orientation = paths
        return

    def update_pdcode(self):
        code = ''
        for vert in self.vertices:
            code += 'V[' + ','.join([str(x) for x in vert]) + '];'
        for cross in self.crossings:
            code += 'X[' + ','.join([str(x) for x in cross]) + '];'
        self.pdcode = code[:-1]

    def update(self, trans={}):
        # filling in the untranslated edges
        for key in self.edges:
            if key not in trans.keys():
                trans[key] = key

        # making the translation
        self.crossings = [[trans[c[i]] for i in range(4)] for c in self.crossings]
        self.vertices = [[trans[v[i]] for i in range(len(v))] for v in self.vertices]
        self.update_pdcode()
        return

    def find_path(self, start, end, graph):
        fringe = [(start, [])]
        while fringe:
            state, path = fringe.pop()
            if path and state == end:
                yield path
                continue
            for next_state, edge_list in graph[state]:
                if edge_list and edge_list[0] in path:
                    continue
                if next_state == start:
                    continue
                fringe.append((next_state, path + edge_list))
        return

    def find_loops(self, output_type=OutputType.PDcode):
        if not self.coordinates:
            return self.find_loops_abstract(output_type=output_type)
        else:
            return self.find_loops_coords(output_type=output_type)

    def find_loops_abstract(self, output_type=OutputType.PDcode):
        if output_type != OutputType.PDcode:
            raise TopolyException("Cannot generate the coordinates! (yet)")
        vertices = list(self.abstract_graph.keys())
        found = []
        for v1, v2 in combinations(vertices, 2):
            for arc1, arc2 in combinations([path for path in self.find_path(v1, v2, self.abstract_graph)], 2):
                loop = arc1 + list(reversed(arc2))
                if not set(arc1) & set(arc2) and set(loop) not in found:
                    g = Graph(self.generate_code_from_edges(loop))
                    result = g.print(output_type=output_type)
                    found.append(set(loop))
                    del g
                    yield result

    def find_loops_coords(self, output_type=OutputType.PDcode):
        vertices = list(self.spatial_graph.keys())
        found = []
        for v1, v2 in combinations(vertices, 2):
            for arc1, arc2 in combinations([path for path in self.find_path(v1, v2, self.spatial_graph)], 2):
                arc1 = [v1] + arc1[:-1]
                arc2 = arc2
                loop = arc1 + list(reversed(arc2))
                if not set(arc1) & set(arc2) and set(loop) not in found:
                    g = Graph(self.generate_coords_from_atom_list([loop]))
                    g.close(method=Closure.CLOSED)
                    g.parse_closed()
                    result = g.print(output_type=output_type)
                    found.append(set(loop))
                    yield result
        return

    def find_thetas(self, output_type=OutputType.PDcode):
        if not self.coordinates:
            return self.find_thetas_abstract(output_type=output_type)
        else:
            return self.find_thetas_coords(output_type=output_type)

    def find_thetas_abstract(self, output_type=OutputType.PDcode):
        if output_type != OutputType.PDcode:
            raise TopolyException("Cannot generate the coordinates! (yet)")
        vertices = list(self.abstract_graph.keys())
        found = []
        for v1, v2 in combinations(vertices, 2):
            for arc1, arc2, arc3 in combinations([path for path in self.find_path(v1, v2, self.abstract_graph)], 3):
                theta = [item for arc in [arc1, arc2, arc3] for item in arc]
                if set(theta) not in found and len(set(arc1) | set(arc2) | set(arc3)) == len(arc1) + len(arc2) + len(arc3):
                    g = Graph(self.generate_code_from_edges(theta))
                    result = g.print(output_type=output_type)
                    found.append(set(theta))
                    del g
                    yield result
        return

    def find_thetas_coords(self, output_type=OutputType.PDcode):
        vertices = list(self.spatial_graph.keys())
        found = []
        for v1, v2 in combinations(vertices, 2):
            for arc1, arc2, arc3 in combinations([path for path in self.find_path(v1, v2, self.spatial_graph)], 3):
                arc1 = [v1] + arc1
                arc2 = [v1] + arc2
                arc3 = [v1] + arc3
                theta = [arc1, arc2, arc3]
                if set(arc1 + arc2 + arc3) not in found and len(set(arc1[1:-1]) | set(arc2[1:-1]) |
                                            set(arc3[1:-1])) == len(arc1[1:-1]) + len(arc2[1:-1]) + len(arc3[1:-1]):
                    g = Graph(self.generate_coords_from_atom_list(theta))
                    result = g.print(output_type=output_type)
                    found.append(set(arc1 + arc2 + arc3))
                    del g
                    yield result

    def find_handcuffs(self, output_type=OutputType.PDcode):
        return

    def find_connected_components(self):
        # 0.1 case
        if len(self.crossings) == 0 and len(self.vertices) == 0:
            return [set()]
        connected = []
        # connected are 0-2 and 1-3
        for c in self.crossings:
            connected.append((c[0], c[2]))
            connected.append((c[1], c[-1]))
        # vertex connects edges
        for v in self.vertices:
            connected.append(tuple(v))
        return self.find_connections(connected)

    def find_connections(self, array):
        out = []
        while len(array) > 0:
            first, rest = array[0], array[1:]
            first = set(first)
            lf = -1
            while len(first) > lf:
                lf = len(first)
                rest2 = []
                for r in rest:
                    if len(first.intersection(set(r))) > 0:
                        first |= set(r)
                    else:
                        rest2.append(r)
                rest = rest2
            out.append(first)
            array = rest
        return out

    def find_disjoined_components(self):
        components = self.find_connected_components()
        for cross in self.crossings:
            k = 0
            while k < len(components):
                l = k + 1
                while l < len(components):
                    if cross[0] in components[k] and cross[1] in components[1]:
                        components[k] |= components[l]
                        components.pop(l)
                    l += 1
                k += 1
        subgraphs = ['' if len(element) != 0 else 'V' for element in components]
        for k in range(len(components)):
            for vertex in self.vertices:
                if len(vertex) > 0 and all(v in components[k] for v in vertex):
                    subgraphs[k] += 'V' + str([int(_) for _ in vertex]).replace(' ', '') + ';'
            for cross in self.crossings:
                if all(c in components[k] for c in cross):
                    subgraphs[k] += 'X' + str([int(_) for _ in cross]).replace(' ', '') + ';'
        subgraphs = [x[:-1] for x in subgraphs]
        return subgraphs

    def find_crossing_sign(self, n):
        signs = [0, 0]
        for path in self.orientation:
            if self.crossings[n][1] in path:
                signs[1] = path.index(self.crossings[n][1]) - path.index(self.crossings[n][3])
            if self.crossings[n][0] in path:
                signs[0] = path.index(self.crossings[n][2]) - path.index(self.crossings[n][0])
        for k in range(2):
            if signs[k] < -1:
                signs[k] = 1
            elif signs[k] > 1:
                signs[k] = -1
        return signs[0] * signs[1]

    def find_reidemeister_1(self, num_cross=-1):
        # num_cross is the number of crossings to be returned
        crossings = []
        for k in range(len(self.crossings)):
            c = self.crossings[k]
            for i in range(4):
                if c[i - 1] == c[i]:  # crossing to be reduced:
                    crossings.append([k, i])
                    break
            if len(crossings) == num_cross:
                return crossings
        return crossings

    def find_reidemeister_1v(self, num_cross=-1):
        # num_cross is the number of crossings to be returned
        crossings = []
        for l in range(len(self.crossings)):
            c = self.crossings[l]
            for k in range(len(self.vertices)):
                v = self.vertices[k]
                if len(v) == 2:
                    for i in range(4):
                        if [c[i], c[i - 1]] == v or [c[i - 1], c[i]] == v:
                            crossings.append([l, i, k])
                            break
            if len(crossings) == num_cross:
                return crossings
        return crossings

    def find_reidemeister_2(self, num_cross=-1):
        # num_cross is the number of crossings to be returned
        crossings = []
        for k in range(len(self.crossings)):
            c1 = self.crossings[k]
            for j in range(k):
                c2 = self.crossings[j]
                for i in range(4):
                    if c1[i] == c2[i] and c1[i - 1] == c2[i - 3]:
                        crossings.append([k, j, c1[i], c1[i - 1]])
                        break
                    elif c1[i] == c2[i] and c1[i - 3] == c2[i - 1]:
                        crossings.append([k, j, c1[i], c1[i - 3]])
                        break
                if len(crossings) == num_cross:
                    return crossings
        return crossings

    def find_reidemeister_2v(self, num_cross=-1):
        # num_cross is the number of crossings to be returned
        crossings = []
        for l in range(len(self.vertices)):
            v = self.vertices[l]
            if len(v) == 2:
                for k in range(len(self.crossings)):
                    c1 = self.crossings[k]
                    for j in range(k):
                        c2 = self.crossings[j]
                        for i in range(4):
                            if c1[i] == c2[i] and ([c1[i - 1], c2[i - 3]] == v or [c2[i - 3], c1[i - 1]] == v):
                                crossings.append([k, j, c1[i], l])
                                break
                            elif c1[i - 1] == c2[i - 3] and ([c1[i], c2[i]] == v or [c2[i], c1[i]] == v):
                                crossings.append([k, j, c1[i - 1], l])
                                break
                            elif c1[i] == c2[i] and ([c1[i - 3], c2[i - 1]] == v or [c2[i - 1], c1[i - 3]] == v):
                                crossings.append([k, j, c1[i], l])
                                break
                            elif c1[i - 3] == c2[i - 1] and ([c1[i], c2[i]] == v or [c2[i], c1[i]] == v):
                                crossings.append([k, j, c1[i - 3], l])
                                break
                        if len(crossings) == num_cross:
                            return crossings
        return crossings

    def find_reidemeister_3(self, num_cross=-1):
        # num_cross is the number of crossings to be returned
        crossings = []
        for i in range(len(self.crossings)):
            for j in range(i):
                for k in range(j):
                    c1, c2, c3 = self.crossings[i], self.crossings[j], self.crossings[k]
                    for m in range(4):
                        # checking if the crosings form a triangle
                        if c1[m] in c3 and c1[m - 1] in c2 and c3[(c3.index(c1[m]) - 3) % 4] in c2:
                            c3, c2 = c2, c3
                        if c1[m] in c2 and c1[m - 1] in c3 and c2[(c2.index(c1[m]) - 3) % 4] in c3:
                            # the edges have to be consecutive counterclockwise
                            if c3.index(c1[m - 1]) - c3.index(c2[(c2.index(c1[m]) - 3) % 4]) not in (1, -3):
                                continue
                            comm12 = c1[m]
                            comm13 = c1[m - 1]
                            comm23 = c2[(c2.index(c1[m]) - 3) % 4]
                            if (1, 1) not in [(c1.index(comm12) % 2, c2.index(comm12) % 2),
                                              (c1.index(comm13) % 2, c3.index(comm13) % 2),
                                              (c2.index(comm23) % 2, c3.index(comm23) % 2)]:
                                continue
                            crossings.append(
                                [self.crossings.index(c1), self.crossings.index(c2), self.crossings.index(c3), comm12,
                                 comm13, comm23])
                            break
                    if len(crossings) == num_cross:
                        return crossings
        return crossings

    def find_reidemeister_4(self, num_cross=-1):
        # num_cross is the number of crossings to be returned
        crossings = []
        for i in range(len(self.crossings)):
            for j in range(i):
                for k in range(len(self.vertices)):
                    c1, c2, v = self.crossings[i], self.crossings[j], self.vertices[k]
                    if len(v) != 3:
                        continue
                    for l in range(3):
                        if v[l] in c2 and v[l - 1] in c1:
                            c1, c2 = c2, c1
                        if v[l] in c1 and v[l - 1] in c2:
                            i1 = (c1.index(v[l]) - 3) % 4
                            i2 = (c2.index(v[l - 1]) - 1) % 4
                            if c1[i1] == c2[i2] and (i1 % 2) == (i2 % 2):
                                comm12 = c1[i1]
                                comm1v = v[l]
                                comm2v = v[l - 1]
                                crossings.append(
                                    [k, self.crossings.index(c1), self.crossings.index(c2), comm12, comm1v, comm2v])
                                break
                    if len(crossings) == num_cross:
                        return crossings
        return crossings

    def find_reidemeister_5(self, num_cross=-1):
        # num_cross is the number of crossings to be returned
        crossings = []
        for k in range(len(self.crossings)):
            c = self.crossings[k]
            for j in range(len(self.vertices)):
                v = self.vertices[j]
                if len(v) != 3:
                    continue
                for i in range(4):
                    if c[i] in v and c[i - 1] in v and abs(v.index(c[i]) - v.index(c[i - 1])) in [1, len(v) - 1]:
                        if i % 2 == 0:
                            crossings.append([j, k, i, i - 1])
                        else:
                            crossings.append([j, k, i - 1, i])
                        break
                if len(crossings) == num_cross:
                    return crossings
        return crossings

    ''' Graph manipulation '''

    def cut_chain(self, beg=-1, end=-1):
        if beg < 0:
            beg = min(list(self.coordinates.keys()))
        if end < 0:
            end = max(list(self.coordinates.keys()))
        coordinates = [[key] + self.coordinates[key] for key in range(beg, end + 1)]
        return coordinates

    def close(self, method=Closure.TWO_POINTS, direction=0, debug=False):
        if self.closed:
            return
        if not self.coordinates:
            raise NotImplementedError('No coordinates - nothing to close (yet).')
        if not self.coordinates_c:
            self.generate_coordinates_c()
        if len(self.coordinates_c) > 1:
            raise NotImplementedError('Only one-arc structures can be closed right now.')

        if debug:
            print("Closure method: " + str(method))
        self.coordinates_c[0] = chain_close(self.coordinates_c[0], method, direction)
        self.closed = True
        self.generate_coords_from_c()
        if debug:
            print(self.coordinates)
        return

    def reidemeister_1(self, arg_list, debug=False):
        ci, i = arg_list
        # ci is the index of the crossing to be reduced
        # i is the index of the edge in the crossing to be reduced
        # so self.crossings[ci][i] == self.crossings[ci][i-1]
        trans = {self.crossings[ci][i - 2]: self.crossings[ci][i - 3]}
        if i % 2 == 1:
            n = 1
        else:
            n = -1
        if debug:
            print("Reidemeister 1:\tRemoving crossing " + str(self.crossings[ci]) +
                  ". Updating: " + str(trans) + ". Sign " + str(n) + ".")
        self.crossings.pop(ci)
        self.update(trans)
        if debug:
            print("\tResult: " + self.pdcode)
        return n

    def reidemeister_1v(self, arg_list, debug=False):
        ci, i, vi = arg_list
        # ci is the index of the crossing to be reduced
        # i is the index of the edge in the crossing to be reduced
        # vi is the index of the vertex to be removed
        # so self.crossings[ci][i] == self.crossings[ci][i-1]
        if i % 2 == 1:
            n = 1
        else:
            n = -1
        v0 = self.vertices[vi]
        v = [self.crossings[ci][i - 2], self.crossings[ci][i - 3]]
        if debug:
            print("Reidemeister 1:\tRemoving crossing " + str(self.crossings[ci]) + ". Swapping vertices: " + str(
                v0) + " -> " + str(v) + ". Sign " + str(n) + ".")
        self.crossings.pop(ci)
        self.vertices.pop(vi)
        self.vertices.append(v)
        self.update()
        if debug:
            print("\tResult: " + self.pdcode)
        return n

    def reidemeister_2(self, arg_list, debug=False):
        c1, c2, comm1, comm2 = arg_list
        # c1 and c2 are the indices of the crossings to be reduced
        # comm1 and comm2 are the common edges in the crossings
        cross1 = self.crossings[c1]
        cross2 = self.crossings[c2]
        if cross1[cross1.index(comm1) - 2] == cross1[cross1.index(comm2) - 2]:
            cross2, cross1 = cross1, cross2
        v1 = [cross1[cross1.index(comm1) - 2], cross2[cross2.index(comm1) - 2]]
        v2 = [cross1[cross1.index(comm2) - 2], cross2[cross2.index(comm2) - 2]]

        if debug:
            print("Reidemeister 2:\tRemoving crossings " + str(self.crossings[c1]) + ", " +
                str(self.crossings[c2]) + ". Adding vertices: V" + str(
                    v1) + " and V" + str(v2) + ".")
        for cross in list(reversed(sorted([c1, c2]))):
            self.crossings.pop(cross)
        self.vertices.append(v1)
        self.vertices.append(v2)
        self.update()
        self.remove_double_verts()
        if debug:
            print("\tResult: " + self.pdcode)
        return

    def reidemeister_2v(self, arg_list, debug=False):
        c1, c2, comm, vi = arg_list
        # c1 and c2 are the indices of the crossings to be reduced
        # comm1 and comm2 are the common edges in the crossings
        # vi is the index of vertex to be removed
        cross1 = self.crossings[c1]
        cross2 = self.crossings[c2]
        v = self.vertices[vi]
        if cross1[cross1.index(comm) - 2] == cross1[cross1.index(comm) - 2]:
            cross2, cross1 = cross1, cross2
        if v[1] in cross1:
            v = [v[1], v[0]]
        v1 = [cross1[cross1.index(comm) - 2], cross2[cross2.index(comm) - 2]]
        v2 = [cross1[cross1.index(v[0]) - 2], cross2[cross2.index(v[1]) - 2]]

        if debug:
            print("Reidemeister 2v:\tRemoving crossings " + str(self.crossings[c1]) + ", " + str(self.crossings[c2]) +
                  ", and vertex " + str(self.vertices[vi]) + ". Adding vertices: V" + str(v1) + " and V" +
                  str(v2) + ".")
        # Updating: " + str(trans) + "." + str(v1) + ' ' + str(v2))
        for cross in list(reversed(sorted([c1, c2]))):
            self.crossings.pop(cross)
        self.vertices.pop(vi)
        self.vertices.append(v1)
        self.vertices.append(v2)
        self.update()
        self.remove_double_verts()
        # self.update(trans)
        if debug:
            print("\tResult: " + self.pdcode)
        return

    def reidemeister_3(self, arg_list, debug=False):
        c1, c2, c3, comm12, comm13, comm23 = arg_list
        # c1, c2, c3 are the indices of the crossings to be reduced
        # comm12, comm13, and comm23 are the common edges between the crossings
        cross1 = self.crossings[c1]
        cross2 = self.crossings[c2]
        cross3 = self.crossings[c3]

        # new crossings
        cn1 = [c for c in cross1]
        cn1[cross1.index(comm12) - 2] = cross2[cross2.index(comm12) - 2]
        cn1[cross1.index(comm13) - 2] = cross3[cross3.index(comm13) - 2]
        cn2 = [c for c in cross2]
        cn2[cross2.index(comm12) - 2] = cross1[cross1.index(comm12) - 2]
        cn2[cross2.index(comm23) - 2] = cross3[cross3.index(comm23) - 2]
        cn3 = [c for c in cross3]
        cn3[cross3.index(comm13) - 2] = cross1[cross1.index(comm13) - 2]
        cn3[cross3.index(comm23) - 2] = cross2[cross2.index(comm23) - 2]

        if debug:
            print("Reidemeister 3:\tRemoving crossing " + str(self.crossings[c1]) + ", " + str(self.crossings[c2]) +
                  ", " + str(self.crossings[c3]) + ". Adding: " + str(cn1) + ", " + str(cn2) + ", " + str(cn3) + ".")

        # updating the list of crossings
        for i in list(reversed(sorted([c3, c2, c1]))):
            self.crossings.pop(i)
        for c in [cn1, cn2, cn3]:
            self.crossings.append(c)
        self.update_pdcode()
        if debug:
            print("\tResult: " + self.pdcode)
        return

    def reidemeister_4(self, arg_list, debug=False):
        vi, c1, c2, comm12, comm1v, comm2v = arg_list
        # vi, c1, and c2 are the indices of the vertex and edges to be reduced
        # comm12, comm1v, and comm2v are the edges common between the crossings and crossings and vertex

        cross1 = self.crossings[c1]
        cross2 = self.crossings[c2]
        v = self.vertices[vi]
        miss = list(set(v) - {comm1v, comm2v})[0]  # TODO generalize for large number of crossings

        if (cross1.index(comm12) % 2) == 1:  # crosing over
            c = [miss, cross2[cross2.index(comm12) - 2], comm12, cross1[cross1.index(comm12) - 2]]
        else:  # crossing under
            c = [cross2[cross2.index(comm12) - 2], comm12, cross1[cross1.index(comm12) - 2], miss]
        vn = [comm12, cross2[cross2.index(comm2v) - 2], cross1[cross1.index(comm1v) - 2]]

        # updating data
        if debug:
            print("Reidemeister 4:\tRemoving crossing " + str(self.crossings[c1]) + ", " + str(self.crossings[c2]) +
                  " and vertex " + str(self.vertices[vi]) + ". Adding crossing: " + str(c) + " and vertex " +
                  str(vn) + ".")

        for cross in list(reversed(sorted([c1, c2]))):
            self.crossings.pop(cross)
        self.vertices.pop(vi)
        self.crossings.append(c)
        self.vertices.append(vn)
        self.update_pdcode()
        if debug:
            print("\tResult: " + self.pdcode)
        return

    def reidemeister_5(self, arg_list, debug=False):
        vi, ci, i, j = arg_list
        # vi and ci are indices of the vertex and the crossing to be reduced
        # i and j are the indices of the edges in the crossing adjacent to the vertex
        # i is the undercrossing, j is the uppercrossing

        vert = self.vertices[vi]
        cross = self.crossings[ci]

        # new vertex
        vn = [v for v in vert]
        vn[vn.index(cross[i])] = cross[j - 2]
        vn[vn.index(cross[j])] = cross[i - 2]
        if i < j:
            n = 1
        else:
            n = -1

        if debug:
            print("Reidemeister 5:\tRemoving crossing " + str(self.crossings[ci]) + ". Updating vertex " +
                  str(self.vertices[vi]) + "->" + str(vn) + ". Sign " + str(n) + ".")

        self.crossings.pop(ci)
        self.vertices.pop(vi)
        self.vertices.append(vn)
        self.update_pdcode()
        if debug:
            print("\tResult: " + self.pdcode)
        return n

    def invert_crossing(self, crossing):
        g = deepcopy(self)
        g.crossings.append(g.crossings[crossing][1:] + [g.crossings[crossing][0]])
        g.crossings.pop(crossing)
        g.update_pdcode()
        code = g.pdcode
        # del(g)
        return code

    def smooth_crossing(self, crossing, smoothing):
        # Smoothings denote the connection of edges. The edges are joined by two-valent vertices.
        # The unnecessary vertices are subsequently reduced.
        g = deepcopy(self)

        if smoothing == 0:
            g.vertices.append(g.crossings[crossing])
        if smoothing == 1:
            g.vertices.append(g.crossings[crossing][:2])
            g.vertices.append(g.crossings[crossing][2:4])
        if smoothing == -1:
            g.vertices.append([g.crossings[crossing][0], g.crossings[crossing][3]])
            g.vertices.append(g.crossings[crossing][1:3])

        # cleaning
        g.crossings.pop(crossing)
        g.remove_double_verts()

        code = g.pdcode
        # del(g)

        # TODO handle missing loops
        return code

    def contract_edge(self, edge, debug=False):
        g = deepcopy(self)
        nvert = []
        to_remove = []
        e = str(edge)
        for k in range(len(g.vertices)):  # to keep the orientation
            # TODO check the list additions
            if e in g.vertices[k]:
                to_remove.append(k)
                if nvert:
                    nvert += g.vertices[k][g.vertices[k].index(e) + 1:] + g.vertices[k][:g.vertices[k].index(e)]
                    break
                else:
                    nvert = g.vertices[k][g.vertices[k].index(e) + 1:] + g.vertices[k][:g.vertices[k].index(e)]
        for k in list(reversed(to_remove)):
            g.vertices.pop(k)
        g.vertices.append(nvert)
        g.update_pdcode()
        code = g.pdcode
        del(g)
        return code

    def contract_edge_vertex(self, v, c, i):
        g = deepcopy(self)
        vert = g.vertices[v]
        cross = g.crossings[c]
        vert[vert.index(cross[i])] = cross[i - 3]
        vert[vert.index(cross[i - 1])] = cross[i - 2]
        g.vertices[v] = vert
        g.crossings.pop(c)
        code = g.pdcode
        del(g)
        return code

    def remove_edge(self, edge, debug=False):
        g = deepcopy(self)
        for v in g.vertices:
            if edge in v:
                v.pop(v.index(edge))
        g.edges.discard(edge)
        g.remove_double_verts()
        g.update_pdcode()
        code = g.pdcode
        del(g)
        return code

    def remove_loop(self, v, k):
        g = deepcopy(self)
        g.vertices[v].pop(k)
        g.vertices[v].pop(k - 1)
        g.remove_double_verts()
        code = g.pdcode
        del g
        return code

    def remove_edge_vertex(self, v, c, i):
        g = deepcopy(self)
        cross = g.crossings[c]
        to_remove = list(reversed(sorted([g.vertices[v].index(cross[i]), g.vertices[v].index(cross[i - 1])])))
        for k in to_remove:
            g.vertices[v].pop(k)
        trans = {cross[i - 2]: cross[i - 3]}
        g.crossings.pop(c)
        g.update(trans)
        code = g.pdcode
        del(g)
        return code

    def remove_double_verts(self):
        split_double_vertices = []
        trans = {}
        for component in self.find_connected_components():
            verts = []
            other_verts = False  # if there exists any vertex with valency > 2
            for k in range(len(self.vertices) - 1, -1, -1):
                vert = self.vertices[k]
                if any(v in component for v in vert):
                    if len(vert) > 2:
                        other_verts = True
                        continue
                    verts.append(k)
            if not other_verts:
                verts = verts[:-1]
            split_double_vertices.append(verts)

        # bulding translating dictionary
        for vert_list in split_double_vertices:
            for k in vert_list:
                vert = sorted(self.vertices[k])
                if vert[1] in trans.keys():
                    trans[vert[0]] = trans[vert[1]]
                elif vert[1] in [trans[key] for key in list(trans)]:
                    for key in list(trans):
                        if trans[key] == vert[1]:
                            trans[key] = vert[0]
                            break
                elif vert[0] in trans.keys():
                    for key in list(trans):
                        if key == vert[0]:
                            trans[vert[1]] = trans[key]
                else:
                    trans[vert[1]] = vert[0]

        # removing unnecessary vertices
        for vert_list in list(reversed(sorted(split_double_vertices))):
            for vert in vert_list:
                self.vertices.pop(vert)

        # updating
        self.update(trans)
        return

    ### simplification ###
    def reduce(self, method=ReduceMethod.KMT, debug=False):
        if not self.coordinates:
            return
        for k in range(len(self.coordinates_c)):
            self.coordinates_c[k] = chain_reduce(self.coordinates_c[k], method)
        self.generate_coords_from_c()
        if debug:
            print('Reducing method: ' + str(method))
            print(self.coordinates)
        return

    def simplify(self, method=ReduceMethod.REIDEMEISTER, steps=1000, debug=False):
        # returns the power from Reidemeister moves 1 and 5
        # TODO implement moves 4.2, 4.3 and 4.4 from Yamada's paper!
        if method == ReduceMethod.EASY:
            return self.simplify_reidemeister_deterministic(debug)
        if method == ReduceMethod.REIDEMEISTER:
            return self.simplify_reidemeister(steps, debug)

    def simplify_reidemeister(self, steps=1000, debug=False):
        n = 0
        previous = [set([tuple(x) for x in self.vertices]), set([tuple(x) for x in self.crossings])]
        n += self.simplify_reidemeister_deterministic(debug)
        for step in range(steps):
            changed = False
            # do a R3 move if it reduces the number of crossings or a random R3 move, which will not restore some previous graph
            crossings = self.find_reidemeister_3()
            if not crossings:
                break
            done = False  # if the move was done
            for cross in crossings:
                g = deepcopy(self)
                g.reidemeister_3(cross, debug=False)
                g.simplify_reidemeister_deterministic(debug=False)
                if len(g.crossings) < len(self.crossings):
                    self.reidemeister_3(cross, debug)
                    previous.append([set([tuple(x) for x in self.vertices]), set([tuple(x) for x in self.crossings])])
                    n += self.simplify_reidemeister_deterministic(debug)
                    done = True
                    changed = True
                    break
            if not done:
                random.shuffle(crossings)
                for cross in crossings:
                    g = deepcopy(self)
                    g.reidemeister_3(cross, debug=False)
                    data = [set([tuple(x) for x in g.vertices]), set([tuple(x) for x in g.crossings])]
                    if data not in previous:
                        self.reidemeister_3(cross, debug=debug)
                        previous.append(
                            [set([tuple(x) for x in self.vertices]), set([tuple(x) for x in self.crossings])])
                        changed = True
                        break
                n += self.simplify_reidemeister_deterministic(debug)
            if not changed:
                break
        return n

    def simplify_reidemeister_deterministic(self, debug=False):
        n = 0
        k = len(self.crossings) + 1
        while len(self.crossings) < k:
            k = len(self.crossings)
            for arg_list in list(reversed(self.find_reidemeister_1())):
                n += 2 * self.reidemeister_1(arg_list, debug=debug)
            for arg_list in list(reversed(self.find_reidemeister_1v(num_cross=1))):
                n += 2 * self.reidemeister_1v(arg_list, debug=debug)
            for arg_list in self.find_reidemeister_2(num_cross=1):
                self.reidemeister_2(arg_list, debug=debug)
            for arg_list in self.find_reidemeister_2v(num_cross=1):
                self.reidemeister_2v(arg_list, debug=debug)
            for arg_list in self.find_reidemeister_4(num_cross=1):
                self.reidemeister_4(arg_list, debug=debug)
            for arg_list in list(reversed(self.find_reidemeister_1())):
                n += 2 * self.reidemeister_1(arg_list, debug=debug)
            for arg_list in list(reversed(self.find_reidemeister_1v(num_cross=1))):
                n += 2 * self.reidemeister_1v(arg_list, debug=debug)
            for arg_list in self.find_reidemeister_5(num_cross=1):
                n += self.reidemeister_5(arg_list, debug=debug)
        return n

    ''' Printing '''
    def print(self, output_type=OutputType.PDcode):
        result = DataParser.print_data(self.coordinates, self.arcs, self.pdcode, self.emcode, output_type)
        return result

    ''' Plotting '''

    def plot(self, palette=[]):
        plt.use('TkAgg')
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        for k in range(len(self.arcs)):
            arc = self.arcs[k]
            x = np.array([float(self.coordinates[_][0]) for _ in arc])
            y = np.array([float(self.coordinates[_][1]) for _ in arc])
            z = np.array([float(self.coordinates[_][2]) for _ in arc])
            if len(self.arcs) == 1:
                ax.scatter3D(x, y, z, c=np.array(range(len(arc))), cmap='hsv')
            else:
                ax.plot3D(x, y, z, plot_colors[k])
        plt.show()
        return

    def all_subclasses(cls):
        return set(cls.__subclasses__()).union(
            [s for c in cls.__subclasses__() for s in cls.all_subclasses(c)])


