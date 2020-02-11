import csv
import random
import sys
from decimal import Decimal as D

from ofxstatement import statement
from ofxstatement.parser import CsvStatementParser
from ofxstatement.plugin import Plugin


class StanbicZmPlugin(Plugin):
    """Stanbic Zambia Plugin
    """

    def get_parser(self, filename):
        f = open(filename, 'r', encoding=self.settings.get("charset", "UTF-8"))
        parser = StanbicZmParser(f)
        return parser

class StanbicZmParser(CsvStatementParser):

    date_format = "%d/%m/%Y"
    mappings = {
        'date': 1,
        'refnum': 0,
        'memo': 2,
        'amount': 5,
        'id': 0
    }
    
    def parse(self):
        """Main entry point for parsers

        super() implementation will call to split_records and parse_record to
        process the file.
        """
        stmt = super(StanbicZmParser, self).parse()
        statement.recalculate_balance(stmt)
        return stmt

    def split_records(self):
        """Return iterable object consisting of a line per transaction
        """
        
        reader = csv.reader(self.fin, delimiter=',')
        next(reader, None)
        return reader

    def fix_amount(self, value):
        return D(value.replace(',', '.').replace(' ', ''))


    def parse_record(self, line):
        """Parse given transaction line and return StatementLine object
        """

        if line[2] == "":
            return None
        elif line[2] == "Opening balance":
            self.statement.start_balance = self.fix_amount(line[6])
            return None
        elif line[2] == "Closing balance":
            return None

        if line[4]:
            line[5] = "-" + line[4]

        line[0] = str(random.randrange(sys.maxsize))

        stmtline = super(StanbicZmParser, self).parse_record(line)
        stmtline.trntype = 'DEBIT' if stmtline.amount < 0 else 'CREDIT'

        return stmtline
