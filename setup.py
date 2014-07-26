try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A minesweeper clone for the terminal',
    'author': 'My Name',
    'url': 'URL',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': [],
    'packages': ['nsweeper'],
    'scripts': [],
    'name': 'nsweeper'
}

setup(**config)
