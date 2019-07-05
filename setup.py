#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='qradar4py',
      version='2.0',
      description='QRadarAPI Client written in Python',
      license='mit',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Ryuki',
      author_email='ryuki@tuta.io',
      url='https://github.com/ryukisec/qradar4py',
      packages=['qradar4py', 'qradar4py.endpoints'],
      install_requires=['requests'],
      python_requires='>=3',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Security'
      ]
      )
