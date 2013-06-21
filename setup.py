import os
from setuptools import setup

import vero

# Don't generate .pyc, .pyo files on import
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = [
    'vero'
]
requires = ['requests==1.2.3']

setup(
    name='vero',
    description='Python wrapper for Vero API',
    long_description=open('README.md').read(),
    version=vero.__version__,
    author=open('AUTHORS.md').read(),
    author_email='rwilsonperkin@waveaccounting.com',
    url='https://github.com/waveaccounting/vero-python',
    packages=packages,
    package_data={'': ['LICENSE.md']},
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
    license=open('LICENSE.md').read(),
)

del os.environ['PYTHONDONTWRITEBYTECODE']
