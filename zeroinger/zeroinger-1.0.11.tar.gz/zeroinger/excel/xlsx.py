from logzero import logger
import pyexcel as p

'''
基于pyexcel实现
http://docs.pyexcel.org/en/latest/quickstart.html
'''


class XLSX:
    def __init__(self):
        pass

    @staticmethod
    def read_dict_sheet(xlsx_path: str, sheet_id_or_name=0) -> list:
        """
        
        :param xlsx_path: xlsx文件路径
        :param sheet_id_or_name: 标签页的id或名称
        :return: 返回值
        """
        book = p.iget_book(file_name=xlsx_path)
        sheet = None
        if type(sheet_id_or_name) == int:
            # 输入的定位标是数字
            if book.number_of_sheets() < sheet_id_or_name:
                # 如果没有读取到数据，就返回空列表
                pass
            else:
                name = book.sheet_names()[sheet_id_or_name]
                sheet = book[name]
        if type(sheet_id_or_name) == str:
            # 输入的定位标是文本
            sheet = book[sheet_id_or_name]
        if sheet == None:
            return []
        ret = []
        cache = sheet.array
        if len(cache) < 1:
            return []
        keys = cache[0]
        for i in range(1, len(cache)):
            data = {}
            for j in range(len(keys)):
                if len(cache[i]) < j + 1:
                    data[keys[j]] = None
                else:
                    data[keys[j]] = cache[i][j]
            ret.append(data)

        return ret

        pass

    @staticmethod
    def write_dict_sheet(xlsx_path: str, list_of_dict: list, sheet_name='sheet1') -> None:
        """
        
        :param xlsx_path: 文件存储路径文件名
        :param list_of_dict: 字典列表
        :param sheet_name: sheet页名
        :return: 
        """
        p.save_as(records=list_of_dict, sheet_name=sheet_name, dest_file_name=xlsx_path)
        pass
