#!/usr/bin/env python

from distutils.core import setup

setup(
    name='bottle-mvc-bootstrap',
    version='0.1.0',
    description='Scaffold for Bottle projects using MVC and Bootstrap',
    author='Antonio Dourado',
    author_email='tonnydourado@gmail.com',
    url='http://fake.com',
    packages=['bottle_mvc_bootstrap'],
    package_data={'bottle_mvc_bootstrap': ['static_files/*']},
    scripts=['bottle_mvc_bootstrap/bottle_mvc_bootstrap.py'],
    license='BSD',
    requires=['bottle (>=0.11.6)']
)
