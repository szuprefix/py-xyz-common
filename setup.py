#!/usr/bin/env python  
from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="xyz-common",
    version="0.3.0",
    author="szuprefix",
    author_email="szuprefix@126.com",
    description="common",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/szuprefix/py-xyz-common",
    packages=find_packages(exclude=['tests.*', 'tests', 'testproject', 'example.*', 'example']),
    include_package_data=True,
    install_requires=[
        'django>=1.11.2'
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
