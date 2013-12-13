#!/usr/bin/env python
"""
pyzopfli
======

"Protected" data types to hide secrets in Django config files.

Running a Django server in debug mode risks exposing secrets like API
keys and passwords to the world.  While Django will "filter out"
certain values, it still makes available the contents of local
variables which might also contain hidden keys. 

Protected works by breaking the object's __repr__ method to prevent casual display.

from protected import ProtectedString

>>> print ProtectedString('abc')
abc

>>> print repr(ProtectedString('abc')
<Protected String 'abc'>

"""

from setuptools import setup, Extension

setup(
    name='protected',
    version='0.0.1',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description='"Proteted" data types suitable for hiding secrets in Django config files.',
    long_description=__doc__,
    py_modules = [
        'protected/__init__',
        'protected/string',
        ],
    packages = ["protected"],
    zip_safe=True,
    license='MIT',
    include_package_data=True,
    classifiers=[
        ],
    scripts = [
        ],
    url = "https://github.com/wnyc/protected",
    install_requires = [
        ]
)

