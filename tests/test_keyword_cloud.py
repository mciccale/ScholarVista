"""
This module contains unit tests for the KeywordCloud class in the scholarvista.keyword_cloud module.
"""

from unittest import main, TestCase
from unittest.mock import patch
from scholarvista.keyword_cloud import KeywordCloud


class KeywordCloudTestCase(TestCase):
    """
    Unit tests for the KeywordCloud class.
    """

    def setUp(self):
        """
        Initializes the KeywordCloud object with some test data.
        """
        self.text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        self.title = "Test Cloud"
        self.keyword_cloud = KeywordCloud(self.text, self.title)

    def test_generate(self):
        """
        Tests the generate method of the KeywordCloud class.
        """
        self.keyword_cloud.generate()
        self.assertIsNotNone(self.keyword_cloud.word_cloud)

    def test_display(self):
        """
        Tests the display method of the KeywordCloud class.
        """
        with patch("matplotlib.pyplot.show") as mock_show:
            self.keyword_cloud.word_cloud = "mock_word_cloud"
            self.keyword_cloud.display()
            mock_show.assert_called_once()

    def test_save_to_file(self):
        """
        Tests the save_to_file method of the KeywordCloud class.
        """
        with patch("matplotlib.pyplot.savefig") as mock_savefig, \
                patch("matplotlib.pyplot.close") as mock_close:
            self.keyword_cloud.word_cloud = "mock_word_cloud"
            self.keyword_cloud.save_to_file("/path/to/directory")
            mock_savefig.assert_called_once_with(
                "/path/to/directory/Test Cloud.png")
            mock_close.assert_called_once()

    def test_save_to_file_no_word_cloud(self):
        """
        Tests the save_to_file method of the KeywordCloud class when
        no word cloud has been generated.
        """
        with self.assertRaises(ValueError):
            self.keyword_cloud.save_to_file("/path/to/directory")


if __name__ == "__main__":
    main()
