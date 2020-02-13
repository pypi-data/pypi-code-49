import string
import re 

useless = string.printable+"，。；’：‘’“”！？《》￥…（）—·【】、"


def has_chinese(str0):
    """判断是否存在汉字
    """
    return bool(re.search(u'[\u4e00-\u9fa5]', str0))
# def is_chinese(uchar):
#     """判断一个unicode是否是汉字"""
#     if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
#         return True
#     else:
#         return False
def has_english(str0):
    return bool(re.search('[a-z]', str0)) or bool(re.search('[A-Z]', str0))

def has_number(str0):
    return bool(re.search('[0-9]', str0))

def replace_bracket(a):
    l0 = a.find('（')
    l1 = a.find('）')
    a=a.replace(a[l0:l1+1],'')
    return a

def sub2empty(useless, str0):
    return re.sub(f"[{useless}]+", "", str0)