import logging
import re
from pathlib import Path

"""
This file contains utility functions that are used across the application.
"""

logging.basicConfig(level=logging.ERROR)


def get_project_root() -> str:
    """
    Returns the root path of the project.
    """
    try:
        return str(Path(__file__).parent.parent)
    except Exception as e:
        logging.error(f"An error occurred in get_project_root(): {str(e)}")
        return ""


def get_links_from_text(text: str) -> list[str]:
    """
    Returns a list of links found in the given text.
    """
    try:
        link_regex = r'((http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))'
        matches = re.findall(link_regex, text)
        return [match[0] for match in matches]
    except Exception as e:
        logging.error(f"An error occurred in get_links_from_text(): {str(e)}")
        return []
