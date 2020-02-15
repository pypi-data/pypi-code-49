from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    name="libspy",
    version="0.0.2",
    license='GNU General Public License version 3',
    description="A api and minimal server of ss",
    author='carl cheung',
    url='https://github.com/zylo117/libspy',
    packages=['libspy'],
    package_data={
        'libspy': ['README.md', 'LICENSE']
    },
    install_requires=['shadowsocks-py'],
    entry_points="""
    [console_scripts]
    sslocal = shadowsocks.local:main
    ssserver = shadowsocks.server:main
    """,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)