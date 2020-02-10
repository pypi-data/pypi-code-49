# coding: utf-8
# PyDERASN -- Python ASN.1 DER codec with abstract structures
# Copyright (C) 2017-2020 Sergey Matveev <stargrave@stargrave.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
"""CRL related schemes, just to test the performance with them
"""

from pyderasn import BitString
from pyderasn import Sequence
from pyderasn import SequenceOf
from pyderasn import tag_ctxc

from tests.test_crts import AlgorithmIdentifier
from tests.test_crts import CertificateSerialNumber
from tests.test_crts import Extensions
from tests.test_crts import Name
from tests.test_crts import Time
from tests.test_crts import Version


class RevokedCertificate(Sequence):
    schema = (
        ("userCertificate", CertificateSerialNumber()),
        ("revocationDate", Time()),
        ("crlEntryExtensions", Extensions(optional=True)),
    )


class RevokedCertificates(SequenceOf):
    schema = RevokedCertificate()


class TBSCertList(Sequence):
    schema = (
        ("version", Version(optional=True)),
        ("signature", AlgorithmIdentifier()),
        ("issuer", Name()),
        ("thisUpdate", Time()),
        ("nextUpdate", Time(optional=True)),
        ("revokedCertificates", RevokedCertificates(optional=True)),
        ("crlExtensions", Extensions(expl=tag_ctxc(0), optional=True)),
    )


class CertificateList(Sequence):
    schema = (
        ("tbsCertList", TBSCertList()),
        ("signatureAlgorithm", AlgorithmIdentifier()),
        ("signatureValue", BitString()),
    )
