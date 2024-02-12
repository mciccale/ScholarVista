#!/usr/bin/env python3

import click
import os
import scholarvista as sv
from tempfile import TemporaryDirectory


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
    tei_xml_dir = TemporaryDirectory().name

    print(f'> Processing all PDFs in {pdf_dir}...')

    sv.PDFParser().process_pdfs(pdf_dir=pdf_dir, output_dir=tei_xml_dir)

    parsed_data = __parse_all_xmls(__get_tei_xml_files_from_dir(tei_xml_dir=tei_xml_dir))

    if save and output_dir:
        if not os.path.exists(output_dir):
            click.echo(f"Output directory '{output_dir}' does not exist.")
            return
    elif save:
        output_dir = os.getcwd()

    __generate_word_clouds(parsed_data, output_dir)
    __generate_figures_histogram(parsed_data, output_dir)


def __get_tei_xml_files_from_dir(tei_xml_dir: str) -> list[str]:
    """
    Returns a list of the paths of all the TEI XML files in the xmls directory.
    """
    return [f'{tei_xml_dir}/{file}' for file in os.listdir(tei_xml_dir) if file.endswith('.tei.xml')]


def __parse_all_xmls(tei_xml_files: list[str]) -> dict[str, dict[str, str | int]]:
    """
    Parses all the TEI XML files in the xmls directory and returns a dictionary containing the parsed data.
    """
    parsed_data = {}
    for tei_xml_file in tei_xml_files:
        print(f' >Parsing TEI XML file {tei_xml_file}...')
        parser = sv.TEIXMLParser(file_path=tei_xml_file)

        parsed_data[parser.get_title()] = {
            'abstract': parser.get_abstract(),
            'figures_count': parser.get_figures_count(),
            'links': parser.get_links()
        }
    return parsed_data


def __generate_word_clouds(parsed_data: dict[str, dict[str, str | int]], output_dir: str | None) -> None:
    """
    Generates and displays a word cloud for each abstract in the parsed data.
    """
    print('> Generating Keyword Clouds...')

    for title, data in parsed_data.items():
        cloud = sv.KeywordCloud(text=str(data['abstract']), title=title).generate()
        if output_dir is None:
            cloud.display()
        else:
            cloud.save_to_file(output_dir)


def __generate_figures_histogram(parsed_data: dict[str, dict[str, str | int]], output_dir: str | None) -> None:
    """
    Plots a histogram for the figures count of each paper in the parsed data.
    """
    print('> Generating a Figures Histogram...')

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
