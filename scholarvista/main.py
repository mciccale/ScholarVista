import os
from keyword_cloud import KeywordCloud
from tei_xml_parser import TeiXmlParser
from plotter import Plotter
from utils import get_project_root

"""
This script demonstrates how to use the TeiXmlParser class to parse TEI XML files, the KeywordCloud class to generate and display word clouds from the abstracts of the parsed documents
and the Plotter class to plot a histogram for the figures count of each paper in the parsed data.
"""


def get_xml_files() -> list[str]:
    """
    Returns a list of the paths of all the TEI XML files in the xmls directory.
    """
    xmls_dir = f'{get_project_root()}/xmls'
    return [f'{xmls_dir}/{file}' for file in os.listdir(xmls_dir) if file.endswith('.tei.xml')]


def parse_all_xmls() -> dict[str, dict[str, str | int]]:
    """
    Parses all the TEI XML files in the xmls directory and returns a dictionary containing the parsed data.
    """
    xml_files = get_xml_files()
    parsed_data = {}
    for xml_file in xml_files:
        print(f'Parsing {xml_file}...')
        parser = TeiXmlParser(file_path=xml_file)

        parsed_data[parser.get_title()] = {
            'abstract': parser.get_abstract(),
            'figures_count': parser.get_figures_count(),
            'links': parser.get_links()
        }
    return parsed_data


def generate_word_clouds(parsed_data: dict[str, dict[str, str | int]]) -> None:
    """
    Generates and displays a word cloud for each abstract in the parsed data.
    """
    for title, data in parsed_data.items():
        KeywordCloud(text=data['abstract'], title=title).generate().display()


def plot_figures_histogram(parsed_data: dict[str, dict[str, str | int]]) -> None:
    """
    Plots a histogram for the figures count of each paper in the parsed data.
    """
    figures_counts = [data['figures_count']
                      for data in list(parsed_data.values())]
    Plotter(x=range(0, len(figures_counts)), y=figures_counts).plot_histogram()


def main():
    parsed_data = parse_all_xmls()
    generate_word_clouds(parsed_data)
    plot_figures_histogram(parsed_data)


if __name__ == '__main__':
    main()
