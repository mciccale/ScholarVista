# Usage Instructions

In this section you will find the instructions for using **ScholarVista's** CLI tool and python modules.

You can wether install the tool locally or using the Docker Image previously built.

## From Source

### CLI Tool

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

1. Start **Grobid** service using the container.

```bash
docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
```

2. Run **ScholarVista's** CLI to process all the PDFs in a given directory and leave the results in another directory.

```bash
# Process PDF files and save the results to a specified directory
scholarvista --input-dir ./pdfs --output-dir ./output process-pdfs
```

### Python Modules

**ScholarVista** provides a set of classes and modules to take leverage of all its functionality from your Python code.

#### Example

```python
"""
Example of the usage of the scholarvista package.

It is required to have the Grobid server running to process the PDFs.
"""

import os
from tempfile import TemporaryDirectory
import scholarvista as sv


def main() -> None:
    """
    1. Process a PDF in the `resources` directory
    2. Display a keyword cloud for the abstract
    3. Print the list of links in the document
    """
    # Create a temporary directory to deposit the TEI XML intermediate files
    xml_file_path = None
    with TemporaryDirectory() as tei_xml_dir:
        # Process the PDFs with PDFParser
        sv.PDFParser().process_pdfs(pdf_dir='./resources',
                                    output_dir=tei_xml_dir)

        # Find the .tei.xml file in the temporary directory
        xml_file_path = os.listdir(tei_xml_dir)[0]

    # Create a parser for the document
    parser = sv.TEIXMLParser(file_path=xml_file_path)

    # Obtain the abstract of the document
    abstract, links = parser.get_abstract(), parser.get_links()

    # Draw a keyword cloud for the abstract
    sv.KeywordCloud(text=abstract, title='Abstract').generate().display()

    # Print the list of links in the document
    print(links)


if __name__ == '__main__':
    main()
```

## Docker Container

If you prefer running **ScholarVista** with Docker, you can make use of **ScholarVista** CLI directly from the Docker Image you created following [these instructions](#docker-container).

1. Start **Grobid** service using the container.

```bash
docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
```

2. Run **ScholarVista's** container with 2 mounted volumes for input and output directories and connected to the host network.


```bash
docker run -it --rm --network=host -v /path/to/input/dir:/input -v /path/to/output/dir:/output scholarvista-app
```

*Note: The default behaviour of ScholarVista's Docker Image is processing pdf files, you can override this by providing the `process-xmls` argument after the image name.* 

### Example

Here's an example where we process a set of PDFs contained in the `foo` directory and we leave the results at `bar` using the Docker Image. Assuming the **Grobid** service is running at `localhost:8070`. 

```bash
docker run -it --rm --network=host -v foo:/input -v bar:/output scholarvista-app process-pdfs
```

## Docker Compose (Experimental)

You can try to run **ScholarVista** through **Docker Compose**. However, this feature is still in development and may not work as expected. **ScholarVista** will be trying to connect to **Grobid** before it has started, and it will be restarted until the **Grobid** service is up and running. You can try it by:

### SH-Shell like

```bash
INPUT_DIR=/path/to/input/dir OUTPUT_DIR=/path/to/output/dir COMMAND='process-pdfs' docker-compose up
```

### PowerShell

```powershell
$env:INPUT_DIR="/path/to/input/dir"; $env:OUTPUT_DIR="/path/to/output/dir"; $env:COMMAND="process-pdfs" docker-compose up
```

_Note: The **COMMAND** variable can be either `process-pdfs` or `process-xmls`. And the directories are the host machine directories where the files are extracted and left, respectively._

