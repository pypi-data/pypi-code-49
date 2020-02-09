# -*- coding: utf-8 -*-
"""Namespace: zeek."""

import enum


@enum.unique
class layer3_proto(enum.IntFlag):
    """
    c.f. {html_path}
    """

    _ignore_ = 'layer3_proto _'
    layer3_proto = vars()

    layer3_proto['L3_IPV4'] = enum.auto()

    layer3_proto['L3_IPV6'] = enum.auto()

    layer3_proto['L3_ARP'] = enum.auto()

    layer3_proto['L3_UNKNOWN'] = enum.auto()


@enum.unique
class link_encap(enum.IntFlag):
    """
    c.f. {html_path}
    """

    _ignore_ = 'link_encap _'
    link_encap = vars()

    link_encap['LINK_ETHERNET'] = enum.auto()

    link_encap['LINK_UNKNOWN'] = enum.auto()


@enum.unique
class rpc_status(enum.IntFlag):
    """
    c.f. {html_path}
    """

    _ignore_ = 'rpc_status _'
    rpc_status = vars()

    rpc_status['RPC_SUCCESS'] = enum.auto()

    rpc_status['RPC_PROG_UNAVAIL'] = enum.auto()

    rpc_status['RPC_PROG_MISMATCH'] = enum.auto()

    rpc_status['RPC_PROC_UNAVAIL'] = enum.auto()

    rpc_status['RPC_GARBAGE_ARGS'] = enum.auto()

    rpc_status['RPC_SYSTEM_ERR'] = enum.auto()

    rpc_status['RPC_TIMEOUT'] = enum.auto()

    rpc_status['RPC_VERS_MISMATCH'] = enum.auto()

    rpc_status['RPC_AUTH_ERROR'] = enum.auto()

    rpc_status['RPC_UNKNOWN_ERROR'] = enum.auto()


@enum.unique
class IPAddrAnonymization(enum.IntFlag):
    """See also: anonymize_addr

    
    c.f. {html_path}
    """

    _ignore_ = 'IPAddrAnonymization _'
    IPAddrAnonymization = vars()

    IPAddrAnonymization['KEEP_ORIG_ADDR'] = enum.auto()

    IPAddrAnonymization['SEQUENTIALLY_NUMBERED'] = enum.auto()

    IPAddrAnonymization['RANDOM_MD5'] = enum.auto()

    IPAddrAnonymization['PREFIX_PRESERVING_A50'] = enum.auto()

    IPAddrAnonymization['PREFIX_PRESERVING_MD5'] = enum.auto()


@enum.unique
class IPAddrAnonymizationClass(enum.IntFlag):
    """See also: anonymize_addr

    
    c.f. {html_path}
    """

    _ignore_ = 'IPAddrAnonymizationClass _'
    IPAddrAnonymizationClass = vars()

    IPAddrAnonymizationClass['ORIG_ADDR'] = enum.auto()

    IPAddrAnonymizationClass['RESP_ADDR'] = enum.auto()

    IPAddrAnonymizationClass['OTHER_ADDR'] = enum.auto()


@enum.unique
class PcapFilterID(enum.IntFlag):
    """Enum type identifying dynamic BPF filters. These are used by
    Pcap::precompile_pcap_filter and Pcap::precompile_pcap_filter.

    
    c.f. {html_path}
    """

    _ignore_ = 'PcapFilterID _'
    PcapFilterID = vars()

    PcapFilterID['None'] = enum.auto()

    # (present if base/frameworks/packet-filter/main.zeek is loaded)
    PcapFilterID['PacketFilter::DefaultPcapFilter'] = enum.auto()

    # (present if base/frameworks/packet-filter/main.zeek is loaded)
    PcapFilterID['PacketFilter::FilterTester'] = enum.auto()


@enum.unique
class pkt_profile_modes(enum.IntFlag):
    """Output modes for packet profiling information.

    See also: pkt_profile_mode, pkt_profile_freq, pkt_profile_file

    
    c.f. {html_path}
    """

    _ignore_ = 'pkt_profile_modes _'
    pkt_profile_modes = vars()

    # No output.
    pkt_profile_modes['PKT_PROFILE_MODE_NONE'] = enum.auto()

    # Output every pkt_profile_freq seconds.
    pkt_profile_modes['PKT_PROFILE_MODE_SECS'] = enum.auto()

    # Output every pkt_profile_freq packets.
    pkt_profile_modes['PKT_PROFILE_MODE_PKTS'] = enum.auto()

    # Output every pkt_profile_freq bytes.
    pkt_profile_modes['PKT_PROFILE_MODE_BYTES'] = enum.auto()


@enum.unique
class transport_proto(enum.IntFlag):
    """A connection’s transport-layer protocol. Note that Zeek uses the term
    “connection” broadly, using flow semantics for ICMP and UDP.

    
    c.f. {html_path}
    """

    _ignore_ = 'transport_proto _'
    transport_proto = vars()

    # An unknown transport-layer protocol.
    transport_proto['unknown_transport'] = enum.auto()

    # TCP.
    transport_proto['tcp'] = enum.auto()

    # UDP.
    transport_proto['udp'] = enum.auto()

    # ICMP.
    transport_proto['icmp'] = enum.auto()


@enum.unique
class Direction(enum.IntFlag):
    """
    c.f. {html_path}
    """

    _ignore_ = 'Direction _'
    Direction = vars()

    # The connection originator is not within the locally-monitored
    # network, but the other endpoint is.
    Direction['INBOUND'] = enum.auto()

    # The connection originator is within the locally-monitored network,
    # but the other endpoint is not.
    Direction['OUTBOUND'] = enum.auto()

    # Only one endpoint is within the locally-monitored network, meaning
    # the connection is either outbound or inbound.
    Direction['BIDIRECTIONAL'] = enum.auto()

    # This value doesn’t match any connection.
    Direction['NO_DIRECTION'] = enum.auto()


@enum.unique
class Host(enum.IntFlag):
    """
    c.f. {html_path}
    """

    _ignore_ = 'Host _'
    Host = vars()

    # A host within the locally-monitored network.
    Host['LOCAL_HOSTS'] = enum.auto()

    # A host not within the locally-monitored network.
    Host['REMOTE_HOSTS'] = enum.auto()

    # Any host.
    Host['ALL_HOSTS'] = enum.auto()

    # This value doesn’t match any host.
    Host['NO_HOSTS'] = enum.auto()
