from artap.problem import Problem
from artap.results import Results
from artap.algorithm_sweep import SweepAlgorithm
from artap.operators import LHSGeneration
from agrossuite import agros as a2d
import random

class CapacitorProblem(Problem):
        def set(self):
            self.parameters = [{'name': 'r1', 'bounds': [0.01, 0.03]},
                               {'name': 'r2', 'bounds': [0.035, 0.1]},
                               {'name': 'eps', 'bounds': [1.5, 4.5]}]
            self.costs = [{'name': 'C'}]

        def create_model(self, r1, r2, eps):
            # problem
            problem = a2d.problem(clear=True)
            problem.coordinate_type = "planar"
            problem.mesh_type = "triangle"

            # project parameters
            problem.parameters["r1"] = r1
            problem.parameters["r2"] = r2
            problem.parameters["eps"] = eps

            # fields
            # electrostatic
            electrostatic = problem.field("electrostatic")
            electrostatic.analysis_type = "steadystate"
            electrostatic.matrix_solver = "umfpack"
            electrostatic.number_of_refinements = 1
            electrostatic.polynomial_order = 2
            electrostatic.adaptivity_type = "disabled"
            electrostatic.solver = "linear"

            # boundaries
            electrostatic.add_boundary("GND", "electrostatic_potential", {"electrostatic_potential": 0})
            electrostatic.add_boundary("V", "electrostatic_potential", {"electrostatic_potential": 1})
            electrostatic.add_boundary("neumann", "electrostatic_surface_charge_density",
                                       {"electrostatic_surface_charge_density": 0})

            # materials
            electrostatic.add_material("dielectric",
                                       {"electrostatic_permittivity": "eps", "electrostatic_charge_density": 0})

            # geometry
            geometry = problem.geometry()
            geometry.add_edge("r1", 0, "r2", 0, boundaries={"electrostatic": "neumann"})
            geometry.add_edge("r2", 0, 0, "r2", angle=90, boundaries={"electrostatic": "GND"})
            geometry.add_edge(0, "r2", 0, "r1", boundaries={"electrostatic": "neumann"})
            geometry.add_edge("r1", 0, 0, "r1", angle=90, boundaries={"electrostatic": "V"})

            geometry.add_label("(r1 + r2) / 2.", "(r2 - r1) / 2", materials={"electrostatic": "dielectric"})

            # computation = problem.computation()
            # computation.solve()

            # solution = computation.solution("electrostatic")
            # result = solution.volume_integrals()["We"]

            # C = 4 * 2 * result * 1e12  # pF
            # print('Capacitance', C)

            return problem

        def capacitance(self, computation):
            solution = computation.solution("electrostatic")
            result = solution.volume_integrals()["We"]

            capacitance = 4.0 * 2.0 * result * 1e12  # pF
            return capacitance

        def evaluate(self, individual):
            x = individual.vector
            problem = self.create_model(r1=x[0], r2=x[1], eps=x[2])

            computation = problem.computation()
            computation.solve()

            capacitance = self.capacitance(computation)
            # print('Evaluated capacitance: {}'.format(capacitance))

            solution = computation.solution("electrostatic")
            solution = solution.solution()

            return [capacitance]


class Capacitor(CapacitorProblem):

    def space(self):
        problem = self.create_model(r1=0.02, r2=0.04, eps=2.5)
        # problem.save("/tmp/pokus.ags")

        computation = problem.computation()
        computation.solve()

        print('Capacitance (reference): {}'.format(self.capacitance(computation)))

        solution = computation.solution("electrostatic")
        solution.exportVTK("/tmp/sln_reference.vtk", -1, -1, variable="electrostatic_potential", variableComp="scalar")
        sln_reference = solution.solution()
        # print(sln_reference)
        # copy sln
        sln = sln_reference.copy()

        # modify sln
        for i in range(len(sln)):
            sln[i] = sln[i]*random.uniform(1.0, 1.2)
        solution.setSolution(sln)
        sln_new = solution.solution()
        solution.exportVTK("/tmp/sln_new.vtk", -1, -1, variable="electrostatic_potential", variableComp="scalar")
        print(sln_new[0])

        print('Capacitance (new): {}'.format(self.capacitance(computation)))


"""
problem = CapacitorProblem()
gen = LHSGeneration(problem)
gen.init(4)

algorithm = SweepAlgorithm(problem, generator=gen)
algorithm.options['max_processes'] = 1
algorithm.run()

individuals = problem.data_store.populations[-1].individuals
print(individuals)
"""


from itertools import product

from pymor.analyticalproblems.elliptic import StationaryProblem
from pymor.domaindescriptions.basic import RectDomain
from pymor.functions.basic import ConstantFunction, ExpressionFunction, LincombFunction
from pymor.parameters.functionals import ProjectionParameterFunctional
from pymor.parameters.spaces import CubicParameterSpace

from pymor.basic import *  # most common pyMOR functions and classes


def thermal_block_agros(num_blocks=(3, 3), parameter_range=(0.1, 1)):
    def parameter_functional_factory(ix, iy):
        return ProjectionParameterFunctional(component_name='diffusion',
                                             component_shape=(num_blocks[1], num_blocks[0]),
                                             coordinates=(num_blocks[1] - iy - 1, ix),
                                             name='diffusion_{}_{}'.format(ix, iy))

    def diffusion_function_factory(ix, iy):
        if ix + 1 < num_blocks[0]:
            X = '(x[..., 0] >= ix * dx) * (x[..., 0] < (ix + 1) * dx)'
        else:
            X = '(x[..., 0] >= ix * dx)'
        if iy + 1 < num_blocks[1]:
            Y = '(x[..., 1] >= iy * dy) * (x[..., 1] < (iy + 1) * dy)'
        else:
            Y = '(x[..., 1] >= iy * dy)'
        return ExpressionFunction('{} * {} * 1.'.format(X, Y),
                                  2, (), {}, {'ix': ix, 'iy': iy, 'dx': 1. / num_blocks[0], 'dy': 1. / num_blocks[1]},
                                  name='diffusion_{}_{}'.format(ix, iy))

    return StationaryProblem(

        domain=RectDomain(),

        rhs=ConstantFunction(dim_domain=2, value=1.),

        diffusion=LincombFunction([diffusion_function_factory(ix, iy)
                                   for ix, iy in product(range(num_blocks[0]), range(num_blocks[1]))],
                                  [parameter_functional_factory(ix, iy)
                                   for ix, iy in product(range(num_blocks[0]), range(num_blocks[1]))],
                                  name='diffusion'),

        parameter_space=CubicParameterSpace({'diffusion': (num_blocks[1], num_blocks[0])}, *parameter_range),

        name='ThermalBlock({})'.format(num_blocks)

    )

def thermal_block_fenics():

    # assemble system matrices - FEniCS code
    ########################################

    import dolfin as df

    mesh = df.UnitSquareMesh(GRID_INTERVALS, GRID_INTERVALS, 'crossed')
    V = df.FunctionSpace(mesh, 'Lagrange', FENICS_ORDER)
    u = df.TrialFunction(V)
    v = df.TestFunction(V)

    diffusion = df.Expression('(lower0 <= x[0]) * (open0 ? (x[0] < upper0) : (x[0] <= upper0)) *' +
                              '(lower1 <= x[1]) * (open1 ? (x[1] < upper1) : (x[1] <= upper1))',
                              lower0=0., upper0=0., open0=0,
                              lower1=0., upper1=0., open1=0,
                              element=df.FunctionSpace(mesh, 'DG', 0).ufl_element())

    def assemble_matrix(x, y, nx, ny):
        diffusion.user_parameters['lower0'] = x/nx
        diffusion.user_parameters['lower1'] = y/ny
        diffusion.user_parameters['upper0'] = (x + 1)/nx
        diffusion.user_parameters['upper1'] = (y + 1)/ny
        diffusion.user_parameters['open0'] = (x + 1 == nx)
        diffusion.user_parameters['open1'] = (y + 1 == ny)
        return df.assemble(df.inner(diffusion * df.nabla_grad(u), df.nabla_grad(v)) * df.dx)

    mats = [assemble_matrix(x, y, XBLOCKS, YBLOCKS)
            for x in range(XBLOCKS) for y in range(YBLOCKS)]
    mat0 = mats[0].copy()
    mat0.zero()
    h1_mat = df.assemble(df.inner(df.nabla_grad(u), df.nabla_grad(v)) * df.dx)

    f = df.Constant(1.) * v * df.dx
    F = df.assemble(f)

    bc = df.DirichletBC(V, 0., df.DomainBoundary())
    for m in mats:
        bc.zero(m)
    bc.apply(mat0)
    bc.apply(h1_mat)
    bc.apply(F)

    # wrap everything as a pyMOR discretization
    ###########################################

    # FEniCS wrappers
    from pymor.bindings.fenics import FenicsVectorSpace, FenicsMatrixOperator, FenicsVisualizer

    # define parameter functionals (same as in pymor.analyticalproblems.thermalblock)
    parameter_functionals = [ProjectionParameterFunctional(component_name='diffusion',
                                                           component_shape=(YBLOCKS, XBLOCKS),
                                                           coordinates=(YBLOCKS - y - 1, x))
                             for x in range(XBLOCKS) for y in range(YBLOCKS)]

    # wrap operators
    ops = [FenicsMatrixOperator(mat0, V, V)] + [FenicsMatrixOperator(m, V, V) for m in mats]
    op = LincombOperator(ops, [1.] + parameter_functionals)
    rhs = VectorOperator(FenicsVectorSpace(V).make_array([F]))
    h1_product = FenicsMatrixOperator(h1_mat, V, V, name='h1_0_semi')

    # build discretization
    visualizer = FenicsVisualizer(FenicsVectorSpace(V))
    parameter_space = CubicParameterSpace(op.parameter_type, 0.1, 1.)
    d = StationaryDiscretization(op, rhs, products={'h1_0_semi': h1_product},
                                 parameter_space=parameter_space,
                                 visualizer=visualizer)

    return d

def thermal_block_problem(num_blocks=(3, 3), parameter_range=(0.1, 1)):
    """Analytical description of a 2D 'thermal block' diffusion problem.

    The problem is to solve the elliptic equation ::

      - ∇ ⋅ [ d(x, μ) ∇ u(x, μ) ] = f(x, μ)

    on the domain [0,1]^2 with Dirichlet zero boundary values. The domain is
    partitioned into nx x ny blocks and the diffusion function d(x, μ) is
    constant on each such block (i,j) with value μ_ij. ::

           ----------------------------
           |        |        |        |
           |  μ_11  |  μ_12  |  μ_13  |
           |        |        |        |
           |---------------------------
           |        |        |        |
           |  μ_21  |  μ_22  |  μ_23  |
           |        |        |        |
           ----------------------------

    Parameters
    ----------
    num_blocks
        The tuple `(nx, ny)`
    parameter_range
        A tuple `(μ_min, μ_max)`. Each |Parameter| component μ_ij is allowed
        to lie in the interval [μ_min, μ_max].
    """

    def parameter_functional_factory(ix, iy):
        return ProjectionParameterFunctional(component_name='diffusion',
                                             component_shape=(num_blocks[1], num_blocks[0]),
                                             coordinates=(num_blocks[1] - iy - 1, ix),
                                             name='diffusion_{}_{}'.format(ix, iy))

    def diffusion_function_factory(ix, iy):
        if ix + 1 < num_blocks[0]:
            X = '(x[..., 0] >= ix * dx) * (x[..., 0] < (ix + 1) * dx)'
        else:
            X = '(x[..., 0] >= ix * dx)'
        if iy + 1 < num_blocks[1]:
            Y = '(x[..., 1] >= iy * dy) * (x[..., 1] < (iy + 1) * dy)'
        else:
            Y = '(x[..., 1] >= iy * dy)'
        return ExpressionFunction('{} * {} * 1.'.format(X, Y),
                                  2, (), {}, {'ix': ix, 'iy': iy, 'dx': 1. / num_blocks[0], 'dy': 1. / num_blocks[1]},
                                  name='diffusion_{}_{}'.format(ix, iy))

    problem = StationaryProblem(

        domain=RectDomain(),

        rhs=ConstantFunction(dim_domain=2, value=1.),

        diffusion=LincombFunction([diffusion_function_factory(ix, iy)
                                   for ix, iy in product(range(num_blocks[0]), range(num_blocks[1]))],
                                  [parameter_functional_factory(ix, iy)
                                   for ix, iy in product(range(num_blocks[0]), range(num_blocks[1]))],
                                  name='diffusion'),

        parameter_space=CubicParameterSpace({'diffusion': (num_blocks[1], num_blocks[0])}, *parameter_range),

        name='ThermalBlock({})'.format(num_blocks)
    )

    d, _ = discretize_stationary_cg(problem, diameter=1. / GRID_INTERVALS)
    return d

####################################################################################################
# Reduction algorithms                                                                             #
####################################################################################################


def reduce_naive(d, reductor, basis_size):

    training_set = d.parameter_space.sample_randomly(basis_size)

    for mu in training_set:
        u = d.solve(mu)
        reductor.extend_basis(u, 'trivial')

    rd = reductor.reduce()

    return rd


def reduce_greedy(d, reductor, snapshots, basis_size):

    training_set = d.parameter_space.sample_uniformly(snapshots)
    pool = new_parallel_pool()

    greedy_data = greedy(d, reductor, training_set,
                         extension_params={'method': 'gram_schmidt'},
                         max_extensions=basis_size,
                         pool=pool)

    return greedy_data['rd']


def reduce_adaptive_greedy(d, reductor, validation_mus, basis_size):

    pool = new_parallel_pool()

    greedy_data = adaptive_greedy(d, reductor, validation_mus=-validation_mus,
                                  extension_params={'method': 'gram_schmidt'},
                                  max_extensions=basis_size,
                                  pool=pool)

    return greedy_data['rd']


def reduce_pod(d, reductor, snapshots, basis_size):

    training_set = d.parameter_space.sample_uniformly(snapshots)

    snapshots = d.operator.source.empty()
    for mu in training_set:
        snapshots.append(d.solve(mu))

    basis, singular_values = pod(snapshots, modes=basis_size, product=reductor.product)
    reductor.extend_basis(basis, 'trivial')

    rd = reductor.reduce()

    return rd

# parameters for high-dimensional models
XBLOCKS = 2             # pyMOR/FEniCS
YBLOCKS = 2             # pyMOR/FEniCS
GRID_INTERVALS = 100    # pyMOR/FEniCS
FENICS_ORDER = 2
NGS_ORDER = 4
RBSIZE = 10
TEST = 5

# setup analytical problem
# discretize using continuous finite elements
# d  = thermal_block_problem(num_blocks=(XBLOCKS, YBLOCKS))
"""
d = thermal_block_fenics()
# select reduction algorithm with error estimator
coercivity_estimator = ExpressionParameterFunctional('min(diffusion)', d.parameter_type)
reductor = CoerciveRBReductor(d, product=d.h1_0_semi_product, coercivity_estimator=coercivity_estimator)

rd = reduce_naive(d, reductor, RBSIZE)

# evaluate the reduction error
results = reduction_error_analysis(rd, d=d, reductor=reductor, estimator=True,
                                   error_norms=[d.h1_0_semi_norm], condition=True,
                                   test_mus=TEST, random_seed=999, plot=True)

# show results
##############
print(results['summary'])
# import matplotlib.pyplot
# matplotlib.pyplot.show(results['figure'])

# visualize reduction error for worst-approximated mu
#####################################################
mumax = results['max_error_mus'][0, -1]
U = d.solve(mumax)
U_RB = reductor.reconstruct(rd.solve(mumax))
d.visualize((U, U_RB, U - U_RB), legend=('Detailed Solution', 'Reduced Solution', 'Error'), separate_colorbars=True, block=True)
"""

c = Capacitor()
c.space()