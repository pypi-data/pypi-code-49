from setuptools import setup, find_packages
from glob import glob

def parse_requirements(requirements):
    with open(requirements) as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

reqs = parse_requirements('NLP_LIB/requirements-cpu.txt')

print(reqs)

with open("NLP_LIB/README.md", "r") as fh:
  long_description = fh.read()

setup(
  name="NLP_LIB_cpu", # Replace with your own username
  version="0.0.5",
  author="Chulayuth Asawaroengchai",
  author_email="twilightdema@gmail.com",
  description="Python library for Language Model / Finetune using Transformer based models.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/twilightdema/NLP_LIB.git",
  packages=find_packages(),
  package_data={
    'NLP_LIB': map(lambda x: x[8:], glob('NLP_LIB/*.json')),
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  install_requires=reqs,
  python_requires='>=3.6',
)