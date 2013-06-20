import os
import re
import sys
import subprocess

from setuptools import setup
from distutils.sysconfig import get_python_lib

import vero_python

# Don't generate .pyc, .pyo files on import
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = [
    'vero_python'
]
requires = ['requests==1.2.3']

setup(
    name='vero_python',
    description='Python wrapper for Vero API',
    long_description=open('README.md').read(),
    version=vero_python.__version__,
    author=open('AUTHORS.md').read(),
    author_email='rwilsonperkin@waveaccounting.com',
    url='https://github.com/waveaccounting/vero-python-client',
    packages=packages,
    package_data={'': ['LICENSE.md']},
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
    license=open('LICENSE.md').read(),
)

del os.environ['PYTHONDONTWRITEBYTECODE']
