import setuptools
import subprocess
import platform

with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/UD-Kanbun"

pl=platform.platform()
if pl.startswith("CYGWIN"):
  install_requires=["ufal.udpipe>=1.2.0","mecab-cygwin>=0.5.0"]
else:
  import sys
  useFugashi=(sys.version_info.major==3)and(sys.version_info.minor>6)
  try:
    d=subprocess.check_output(["mecab-config","--libs-only-L"])
  except:
    import os
    useFugashi&=(os.name=="nt")
  if useFugashi:
    install_requires=["ufal.udpipe>=1.2.0.3","fugashi>=0.1.8"]
  else:
    from pkg_resources import get_distribution
    if pl.startswith("Linux") and int(get_distribution("pip").version.split(".")[0])<19:
      install_requires=["ufal.udpipe>=1.2.0","mecab-cygwin>=0.5.0"]
    else:
      install_requires=["ufal.udpipe>=1.2.0","mecab-python3>=0.996.3"]

setuptools.setup(
  name="udkanbun",
  version="1.9.0",
  description="Tokenizer POS-tagger and Dependency-parser for Classical Chinese",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="MIT",
  keywords="udpipe mecab nlp",
  packages=setuptools.find_packages(),
  install_requires=install_requires,
  python_requires=">=3.6",
  package_data={
    "udkanbun":["./*.js","./ud-kanbun.udpipe","./mecab-kanbun/*"],
  },
  entry_points={
    "console_scripts":["udkanbun=udkanbun.cli:main"],
  },
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Topic :: Text Processing :: Linguistic",
  ],
  project_urls={
    "ud-kanbun":"https://corpus.kanji.zinbun.kyoto-u.ac.jp/gitlab/Kanbun/ud-kanbun",
    "Source":URL,
    "Tracker":URL+"/issues",
  }
)
