import Salary
import Salary as Salary1

# 用doc命令输出文本注释，可以看到#的注释不会显示
# 且只显示第一个""""""对应的
print(Salary.__doc__)
print(Salary.day_salary.__doc__)
print(Salary.day_salary(5000).__doc__)

# 输出一下
print(Salary.day_salary(5000))
print(Salary1.day_salary(10000))
