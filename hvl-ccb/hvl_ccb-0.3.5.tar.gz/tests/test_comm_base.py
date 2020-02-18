#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Tests for the base class CommunicationProtocol.
"""

from hvl_ccb.comm import CommunicationProtocol
from hvl_ccb.configuration import configdataclass


@configdataclass
class EmptyConfig:
    pass


class DummyCommmunicationProtocol(CommunicationProtocol):
    @staticmethod
    def config_cls():
        return EmptyConfig

    def open(self):
        pass

    def close(self):
        pass


def test_communication_protocol():
    with DummyCommmunicationProtocol({}) as c:
        assert c is not None
