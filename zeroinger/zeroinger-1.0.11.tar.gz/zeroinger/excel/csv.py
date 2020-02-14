import csv
from logzero import logger

from zeroinger.time import StopWatch


class CSV:
    default_delimiter = ','
    default_encoding = 'utf-8'

    def __init__(self):
        pass

    @staticmethod
    def read_dict_csv(file_path: str, delimiter: str = default_delimiter, encoding: str = default_encoding) -> list:
        """
        读取一个带header的CSV文件，返回数据格式为list of dict
        :param file_path: 
        :param delimiter: 
        :param encoding: 
        :return: 
        """
        timer = StopWatch.create_instance()
        logger.info(
            'start read csv\tpath: {}\tdelimiter: {}\tencoding: {}'.format(file_path, delimiter, encoding))
        list_of_dict = []
        with open(file_path, 'r', encoding=encoding) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            for row in reader:
                list_of_dict.append(row)
        time_cost = timer.duration()
        logger.info('done read csv, time cost: {}'.format(time_cost))
        return list_of_dict
        pass

    @staticmethod
    def write_dict_csv(file_path: str, list_of_dict: list, delimiter: str = default_delimiter,
                       encoding: str = default_encoding, headers: list = None) -> None:
        """
        将list of dict数据写入CSV，如果不指定headers，则会自动根据数据内容生成header列表
        :param file_path: 
        :param list_of_dict: 
        :param delimiter: 
        :param encoding: 
        :param headers: 
        :return: 
        """
        timer = StopWatch.create_instance()
        logger.info('start write csv\tpath: {}\tdelimiter: {}\tencoding: {}\theaders: {}'.
                    format(file_path, delimiter, encoding, headers))
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
        time_cost = timer.duration()
        logger.info('done write csv, time cost: {}'.format(time_cost))
        pass

    @staticmethod
    def read_list_csv(file_path: str, delimiter: str = default_delimiter, encoding: str = default_encoding) -> list:
        """
        读取无头部的csv，每行多个元素，返回数据格式为 list of list
        :param file_path: 
        :param delimiter: 
        :param encoding: 
        :return: 
        """
        timer = StopWatch.create_instance()
        logger.info(
            'start read csv\tpath: {}\tdelimiter: {}\tencoding: {}'.format(file_path, delimiter, encoding))
        list_of_list = []
        with open(file_path, 'r', encoding=encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            for row in reader:
                list_of_list.append(row)
        time_cost = timer.duration()
        logger.info('done read csv, time cost: {}'.format(time_cost))
        return list_of_list
        pass

    @staticmethod
    def write_list_csv(file_path: str, list_of_list: list, delimiter: str = default_delimiter,
                       encoding: str = default_encoding) -> None:
        """
        写入多行数据，每行有多个数据组成
        :param file_path: 
        :param list_of_list: 
        :param delimiter: 
        :param encoding: 
        :return: 
        """
        timer = StopWatch.create_instance()
        logger.info('start write csv\tpath: {}\tdelimiter: {}\tencoding: {}'.
                    format(file_path, delimiter, encoding))
        outf = open(file_path, 'w', encoding=encoding)
        writer = csv.writer(outf, delimiter=delimiter)
        for row in list_of_list:
            writer.writerow(row)
        outf.close()
        time_cost = timer.duration()
        logger.info('done write csv, time cost: {}'.format(time_cost))
        pass

    @staticmethod
    def read_line_csv(file_path: str, delimiter: str = default_delimiter, encoding: str = default_encoding) -> list:
        timer = StopWatch.create_instance()
        logger.info(
            'start read csv\tpath: {}\tdelimiter: {}\tencoding: {}'.format(file_path, delimiter, encoding))
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
        time_cost = timer.duriation()
        logger.info('done read csv, time cost: {}'.format(time_cost))
        return lines
        pass

    @staticmethod
    def write_line_csv(file_path: str, lines: list, delimiter: str = default_delimiter,
                       encoding: str = default_encoding) -> None:
        """
        写入CSV，每行只有一个元素
        :param file_path: 
        :param lines: 
        :param delimiter: 
        :param encoding: 
        :return: 
        """
        timer = StopWatch.create_instance()
        logger.info('start write csv\tpath: {}\tdelimiter: {}\tencoding: {}'.
                    format(file_path, delimiter, encoding))
        outf = open(file_path, 'w', encoding=encoding)
        writer = csv.writer(outf, delimiter=delimiter)
        for line in lines:
            writer.writerow([line])
        outf.close()
        time_cost = timer.duriation()
        logger.info('done write csv, time cost: {}'.format(time_cost))
        pass
