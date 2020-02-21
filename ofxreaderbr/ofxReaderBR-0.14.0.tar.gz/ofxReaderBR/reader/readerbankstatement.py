import abc
import logging
from decimal import Decimal

from ofxReaderBR.model import BankStatement, Origin

logger = logging.getLogger(__name__)


class ReaderBankStatement(abc.ABC):

    def __init__(self, factory, file, data, options=None):
        self.data = data
        self.factory = factory
        self.file = file
        self.options = options

    @abc.abstractmethod
    def read(self):
        pass


class OFXReaderBankStatement(ReaderBankStatement):

    def read(self):
        options = self.options
        ofx = self.data
        file = self.file
        factory = self.factory

        signal_multiplier = 1
        if options:
            if options['creditcard'] is True and options['bancodobrasil'] is False:
                signal_multiplier = -1

        stmts = ofx.statements

        cs_reader = factory.create_reader_cash_flow()

        bank_statement = BankStatement(file)

        bank_statement.read_status = BankStatement.COMPLETE
        # btmts -> bs
        for stmt in stmts:
            bs = BankStatement(file)
            account = stmt.account
            origin = Origin(account)

            txs = stmt.transactions

            # FT-491
            is_bb_credit_card = options['creditcard'] and options.get('bancodobrasil')
            bb_cash_date = stmt.ledgerbal.dtasof if is_bb_credit_card else None

            for tx in txs:
                cs = cs_reader.read(factory, tx)
                cs.value = Decimal(cs.value)
                cs.value *= signal_multiplier

                cs.origin = origin
                if origin.is_bank_account():
                    cs.cash_date = cs.date
                elif options['creditcard'] and options.get('bradesco'):
                    cs.cash_date = stmt.dtstart
                # FT-491
                elif is_bb_credit_card:
                    cs.cash_date = bb_cash_date
                else:
                    raise NotImplementedError(f'Not implemented cash date for origin: {origin}')

                if cs.is_valid():
                    bs.transactions.append(cs)
                else:
                    bank_statement.read_status = BankStatement.INCOMPLETE

            bank_statement += bs

        return bank_statement


class PDFReaderBankStatement(ReaderBankStatement):

    def read(self):
        factory = self.factory
        result = self.data
        options = self.options

        bs = BankStatement(self.file)

        cs_reader = factory.create_reader_cash_flow()
        header_row = True
        bs.read_status = BankStatement.COMPLETE
        for row in result:
            # Pulando o cabecalho
            has_header = options.get('has_header', True)
            if header_row and has_header:
                header_row = False
                continue

            cs = cs_reader.read(factory, row)
            if not cs.is_valid():
                bs.read_status = BankStatement.INCOMPLETE
            else:
                bs.transactions.append(cs)

        return bs


class XMLReaderBankStatement(ReaderBankStatement):

    def read(self):
        factory = self.factory
        ofx = self.data
        options = self.options

        bs = BankStatement(self.file)

        if options is not None and options.get('creditcard'):
            tran_list = ofx.find('CREDITCARDMSGSRSV1').find('CCSTMTTRNRS').find(
                'CCSTMTRS')

            # Origin
            institution = None
            branch = None
            account_id = tran_list.find('CCACCTFROM').find('ACCTID').text
            account_type = 'CREDITCARD'
        else:
            tran_list = ofx.find('BANKMSGSRSV1').find('STMTTRNRS').find(
                'STMTRS')

            # Origin
            account = tran_list.find('BANKACCTFROM')
            institution = account.find('BANKID').text
            branch = account.find('BRANCHID').text
            account_id = account.find('ACCTID').text
            account_type = 'BANKACCOUNT'

        origin = Origin(
            account_id=account_id,
            branch=branch,
            institution=institution,
            type=account_type,
        )

        if tran_list is not None:
            tran_list = tran_list.find('BANKTRANLIST')

        txs = tran_list.findall('STMTTRN')

        cs_reader = factory.create_reader_cash_flow()
        bs.read_status = BankStatement.COMPLETE
        for tx in txs:
            cs = cs_reader.read(factory, tx)
            cs.origin = origin
            cs.value = float(cs.value)
            if cs.is_valid():
                bs.transactions.append(cs)
            else:
                bs.read_status = BankStatement.INCOMPLETE

        return bs


class XLSReaderBankStatement(ReaderBankStatement):

    def read(self):
        factory = self.factory
        ws = self.data

        bs = BankStatement(self.file)

        cs_reader = factory.create_reader_cash_flow()
        header_row = True
        bs.read_status = BankStatement.COMPLETE
        for row in ws.values:
            # Pulando o cabeçalho
            if header_row:
                if len(row) != 6:
                    raise ValueError('XLS expected to have 6 columns.')
                header_row = False
                continue

            cs = cs_reader.read(factory, row)

            if cs.is_blank():
                continue

            if cs.is_valid():
                if isinstance(cs.value, str):
                    cs.value = Decimal(cs.value.replace(',', '.'))
                bs.transactions.append(cs)
            else:
                bs.read_status = BankStatement.INCOMPLETE

        return bs
