#!/usr/bin/env python

from distutils.core import setup

setup(
    name='bottle-mvc-bootstrap',
    version='0.1.0',
    description='Scaffold generator for Bottle projects using MVC and Bootstrap',
    author='Antonio Dourado',
    author_email='tonnydourado@gmail.com',
    packages=['bottle_mvc_bootstrap'],
    data_files=[('static_files', ['bootstrap.zip', 'index.tpl', 'jquery.js'])],
)
