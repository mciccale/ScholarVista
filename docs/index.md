# ScholarVista

**ScholarVista** is a tool that extracts and plots information from a set of Academic Research Papers in PDF / TEI XML format. To process PDFs, it utilizes [Grobid](https://github.com/kermitt2/grobid/) to generate the TEI XML files, then **ScholarVista** extracts the relevant information from the TEI XML files and generates the following data:

1. **Keyword Cloud** for each of the paper's abstract and for the total of all abstracts.
2. **Links List** for each one of the links found in the paper.
3. **Figures Histogram** comparing the number of figures per paper.

