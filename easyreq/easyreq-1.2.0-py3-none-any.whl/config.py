import os

rootDir    = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
reqPath    = os.path.join(rootDir, 'requirements.txt')
readmePath = os.path.join(rootDir, 'README.md')
version    = '1.2.0'