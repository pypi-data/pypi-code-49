import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def parse_requirements(filename):
    ''' Load requirements from a pip requirements file '''
    with open(filename, 'r') as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines

requirements = parse_requirements('requirements.txt')

setuptools.setup(
    name="diff_cov_lint",
    version="0.1.4",
    author="Sergey Verentsov",
    author_email="verentsov@eora.ru",
    description="Linting and coverage reports for diff only",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/sVerentsov/diff-cov-lint",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['diff-cov-lint=diff_cov_lint:main']
    },
    python_requires='>=3.6',
)