import setuptools
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here,"README.md"),encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
        name="cleanport",
        version="1.0.2",
        author="Shamsher Ahmed",
        author_email='hi@shamsherahmed.in',
        description="A package to free port for non root owner only",
        long_description=long_description,
        long_description_content_type="text/markdown",
        scripts=['src/cleanport'],
        url="https://github.com/shamsid/cleanport",
        package_dir={'': 'src'},
        packages=setuptools.find_packages(where='src'),
        keywords='port-clean process-kill development',
        python_requires='>=3.6.0',
        classifiers=[
            "Programming Language :: Python :: 3",
            'License :: OSI Approved :: MIT License',
            "Operating System :: OS Independent",
        ],
        project_urls={  # Optional
                'Bug Reports': 'https://github.com/shamsid/cleanport/issues',
                'Source': 'https://github.com/shamsid/cleanport',
        },
)


