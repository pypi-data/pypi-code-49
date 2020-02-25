"""This is the stangard way to include a multiple-line comment in your code"""
def print_lol(the_list,level):
    """这个函数取一个位置参数，名称为"the_list",这里可以是任何列表。所有指定的列表中的每个数据，全（递归）的显示到屏幕上，各数据项各占一行。
    第二个参数level用来遇到嵌套的列表时插入制表符"""
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print("\t",end="")
        print(each_item)
cast = ["palin","caless","idle","jone",["LIU","zhang"],"chian"]
print_lol(cast,0)