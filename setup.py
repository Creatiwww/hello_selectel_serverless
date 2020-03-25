from setuptools import setup
from os import path
here = path.abspath(path.dirname(__file__))

setup(
    name="fun",
    packages=["fun"],
    install_requires=["requests"]
)