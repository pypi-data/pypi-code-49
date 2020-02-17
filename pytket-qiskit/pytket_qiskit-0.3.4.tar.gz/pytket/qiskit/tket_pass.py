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

import qiskit
from qiskit.dagcircuit import DAGCircuit
from qiskit.providers import BaseBackend
from qiskit.transpiler.basepasses import TransformationPass, BasePass as qBasePass
from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.providers.aer.aerprovider import AerProvider
from qiskit.providers.ibmq.accountprovider import AccountProvider
from typing import Optional

from pytket.passes import BasePass, OptimisePhaseGadgets, SequencePass
from pytket.predicates import CompilationUnit
from .qiskit_convert import qiskit_to_tk, tk_to_qiskit, process_device
from pytket.backends.ibm import IBMQBackend, AerBackend, AerStateBackend, AerUnitaryBackend

class TketPass(TransformationPass):
    """The :math:`\\mathrm{t|ket}\\rangle` compiler to be plugged in to the Qiskit compilation sequence"""
    filecount = 0
    _aer_backend_map = {
        'QasmSimulator': AerBackend,
        'StatevectorSimulator': AerStateBackend,
        'UnitarySimulator': AerUnitaryBackend
    }
    def __init__(self, backend:BaseBackend, tket_pass:Optional[BasePass]=None) :
        """Wraps a pytket compiler pass as a :py:class:`qiskit.transpiler.TransformationPass`.
        A :py:class:`qiskit.dagcircuit.DAGCircuit` is converted to a pytket :py:class:`Circuit`.
        If specified, `tket_pass` will be run, otherwise a default pass is used. The circuit is
        then routed and rebased for the `backend`, and converted back.
        
        :param backend: The Qiskit backend to target
        :type backend: BaseBackend
        :param tket_pass: The pytket compiler pass to run. Defaults to None
        :type tket_pass: Optional[BasePass], optional
        """
        qBasePass.__init__(self)
        if not isinstance(backend, BaseBackend) :
            raise ValueError("Requires BaseBackend instance")

        if not tket_pass :
            tket_pass = OptimisePhaseGadgets()
        passlist = [tket_pass]
        if isinstance(backend._provider, AerProvider):
            tk_backend = self._aer_backend_map[type(backend).__name__]()
        elif isinstance(backend._provider, AccountProvider):
            tk_backend = IBMQBackend(backend.name())
        else:
            raise NotImplementedError("This backend provider is not supported.")

        passlist.append(tk_backend.default_compilation_pass)
        self._pass = SequencePass(passlist)

    def run(self, dag:DAGCircuit) -> DAGCircuit :
        """Run a preconfigured optimisation pass on the circuit and route for the given backend.

        :param dag: The circuit to optimise and route

        :return: The modified circuit
        """
        qc = dag_to_circuit(dag)
        circ = qiskit_to_tk(qc)
        cu = CompilationUnit(circ)
        self._pass.apply(cu)
        circ = cu.circuit
        qc = tk_to_qiskit(circ)
        newdag = circuit_to_dag(qc)
        newdag.name = dag.name
        return newdag
