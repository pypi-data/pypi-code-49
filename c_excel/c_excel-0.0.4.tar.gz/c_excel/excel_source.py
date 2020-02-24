from c_excel import Excel
import xlrd

def get_int_str(num):
    if type(num)==int:
        return num
    elif type(num)==float:
        num=float(num)
        if int(num)==float(num):
            return int(num)
        else:
            return num
    elif type(num)==str:
        try:
           if int(num)==str(num):
               return int(num)
           else:
               return num
        except:
            return num
    else:
        return num

class Excel_Source(Excel):
    def __init__(self,file_name,excel_rev="03"):
        self.excel_rev=excel_rev
        self.file_name=file_name
    
    def get_data_dict(self,sheet_name,with_title=True,title_data=None,int_list=None,out_title=False,row_start=0,col_start=0):
        workbook = xlrd.open_workbook(self.file_name)
        sheet = workbook.sheet_by_name(sheet_name)
        row=row_start
        if with_title:
            if title_data is None:
                title_data=sheet.row_values(0)
            else:
                raise("标题行不能为空")
            row+=1
        # if int_list is None and type(title_data)==dict:
        #     int_list=[title for title in title_data if title_data[title]=="int"]
        dataList=[]
        for i in range(row,sheet.nrows):
            rowdict={}
            col=col_start
            for title in title_data:
                rowdict[title]= get_int_str(sheet.row_values(i)[col])
                col+=1
            dataList.append(rowdict)
        if out_title:
            return title_data,dataList
        else:
            return dataList