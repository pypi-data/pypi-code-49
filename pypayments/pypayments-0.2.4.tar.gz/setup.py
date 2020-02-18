from setuptools import setup


requires = [
    'requests>=2.21.0'
]


setup(
    name='pypayments',
    packages=['pypayments'],
    version='0.2.4',
    description='Unofficial library for make payments in Python',
    author='Daniel Guilhermino',
    author_email='daniel@hubtec.com.br',
    license='MIT',
    url='https://github.com/hubtec/pypayments',
    keywords=['ebanx', 'payments', 'gateway'],
    classifiers=[],
)
