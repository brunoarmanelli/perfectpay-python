#!/usr/bin/env python
from setuptools import setup
from io import open

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

setup(name='perfectpay-python',
      version='0.2',
      description='Perfect Pay requests made easy',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      author='Bruno Armanelli',
      author_email='brunoarmanelli@me.com',
      url='https://github.com/brunoarmanelli/perfectpay-python',
      packages=['perfectpay'],
      keywords='perfectpay',
      install_requires=['requests', 'six']
     )