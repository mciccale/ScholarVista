from grobid_client.grobid_client import GrobidClient

"""
This file contains the PDFParser class, which is used to process PDFs using Grobid.
"""

class PDFParser:
    def __init__(self, port: int=8070) -> None:
        """
        Initializes the PDFParser object by creating a Grobid Client.
        """
        self.grobid_client = GrobidClient(grobid_server=f'https://localhost:{port}')

    def process_pdfs(self, pdf_dir: str, output_dir: str) -> None:
        """
        Processes all the PDFs contained in the `pdf_dir` directory and
        leaves the results in the `output_dir` directory.
        """
        self.grobid_client.process(service='processFulltextDocument',
                                   input_path=pdf_dir,
                                   output=output_dir)
