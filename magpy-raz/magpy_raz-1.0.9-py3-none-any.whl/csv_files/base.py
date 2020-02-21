import csv
import os


class CsvFile:
    '''
    '''

    def __init__(self, file_name, header, row, data_list):
        self.file_name = file_name
        self.data_rows = [header]
        for data_item in data_list:
            self.data_rows.append(row(data_item))

    def write(self):
        print(f'Writing file {self.file_name}: {len(self.data_rows)} rows')
        with open(self.file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"')
            writer.writerows(self.data_rows)
