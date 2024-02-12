"""
This file is used to install the package using pip.
"""

from setuptools import setup, find_packages

setup(
    name='scholarvista',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click>=8.1.7',
        'matplotlib>=3.8.0',
        'wordcloud>=1.9.2',
        'grobid-client-python>=0.0.8'
    ],
    entry_points={
        'console_scripts': [
            'scholarvista = cli.cli:main',
        ],
    }
)
