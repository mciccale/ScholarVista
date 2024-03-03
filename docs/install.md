# Installation Instructions

There are two ways of installing **ScholarVista**:

1. **The Python package**. This option provides all the functionality of **ScholarVista**: a CLI tool and the separate Python modules.

2. **The Docker Image**. This option only lets you run the CLI but there is no need for installing the package in your system.

## From Source

To install **ScholarVista** from source, you can clone the repository and install the package using **_pip_**. When using **_pip_** it is a good practice to use virtual environments. Check out the official documentation on virtual envornments [here](https://docs.python.org/3/library/venv.html).

#### Conda

```bash
git clone https://github.com/mciccale/ScholarVista
cd ScholarVista
conda create -n scholarvista-env-3.12 python=3.12
conda activate scholarvista-env-3.12
pip install .
```

_Note: You can use **PyEnv** to create a virtual environment. But since **ScholarVista** needs Python >=3.12, it is more suitable to use **Conda**, where you can select the **Python** version to use._

## Docker Container

If you prefer running **ScholarVista** from a Docker Container, you can build the Docker Image with the following commands.

```bash
git clone https://github.com/mciccale/ScholarVista
cd ScholarVista
docker build -t scholarvista-app .
```

This will create a Docker Image called **scholarvista-app**. You're free of choosing the name you want for your image.

