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
    dependency_links=[
      'git+https://github.com/kermitt2/grobid_client_python.git#egg=grobid_client_python'
    ],
    entry_points={
        'console_scripts': [
            'scholarvista = cli.cli:main',
        ],
    }
)
