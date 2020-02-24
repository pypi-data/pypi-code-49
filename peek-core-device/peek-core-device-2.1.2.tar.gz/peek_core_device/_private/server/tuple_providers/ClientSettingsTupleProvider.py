import logging
from typing import Union

from peek_core_device._private.storage.Setting import OFFICE_ENROLLMENT_ENABLED, \
    FIELD_ENROLLMENT_ENABLED, globalSetting
from peek_core_device._private.tuples.ClientSettingsTuple import ClientSettingsTuple
from twisted.internet.defer import Deferred
from vortex.DeferUtil import deferToThreadWrapWithLogger
from vortex.Payload import Payload
from vortex.TupleSelector import TupleSelector
from vortex.handler.TupleDataObservableHandler import TuplesProviderABC

logger = logging.getLogger(__name__)


class ClientSettingsTupleProvider(TuplesProviderABC):
    def __init__(self, ormSessionCreator):
        self._ormSessionCreator = ormSessionCreator

    @deferToThreadWrapWithLogger(logger)
    def makeVortexMsg(self, filt: dict,
                      tupleSelector: TupleSelector) -> Union[Deferred, bytes]:

        ormSession = self._ormSessionCreator()
        try:
            clientSetting = ClientSettingsTuple()

            clientSetting.fieldEnrollmentEnabled = globalSetting(ormSession,
                                                                 FIELD_ENROLLMENT_ENABLED)

            clientSetting.officeEnrollmentEnabled = globalSetting(ormSession,
                                                                  OFFICE_ENROLLMENT_ENABLED)

            # Create the vortex message
            return Payload(filt,
                           tuples=[clientSetting]).makePayloadEnvelope().toVortexMsg()

        finally:
            ormSession.close()
