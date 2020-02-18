import os

from setuptools import setup

if os.environ.get('CI_COMMIT_TAG'):
    if os.environ['CI_COMMIT_TAG'].startswith('v'):
        version = os.environ['CI_COMMIT_TAG'][1:]
    else:
        version = os.environ['CI_COMMIT_TAG']
else:
    version = '0.' + os.environ['CI_JOB_ID']

setup(name='gym_grasshoppers',
      description='OpenAI Gym environment for Grasshoppers project',
      version=version,
      url='https://gitlab.com/kdg-ti/integratieproject-2/dekwo-kybons-fanclub/environment-ai',
      author='Dekwo Kybons Fanclub',
      author_email='mees.vankaam@student.kdg.be',
      zip_safe=True,
      install_requires=['gym>=0.16', 'numpy', 'shapely', 'matplotlib', 'pyproj<=2.4.1']
      )
