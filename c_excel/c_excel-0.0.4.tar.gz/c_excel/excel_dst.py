import xlrd
from xlutils.copy import copy
import os
from c_excel.excel_source import Excel_Source


class Excel_Dst(Excel_Source):
    """description of class"""
    def __init__(self,file_name,excel_rev="03"):
        self.excel_rev=excel_rev
        self.file_name=file_name

    #行数据处理
    def row_process(self,dict_source_row):
        return dict_source_row
        
    def import_into_sheet(self,sheet,data_list,dst_title=None):
        row=1
        #写标题
        if dst_title is not None:
            col=1
            for title in dst_title:
                self.write_cell(sheet,row,col,title)
                col+=1
            row+=1

        for row_data in data_list:
            # 行数据处理
            row_data_pro=self.row_process(row_data)
            col=1
            if type(row_data_pro)==dict:
                for title in dst_title:
                    if title in row_data_pro:
                        self.write_cell(sheet,row,col,row_data_pro[title])
                    col+=1
            else:
                for value in row_data_pro:
                    self.write_cell(sheet,row,col,value)
                    col+=1
            row+=1
        return row-2

    def import_into_dst(self,sheet_name,data_list,dst_title=None):
        workbook,sheet=self.add_sheet(sheet_name)
        
        if dst_title is None and len(data_list)>0 and type(data_list[0])==dict:
            dst_title=[]
            for title in data_list[0]:
                dst_title.append(title)

        if dst_title is not None or len(data_list)>0:
            row_count=self.import_into_sheet(sheet,data_list,dst_title)
        self.save_file(workbook)
        return row_count

