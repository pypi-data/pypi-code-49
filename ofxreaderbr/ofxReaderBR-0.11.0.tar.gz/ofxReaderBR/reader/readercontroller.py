import abc
import logging

from lxml import etree
from ofxtools import OFXTree
from openpyxl import load_workbook

from ofxReaderBR.model import BankStatement
from ofxReaderBR.reader.exceptions import OFXVersionError
from ofxReaderBR.reader.pdf.PDFParserSantander import PDFParserSantander
from ofxReaderBR.reader.pdf.pdfParser import PDFParser

logger = logging.getLogger(__name__)


class BaseReaderController(abc.ABC):

    def __init__(self, factory):
        self.factory = factory

    def read(self, files):
        logger.debug(files)

        bank_stmts = []
        for file in files:
            options = {}

            try:
                data = self._get_data(file, options)
                bs_reader = self.factory.create_reader_bank_statement(file, data, options)
            except OFXVersionError:
                # ofx nao consegue ler versão 220. Ler como XML
                data = OFXReaderController.get_xml_data(file, options)
                factory = self.factory.create_xml_factory()
                bs_reader = factory.create_reader_bank_statement(file, data, options)

            try:
                bs = bs_reader.read()
            except (RuntimeError, ValueError) as err:
                bs = BankStatement(file)
                bs.read_status = BankStatement.ERROR
                logger.error(f'Error reading file {file}: {err}')

            bank_stmts.append(bs)

        return bank_stmts

    @abc.abstractmethod
    def _get_data(self, file, options):
        pass


class PDFReaderController(BaseReaderController):

    def _get_data(self, file, options):
        try:
            parser = PDFParserSantander(file)
            result = parser.run()
            options['has_header'] = False
        except ValueError as err:
            logger.debug(err)
            parser = PDFParser()
            result = parser.run(file)
        return result


class XLSReaderController(BaseReaderController):

    def _get_data(self, file, options):
        wb = load_workbook(file)
        return wb.active


class OFXReaderController(BaseReaderController):

    @classmethod
    def get_xml_data(cls, file, options):
        file.seek(0)
        data = file.read().decode("latin-1")
        data = data[data.find('<OFX>'):]
        parser = etree.XMLParser(recover=True)
        tree = etree.fromstring(data, parser=parser)
        options['creditcard'] = cls.__is_credit_card(tree)
        return tree

    def _get_data(self, file, options):
        file.seek(0)
        tree = OFXTree()
        try:
            tree.parse(file)
        except IndexError:
            raise OFXVersionError()

        options['creditcard'] = self.__is_credit_card(tree)

        root = tree.getroot()

        if options['creditcard']:
            options['bradesco'] = self.__is_bradesco_credit_card(root)
        options['bancodobrasil'] = self.__is_banco_do_brasil(root)

        self.__treat_bradesco_exception(root)

        return tree.convert()

    @staticmethod
    def __is_banco_do_brasil(root):
        fi = root.findall("SIGNONMSGSRSV1")[0].findall(
            "SONRS")[0].findall("FI")
        if fi:
            org = fi[0].findall("ORG")
            if org and "Banco do Brasil" in org[0].text:
                return True
        return False

    @staticmethod
    def __is_bradesco_credit_card(root):
        # KN-177 - Check if Bradesco credit card
        cc_stmt_trn_rs = root.findall('CREDITCARDMSGSRSV1')[0].findall('CCSTMTTRNRS')[0]
        bank_tran_list = cc_stmt_trn_rs.findall('CCSTMTRS')[0].findall('BANKTRANLIST')[0]
        dt_start = bank_tran_list.findall('DTSTART')[0]
        dt_end = bank_tran_list.findall('DTEND')[0]
        return dt_start.text == dt_end.text

    @staticmethod
    def __is_credit_card(tree):
        return True if tree.findall("CREDITCARDMSGSRSV1") else False

    # Este tratamento de erro tem que ser melhor descrito
    @staticmethod
    def __treat_bradesco_exception(root):
        unknown_date_in_the_past = '19851021000000[-3:GMT]'

        dt_server = root.findall("SIGNONMSGSRSV1")[0].findall(
            "SONRS")[0].findall("DTSERVER")[0]
        try:
            if int(dt_server.text) == 0:
                dt_server.text = unknown_date_in_the_past
        except ValueError:
            pass
            # se dtServer for um datetime, ele da erro na conversao para int
            # logger.info('Correcting DTServer')

        # se for cartao de credito, a data do balanco vem errada
        try:
            credit_card_trans_rs = root.findall("CREDITCARDMSGSRSV1")[0].findall(
                "CCSTMTTRNRS")

            for c in credit_card_trans_rs:
                dt_balance = c.findall("CCSTMTRS")[0].findall(
                    "LEDGERBAL")[0].findall("DTASOF")[0]

                try:
                    if int(dt_balance.text) == 0:
                        dt_balance.text = unknown_date_in_the_past
                except ValueError:
                    pass
        except IndexError:
            pass
