import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "pyobd",
	version = "0.0.4",
	author = "Souvik Banerjee",
	author_email = "souvik@souvik.me",
	description = ("An OBD-II compliant car diagnostic tool library"),
	license = "GPL",
	keywords = "OBD-II library",
	url = "https://souvik.me/cgit/pyobd",
	packages=['pyobd'],
	install_requires=['serial'],
	long_description=read('README'),
)