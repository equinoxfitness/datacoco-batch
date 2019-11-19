#!/usr/bin/env python

from setuptools import setup
setup(
    name="datacoco-batch",
    version="0.1.0",
    author="Equinox",
    description="",
    long_description=open("README.rst").read(),
    url="https://github.com/equinoxfitness/datacoco-batch",
    download_url = 'https://github.com/equinoxfitness/datacoco-batch/archive/v-0.1.0.tar.gz',
    keywords = ['helper', 'config', 'logging', 'common'],
    scripts=[],
    license="MIT",
    packages = ['datacoco_batch'],
    install_requires=["requests==2.22.0"]
)
