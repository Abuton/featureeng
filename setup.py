#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Abubakar Alaro",
    author_email='alaroabubakarolayemi@yahoo.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A bunch of functions to enable and make FE easy when building Machine Learning Models",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='featureeng',
    name='featureeng',
    packages=find_packages(include=['featureeng', 'featureeng.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Abuton/featureeng',
    version='0.1.0',
    zip_safe=False,
)
