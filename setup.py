import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "xzntter09",
    version = "0.0.1",
    author = "dntfury",
    author_email = "#",
    description = ("fastapi stream video with OpenCV"
                                   "video Web"),
    license = "Apache License 2.0",
    keywords = "async applcation zzy",
    url = "#",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 -Planning ",
        "Topic :: Tool Platform",
        "License :: Apache License 2.0",
    ],
)