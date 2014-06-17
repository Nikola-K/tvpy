#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='tvpy',
    version='0.1.0',
    description='Searches and parses pages that contain tv show links for streaming, extracts direct file location and opens it in your default player.',
    long_description=readme + '\n\n' + history,
    author='Nikola Kovacevic',
    author_email='nikolak@outlook.com',
    url='https://github.com/nikola-k/tvpy',
    packages=[
        'tvpy',
    ],
    package_dir={'tvpy':
                 'tvpy'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache",
    zip_safe=False,
    keywords='tvpy',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)