# Installation Instructions

To install **ScholarVista** you have 2 of the following options:

1. Install de python package in your system. This option is the most complete one, because the package exposes a CLI with a series of python modules so you can use the functionality programmaticaly.

2. Build a Docker Image. This option only lets you run the CLI but there is no need for installing the package in your system.

## From Source

### Prerequisites

**ScholarVista** needs 

To install **ScholarVista** from source, you can clone the repository and install the package using **_pip_** in a clean environment.

```bash
git clone https://github.com/mciccale/ScholarVista
cd ScholarVista
pip install .
```

When using **_pip_** it is a good practice to use virtual environments. Check out the official documentation on virtual envornments [here](https://docs.python.org/3/library/venv.html).

## Docker Container

If you prefer running **ScholarVista** from a Docker Container, you can build the Docker Image with the following commands.

```bash
git clone https://github.com/mciccale/ScholarVista
cd ScholarVista
docker build -t scholarvista-app .
```

This will create a Docker Image called **scholarvista-app**. You're free of choosing the name you want for your image.

