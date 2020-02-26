from setuptools import setup, find_packages
import io

setup(name='qatools-ifchange',\
        version='0.0.7',\
        description='fix encoding version',\
        #long_description=open('README.md',encoding='utf-8').read(),\
        #long_description=io.open('./QAplatform/README.md','r',-1,'utf-8').read(),\
        long_description_content_type="text/markdown",\
        url='https://github.com',\
        author='LH19880520',\
        author_email='peng.wang@ifchange.com',\
        license='ifchange',\
        install_requires=['tensorflow>=1.12.0','pyyaml','requests','sklearn','rank_bm25','jieba','gensim','faiss-cpu','tornado==5.0.2'],\
        packages=find_packages(),\
        package_data={'QAplatform': ['conf/*','data/*']},\
        include_package_data=True,\
        zip_safe=False)
