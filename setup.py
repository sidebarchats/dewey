#/usr/bin/env python
import os
from setuptools import setup, find_packages
from dewey import VERSION

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="dewey",
    description="A helpful CLI friend",
    author="Steven Skoczen",
    author_email="skoczen@gmail.com",
    url="https://github.com/sidebarchats/dewey",
    version=VERSION,
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    entry_points = {
        "console_scripts": [
            "hey_dewey = dewey.hey_dewey:main",
        ],
    },
)