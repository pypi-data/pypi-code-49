import setuptools

setuptools.setup(
    name='simple-proxy-wysohn',
    version='0.0.2',
    author='wysohn',
    author_email='wysohn2002@naver.com',
    python_requires='>=3.6',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'selenium',
    ],
)
