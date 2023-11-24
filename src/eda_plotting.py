## EDA Plotting Functions
import altair as alt
import altair_viewer
import pandas as pd
from IPython.display import display

alt.data_transformers.enable("vegafusion")

def text_EDA(data):
    """
    Perform exploratory data analysis (EDA) by displaying information, descriptive statistics, the first 5 rows, and the last 5 rows of the given DataFrame.

    Parameters:
    - data: The input df for exploratory data analysis.

    Returns:None
    """
    print("DataFrame Information:")
    display(pd.DataFrame(data.info()))

    print("\nDescriptive Statistics:")
    display(pd.DataFrame(data.describe()).T)

    print("\nFirst 5 Rows:")
    display(data.head(5))

    print("\nLast 5 Rows:")
    display(data.tail(5))

def EDA_plot(data, numeric_cols=[], categorical_cols=[]):
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

    return display(categorical_plot), display(numeric_plot)


def spearman_correlation_matrix(data, numerical_cols):
    """
    Generate a Spearman correlation matrix for numerical columns in the df.

    Parameters:
    - data (DataFrame): The input df containing the data for correlation analysis.
    - numerical_cols: List of numerical column names for which the correlation matrix is calculated.

    Returns:
    - A styled representation of the Spearman correlation matrix, with a background gradient for a better visual experience.
    """
    numerical_data = data[numerical_cols]
    
    correlation_matrix = numerical_data.corr(method="spearman")
    styled_correlation_matrix = correlation_matrix.style.background_gradient()
    
    return styled_correlation_matrix
