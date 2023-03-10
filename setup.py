"""Setup for wheel distribution. We only use this for colab. For everything else we use conda."""

import os
import setuptools

from setuptools import setup
requirements = []

setup(
    name='luenn',
    version='0.10.02',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    license='UB',
    author='Armin Abdehkakha',
    author_email='arminabd@buffalo.edu',
    description=''
)