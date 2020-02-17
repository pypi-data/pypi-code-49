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
import pytest
import numpy as np
import qiskit
from qiskit import (QuantumCircuit, QuantumRegister, ClassicalRegister, execute,
    Aer, IBMQ, execute, transpile)
from qiskit.converters import dag_to_circuit, circuit_to_dag
from qiskit.transpiler import PassManager

from math import pi
from pytket import Circuit, CircBox, Unitary2qBox
from pytket.qiskit import tk_to_qiskit, qiskit_to_tk
from pytket.qiskit.tket_pass import TketPass
from sympy import Symbol
from pytket.passes import USquashIBM

def get_test_circuit(measure) :
    qr = QuantumRegister(4)
    cr = ClassicalRegister(4)
    qc = QuantumCircuit(qr, cr)
    qc.h(qr[0])
    qc.cx(qr[1],qr[0])
    qc.h(qr[0])
    qc.cx(qr[0],qr[3])
    qc.barrier(qr[3])
    qc.rx(pi/2,qr[3])
    qc.z(qr[2])
    if measure:
        qc.measure(qr[0],cr[0])
        qc.measure(qr[1],cr[1])
        qc.measure(qr[2],cr[2])
        qc.measure(qr[3],cr[3])
    return qc

def test_convert() :
    qc = get_test_circuit(False)
    backend = Aer.get_backend('statevector_simulator')
    job = execute([qc],backend)
    state0 = job.result().get_statevector(qc)
    tkc = qiskit_to_tk(qc)
    qc = tk_to_qiskit(tkc)
    job = execute([qc],backend)
    state1 = job.result().get_statevector(qc)
    assert(np.allclose(state0, state1, atol=1e-10))

def test_symbolic():
    pi2 = Symbol('pi2')
    pi3 = Symbol('pi3')

    tkc = Circuit(3, 3).Ry(pi2, 1).Rx(pi3, 1).CX(1, 0)
    USquashIBM().apply(tkc)

    tkc.symbol_substitution({pi2: pi/2, pi3: pi/3})

    backend = Aer.get_backend('statevector_simulator')
    qc = tk_to_qiskit(tkc)
    job = execute([qc],backend)
    state1 = job.result().get_statevector(qc)
    state0 = np.array([[ 0.6252345 +0.j        ,  0.        +0.j        ,
        0.        +0.j        , -0.78000172+0.02606021j,
        0.        +0.j        ,  0.        +0.j        ,
        0.        +0.j        ,  0.        +0.j        ]])
    assert(np.allclose(state0, state1, atol=1e-10))


def test_measures() :
    qc = get_test_circuit(True)
    backend = Aer.get_backend('qasm_simulator')
    job = execute([qc], backend, seed_simulator=7)
    counts0 = job.result().get_counts(qc)
    tkc = qiskit_to_tk(qc)
    qc = tk_to_qiskit(tkc)
    job = execute([qc], backend, seed_simulator=7)
    counts1 = job.result().get_counts(qc)
    for result, count in counts1.items() :
        result_str = result.replace(' ', '')
        if (counts0[result_str] != count) :
            assert(False)

def test_boxes():
    c = Circuit(2)
    c.S(0)
    c.H(1)
    c.CX(0,1)
    cbox = CircBox(c)
    d = Circuit(3)
    d.add_circbox(cbox, [0,1], [])
    d.add_circbox(cbox, [1,2], [])
    u = np.asarray([[0,0,1,0],[0,1,0,0],[0,0,0,1],[1,0,0,0]])
    ubox = Unitary2qBox(u)
    d.add_unitary2qbox(ubox, 0, 1)
    qsc = tk_to_qiskit(d)
    d1 = qiskit_to_tk(qsc)
    assert len(d1.get_commands()) == 2 * len(c.get_commands()) + 1

def test_Unitary2qBox():
    c = Circuit(2)
    u = np.asarray([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    ubox = Unitary2qBox(u)
    c.add_unitary2qbox(ubox, 0, 1)
    # Convert to qiskit
    qc = tk_to_qiskit(c)
    # Verify that unitary from simulator is correct
    back = Aer.get_backend('unitary_simulator')
    job = execute(qc, back).result()
    a = job.get_unitary(qc)
    assert np.allclose(a, u)

def test_tketpass():
    backends = [
        Aer.get_backend('statevector_simulator'),
        Aer.get_backend('qasm_simulator'),
        Aer.get_backend('unitary_simulator')
        ]
    if IBMQ.stored_account():
        if not IBMQ.active_account():
            IBMQ.load_account()
        provider = IBMQ.providers()[0]
        backends.append(provider.get_backend('ibmq_essex'))
    for back in backends :
        tkpass = TketPass(back)
        qc = get_test_circuit(True)
        pm = PassManager(passes=tkpass)
        output = transpile(qc, pass_manager=pm)

if __name__ == '__main__' :
    test_convert()
    test_measures()
    test_boxes()
    test_Unitary2qBox()
    test_tketpass()
    test_symbolic()