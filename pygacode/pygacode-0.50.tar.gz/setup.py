from numpy.distutils.core import setup, Extension
import sys

wrapper = Extension('gacode_ext',
                    sources=['expro/expro.f90',
                             'expro/expro_util.f90',
                             'expro/expro_pycomm.f90',
                             'geo/geo.f90',
                             'vis/vis.f90'])

setup(name='pygacode',
      version='0.50',
      description='Python interface to gacode profile and geometry tools',
      url='https://gacode.io',
      author='General Atomics Theory Group',
      author_email='candy@fusion.gat.com',
      license='MIT',
      py_modules=['pygacode.__init__', 'pygacode.test.test_install'],
      package_data={'pygacode.test': ['input.gacode']},
      packages=['pygacode.test'],
      ext_modules=[wrapper]
      )

# only run tests when installing
if 'install' in sys.argv:
    from pygacode.test import test_install
