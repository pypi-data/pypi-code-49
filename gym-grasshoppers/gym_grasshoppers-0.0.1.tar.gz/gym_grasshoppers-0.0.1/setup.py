
from setuptools import setup

setup(name='gym_grasshoppers',
      description='OpenAI Gym environment for Grasshoppers project',
      version='0.0.1',
      url='https://gitlab.com/kdg-ti/integratieproject-2/dekwo-kybons-fanclub/environment-ai',
      author='Dekwo Kybons Fanclub',
      author_email='mees.vankaam@student.kdg.be',
      zip_safe=True,
      install_requires=['gym>=0.16', 'numpy', 'shapely', 'matplotlib', 'pyproj<=2.4.1']
      )
