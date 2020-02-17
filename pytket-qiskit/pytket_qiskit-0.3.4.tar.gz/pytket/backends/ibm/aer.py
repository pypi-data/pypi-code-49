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

from typing import Dict, Iterable, List, Optional, Tuple
import numpy as np
from qiskit import Aer
from qiskit.compiler import assemble
from qiskit.providers import BaseBackend
from qiskit.providers.aer.noise import NoiseModel

from pytket import Architecture, Circuit, OpType, BasisOrder
from pytket.backends import Backend
from pytket.device import Device, GateError, GateErrorContainer
from pytket.qiskit import tk_to_qiskit
from pytket.predicates import (
    Predicate, GateSetPredicate, NoClassicalControlPredicate,
    NoFastFeedforwardPredicate, ConnectivityPredicate)
from pytket.passes import BasePass, gen_full_mapping_pass, SynthesiseIBM, SequencePass, RebaseIBM
from pytket.routing import NoiseAwarePlacement
from pytket.utils.results import reverse_permutation_matrix
from .ibm import _convert_bin_str, _shots_from_result

class AerBackend(Backend) :

    def __init__(self, noise_model:Optional[NoiseModel]=None) :
        """Backend for running simulations on the Qiskit Aer QASM simulator.

        :param noise_model: Noise model to apply during simulation. Defaults to None.
        :type noise_model: Optional[NoiseModel], optional
        """
        super().__init__(shots=True, counts=True)
        self._backend = Aer.get_backend('qasm_simulator')
        self._noise_model = noise_model
        if noise_model :
            self._device = _process_model(noise_model)
        self._cache = {}

    @property
    def required_predicates(self) -> List[Predicate] :
        pred_list = [
            NoClassicalControlPredicate(),
            NoFastFeedforwardPredicate(),
            GateSetPredicate(_aer_ops.union({OpType.Measure}))
        ]
        if self._noise_model and self._device :
            pred_list.append(ConnectivityPredicate(self._device))
        return pred_list

    @property
    def default_compilation_pass(self) -> BasePass :
        if self._noise_model and self._device :
            return SequencePass([
                RebaseIBM(),
                gen_full_mapping_pass(self._device, NoiseAwarePlacement(self._device)),
                SynthesiseIBM()
            ])
        else :
            return SynthesiseIBM()

    def process_circuits(self, circuits:Iterable[Circuit], n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True) :
        cs = list(circuits)
        if valid_check :
            for c in cs :
                for p in self.required_predicates :
                    if not p.verify(c) :
                        raise ValueError("Circuits do not satisfy all required predicates for this backend")
        qcs = list(map(tk_to_qiskit, cs))
        qobj = assemble(qcs, shots=n_shots, memory=True, seed_simulator=seed)
        job = self._backend.run(qobj, noise_model=self._noise_model)
        for i, c in enumerate(cs) :
            self._cache[c] = (job, i)

    def empty_cache(self) :
        self._cache = {}

    def get_shots(self, circuit:Circuit, n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> np.ndarray :
        if circuit not in self._cache :
            if not n_shots :
                raise ValueError("Circuit has not been processed; please specify a number of shots")
            self.process_circuits([circuit], n_shots, seed, valid_check)
        job, i = self._cache[circuit]
        if remove_from_cache :
            del self._cache[circuit]
        table = _shots_from_result(i, job.result(), True, basis)
        return table

    def get_counts(self, circuit:Circuit, n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> Dict[Tuple[int, ...], int] :
        if circuit not in self._cache :
            if not n_shots :
                raise ValueError("Circuit has not been processed; please specify a number of shots")
            self.process_circuits([circuit], n_shots, seed, valid_check)
        job, i = self._cache[circuit]
        counts = job.result().get_counts(i)
        if remove_from_cache :
            del self._cache[circuit]
        counts = {tuple(_convert_bin_str(b, basis)) : c for b, c in counts.items()}
        return counts

class AerStateBackend(Backend) :

    def __init__(self) :
        """Backend for running simulations on the Qiskit Aer Statevector simulator.
        """
        super().__init__(state=True)
        self._backend = Aer.get_backend('statevector_simulator')
        self._cache = {}

    @property
    def required_predicates(self) -> List[Predicate] :
        return _pure_aer_predicates

    @property
    def default_compilation_pass(self) -> BasePass :
        return SynthesiseIBM()

    def process_circuits(self, circuits:Iterable[Circuit], n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True) :
        cs = list(circuits)
        if valid_check :
            for c in cs :
                for p in self.required_predicates :
                    if not p.verify(c) :
                        raise ValueError("Circuits do not satisfy all required predicates for this backend")
        qcs = list(map(lambda c : tk_to_qiskit(c), cs))
        qobj = assemble(qcs)
        job = self._backend.run(qobj)
        for i, c in enumerate(cs) :
            self._cache[c] = (job, i)

    def empty_cache(self) :
        self._cache = {}

    def get_state(self, circuit:Circuit, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> np.ndarray :
        if circuit not in self._cache :
            self.process_circuits([circuit], valid_check=valid_check)
        job, i = self._cache[circuit]
        if remove_from_cache :
            del self._cache[circuit]
        state = np.asarray(job.result().get_statevector(i, decimals=16))
        if basis == BasisOrder.ilo :
            state = reverse_permutation_matrix(circuit.n_qubits).dot(state)
        return state

class AerUnitaryBackend(Backend) :

    def __init__(self) :
        """Backend for running simulations on the Qiskit Aer Unitary simulator.
        """
        super().__init__(unitary=True)
        self._backend = Aer.get_backend('unitary_simulator')
        self._cache = {}

    @property
    def required_predicates(self) -> List[Predicate] :
        return _pure_aer_predicates

    @property
    def default_compilation_pass(self) -> BasePass :
        return SynthesiseIBM()

    def process_circuits(self, circuits:Iterable[Circuit], n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True) :
        cs = list(circuits)
        if valid_check :
            for c in cs :
                for p in self.required_predicates :
                    if not p.verify(c) :
                        raise ValueError("Circuits do not satisfy all required predicates for this backend")
        qcs = list(map(lambda c : tk_to_qiskit(c), cs))
        qobj = assemble(qcs)
        job = self._backend.run(qobj)
        for i, c in enumerate(cs) :
            self._cache[c] = (job, i)

    def empty_cache(self) :
        self._cache = {}

    def get_unitary(self, circuit:Circuit, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> np.ndarray :
        if circuit not in self._cache :
            self.process_circuits([circuit], valid_check=valid_check)
        job, i = self._cache[circuit]
        if remove_from_cache :
            del self._cache[circuit]
        unitary = np.asarray(job.result().get_unitary(i, decimals=16))
        if basis == BasisOrder.ilo :
            rev = reverse_permutation_matrix(circuit.n_qubits)
            unitary = rev.dot(unitary.dot(rev))
        return unitary

_aer_ops = {
    OpType.U1,  OpType.U2,  OpType.U3,  OpType.CX,
    OpType.CZ,  OpType.CU1, OpType.noop,OpType.X,
    OpType.Y,   OpType.Z,   OpType.H,   OpType.S,
    OpType.Sdg, OpType.T,   OpType.Tdg, OpType.CCX,
    OpType.SWAP,OpType.Unitary1qBox,    OpType.Unitary2qBox
}

_pure_aer_predicates = [
    NoClassicalControlPredicate(),
    NoFastFeedforwardPredicate(),
    GateSetPredicate(_aer_ops)
]

def _process_model(noise_model:NoiseModel) -> Device:
    # obtain approximations for gate errors from noise model by using probability of "identity" error
    _gate_str_2_optype = {
        'u1': OpType.U1,
        'u2': OpType.U2,
        'u3': OpType.U3,
        'cx': OpType.CX,
        'id': OpType.noop
    }
    errors = [e for e in noise_model.to_dict()['errors'] if e['type'] == 'qerror']
    link_ers_dict = {}
    node_ers_dict = {}
    coupling_map = []
    for error in errors:
        name = error['operations']
        if len(name) > 1:
            raise RuntimeWarning("Error applies to multiple gates.")
        name = name[0]
        qubits = error['gate_qubits'][0]
        gate_fid = error['probabilities'][-1]
        if len(qubits) == 1:
            error_cont = GateErrorContainer()
            error_cont.add_error((_gate_str_2_optype[name], GateError(1 - gate_fid, 1)))
            node_ers_dict[qubits[0]] = error_cont
        elif len(qubits) == 2:
            error_cont = GateErrorContainer()
            error_cont.add_error((_gate_str_2_optype[name], GateError(1 - gate_fid, 1)))
            link_ers_dict[tuple(qubits)] = error_cont
            # to simulate a worse reverse direction square the fidelity
            rev_error_cont = GateErrorContainer()
            rev_error_cont.add_error((_gate_str_2_optype[name], GateError(1 - gate_fid**2, 1)))
            link_ers_dict[tuple(qubits[::-1])] = rev_error_cont
            coupling_map.append(qubits)

    if len(coupling_map) == 0:
        return None
    arc = Architecture(coupling_map)
    # convert qubits to architecture Nodes
    node_ers_dict = {arc.map_vertex(
        q_index): ers for q_index, ers in node_ers_dict.items()}
    link_ers_dict = {(arc.map_vertex(q_indices[0]), arc.map_vertex(
        q_indices[1])): ers for q_indices, ers in link_ers_dict.items()}
    return Device(node_ers_dict, link_ers_dict, arc)
