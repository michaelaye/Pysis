#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='Pysis',
    version='0.3.1',
    author='William Trevor Olson',
    author_email='wtolson@gmail.com',
    packages=[
        'pysis',
        'pysis.binning',
        'pysis.util'
    ],
    scripts=[],
    url='https://github.com/wtolson/Pysis',
    license='LICENSE.txt',
    description='Useful toolkit for working with Isis in Python.',
    long_description=open('README.md').read(),
    install_requires=[]
)
