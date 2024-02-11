import logging
import xml.etree.ElementTree as ET
from utils import get_links_from_text

"""
This file contains the TeiXmlParser class, which is used to parse TEI XML files.

The TeiXmlParser class provides methods to extract information from TEI XML files, such as the title, abstract, body text,
figures count, and links.
"""

logging.basicConfig(filename='logs/error.log', level=logging.ERROR)


class TeiXmlParser:
    def __init__(self, file_path: str) -> None:
        """
        Initializes the TeiXmlParser object with the given file path.
        """
        try:
            self.file_path = file_path
            self.namespace = 'http://www.tei-c.org/ns/1.0'
            self.root = ET.parse(self.file_path).getroot()
            self.body = self.__find_element_by_tag('body')
        except FileNotFoundError as e:
            logging.error(f"File not found: {file_path}")
            raise e
        except ET.ParseError as e:
            logging.error(f"Error parsing XML file: {file_path}")
            raise e

    def get_title(self) -> str:
        """
        Returns the text of the title of the document.
        """
        return self.__find_element_by_tag('title').text

    def get_abstract(self) -> str:
        """
        Returns the text of the abstract of the document.
        """
        return self.__find_element_by_tag('abstract')[0][0].text

    def get_body(self) -> str:
        """
        Returns the text of the body of the document.
        """
        try:
            body_text = ''
            for paragraph in self.body.iter(self.__wrap_tag_with_namespace('p')):
                if paragraph.text is not None:
                    body_text += (paragraph.text + ' ')
            return body_text
        except AttributeError as e:
            logging.error("Invalid XML structure: missing body element")
            raise e

    def get_figures_count(self) -> int:
        """
        Returns the number of figures in the document.
        """
        try:
            return len(list(self.body.iter(self.__wrap_tag_with_namespace('figure'))))
        except AttributeError as e:
            logging.error("Invalid XML structure: missing body element")
            raise e

    def get_links(self) -> list[str]:
        """
        Returns a list of links found in the document.
        """
        try:
            links = []
            for elem in self.root.iter():
                if elem.text is None:
                    continue
                links.extend(get_links_from_text(elem.text))
            return links
        except Exception as e:
            logging.error("Error occurred while extracting links")
            raise e

    def __find_element_by_tag(self, tag: str) -> ET.Element:
        """
        Returns the first element with the given tag in the document.
        """
        for elem in self.root.iter(self.__wrap_tag_with_namespace(tag)):
            return elem

    def __wrap_tag_with_namespace(self, tag: str) -> str:
        """
        Wraps the given tag with the TEI namespace.
        """
        return '{' + self.namespace + '}' + tag
