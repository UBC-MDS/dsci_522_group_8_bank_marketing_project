import pandas as pd
from IPython.display import display

def get_uniques(df):
    """
    Extracts unique values for selected columns in a DataFrame, considering them as categorical if the ratio of their unique values to the total number of columns is less than or equal to 0.1.

    Parameters:
    - df (pd.DataFrame): The input DataFrame 

    Returns:
    - dict: A dictionary where keys are column names, and values are Pandas Series containing unique values for columns identified as categorical.

    """
    unique_values_dict = {}

    for col in df.columns:
        if len(df[col].unique()) / df.shape[0] <= 0.1:
            unique_values = pd.Series(df[col].unique()).sort_index()
            unique_values_dict[col] = unique_values

    return unique_values_dict