[![Documentation Status](https://readthedocs.org/projects/scholarvista/badge/?version=latest)](https://scholarvista.readthedocs.io/en/latest/?badge=latest)
[![zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.10654761.svg)](https://zenodo.org/doi/10.5281/zenodo.10654760)
![test workflow](https://github.com/mciccale/ScholarVista/actions/workflows/test.yml/badge.svg)
![lint workflow](https://github.com/mciccale/ScholarVista/actions/workflows/lint.yml/badge.svg)

# ScholarVista

**ScholarVista** is a tool that extracts and plots information from a set of Academic Research Papers in PDF / TEI XML format. To process PDFs, it utilizes [Grobid](https://github.com/kermitt2/grobid/) to generate the TEI XML files, then **ScholarVista** extracts the relevant information from the TEI XML files and generates the following data:

1. **Keyword Cloud** for each of the paper's abstract and for the total of all abstracts.
2. **Links List** for each one of the links found in the paper.
3. **Figures Histogram** comparing the number of figures per paper.

## Table of Contents:

- [Requirements](#requirements)
- [Install ScholarVista](#install-scholarvista)
- [Execution Instructions](#execution-instructions)
- [License](#license)
- [Where to Get Help](#where-to-get-help)

## Requirements

If you want to generate the results from a set of PDF academic papers, you must ensure that the **Grobid Service** is installed and running in your machine. See Grobid installation instrucions [here](https://grobid.readthedocs.io/en/latest/Run-Grobid/).

The most straight-forward way of starting and running **Grobid Service** is by running a _Docker_ image. Make sure you have _Docker_ installed in your system.

```bash
docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
```

This command will run **Grobid** and expose a web client in port 8070.

If you already have the TEI XML files generated from Grobid saved in a folder, you can directly generate the information from them.

_Note: The TEI XML files **MUST** be obtained using Grobid, as this tool is intended to work only with Grobid generated TEI XML files._


## Install ScholarVista

### From Source

To install **ScholarVista** from source, you can clone the repository and install the package using **_pip_**.

```bash
git clone https://github.com/mciccale/ScholarVista
cd ScholarVista
pip install .
```

When using **_pip_** it is a good practice to use virtual environments. Check out the official documentation on virtual envornments [here](https://docs.python.org/3/library/venv.html).

### Docker Container

If you prefer running **ScholarVista** from a Docker Container, you can build the Docker Image with the following commands.

```bash
git clone https://github.com/mciccale/ScholarVista
cd ScholarVista
docker build -t scholarvista-app .
```

This will create an image called **scholarvista-app**.

 
## Execution Instructions

### From Source

#### CLI Tool

The most convenient way of using **ScholarVista** is by using its CLI.

The CLI Tool will generate and save to a directory a **keyword cloud** of the abstract of each paper and a **list of URLs** for each PDF analyzed; together with a **histogram** comparing the numer of figures of each PDF and a general **keyword cloud** of all abstracts.

```
Usage: scholarvista [OPTIONS] COMMAND [ARGS]...

  ScholarVista's CLI main entry point.

Options:
  --input-dir PATH   Directory containing PDF files.  [required]
  --output-dir PATH  Directory to save results. Defaults to current directory.
  --help             Show this message and exit.

Commands:
  process-pdfs  Process all PDFs in the given directory.
  process-xmls  Process all TEI XMLs in the given directory.
```

##### Example

You can execute **ScholarVista CLI** from your shell like this:

```bash
# Process PDF files and save the results to a specified directory
scholarvista --input-dir ./pdfs --output-dir ./output process-pdfs
```

_Note: The `process-pdfs` command requires the Grobid Service to be up and running as described in [requirements](#requirements)._

```bash
# Process TEI XML files and save the results to the current directory
scholarvista --input-dir ./xmls process-xmls
```

#### Python Modules

**ScholarVista** provides a set of classes and modules to take leverage of all its functionality from your Python code. To see an example, see `example.py`

### Docker Container

If you prefer running **ScholarVista** with Docker, you can make use of **ScholarVista** CLI directly from the Docker Image you created following [these instructions](#docker-container).

1. Create a Docker Network so **ScholarVista** and **Grobid** containers can communicate between each other.

```bash
docker network create --driver bridge foo-net
```

2. Start **Grobid** service using the container and connect it to the network.

```bash
docker run --rm --init --ulimit core=0 -p 8070:8070 --network foo-net lfoppiano/grobid:0.8.0
```

3. Run **ScholarVista's** container with 2 mounted volumes for input and output directories and connect to the network.

```bash
docker run --rm -v /path/to/input/dir:/input -v /path/to/output/dir:/output --network foo-net scholarvista-app
```

*Note: The default behaviour of ScholarVista's Docker Image is processing pdf files, you can override this by providing the `process-xmls` argument after the image name.* 


## License

Please refer to the `LICENSE` file.

## Where to Get Help

For further assistance or to contribute to the project, please refer to the `CONTRIBUTING.md` file.
