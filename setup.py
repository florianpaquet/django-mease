#!/usr/bin/env python
from setuptools import setup

dependencies = []
requires = [
    'colorama',
    'tornado',
    'redis',
    'tornado-redis',
]

setup(
    name='django-mease',
    version='0.1.3',
    description="Mease: Websocket integration made easy for Django",
    url="https://github.com/florianpaquet/django-mease",
    author="Florian PAQUET",
    author_email="contact@florianpaquet.com",
    license='MIT',
    packages=[
        'mease',
        'mease.management',
        'mease.management.commands'
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
