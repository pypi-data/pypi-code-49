from datetime import datetime
import re

from .pdfReader import PDFReader


class PDFParserSantander:
    def __init__(self, file):
        self.file = file
        self.cards = []
        self.results = []

        self._text = None
        self._type = None

    @staticmethod
    def __change_sign(value_str):
        if '-' in value_str:
            return value_str.strip('-')
        else:
            return f'-{value_str}'

    @staticmethod
    def __replace_separator(value_str_brl):
        # Remove thousands separator and then replace decimal separator
        return value_str_brl.replace('.', '').replace(',', '.')

    def run(self):
        self.results.clear()

        reader = PDFReader()
        self._text = reader.run(self.file)

        pdf_type = self._get_type()

        if pdf_type == 'internet':
            self._run_internet_banking()
        elif pdf_type in ['standard', 'unique']:
            self._run()
        elif pdf_type == 'unknown':
            raise ValueError(f'Parser does not know how to handle this file: {self.file}')
        else:
            raise ValueError(f'Unexpected value for type: {pdf_type}')

        return self.results

    def _get_type(self):
        if self._type is None:
            if self._text is None:
                raise ValueError(
                    'Run parser before calling this method or check if text is being improperly assigned'
                )
            if self._text.startswith('Internet Banking'):
                self._type = 'internet'
            elif any(
                    card_type in self._text for card_type in [
                        'SANTANDER NACIONAL',
                        'SANTANDER STYLE PLATINUM',
                        'SANTANDER FREE',
                    ]
            ):
                self._type = 'standard'
            elif self._text.find('SANTANDER UNIQUE') != -1:
                self._type = 'unique'
            else:
                self._type = 'unknown'
        return self._type

    def _run_internet_banking(self):
        cash_flows_delimiter = 'Resumo das despesas'
        if cash_flows_delimiter in self._text:
            tables_and_footers, _ = self._text.split(cash_flows_delimiter)
            cash_date = self.__find_cash_date()
        else:
            tables_and_footers = self._text
            cash_date = None

        header_delimiter = 'Data\nDescrição\nValor (US$)\nValor (R$)'
        tables_and_footers_list = tables_and_footers.split(header_delimiter)

        footer_delimiter = ' Central de Atendimento Santander'
        table_list = [t.split(footer_delimiter)[0].strip() for t in tables_and_footers_list]
        tables = '\n'.join(table_list)

        cards_raw = tables.split('NªCartao')[1:]
        for raw in cards_raw:
            card = {}
            tokens = raw.strip().split('\n')
            card['last_digits'] = tokens[0].strip('Final:')
            card['owner'] = tokens[1].strip('Titular:')
            card['cash_flows'] = []
            for i in range(2, len(tokens), 4):
                cash_flow = {
                    'date': datetime.strptime(tokens[i], '%d/%m/%Y'),
                    'description': tokens[i + 1],
                    'value_usd': self.__change_sign(self.__replace_separator(tokens[i + 2].strip('US$ '))),
                    'value_brl': self.__change_sign(self.__replace_separator(tokens[i + 3].strip('R$ '))),
                }

                # TODO: process expenses when currency is usd
                self.results.append([
                    cash_flow['date'],
                    cash_flow['description'],
                    cash_flow['value_brl'],
                    card['last_digits'],
                    cash_date,
                ])

                card['cash_flows'].append(cash_flow)

            self.cards.append(card)

    def _run(self):
        cash_date = self.__find_cash_date()
        origin = self.__find_card_number()

        pages = self._text.split('Nº DO CARTÃO ')

        if self._type == 'unique':
            expense_pages = pages[2:]
        elif self._type == 'standard':
            expense_pages = pages[3:]
        else:
            raise ValueError(f'Could not run type={self._type}')

        expense_pages[0] = expense_pages[0].split('IOF e CET')[0]

        expense_history = ''.join(expense_pages)
        tokens = expense_history.split()
        start = False
        card_tokens = []
        for token in tokens:
            if token in ['Histórico', 'TransaçõesNacionais', 'TransaçõesInternacionais']:
                start = True
            elif token in ['DataDescrição', '(+)Despesas/DébitosnoBrasil']:
                start = False
            elif start is True:
                card_tokens.append(token)

        for i in range(len(card_tokens)):
            token = card_tokens[i]
            if re.match(r"\d{2}/\d{2}", token[:5]):
                date_str = f"{token[:5]}/{cash_date.year}"
                date = datetime.strptime(date_str, '%d/%m/%Y')

                description = token[5:]

                next_token = card_tokens[i + 1]
                if next_token.startswith('PARC'):
                    description = f"{description} {next_token}"
                    next_token = card_tokens[i + 2]

                value_without_separator = self.__replace_separator(next_token)
                value = self.__change_sign(value_without_separator)

                self.results.append([date, description, value, origin, cash_date])

    def __find_card_number(self):
        pos = self._text.find('Nº DO CARTÃO ')
        # format: Nº DO CARTÃO 1234 XXXX XXXX 4321
        return self._text[pos + 13:pos + 32]

    def __find_cash_date(self):
        if self._type == 'internet':
            delimiter = 'Data de vencimento:\n'
            pos = self._text.find(delimiter) + len(delimiter)
        elif self._type in ['unique', 'standard']:
            delimiter = '!Vencimento\n'
            pos = self._text.find(delimiter) + len(delimiter)
        else:
            raise ValueError('Could not find cash date.')

        # format dd/mm/YYYY (len=10)
        date_str = self._text[pos:pos + 10]
        return datetime.strptime(date_str, '%d/%m/%Y')
