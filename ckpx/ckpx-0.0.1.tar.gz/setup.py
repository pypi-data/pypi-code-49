from setuptools import setup, find_packages
import px;

setup(
    name='ckpx',
    version=px.__version__,
    packages=find_packages(),
    install_requires=['grpcio>=1.27.2'],
    author='p2trx',
    description='Modern test automation framework using GRPC protocol',
    url='https://github.com/p2trx/px',
)
