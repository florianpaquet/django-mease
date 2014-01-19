#!/usr/bin/env python
import sys
from setuptools import setup

dependencies = []
requires = [
    'colorlog>=2.0.0',
    'tornado>=3.2',
    'redis>=2.9.0',
    'toredis>=0.1.3',
]

if sys.version_info[0] == 2:
    requires.append('futures')

setup(
    name='django-mease',
    version='0.1.6',
    description="Mease: Websocket integration made easy for Django",
    url="https://github.com/florianpaquet/django-mease",
    author="Florian PAQUET",
    author_email="contact@florianpaquet.com",
    long_description=open('README.md').read(),
    license='MIT',
    packages=[
        'mease',
        'mease.management',
        'mease.management.commands'
    ],
    dependency_links=[
        'https://github.com/florianpaquet/toredis/tarball/0.1.3#egg=toredis-0.1.3'
    ],
    install_requires=requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
