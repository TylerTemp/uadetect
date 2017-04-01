import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

from uadetect import __version__


setup(
    name='uadetect',
    version=__version__,
    author='TylerTemp',
    author_email='tylertempdev@gmail.com',
    description='A simple User-Agent detect for Chinese UA',
    license='MIT',
    keywords='user-agent',
    url='http://github.com/TylerTemp/',
    py_modules=['uadetect'],
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
)
