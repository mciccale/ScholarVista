"""
Unit tests for the Plotter class.
"""

import unittest
from unittest.mock import patch
from scholarvista.plotter import Plotter


class PlotterTestCase(unittest.TestCase):
    """
    Unit tests for the Plotter class.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.title = 'Histogram'
        self.x_label = 'X'
        self.x_data = [1, 2, 3, 4, 5]
        self.y_label = 'Y'
        self.y_data = [10, 20, 30, 40, 50]
        self.plotter = Plotter(self.title, self.x_label,
                               self.x_data, self.y_label, self.y_data)

    def test_generate(self):
        """
        Test the generate method.
        """
        self.plotter.generate()
        self.assertTrue(self.plotter.figure_created)

    @patch('scholarvista.plotter.plt.show')
    def test_display(self, mock_show):
        """
        Test the display method.
        """
        self.plotter.figure_created = True
        self.plotter.display()
        mock_show.assert_called_once()

    @patch('scholarvista.plotter.plt.savefig')
    @patch('scholarvista.plotter.plt.close')
    def test_save_to_file(self, mock_savefig, mock_close):
        """
        Test the save_to_file method.
        """
        self.plotter.figure_created = True
        dir_path = '/path/to/directory'
        self.plotter.save_to_file(dir_path)
        mock_savefig.assert_called_once()
        mock_close.assert_called_once()

    def test_display_without_figure(self):
        """
        Test the display method when no figure is generated.
        """
        with patch('scholarvista.plotter.logging.error') as mock_error:
            self.plotter.display()
            mock_error.assert_called_once()

    def test_save_to_file_without_figure(self):
        """
        Test the save_to_file method when no figure is generated.
        """
        with patch('scholarvista.plotter.logging.error') as mock_error:
            dir_path = '/path/to/directory'
            self.plotter.save_to_file(dir_path)
            mock_error.assert_called_once()


if __name__ == '__main__':
    unittest.main()
