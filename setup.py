#!/usr/bin/env python

# ...

from distutils.core import setup
from w3 import __version__

setup(name='w3.py',
      version=__version__,
      description='w3.py: makes web apps',
      author='Aaron Swartz',
      author_email='me@aaronsw.com',
      maintainer='Alexander Demsky',
      maintainer_email='a@demsky.ru',
      url=' http://webpy.org/',
      packages=['w3', 'w3.wsgiserver', 'w3.contrib'],
      long_description="Think about the ideal way to write a web app. Write the code to make it happen.",
      license="Public domain",
      platforms=["any"],
     )
