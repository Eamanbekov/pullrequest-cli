from os.path import abspath, dirname, join
from setuptools import find_packages, setup
from src import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

# Actual setup with handling import errors
try:
    setup(
        name='pullrequest-cli',
        python_requires='>=3.6.2',
        version=__version__,
        description='A command line program to get bitbucket pullrequests',
        long_description=long_description,
        author='Emir Amanbekov',
        author_email='amanbekoff@gmail.com',
        url='https://bitbucket.org/bookinman/pullrequest-cli',
        license='UNLICENSE',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'pullrequest-cli=src.cli:main',
            ],
        },
    )
except ImportError as e:
    print(e)
