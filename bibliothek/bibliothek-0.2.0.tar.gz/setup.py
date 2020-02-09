from setuptools import setup, find_packages

with open('./README.md', 'r') as f:
    readme = f.read()

setup(
    name='bibliothek',
    version='0.2.0',
    author='ereyue',
    author_email='python@ereyue.me',
    description='Managing Markup Files',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/ereyue/bibliothek',
    package_data={'': ['LICENSE']},
    package_dir={'bibliothek': 'bibliothek'},
    include_package_data=True,
    install_requires=['pyyaml'],
    packages=find_packages(),
    python_requires='>=3.6',
    license='gpl-3.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
