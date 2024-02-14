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
