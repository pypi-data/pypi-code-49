s = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

s_cn = """Python 之禅

优美胜于丑陋
清晰胜于晦涩
简单胜于复杂
复杂胜于错综复杂
扁平胜于嵌套
稀疏胜于密集
可读性很重要
特殊情况也不应该违反这些规则
但现实往往并不那么完美
异常不应该被静默处理
除非你希望如此
遇到模棱两可的地方，不要胡乱猜测
肯定有一种通常也是最佳的解决方案
虽然这种方案并不是显而易见的，因为你不是那个荷兰人^这里指的是Python之父Guido^
现在开始比不做好
不做比盲目去做好^极限编程中的YAGNI原则^
如果一个实现方案难于理解，它就不好
如果一个实现方案易于理解，它可能是一个好方案
命名空间非常有用，我们应当多加利用！
"""

for i, c in enumerate(s.splitlines()):
    if i != 1:
        print("{}\n{}\n".format(c, s_cn.splitlines()[i]))
