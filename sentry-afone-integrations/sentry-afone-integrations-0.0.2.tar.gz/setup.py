#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sentry-afone-integrations",
    version='0.0.2',
    author='RayLau',
    author_email='raylua2566@hotmail.com',
    url='https://github.com/raylua2566/sentry-afone-integrations',
    description=u'All for one integerations.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry webhook integrations afone diligent',
    include_package_data=True,
    zip_safe=False,
    packages=['afone_wechat_webhook'],
    install_requires=[
        'sentry>=10.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_afone_integrations = afone_wechat_webhook.plugin:AfoneWechatWebhookPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ]
)