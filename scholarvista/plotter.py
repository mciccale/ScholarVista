import matplotlib.pyplot as plt

"""
This module contains the Plotter class which is used to plot a histogram of the given data.
"""


class Plotter:
    def __init__(self, x, y) -> None:
        """
        Initializes the Plotter object with the given data.
        """
        self.x = x
        self.y = y

    def plot_histogram(self):
        """
        Plots a histogram of the given data.
        """
        plt.bar(self.x, self.y)
        plt.xlabel('Articles')
        plt.ylabel('Figures')
        plt.title('Figures per Article')
        plt.show()
