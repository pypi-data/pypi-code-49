from unittest import TestCase
from zeroinger.excel.xlsx import XLSX
from logzero import logger
import os


class TestXLSX(TestCase):
    def test_read_dict_sheet(self):
        test_read_file_path = os.path.join(os.path.dirname(__file__), 'read_test_file.xlsx')
        data = XLSX.read_dict_sheet(test_read_file_path, 0)
        logger.info("读出的数据-{}".format(data))
        golden = [{'列1': 1, '列2': 4, '列3': 7}, {'列1': 2, '列2': 5, '列3': 8}, {'列1': 3, '列2': 6, '列3': 9}]
        self.assertEqual(data, golden, "读取出的数据不同")

    def test_write_dict_sheet(self):
        golden = [{'列1': 1, '列2': 4, '列3': 7}, {'列1': 2, '列2': 5, '列3': 8}, {'列1': 3, '列2': 6, '列3': 9}]
        test_write_file_path = os.path.join(os.path.dirname(__file__), 'write_test_file.xlsx')
        if os.path.exists(test_write_file_path):
            os.remove(test_write_file_path)
        self.assertTrue(not os.path.exists(test_write_file_path), "写入测试文件未清除")
        XLSX.write_dict_sheet(test_write_file_path, golden)
        self.assertTrue(os.path.exists(test_write_file_path), "写入测试文件未生成")
        act_data = XLSX.read_dict_sheet(test_write_file_path)
        logger.info("写入的数据-{}".format(act_data))
        self.assertEqual(act_data, golden, "写入的数据不一致")
