from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='httpsx',


    version="0.0.1",
    description=(
        ''

    ),
    long_description=open('README.md', 'r').read(),
    author='huangzhengrui',
    author_email='156546731@qq.com',
    maintainer='huangzhengrui',
    maintainer_email='156546731@qq.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://hjfgakhdgfhjkadgfjagdkfjhahfa.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[              # 这里是依赖列表，表示运行这个包的运行某些功能还需要你安装其他的包
        'requests',
    ]
)