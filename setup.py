try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A minesweeper clone for the terminal',
    'author': '4Evergreen4',
    'url': 'https://github.com/4Evergreen4/nsweeper',
    'download_url': 'https://github.com/4Evergreen4/nsweeper/archive/master.zip',
    'author_email': 'email',
    'version': '0.1',
    'install_requires': [],
    'packages': ['game'],
    'scripts': [],
    'name': 'nsweeper'
}

setup(**config)
