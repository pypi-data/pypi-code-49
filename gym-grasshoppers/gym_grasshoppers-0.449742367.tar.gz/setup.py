import os

from setuptools import setup, find_packages

try:
    if os.environ.get('CI_COMMIT_TAG'):
        if os.environ['CI_COMMIT_TAG'].startswith('v'):
            version = os.environ['CI_COMMIT_TAG'][1:]
        else:
            version = os.environ['CI_COMMIT_TAG']
    else:
        version = '0.' + os.environ['CI_JOB_ID']  # Use job ID if no commmit tag provided
except KeyError:
    import datetime

    version = '0.' + str(datetime.datetime.now())[0:23].replace(' ', '-').replace(':', '')

setup(name='gym_grasshoppers',
      description='OpenAI Gym environment for Grasshoppers project',
      version=version,
      url='https://gitlab.com/kdg-ti/integratieproject-2/dekwo-kybons-fanclub/environment-ai',
      author='Dekwo Kybons Fanclub',
      author_email='mees.vankaam@student.kdg.be',
      packages=find_packages(),
      zip_safe=True,
      install_requires=['gym>=0.16', 'numpy', 'shapely', 'matplotlib', 'pyproj<=2.4.1']
      )
