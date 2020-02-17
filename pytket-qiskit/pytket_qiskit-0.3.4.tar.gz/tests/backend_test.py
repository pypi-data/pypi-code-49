# Copyright 2019 Cambridge Quantum Computing
#
# Licensed under a Non-Commercial Use Software Licence (the "Licence");
# you may not use this file except in compliance with the Licence.
# You may obtain a copy of the Licence in the LICENCE file accompanying
# these documents or at:
#
#     https://cqcl.github.io/pytket/build/html/licence.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Licence is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and
# limitations under the Licence, but note it is strictly for non-commercial use.
import os
import sys
import numpy as np
from pytket.circuit import Circuit, OpType, UnitID, BasisOrder
from pytket.predicates import CompilationUnit
from pytket.routing import Architecture,route
from pytket.transform import Transform
from pytket.backends.ibm import IBMQBackend, AerBackend, AerStateBackend, AerUnitaryBackend
from pytket.backends.ibm.ibm import process_device
from pytket.qiskit import qiskit_to_tk, tk_to_qiskit
from pytket.utils.expectations import _get_pauli_expectation_value, _get_operator_expectation_value

import qiskit
from qiskit import IBMQ
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit.providers.aer import noise
from qiskit.converters import circuit_to_dag, dag_to_circuit

import pytest
import math
import pickle

#TODO add tests for `get_operator_expectation_value`

def circuit_gen(measure=False):
    c = Circuit(2,2)
    c.H(0)
    c.CX(0,1)
    if measure :
        c.measure_all()
    return c

def get_test_circuit(measure):
    qr = QuantumRegister(5)
    cr = ClassicalRegister(5)
    qc = QuantumCircuit(qr, cr)
    # qc.h(qr[0])
    qc.x(qr[0])
    qc.x(qr[2])
    qc.cx(qr[1],qr[0])
    # qc.h(qr[1])
    qc.cx(qr[0],qr[3])
    qc.cz(qr[2],qr[0])
    qc.cx(qr[1],qr[3])
    # qc.rx(PI/2,qr[3])
    qc.z(qr[2])
    if measure:
        qc.measure(qr[0],cr[0])
        qc.measure(qr[1],cr[1])
        qc.measure(qr[2],cr[2])
        qc.measure(qr[3],cr[3])
    return qc

def test_statevector():
    c = circuit_gen()
    b = AerStateBackend()
    state = b.get_state(c)
    assert np.allclose(state, [math.sqrt(0.5), 0, 0, math.sqrt(0.5)], atol=1e-10)

def test_sim():
    c = circuit_gen(True)
    b = AerBackend()
    shots = b.get_shots(c,1024)
    print(shots)

def test_measures():
    n_qbs = 12
    c = Circuit(n_qbs, n_qbs)
    x_qbs = [2, 5, 7, 11]
    for i in x_qbs:
        c.X(i)
    c.measure_all()
    b = AerBackend()
    shots = b.get_shots(c,10)
    print(shots)
    all_ones = True
    all_zeros = True
    for i in x_qbs:
        all_ones = all_ones and np.all(shots[:,i])
    for i in range(n_qbs):
        if i not in x_qbs:
            all_zeros = all_zeros and (not np.any(shots[:,i]))
    assert all_ones
    assert all_zeros

def test_noise():
    with open(os.path.join(sys.path[0], 'ibmqx4_properties.pickle'), 'rb') as f:
        properties = pickle.load(f)

    noise_model = noise.device.basic_device_noise_model(properties)
    n_qbs = 5
    c = Circuit(n_qbs, n_qbs)
    x_qbs = [2, 0, 4]
    for i in x_qbs:
        c.X(i)
    c.measure_all()
    b = AerBackend(noise_model)
    n_shots = 50
    b.compile_circuit(c)
    shots = b.get_shots(c,n_shots,seed=4)
    zer_exp = []
    one_exp = []
    for i in range(n_qbs):
        expectation = np.sum(shots[:,i])/n_shots
        if i in x_qbs:
            one_exp.append(expectation)
        else:
            zer_exp.append(expectation)

    assert min(one_exp) > max(zer_exp)

    c2 = Circuit(4, 4).H(0).CX(0, 2).CX(3, 1).T(2).CX(0,1).CX(0,3).CX(2, 1).measure_all()

    b.compile_circuit(c2)
    shots = b.get_shots(c2, 10, seed=5)
    assert (shots.shape == (10, 4))

@pytest.mark.skip()
def test_process_device():
    if not IBMQ.active_account():
        IBMQ.load_account()

    provider = IBMQ.providers()[0]
    # back =  IBMQBackend('ibmq_ourense')
    back = provider.get_backend('ibmq_ourense')
    # i_ba = back._backend
    dev = process_device(back)

    assert(dev)

# @pytest.mark.skipif(IBMQ.stored_account()) is None, reason="Only valid if IBMQ API setup")
@pytest.mark.skip()
def test_device():
    from openfermion import QubitOperator
    c = circuit_gen(False)
    b = IBMQBackend('ibmq_essex')
    operator = QubitOperator('') + QubitOperator('Z0') + 0.5 * QubitOperator('X0')
    val = _get_operator_expectation_value(c, operator, b, 8000)
    print(val)
    c1 = circuit_gen(True)
    c2 = circuit_gen(True)
    b.compile_circuit(c1)
    b.compile_circuit(c2)

    b.process_circuits([c1, c2], 10)
    print(b.get_shots(c1, 10))
    print(b.get_shots(c2, 10))
    # print(list(b.get_counts_batch([cr,c], 100)))

def test_pauli_statevector():
    c = Circuit(2)
    c.Rz(0.5,0)
    Transform.OptimisePostRouting().apply(c)
    b = AerStateBackend()
    zi = [(0,'Z')]
    assert _get_pauli_expectation_value(c, zi, b) == 1
    c.X(0)
    assert _get_pauli_expectation_value(c, zi, b) == -1

def test_pauli_sim():
    c = Circuit(2,2)
    c.Rz(0.5,0)
    Transform.OptimisePostRouting().apply(c)
    b = AerBackend()
    zi = [(0,'Z')]
    energy = _get_pauli_expectation_value(c, zi, b, 8000)
    assert abs(energy-1) < 0.001
    c.X(0)
    energy = _get_pauli_expectation_value(c, zi, b, 8000)
    assert abs(energy+1) < 0.001

@pytest.mark.skip()
def test_default_pass():
    b = IBMQBackend('ibmq_ourense')
    comp_pass = b.default_compilation_pass
    qc = get_test_circuit(False)
    circ = qiskit_to_tk(qc)
    cu = CompilationUnit(circ)
    comp_pass.apply(cu)
    c = cu.circuit
    for pred in b.required_predicates :
        assert pred.verify(c)
    b.compile_circuit(circ)
    assert b.valid_circuit(circ)

def test_aer_default_pass():
    b = AerBackend()
    comp_pass = b.default_compilation_pass
    qc = get_test_circuit(False)
    circ = qiskit_to_tk(qc)
    cu = CompilationUnit(circ)
    comp_pass.apply(cu)
    c = cu.circuit
    for pred in b.required_predicates :
        assert pred.verify(c)
    b.compile_circuit(circ)
    assert b.valid_circuit(circ)


def test_routing_measurements():
    qc = get_test_circuit(True)
    circ = qiskit_to_tk(qc)
    sim = AerBackend()
    original_results = sim.get_shots(circ, 10, seed=4)
    coupling =  [[1, 0], [2, 0], [2, 1], [3, 2], [3, 4], [4, 2]]
    arc = Architecture(coupling)
    physical_c = route(circ, arc)
    Transform.DecomposeSWAPtoCX().apply(physical_c)
    Transform.DecomposeCXDirected(arc).apply(physical_c)
    Transform.OptimisePostRouting().apply(physical_c)
    assert((sim.get_shots(physical_c, 10) == original_results).all())

def test_routing_no_cx():
    circ = Circuit(2,2)
    circ.H(1)
    #c.CX(1, 2)
    circ.Rx(0.2, 0)
    circ.measure_all()
    coupling =  [[1, 0], [2, 0], [2, 1], [3, 2], [3, 4], [4, 2]]
    arc = Architecture(coupling)
    physical_c = route(circ, arc)

    assert(len(physical_c.get_commands()) == 4)



def test_counts() :
    qc = get_test_circuit(True)
    circ = qiskit_to_tk(qc)
    sim = AerBackend()
    counts = sim.get_counts(circ, 10, seed=4)
    assert counts == {(1, 0, 1, 1, 0) : 10}

def test_ilo():
    b = AerBackend()
    bs = AerStateBackend()
    bu = AerUnitaryBackend()
    c = Circuit(2)
    c.X(1)
    assert (bs.get_state(c) == np.asarray([0, 1, 0, 0])).all()
    assert (bs.get_state(c, basis=BasisOrder.dlo) == np.asarray([0, 0, 1, 0])).all()
    assert (bu.get_unitary(c) == np.asarray([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])).all()
    assert (bu.get_unitary(c, basis=BasisOrder.dlo) == np.asarray([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])).all()
    c.measure_all()
    assert (b.get_shots(c, 2) == np.asarray([[0,1],[0,1]])).all()
    assert (b.get_shots(c, 2, basis=BasisOrder.dlo) == np.asarray([[1,0],[1,0]])).all()
    assert b.get_counts(c, 2) == {(0,1) : 2}
    assert b.get_counts(c, 2, basis=BasisOrder.dlo) == {(1,0) : 2}


if __name__ =='__main__':
    # IBMQ.load_accounts()
    # device = IBMQ.get_backend('ibmqx4')
    # properties = device.properties()
    # coupling_map = device.configuration().coupling_map
    # with open(os.path.join(sys.path[0],'ibmqx4_properties.pickle'), 'wb') as f:
    #     pickle.dump(properties, f)
    # with open(os.path.join(sys.path[0],'ibmqx4_coupling.pickle'), 'wb') as f:
    #     pickle.dump(coupling_map, f)
    # test_routing_no_cx()
    # test_measures()
    # test_noise()
    test_device()
    # test_pauli_statevector()
    # test_pauli_sim()
    # test_process_device()
    # test_routed_ibmq_circuit()
    # test_routing_measurements()
    # test_statevector()
    # test_sim()
    # test_routing_measurements()
    # test_counts()
    # test_basic_routing()
    # test_basic_routing_with_line_map()
    # test_basic_routing_with_noise_map()
    # test_decompose_swap_to_cx()
    # test_commuting_sq_through_swap()
    # test_greedy_noise_route()
    # test_default_pass()
