#!/usr/bin/python3

from rjgtoys.projects import setup


setup(
    name = "rjgtoys.readthedocs",
    version = "0.0.1",
    author = "Bob Gautier",
    author_email = "bob.gautier@gmail.com",
    url = "https://github.com/bobgautier/rjgtoys-readthedocs",
    description = ("Parent project for rjgtoys on readthedocs"),
    namespace_packages=['rjgtoys'],
    packages = ['rjgtoys'],
)
