#!/usr/bin/env python
import os
import sys
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

dependencies = []
requires = [
    'mease',
]

if sys.version_info[0] == 2:
    requires.append('futures')

setup(
    name='django-mease',
    version='0.1.7',
    description="Mease: Websocket integration made easy for Django",
    url="https://github.com/florianpaquet/django-mease",
    author="Florian PAQUET",
    author_email="contact@florianpaquet.com",
    long_description=read('README.md'),
    license='MIT',
    packages=[
        'djmease',
        'djmease.management',
        'djmease.management.commands',
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
