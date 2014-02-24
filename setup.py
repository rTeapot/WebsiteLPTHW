try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
	
config = {
    'description': 'gothonweb',
	'author': 'rTeapot',
	'url': 'url where to get this shiz',
	'download_url': 'Where to download it',
	'author_email': 'c10jakejeffcoat@yahoo.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['gothonweb'],
	'scripts': [],
	'name': 'gothonweb'
}

setup(**config)