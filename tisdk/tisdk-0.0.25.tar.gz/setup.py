from setuptools import setup, find_packages



try:
    long_description = open('README.md', encoding='utf8').read()
except Exception as e:
    long_description = ''


try:
    install_requires = []
    for line in open('requirements.txt').readlines():
        line = line.strip()
        if line and not line.startswith('#'):
            install_requires.append(line)
except Exception as e:
    pass


setup(
    name='tisdk',
    version='0.0.25',
    description='python sdk of taiqiyun [private]',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.22.0',
        'pycrypto>=2.6.1',
    ],
    # py_modules=['tisdk'],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['tireq=tisdk:main'],
    },
    include_package_data=True,
)
