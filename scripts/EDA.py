# EDA.py
# author: Sid Grover
# date: 2023-11-29

import click
import pandas as pd
import altair as alt
import os
import sys
from IPython.display import display

@click.command()
@click.option('--data_frame', type=str, help="path to df")
@click.option('--plot_to', type=str, help="path to dir with eda plots")

def main(data_frame, plot_to):
    # Read the data
    data = pd.read_csv(data_frame, delimiter=";")

    # Define numerical and categorical columns
    numerical_cols = ["age", "balance", "duration", "campaign", "pdays", "previous"]
    categorical_cols = ["job", "marital", "education", "default", "housing", "loan", "poutcome"]

    # Create histograms for numerical columns
    numerical_plot = (
        alt.Chart(data)
        .mark_bar(opacity=0.5)
        .encode(
            x=alt.X(alt.repeat(), type="quantitative", bin=True),
            y=alt.Y("count()", title="Count"),
            color=alt.Color("y:N", title="Target")
        ).properties(
            width=300,
            height=200)
        .repeat(numerical_cols, columns=2)
    )
    numerical_plot.save(os.path.join(plot_to, "numerical_dist_by_feat.png"))

    # Create histograms for categorical columns
    categorical_plot = (
        alt.Chart(data)
        .mark_bar(opacity=0.5)
        .encode(
            x=alt.X(alt.repeat(), type="nominal"),
            y=alt.Y("count()", title="Count"),
            color=alt.Color("y:N", title="Target")
        ).properties(
            width=300,
            height=200)
        .repeat(categorical_cols, columns=2)
    )
    categorical_plot.save(os.path.join(plot_to, "categorical_dist_by_feat.png"))

    # Correlation matrix for numerical columns
    numerical_data = data[numerical_cols]
    corr_matrix = numerical_data.corr().reset_index().melt('index')
    corr_matrix.columns = ['x', 'y', 'value']

    # Create a heatmap using Altair
    heatmap = alt.Chart(corr_matrix).mark_rect().encode(
        x='x:N',
        y='y:N',
        color='value:Q'
    ).properties(
        title='Correlation Matrix',
        width=300,
        height=300
    )

    heatmap.save(os.path.join(plot_to, 'corr_matx.png'))

if __name__ == '__main__':
    main()