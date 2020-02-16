# 测试单函数调用和掉包功能

from Salary import day_salary
from b.Module_a import say_job
import sys

print(day_salary(10000))
say_job()

print(sys.path)  # 可以打印出所有的模块搜索路径
