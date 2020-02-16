from distutils.core import setup

# 这是一个元组，一旦定义就不能再改了
setup(
    name='Jarvis_test_000001',
    version='1.0',
    description='对外发布的模块，测试用',
    author='Jarvis',
    author_email='314645343@qq.com',
    py_modules=['Jarvis_test_000001.Py01', 'Jarvis_test_000001.Py02']  # 要发布的模块(这是一个列表，可以后续修改的)
)