import csv
from logzero import logger


class CSVUtils:
    default_delimiter = ','
    default_encoding = 'utf-8'

    def __init__(self):
        pass

    @staticmethod
    def read_dict_csv(file_path, delimiter=default_delimiter, encoding=default_encoding):
        logger.info('start reading csv of dict \t{}\t{}\t{}'.format(file_path, delimiter, encoding))
        list_of_dict = []
        with open(file_path, 'r', encoding=encoding) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            for row in reader:
                list_of_dict.append(row)
        return list_of_dict
        pass

    @staticmethod
    def write_dict_csv(file_path, list_of_dict, delimiter=default_delimiter, encoding=default_encoding, headers=None):
        if headers is None:
            headers = set()
            for dict in list_of_dict:
                for key in dict:
                    headers.add(key)
        outf = open(file_path, 'w', encoding=encoding)
        writer = csv.DictWriter(outf, delimiter=delimiter, fieldnames=headers)
        writer.writeheader()
        for row in list_of_dict:
            writer.writerow(row)
        outf.close()
        pass

    @staticmethod
    def read_list_csv(file_path, delimiter=default_delimiter, encoding=default_encoding):
        """
        读取无头部的csv，每行多个元素
        :param file_path: 
        :param delimiter: 
        :param encoding: 
        :return: 
        """
        list_of_list = []
        with open(file_path, 'r', encoding=encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            for row in reader:
                list_of_list.append(row)
        return list_of_list
        pass

    @staticmethod
    def write_list_csv(file_path, list_of_list, delimiter=default_delimiter, encoding=default_encoding):
        """
        写入多行数据，每行有多个数据组成
        :param file_path: 
        :param list_of_list: 
        :param delimiter: 
        :param encoding: 
        :return: 
        """
        outf = open(file_path, 'w', encoding=encoding)
        writer = csv.writer(outf, delimiter=delimiter)
        for row in list_of_list:
            writer.writerow(row)
        outf.close()
        pass

    @staticmethod
    def read_line_csv(file_path, delimiter=default_delimiter, encoding=default_encoding):
        """
        读取CSV 每行只有一个文本
        :param file_path: 
        :param delimiter: 
        :param encoding: 
        :return: 
        """
        lines = []
        with open(file_path, 'r', encoding=encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            for row in reader:
                if len(row) > 0:
                    lines.append(row[0])
        return lines
        pass

    @staticmethod
    def write_line_csv(file_path, lines, delimiter=default_delimiter, encoding=default_encoding):
        """
        写入CSV，每行只有一个元素
        :param file_path: 
        :param lines: 
        :param delimiter: 
        :param encoding: 
        :return: 
        """
        outf = open(file_path, 'w', encoding=encoding)
        writer = csv.writer(outf, delimiter=delimiter)
        for line in lines:
            writer.writerow([line])
        outf.close()
        pass
