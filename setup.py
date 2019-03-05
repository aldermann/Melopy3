#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

config = {
    'name': 'Melopy3',
    'author': 'Aldermann',
    'author_email': 'vietanisme@gmail.com',
    'description': 'Python music library',
    'long_description': open('README.txt').read(),
    'packages': ['melopy'],
    'version': '0.1.2',
    'url': 'https://github.com/aldermann/Melopy3',
    'license': 'LICENSE.txt',
    'classifiers': []
}

setup(**config)

# Licensed under The MIT License (MIT)
# See LICENSE file for more
