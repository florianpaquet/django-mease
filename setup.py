#!/usr/bin/env python
import sys
from setuptools import setup

dependencies = []
requires = [
    'colorama',
    'tornado',
    'redis',
    'toredis',
]

if sys.version_info[0] == 3:
    dependencies.append(
        'https://github.com/mrjoes/toredis/tarball/master#egg=toredis')

setup(
    name='mease',
    version='0.1',
    description="Mease: Websocket integration made easy for Django",
    author="Florian PAQUET",
    author_email="contact@florianpaquet.com",
    packages=['mease'],
    install_requires=requires,
    dependency_links=dependencies)
