try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'vero'
]
requires = ['requests==1.2.3']

setup(
    name='vero',
    description='Python wrapper for Vero API',
    long_description=open('README.rst').read(),
    version='1.1.0',
    author=open('AUTHORS.rst').read(),
    author_email='opensource@waveaccounting.com',
    url='https://github.com/waveaccounting/vero-python',
    packages=packages,
    package_data={'': ['LICENSE.rst', 'AUTHORS.rst', 'README.rst']},
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
    license=open('LICENSE.rst').read(),
)
