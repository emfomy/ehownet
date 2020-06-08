#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'

import setuptools
import ehn as about

with open('README.rst') as fin:
    readme = fin.read()

setuptools.setup(
    name=about.__title__,
    version=about.__version__,
    author=about.__author_name__,
    author_email=about.__author_email__,
    description=about.__description__,
    long_description=readme,
    long_description_content_type='text/x-rst',
    url=about.__url__,
    download_url=about.__download_url__,
    platforms=['linux_x86_64'],
    license=about.__license__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: Free for non-commercial use',
        'Natural Language :: Chinese (Traditional)',
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'ply>=3.11',
        'treelib>=1.5.5',
        'wcwidth>=0.1.7',
    ],
    entry_points={
        'console_scripts': [
            'ehn-parser = ehn._bin.parser:main',
        ],
    },
)
