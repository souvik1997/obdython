from setuptools import setup

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
	install_requires=['pyserial', 'pybluez'],
)