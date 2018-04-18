# -*- coding: utf-8 -*-
__author__ = "https://github.com/Biowulf513"
__email__ = "cherepanov92@gmail.com"

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='twitter-console',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)