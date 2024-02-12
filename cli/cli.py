#!/usr/bin/env python3

import click
import os
import scholarvista as sv
from scholarvista._utils import get_project_root


@click.command()
@click.option('--pdf-dir',
              required=True,
              type=click.Path(exists=True),
              help='Directory containing PDF files.')
@click.option('--save/--no-save',
              default=False,
              help='Save results to a file. Default is to display results without saving.')
@click.option('--output-dir',
              type=click.Path(),
              help='Directory to save results. Defaults to current directory if --save is provided.')
def main(pdf_dir: str, save: bool, output_dir: str | None):
    # TODO: Call to Grobid Module
    parsed_data = parse_all_xmls()

    if save and output_dir:
        if not os.path.exists(output_dir):
            click.echo(f"Output directory '{output_dir}' does not exist.")
            return
    elif save:
        output_dir = os.getcwd()

    generate_word_clouds(parsed_data, output_dir)
    generate_figures_histogram(parsed_data, output_dir)


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
        parser = sv.TEIXMLParser(file_path=xml_file)

        parsed_data[parser.get_title()] = {
            'abstract': parser.get_abstract(),
            'figures_count': parser.get_figures_count(),
            'links': parser.get_links()
        }
    return parsed_data


def generate_word_clouds(parsed_data: dict[str, dict[str, str | int]], output_dir: str | None) -> None:
    """
    Generates and displays a word cloud for each abstract in the parsed data.
    """
    for title, data in parsed_data.items():
        cloud = sv.KeywordCloud(text=str(data['abstract']), title=title).generate()
        if output_dir is None:
            cloud.display()
        else:
            cloud.save_to_file(output_dir)


def generate_figures_histogram(parsed_data: dict[str, dict[str, str | int]], output_dir: str | None) -> None:
    """
    Plots a histogram for the figures count of each paper in the parsed data.
    """
    figures_counts = [data['figures_count']
                      for data in list(parsed_data.values())]
    histogram = sv.Plotter(title='Figures per Article',
            x_label='Article',
            x_data=range(0, len(figures_counts)),
            y_label='Figures',
            y_data=figures_counts).generate()

    if output_dir is None:
        histogram.display()
    else:
        histogram.save_to_file(output_dir)

if __name__ == '__main__':
    main()
