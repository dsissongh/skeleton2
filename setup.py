try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setup

config = [
	'description': 'My Project',
	'author': 'David Sisson',
	'url': '',
	'download_url': '',
	'author_email': '',
	'version': '0.1',
	''	
]

setup(**config)