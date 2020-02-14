import abc
import logging
from collections import namedtuple
from datetime import datetime

from ofxReaderBR.model import AccountType, CashFlow, CashFlowType, Origin

logger = logging.getLogger(__name__)


class IReaderCashFlow(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, factory, ofx) -> CashFlow:
        pass


class OFXReaderCashFlow(IReaderCashFlow):
    def read(self, factory, ofx) -> CashFlow:
        cs = CashFlow()

        cs.name = ofx.memo
        cs.value = ofx.trnamt
        cs.date = ofx.dtposted

        if ofx.trntype == 'CREDIT':
            cs.flowType = CashFlowType.CREDIT

        return cs


class PDFReaderCashFlow(IReaderCashFlow):
    def read(self, factory, ofx) -> CashFlow:
        cs = CashFlow()

        result = ofx

        cs.date = result[0]
        cs.name = result[1]
        cs.value = result[2]

        if len(result) > 3:
            last_digits = result[3]
            cs.origin = Origin(type='CREDITCARD', account_id=last_digits)

        if len(result) > 4:
            cash_date = result[4]
            if cash_date:
                cs.cash_date = cash_date

        if not cs.cash_date:
            cs.cash_date = cs.date

        return cs


class XMLReaderCashFlow(IReaderCashFlow):
    def read(self, factory, ofx) -> CashFlow:
        cs = CashFlow()

        cs.name = ofx.find('MEMO').text
        cs.value = float(ofx.find('TRNAMT').text)
        dtposted = ofx.find('DTPOSTED').text

        try:
            # YYYYMMDDHHMMSS
            cs.date = datetime.strptime(dtposted[:dtposted.find('[')],
                                        '%Y%m%d%H%M%S')
        except:
            cs.date = datetime.strptime(dtposted, '%Y%m%d')

        # FT-272
        cs.cash_date = cs.date

        if ofx.find('TRNTYPE') == 'CREDIT':
            cs.flowType = CashFlowType.CREDIT

        return cs


class XLSReaderCashFlow(IReaderCashFlow):
    def read(self, factory, ofx) -> CashFlow:
        cs = CashFlow()

        row = ofx

        cell_values = []
        for cellValue in row:
            cell_values.append(cellValue)

        if all([value is None for value in cell_values]):
            logger.info('Row with blank columns. Made cash flow invalid.')
            return cs


        Account = namedtuple('Account', 'acctid')
        account = Account(acctid=cell_values[1])
        origin = Origin(account)

        if cell_values[0] is None or cell_values[1] is None:
            origin = None
        elif cell_values[0].upper() == 'C/C':
            origin.account_type = AccountType.BANKACCOUNT
        elif cell_values[0].lower() == 'cartão de crédito':
            origin.account_type = AccountType.CREDITCARD
        else:
            raise ValueError("The value for origin type is not valid")

        cs.origin = origin
        cs.date = cell_values[2]
        cs.cash_date = cell_values[3]
        cs.name = cell_values[4]
        cs.value = cell_values[5]

        return cs
