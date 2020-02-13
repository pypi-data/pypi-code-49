## -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Author: WinGram Inc. 
Copyright (c) 2020, Code for China. All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer. Redistributions in binary form
must reproduce the above copyright notice, this list of conditions and the
following disclaimer in the documentation and/or other materials provided with
the distribution. Neither the name of Code for America nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission. THIS SOFTWARE IS PROVIDED
BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
 
 
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

 
setup(name="Finder138",
      version="1.2.5",
      description="iP138数据查询",
      long_description="请从https://github.com/wingram01/Finder138获取详细信息！",
      keywords="iP138",
      author="Andrew Luo",
      author_email="luoyanze07@gmail.com",
      url="https://github.com/wingram01/Finder138",
      packages=["Finder138"],
      install_requires=["requests"],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   "Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   'Natural Language :: Chinese (Simplified)',
                   'Operating System :: OS Independent',
                   'Topic :: Internet'
                  ],
      python_requires = '>=3.6'    
                    )