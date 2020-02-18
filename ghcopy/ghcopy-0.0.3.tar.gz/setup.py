from setuptools import setup
from setuptools.command.install import install as _install


class PostInstall(_install):
    def run(self):
        import ghcopy
        ghcopy.copy_config()
        super(PostInstall, self).run()


setup(name='ghcopy',
      version='0.0.3',
      packages=['ghcopy', 'ghcopy.config', 'ghcopy.utils'],
      url='https://github.com/oleglpts/github-copier',
      license='MIT',
      platforms='any',
      author='Oleg Lupats',
      author_email='oleglupats@gmail.com',
      description='Clone, fetch, pull user\'s Github repositories',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
      classifiers=[
            'Operating System :: POSIX',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5'
      ],
      entry_points={
          'console_scripts': [
              'ghcopy = ghcopy.__main__:main'
          ]
      },
      python_requires='>=3',
      package_data={'ghcopy': ['data']},
      install_requires=[
          'GitPython>=3.0.8',
          'PyGithub>=1.46',
          'bitbucket-python>=0.2.2'
      ],
      cmdclass={'install': PostInstall})
