# -*- coding: utf-8 -*-
import sys
from os import path
from setuptools import setup, find_packages, Extension

NAME = "Rider"
DESCRIPTION = "Python Web Application Framework"
AUTHOR = "Jan Češpivo (http://www.cespivo.cz/)"
AUTHOR_EMAIL = "jan.cespivo@gmail.com"
URL = "http://www.riderframework.com/"
VERSION = '0.1.4a'
REQUIRES = ['falcon', 'six']

PYPY = True
CYTHON = False
try:
    sys.pypy_version_info
except AttributeError:
    PYPY = False

if not PYPY:
    try:
        from Cython.Distutils import build_ext
        CYTHON = True
    except ImportError:
        print('\nWARNING: Cython not installed. '
              'Rider will still work fine, but may run '
              'a bit slower.\n')
        CYTHON = False

if CYTHON:
    ext_names = (
        'routes',
        'api_helpers',
        'http',
        'exceptions',
        'views'
    )

    cmdclass = {'build_ext': build_ext}
    ext_modules = [
        Extension('rider.' + ext, [path.join('rider', ext + '.py')])
        for ext in ext_names]
else:
    cmdclass = {}
    ext_modules = []

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache 2.0",
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=REQUIRES,
    cmdclass=cmdclass,
    ext_modules=ext_modules
)
