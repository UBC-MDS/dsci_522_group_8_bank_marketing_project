# EDA.py
# author: Sid Grover
# date: 2023-11-29

import click
import pandas as pd
import altair as alt
import os
from IPython.display import display

@click.command()
@click.option('--data-frame', type=str, help="path to df")
@click.option('--plot-to', type=str, help="path to dir with eda plots)

def main(dataframe, plot_to):

    """
    Perform exploratory data analysis (EDA) by displaying information, descriptive statistics, the first 5 rows, and the last 5 rows of the given DataFrame.

    Parameters:
    - data: The input df for exploratory data analysis.

    Returns:None
    """

    #READ THE DATA
    data = pd.read_csv(dataframe)

    #DEFINE COLUMN TYPES
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns.to_list()
categorical_cols = ["job", "marital", "education", "default", "housing", "loan", "poutcome"]
    numerical_cols = numeric_cols
    
    print("DataFrame Information:")
    display(pd.DataFrame(data.info()))

    print("\nDescriptive Statistics:")
    display(pd.DataFrame(data.describe()).T)

    print("\nFirst 5 Rows:")
    display(data.head(5))

    print("\nLast 5 Rows:")
    display(data.tail(5))

