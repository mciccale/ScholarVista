"""
Unit tests for the utility functions.
"""

from unittest import TestCase, main
from scholarvista._utils import get_project_root, get_links_from_text


class UtilsTestCase(TestCase):
    """
    Unit tests for the utility functions.
    """

    def test_get_project_root(self):
        """
        Tests the get_project_root function.
        """
        project_root = get_project_root()
        self.assertIsNotNone(project_root)
        self.assertTrue(project_root.endswith("ScholarVista"))

    def test_get_links_from_text(self):
        """
        Tests the get_links_from_text function.
        """
        text = "This is a sample text with a link: https://www.example.com"
        links = get_links_from_text(text)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0], "https://www.example.com")

    def test_get_links_from_text_multiple_links(self):
        """
        Tests the get_links_from_text function with multiple links.
        """
        text = "This is a sample text with multiple links: " \
               "https://www.example.com and http://www.google.com"
        links = get_links_from_text(text)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0], "https://www.example.com")
        self.assertEqual(links[1], "http://www.google.com")

    def test_get_links_from_text_no_links(self):
        """
        Tests the get_links_from_text function when no links are present.
        """
        text = "This is a sample text without any links."
        links = get_links_from_text(text)
        self.assertEqual(len(links), 0)


if __name__ == "__main__":
    main()
