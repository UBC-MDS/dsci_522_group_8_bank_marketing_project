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
@click.option('--plot-to', type=str, help="path to dir with eda plots")

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

    """
    Generate Exploratory Data Analysis (EDA) plots for visualizing both categorical and
    numerical features in the given df.

    Parameters:
    - data (DataFrame): The input DataFrame containing the data for analysis.
    - numeric_cols (list): List of numerical columns for EDA plots.
    - categorical_cols (list): List of categorical columns for EDA plots.
      Default for numeric_cols or categorical_cols is an empty list.

    Returns:
    - Two plots: The first element is the Altair chart for categorical features, 
    and the second element is the Altair chart for numerical features.
    """
    
    if len(categorical_cols) != 0:
        categorical_plot = (
            alt.Chart(data)
            .mark_bar(opacity=0.9)
            .encode(
                y=alt.Y(alt.repeat()).type("nominal").sort("-x"),
                x=alt.X("count()", title="Count").stack(False),
            )
            .repeat(categorical_cols, columns=2)
        )

    if len(numeric_cols) != 0:
        numeric_plot = (
            alt.Chart(data)
            .mark_bar(opacity=0.9)
            .encode(
                y=alt.Y(alt.repeat()).type("quantitative").bin(maxbins=25).sort("-x"),
                x=alt.X("count()", title = "Count").stack(False),
            )
            .repeat(numeric_cols, columns=2)
        )
    #SAVE PLOTS AS .PNG
    categorical_plot.save(os.path.join(plot_to, "categorical_dist_by_feat.png", format='png'))
    numerical_plot.save(os.path.join(plot_to, "numerical_dist_by_feat.png", format='png'))

    numerical_data = data[numerical_cols]
    
    correlation_matrix = numerical_data.corr(method="spearman")
    styled_correlation_matrix = correlation_matrix.style.background_gradient()
    styled_correlation_matrix.save(os.path.join(plot_to, "corr_matx.png", format='png'))
