import logging
import matplotlib.pyplot as plt
from typing import Self
from collections import Counter
from wordcloud import WordCloud

logging.basicConfig(filename='logs/error.log', level=logging.ERROR)


class KeywordCloud:
    def __init__(self, text: str, title: str = None) -> None:
        """
        Initializes the KeywordCloud object with the given text.
        """
        self.title = title
        self.words_freq = Counter(text.split())
        self.word_cloud = None

    def generate(self) -> Self:
        """
        Generates the word cloud from the frequency of words in the text.
        """
        try:
            self.word_cloud = WordCloud(
                width=800, height=400).generate_from_frequencies(self.words_freq)
        except Exception as e:
            logging.error(f"Error generating word cloud: {str(e)}")
        return self

    def display(self) -> None:
        """
        Displays the generated word cloud.
        """
        try:
            if self.word_cloud is None:
                raise ValueError("Word cloud has not been generated yet.")
            plt.figure(figsize=(10, 5))
            plt.imshow(self.word_cloud, interpolation='bilinear')
            plt.axis('off')
            plt.show()
        except Exception as e:
            logging.error(f"Error displaying word cloud: {str(e)}")
