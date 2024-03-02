"""
Unit tests for the PDFParser class.
"""

import unittest
from unittest.mock import patch, MagicMock
from scholarvista.pdf_parser import PDFParser


class PDFParserTestCase(unittest.TestCase):
    """
    Unit tests for the PDFParser class.
    """

    @patch('scholarvista.pdf_parser.GrobidClient')
    def test_init(self, mock_grobid_client):
        """
        Tests the initialization of the PDFParser object.
        """
        parser = PDFParser()
        mock_grobid_client.assert_called_with(grobid_server='http://localhost:8070',
                                              timeout=360)
        self.assertIsNotNone(parser.grobid_client)

    @patch('scholarvista.pdf_parser.GrobidClient')
    def test_init_connection_refused(self, mock_grobid_client):
        """
        Tests the initialization of the PDFParser object when the Grobid server is not running.
        """
        mock_grobid_client.side_effect = ConnectionRefusedError
        with self.assertRaises(ConnectionRefusedError):
            PDFParser()

    @patch('scholarvista.pdf_parser.GrobidClient')
    # pylint: disable=unused-argument
    # The mock_grobid_client argument is not used in the test.
    def test_process_pdfs(self, mock_grobid_client):
        """
        Tests the process_pdfs method of the PDFParser class.
        """
        parser = PDFParser()
        parser.grobid_client.process = MagicMock()
        pdf_dir = '/path/to/pdf/dir'
        output_dir = '/path/to/output/dir'
        parser.process_pdfs(pdf_dir, output_dir)
        parser.grobid_client.process.assert_called_with(service='processFulltextDocument',
                                                        input_path=pdf_dir,
                                                        output=output_dir)


if __name__ == '__main__':
    unittest.main()
