from distutils.core import setup
setup(
  name = 'Nidhi_Topsis',         
  packages = ['Nidhi_Topsis'],   
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Topsis, R in python ',   
  author = 'Nidhi Alipuria',                   
  author_email = 'nidhialipuria@gmail.com',      
  url = 'https://github.com/NidhiAlipuria/topsis',   
  download_url = 'https://github.com/NidhiAlipuria/topsis/archive/v_01.tar.gz',   
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   
  install_requires=[    'numpy','pandas','math'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)