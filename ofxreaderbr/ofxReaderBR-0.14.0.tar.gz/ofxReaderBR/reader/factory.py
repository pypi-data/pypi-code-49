from abc import abstractmethod, ABC

from ofxReaderBR.reader.readerbankstatement import (PDFReaderBankStatement,
                                                    XLSReaderBankStatement,
                                                    XMLReaderBankStatement,
                                                    OFXReaderBankStatement)
from ofxReaderBR.reader.readercashflow import (PDFReaderCashFlow,
                                               XLSReaderCashFlow,
                                               XMLReaderCashFlow,
                                               OFXReaderCashFlow)
from ofxReaderBR.reader.readercontroller import (PDFReaderController,
                                                 XLSReaderController,
                                                 OFXReaderController)


class AbstractReaderFactory(ABC):

    @abstractmethod
    def create_reader_controller(self):
        pass

    @abstractmethod
    def create_reader_bank_statement(self, file, data, options=None):
        pass

    @abstractmethod
    def create_reader_cash_flow(self):
        pass


class OFXReaderFactory(AbstractReaderFactory):

    def create_reader_controller(self):
        return OFXReaderController(self)

    def create_reader_bank_statement(self, file, data, options=None):
        return OFXReaderBankStatement(self, file, data, options)

    def create_reader_cash_flow(self):
        return OFXReaderCashFlow()

    class XMLReaderFactory:
        """ Special case for OFX files """

        def create_reader_bank_statement(self, file, data, options=None):
            return XMLReaderBankStatement(self, file, data, options)

        @staticmethod
        def create_reader_cash_flow():
            return XMLReaderCashFlow()

    @classmethod
    def create_xml_factory(cls):
        return cls.XMLReaderFactory()


class PDFReaderFactory(AbstractReaderFactory):

    def create_reader_controller(self):
        return PDFReaderController(self)

    def create_reader_bank_statement(self, file, data, options=None):
        return PDFReaderBankStatement(self, file, data, options)

    def create_reader_cash_flow(self):
        return PDFReaderCashFlow()


class XLSReaderFactory(AbstractReaderFactory):

    def create_reader_controller(self):
        return XLSReaderController(self)

    def create_reader_bank_statement(self, file, data, options=None):
        return XLSReaderBankStatement(self, file, data, options)

    def create_reader_cash_flow(self):
        return XLSReaderCashFlow()
