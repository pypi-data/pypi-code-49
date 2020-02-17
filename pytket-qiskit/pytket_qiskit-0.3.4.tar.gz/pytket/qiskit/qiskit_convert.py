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


"""Methods to allow conversion between Qiskit and pytket circuit classes
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit import Instruction, Measure
from qiskit.extensions.standard import *
from qiskit.extensions.unitary import UnitaryGate
from qiskit.providers import BaseBackend

from pytket.circuit import Circuit, OpType, Unitary2qBox
from pytket.device import Device, GateError, GateErrorContainer
from pytket.routing import Architecture
from math import pi

_known_qiskit_gate = {
    IdGate  : OpType.noop,
    XGate   : OpType.X,
    YGate   : OpType.Y,
    ZGate   : OpType.Z,
    SGate   : OpType.S,
    SdgGate : OpType.Sdg,
    TGate   : OpType.T,
    TdgGate : OpType.Tdg,
    HGate   : OpType.H,
    RXGate  : OpType.Rx,
    RYGate  : OpType.Ry,
    RZGate  : OpType.Rz,
    U1Gate  : OpType.U1,
    U2Gate  : OpType.U2,
    U3Gate  : OpType.U3,
    CnotGate    : OpType.CX,
    CyGate  : OpType.CY,
    CzGate  : OpType.CZ,
    CHGate  : OpType.CH,
    SwapGate : OpType.SWAP,
    ToffoliGate : OpType.CCX,
    FredkinGate : OpType.CSWAP,
    CrzGate : OpType.CRz,
    Cu1Gate : OpType.CU1,
    Cu3Gate : OpType.CU3,
    Measure : OpType.Measure,
    UnitaryGate : OpType.Unitary2qBox,
    Barrier : OpType.Barrier
}

_known_qiskit_gate_rev = {v : k for k, v in _known_qiskit_gate.items()}

def qiskit_to_tk(qcirc: QuantumCircuit) -> Circuit :
    """Convert a :py:class:`qiskit.QuantumCircuit` to a :py:class:`Circuit`.

    :param qcirc: A circuit to be converted
    :type qcirc: QuantumCircuit
    :return: The converted circuit
    :rtype: Circuit
    """
    tkc = Circuit()
    qregmap = {}
    for reg in qcirc.qregs :
        tk_reg = tkc.add_q_register(reg.name, len(reg))
        qregmap.update({reg : tk_reg})
    cregmap = {}
    for reg in qcirc.cregs :
        tk_reg = tkc.add_c_register(reg.name, len(reg))
        cregmap.update({reg : tk_reg})
    for i, qargs, cargs in qcirc.data :
        if i.condition is not None:
            raise NotImplementedError("Cannot convert conditional gates from Qiskit to tket")
        optype = _known_qiskit_gate[type(i)]
        qubits = [qregmap[qbit.register][qbit.index] for qbit in qargs]
        bits = [cregmap[bit.register][bit.index] for bit in cargs]
        if optype == OpType.Measure :
            tkc.Measure(*qubits, *bits)
        elif optype == OpType.Unitary2qBox:
            u = i.to_matrix()
            ubox = Unitary2qBox(u)
            tkc.add_unitary2qbox(ubox, qubits[0].index[0], qubits[1].index[0])
        else:
            params = [p/pi for p in i.params]
            tkc.add_gate(optype, params, qubits, [])
    return tkc

def append_tk_command_to_qiskit(op, qubits, bits, controls, qcirc, qregmap, cregmap):
    qargs = [qregmap[q.reg_name][q.index[0]] for q in qubits]
    if controls:
        raise NotImplementedError("Cannot convert conditional gates from tket to Qiskit")
    optype = op.get_type()
    if optype == OpType.Measure :
        pbits = [cregmap[b.reg_name][b.index[0]] for b in bits]
        qcirc.measure(*qargs, *pbits)
    elif optype in [OpType.CircBox, OpType.ExpBox, OpType.PauliExpBox]:
        subcircuit = op.get_circuit()
        for subcommand in subcircuit:
            # recurse
            subqubits = [qubits[q.index[0]] for q in subcommand.qubits]
            subbits = [bits[b.index[0]] for b in subcommand.bits]
            subcontrols = [controls[c.index[0]] for c in subcommand.conditions]
            append_tk_command_to_qiskit(subcommand.op, subqubits, subbits, subcontrols, qcirc, qregmap, cregmap)
    elif optype == OpType.Unitary2qBox:
        u = op.get_matrix()
        g = UnitaryGate(u)
        qcirc.append(g, qargs=qargs)
    elif optype == OpType.Barrier:
        g = Barrier(len(qubits))
        qcirc.append(g, qargs=qargs)
    else:
        params = [p * pi for p in op.get_params()]
        try :
            gatetype = _known_qiskit_gate_rev[op.get_type()]
        except KeyError as error :
            raise NotImplementedError("Cannot convert tket Op to Qiskit gate: " + op.get_name()) from error
        g = gatetype(*params)
        qcirc.append(g, qargs=qargs)

def tk_to_qiskit(tkcirc: Circuit) -> QuantumCircuit :
    """Convert back

    :param tkcirc: A circuit to be converted
    :type tkcirc: Circuit
    :return: The converted circuit
    :rtype: QuantumCircuit
    """
    tkc = tkcirc
    qcirc = QuantumCircuit()
    qreg_sizes = {}
    for qb in tkc.qubits :
        if len(qb.index) != 1 :
            raise NotImplementedError("Qiskit registers must use a single index")
        if (qb.reg_name not in qreg_sizes) or (qb.index[0] >= qreg_sizes[qb.reg_name]) :
            qreg_sizes.update({qb.reg_name : qb.index[0] + 1})
    creg_sizes = {}
    for b in tkc.bits :
        if len(b.index) != 1 :
            raise NotImplementedError("Qiskit registers must use a single index")
        if (b.reg_name not in creg_sizes) or (b.index[0] >= creg_sizes[b.reg_name]) :
            creg_sizes.update({b.reg_name : b.index[0] + 1})
    qregmap = {}
    for reg_name, size in qreg_sizes.items() :
        qis_reg = QuantumRegister(size, reg_name)
        qregmap.update({reg_name : qis_reg})
        qcirc.add_register(qis_reg)
    cregmap = {}
    for reg_name, size in creg_sizes.items() :
        qis_reg = ClassicalRegister(size, reg_name)
        cregmap.update({reg_name : qis_reg})
        qcirc.add_register(qis_reg)
    for command in tkc:
        append_tk_command_to_qiskit(command.op, command.qubits, command.bits, command.conditions, qcirc, qregmap, cregmap)
    return qcirc


def process_device(backend : BaseBackend) -> Device :
    """Convert a :py:class:`qiskit.BaseBackend` to a :py:class:`Device`.

    :param backend: A backend to be converted
    :type backend: BaseBackend
    :return: A :py:class:''Device' containing device information
    :rtype: Device
    """
    properties = backend.properties()
    gate_str_2_optype = {
        'u1': OpType.U1,
        'u2': OpType.U2,
        'u3': OpType.U3,
        'cx': OpType.CX,
        'id': OpType.noop
    }

    def return_value_if_found(iterator, name):
        try:
            first_found = next(filter(lambda item: item.name == name, iterator))
        except StopIteration:
            return None
        if hasattr(first_found, 'value'):
            return first_found.value
        return None

    coupling_map = backend.configuration().coupling_map

    node_ers_dict = {}
    link_ers_dict = {tuple(pair): GateErrorContainer()
                     for pair in coupling_map}

    for index, qubit_info in enumerate(properties.qubits):
        error_cont = GateErrorContainer()
        error_cont.add_readout(
            return_value_if_found(qubit_info, 'readout_error'))
        error_cont.add_t1_time(return_value_if_found(qubit_info, 'T1'))
        error_cont.add_t2_time(return_value_if_found(qubit_info, 'T2'))
        error_cont.add_frequency(
            return_value_if_found(qubit_info, 'frequency'))
        node_ers_dict[index] = error_cont

    for gate in properties.gates:
        name = gate.gate
        if name in gate_str_2_optype:
            optype = gate_str_2_optype[name]
            qubits = gate.qubits
            gate_error = return_value_if_found(gate.parameters, 'gate_error')
            gate_error = gate_error if gate_error else 0.0
            gate_length = return_value_if_found(gate.parameters, 'gate_length')
            gate_length = gate_length if gate_length else 0.0
            # add gate fidelities to their relevant lists
            if len(qubits) == 1:
                node_ers_dict[qubits[0]].add_error(
                    (optype, GateError(gate_error, gate_length)))
            elif len(qubits) == 2:
                link_ers_dict[tuple(qubits)].add_error(
                    (optype, GateError(gate_error, gate_length)))
                opposite_link = tuple(qubits[::-1])
                if opposite_link not in coupling_map:
                    # to simulate a worse reverse direction square the fidelity
                    link_ers_dict[opposite_link] = GateErrorContainer()
                    link_ers_dict[opposite_link].add_error(
                        (optype, GateError(2*gate_error, gate_length)))

    arc = Architecture(coupling_map)
    # convert qubits to architecture Nodes
    node_ers_dict = {arc.map_vertex(
        q_index): ers for q_index, ers in node_ers_dict.items()}
    link_ers_dict = {(arc.map_vertex(q_indices[0]), arc.map_vertex(
        q_indices[1])): ers for q_indices, ers in link_ers_dict.items()}

    device = Device(node_ers_dict, link_ers_dict, arc)
    return device
