class Table:

    def __init__(self, field_names: list, rows: list = None, ttl: bool = True):
        self.table = [field_names]
        self.ttl = ttl
        for row in rows:
            self.add_row(row)

    def add_row(self, row: list):
        if row is not None:
            if self.ttl:
                row[1] = self.convert_ttl(row[1])
            self.table.append(row)

    def convert_ttl(self, value: int, unit: str = 's') -> str:
        value_org = value
        unit = 's'

        try:
            value = int(value)
        except ValueError:
            value = f"{value} {unit}"

        for u in ['m', 'h', 'd']:
            div = 24 if u == 'd' else 60
            if value >= div:
                unit = u
                if value % div == 0:
                    value = int(value / div)
                else:
                    value /= div

        return f"{value_org} s ({value} {unit})"

    def __str__(self) -> str:
        table_str = ''
        longest_cols = [
            (max([len(str(row[i])) for row in self.table]) + 3) for i in range(len(self.table[0]))
        ]
        row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])
        for row in self.table:
            table_str += (row_format.format(*row)) + '\n'

        return table_str
