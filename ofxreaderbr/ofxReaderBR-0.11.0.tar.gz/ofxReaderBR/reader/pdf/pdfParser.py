import logging
import re

from .pdfReader import PDFReader

logger = logging.getLogger(__name__)


class PDFParser:
    def parseMatch(self, match, emisDate):
        regex = '[-]?[\s]*[0-9\.]+,'
        start_value = re.search(regex, match).start()
        end_date = 5

        date = match[0:end_date].replace(' ', '')
        desc = match[end_date:start_value]
        if str(desc).endswith('/'):
            start_value += 2
        desc = match[end_date:start_value]
        value = match[start_value:].replace(' ', '')

        emis_date_month = emisDate[3:5]
        emis_date_year = emisDate[6:]

        date_month = date[3:]

        year = int(emis_date_year)
        if int(date_month) > int(emis_date_month):
            year -= 1

        date += '/' + str(year)

        return [date, desc, value]

    def run(self, file):
        reader = PDFReader()
        pdf_string = reader.run(file)

        print('run string')
        logger.info(pdf_string)

        regex = '[0-9][0-9]\/[0-9][0-9].{1,23}[0-9]+,[0-9][0-9]'
        matches = re.findall(regex, pdf_string)

        emis_start = pdf_string.find('Emissão: ')
        emis_date = pdf_string[emis_start + 9:emis_start + 19]

        results = []

        for m in matches:
            r = self.parseMatch(m, emis_date)
            logger.info(r)
            results.append(r)
        return results
