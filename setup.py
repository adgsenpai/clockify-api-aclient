from setuptools import setup, find_packages
import re
import ast

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('clockify_api_client_adgstudios/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='clockify-api-client-adgstudios',
    version=version,
    author="Michael Bláha, Ashlin Darius Govindasamy",
    author_email="michael.blaha@eluvia.com, adg@adgstudios.co.za",
    description="Simple python API client for clockify. Inspired by https://pypi.org/project/clockify/library.",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eluvia-com/clockify-api-aclient",
    install_requires=['requests', 'factory_boy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={"dev": ["twine"]}
)
