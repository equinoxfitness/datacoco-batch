#!/usr/bin/env python

"""
setuptools install script.
"""
from setuptools import setup, find_packages

from module import VERSION

requires = [
  "requests==2.22.0"
]

setup(
    name="datacoco-batch",
    version=VERSION,
    author="Equinox",
    description="",
    long_description=open("README.rst").read(),
    url="https://github.com/equinoxfitness/datacoco-batch",
    scripts=[],
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=requires
)
