try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='intervalcron',
    packages=['intervalcron'],
    version='0.0.1',
    py_modules=['intervalcron'],
    install_requires=['APScheduler'],
    test_suite="tests",
    entry_points={
        'apscheduler.triggers': ['intervalcron = intervalcron:IntervalCronTrigger']
    },

    license='MIT',
    description='Interval + Cron Trigger Plugin for APScheduler',
    author='code0987',
    author_email='durgapalneeraj@gmail.com',
    url='https://github.com/Code0987/apscheduler-trigger-intervalcron',
    keywords=['APScheduler', 'Interval', 'Cron'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
