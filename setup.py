#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Pysis',
    version='0.4.0b0',
    author='William Trevor Olson',
    author_email='wtolson@gmail.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/wtolson/Pysis',
    license='LICENSE.txt',
    description='Useful toolkit for working with Isis in Python.',
    long_description=open('README.md').read(),
    install_requires=[]
)
