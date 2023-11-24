import pytest
import pandas as pd
import altair as alt
import pytest
import sys
import os
from IPython.display import display

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from eda_functions import text_EDA, EDA_plot, spearman_correlation_matrix

""" Test Description

Check if the EDA functions run without errors.
Check if the returned values are of the correct types.
Test for correct error handling for incorrect types of function parameters.

"""

# Sample DataFrame for testing
data = {
    'Numeric1': [12, 23, 34, 45, 54],
    'Numeric2': [5, 4, 3, 2, 1],
    'Category1': ['Abba', 'Baba', 'Abba', 'Baba', 'Abba'],
    'Category2': ['Xoxo', 'Yoyo', 'Xoxo', 'Yoyo', 'Xoxo']
}
test_df = pd.DataFrame(data)

# Test 1: Check if EDA functions run without errors
def test_EDA_functions_run_without_errors():
    try:
        text_EDA(test_df)
        EDA_plot(test_df, numeric_cols=['Numeric1'], categorical_cols=['Category1'])
        spearman_correlation_matrix(test_df, numerical_cols=['Numeric1'])
    except Exception as e:
        pytest.fail(f"Unexpected exception: {str(e)}")

# Test 2: Check if the returned values are of the correct types
def test_EDA_functions_return_correct_types():
    try:
        text_EDA(test_df)
        categorical_plot, numeric_plot = EDA_plot(test_df, numeric_cols=['Numeric1'], categorical_cols=['Category1'])
        styled_correlation_matrix = spearman_correlation_matrix(test_df, numerical_cols=['Numeric1'])

        assert isinstance(categorical_plot, alt.Chart)
        assert isinstance(numeric_plot, alt.Chart)
        assert isinstance(styled_correlation_matrix, pd.io.formats.style.Styler)
    except Exception as e:
        pytest.fail(f"Unexpected exception: {str(e)}")

# Test 3: Test for correct error handling for incorrect type of function parameters
def test_EDA_functions_type_error():
    with pytest.raises(TypeError):
        EDA_plot(test_df, numeric_cols='Numeric1', categorical_cols=['Category1'])
    with pytest.raises(TypeError):
        EDA_plot(test_df, numeric_cols=['Numeric1'], categorical_cols='Category1')
    with pytest.raises(TypeError):
        spearman_correlation_matrix(test_df, numerical_cols='Numeric1')

if __name__ == '__main__':
    pytest.main()
