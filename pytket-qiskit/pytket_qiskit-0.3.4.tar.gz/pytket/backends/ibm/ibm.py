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

import itertools
import numpy as np
from typing import Dict, Iterable, List, Optional, Tuple
from qiskit import IBMQ
from qiskit.compiler import assemble
from qiskit.providers.aer.noise import NoiseModel
from qiskit.result import Result
from qiskit.tools.monitor import job_monitor

from pytket import Circuit, OpType, BasisOrder
from pytket.backends import Backend
from pytket.qiskit.qiskit_convert import tk_to_qiskit, process_device
from pytket.predicates import (
    Predicate, GateSetPredicate, NoClassicalControlPredicate,
    NoFastFeedforwardPredicate, DirectednessPredicate)
from pytket.passes import (
    BasePass, gen_directed_cx_routing_pass, SequencePass,
    SynthesiseIBM, RebaseIBM, gen_placement_pass)
from pytket.routing import NoiseAwarePlacement

_MACHINE_DEBUG = False

class IBMQBackend(Backend) :

    def __init__(self, backend_name : str, hub : Optional[str] = None, monitor : bool = True) :
        """A backend for running circuits on remote IBMQ devices.

        :param backend_name: Name of the IBMQ device, e.g. `ibmqx4`, `ibmq_16_melbourne`.
        :type backend_name: str
        :param hub: Name of the IBMQ hub to use for the provider. If None, just uses the first hub found. Defaults to None.
        :type hub: Optional[str], optional
        :param monitor: Use the IBM job monitor. Defaults to True.
        :type monitor: bool, optional
        :raises ValueError: If no IBMQ account is loaded and none exists on the disk.
        """
        super().__init__(shots=True, counts=True)
        if not IBMQ.active_account() :
            if IBMQ.stored_account() :
                IBMQ.load_account()
            else :
                raise ValueError("No IBMQ credentials found on disk")
        if hub :
            provider = IBMQ.get_provider(hub=hub)
        else :
            provider = IBMQ.providers()[0]
        self._backend = provider.get_backend(backend_name)
        self._config = self._backend.configuration()
        self._device = process_device(self._backend)
        self._monitor = monitor
        self._cache = {}

    @property
    def required_predicates(self) -> List[Predicate] :
        return [
            NoClassicalControlPredicate(),
            NoFastFeedforwardPredicate(),
            GateSetPredicate({OpType.CX, OpType.U1, OpType.U2, OpType.U3, OpType.noop, OpType.Measure}),
            DirectednessPredicate(self._device.architecture)
        ]

    @property
    def default_compilation_pass(self) -> BasePass :
        passlist = [
            RebaseIBM(),
            gen_placement_pass(NoiseAwarePlacement(self._device)),
            gen_directed_cx_routing_pass(self._device),
            SynthesiseIBM()
        ]
        return SequencePass(passlist)

    def process_circuits(self, circuits:Iterable[Circuit], n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True) :
        MAX_PER_JOB = 75
        for chunk in itertools.zip_longest(*([iter(circuits)]*MAX_PER_JOB)) :
            ch = list(filter(lambda x : x is not None, chunk))
            if valid_check :
                for c in ch :
                    if not self.valid_circuit(c) :
                        raise ValueError("Circuits do not satisfy all required predicates for this backend")
            qcs = list(map(tk_to_qiskit, ch))
            qobj = assemble(qcs, shots=n_shots, memory=self._config.memory)
            job = None if _MACHINE_DEBUG else self._backend.run(qobj)
            for i, c in enumerate(ch) :
                self._cache[c] = (job, i)

    def empty_cache(self) :
        self._cache = {}

    def get_shots(self, circuit:Circuit, n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> np.ndarray :
        if circuit not in self._cache :
            if not n_shots :
                raise ValueError("Circuit has not been processed; please specify a number of shots")
            self.process_circuits([circuit], n_shots, seed, valid_check)
        job, i = self._cache[circuit]
        if self._monitor and job :
            job_monitor(job)
        if remove_from_cache :
            del self._cache[circuit]
        if _MACHINE_DEBUG :
            return np.zeros((n_shots, circuit.n_qubits))
        else :
            table = _shots_from_result(i, job.result(), self._config.memory, basis)
            return table

    def get_counts(self, circuit:Circuit, n_shots:Optional[int], seed:Optional[int]=None, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> Dict[Tuple[int, ...], int] :
        if circuit not in self._cache :
            if not n_shots :
                raise ValueError("Circuit has not been processed; please specify a number of shots")
            self.process_circuits([circuit], n_shots, seed, valid_check)
        job, i = self._cache[circuit]
        if self._monitor and job :
            job_monitor(job)
        if remove_from_cache :
            del self._cache[circuit]
        if _MACHINE_DEBUG :
            return {(0,)*circuit.n_qubits : n_shots}
        else :
            counts = job.result().get_counts(i)
            counts = {tuple(_convert_bin_str(b, basis)) : c for b, c in counts.items()}
            return counts

def _shots_from_result(index:int, result:Result, memory:bool, basis:BasisOrder) -> np.ndarray :
    if memory:
        shot_list = result.get_memory(index)
    else:
        for string, count in result.get_counts(index).items():
            shot_list += [string]*count
    return np.asarray([_convert_bin_str(shot, basis) for shot in shot_list])

def _convert_bin_str(string, basis) :
    direction = (-1)**(basis == BasisOrder.ilo)
    return [int(b) for b in string.replace(' ', '')][::direction]
