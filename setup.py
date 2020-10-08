'''
MDSANIMA
'''

import sys
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""==========================
Unsupported Python Version
==========================
This version of MDSANIMA requires Python {}.{}
but you're trying to install it on Python {}.{}
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

VERSION = '0.1.0'
PACKAGE_NAME = 'mdsanima'
AUTHOR = 'Marcin Rozewski'
AUTHOR_EMAIL = 'marcinrozewski@gmail.com'
URL = 'https://github.com/mdsanima/mdsanima'

LICENSE = 'MIT License'
DESCRIPTION = 'The package contains modules that will help in calculating rendering time.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'humanfriendly'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )