# Rationale

The purpose of this file is to provide a rationale for the project. It explains the reasons behind the decisions made, the goals and objectives of the project, and the justification for its implementation. The rationale serves as a guide for understanding the project's context and helps understand the architecture / pipeline.

## Grobid

### Description

TODO

### Functionality

TODO

### Usage

TODO

## TeiXmlParser

### Description

The **TeiXmlParser** module is responsible for extracting all the desired information of a **TEI XML** file outputed by **_Grobid_**. It can extract the following information about the papers:

- **Title**
- **Abstract**
- **Body**
- **Links**
- Number of **Figures**

### Functionality

This module searches for specific tags in the **TEI XML** file and iterates through its child obtaining the text within them.

### Usage

Create an instance of the parser:

```py
parser = TeiXmlParser(file_path='/path/to/tei/xml/file')
```

Extract the desired information:

```py
abstract = parser.get_abstract()
body = parser.get_body()
figures_count = parser.get_figures_count()
links = parser.get_links()
title = parser.get_title()
```

## KeywordCloud

### Description

The **KeywordCloud** module is responsible for generating and displaying a keyword cloud from an input text.

### Functionality

This module makes use of the **[WordCloud](https://pypi.org/project/wordcloud/)** package.

### Usage

Create an instance of KeywordCloud with one article's abstract extracted with `TeiXmlParser`:

```py
parser = TeiXmlParser(file_path='/path/to/tei/xml/file')
text = parser.get_abstract()
title = 'Abstract'
keyword_cloud = KeywordCloud(text=text, title=title)
```

Generate and display the figure:

```py
keyword_cloud.generate().display()
```

## Plotter

### Description

The **Plotter** module is responsible for generating and displaying an histogram from two lists of values passed as arguments.

### Functionality

This module makes use of the **[Matplotlib](https://pypi.org/project/matplotlib/)** package.

### Usage

Generate a Plotter that will show the number of figures obtained by the `TeiXmlParser`:

```py
xml_files = ['/path/to/tei/xml/file1', '/path/to/tei/xml/file2']
parsed_data = {}
for xml_file in xml_files:
    parser = TeiXmlParser(file_path=xml_file)
    parsed_data[parser.get_title()] = {
        'abstract': parser.get_abstract(),
        'figures_count': parser.get_figures_count(),
        'links': parser.get_links()
    }

figures_counts = [data['figures_count']
                      for data in list(parsed_data.values())]
figures_per_article_histogram = Plotter(x=range(0, len(figures_counts)), y=figures_counts)
```

Display the figure:

```py
figures_per_article_histogram.plot_histogram()
```
