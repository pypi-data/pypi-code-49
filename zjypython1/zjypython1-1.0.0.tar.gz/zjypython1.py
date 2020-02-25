"""This is the stangard way to include a multiple-line comment in your code"""
def print_lol(the_list):
    """这个函数取一个位置参数，名称为"the_list",这里可以是任何列表。所有指定的列表中的每个数据，全（递归）的显示到屏幕上，各数据项各占一行。"""
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)