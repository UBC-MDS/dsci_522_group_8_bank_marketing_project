import pytest
import sys
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.preprocessor import preprocess_data 

data = {
        "age": np.random.randint(18, 65, size=100),
        "balance": np.random.randint(0, 10000, size=100),
        "education": np.random.choice(["High School", "Bachelor's", "Master's"], size=100),
        "default": np.random.choice([0, 1], size=100),
        "target": np.random.choice([0, 1], size=100)
    }

df = pd.DataFrame(data)

# Split the data into train and test sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Define feature lists
numerical_features = ["age", "balance"]
categorical_features = ["education", "default"]
drop_features = []
target = "target"

# Test Case 1: Check if the type of returned values are pandas dataframes
def test_preprocessor_returns_dataframe():
    X_train_enc, X_train, y_train, X_test, y_test = preprocess_data(train_df, test_df, numerical_features, categorical_features, drop_features, target)
    assert isinstance(X_train_enc, pd.DataFrame)
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(y_train, pd.Series) 
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_test, pd.Series)

# Test Case 2: Check if the returned DataFrames have the correct shapes
def test_preprocess_data_shape():

    # Preprocess the data
    X_train_enc, X_train, y_train, X_test, y_test = preprocess_data(train_df, test_df, numerical_features, categorical_features, drop_features, target)

    # Check if the shapes match
    assert X_train_enc.shape == (80, 6)  # Check the shape of the preprocessed training data
    assert X_train.shape == (80, 4)       # Check the shape of the training data
    assert y_train.shape == (80,)         # Check the shape of the training labels
    assert X_test.shape == (20, 4)        # Check the shape of the testing data
    assert y_test.shape == (20,)          # Check the shape of the testing labels

# Test Case 3: Test for correct error handling for incorrect type of function parameters
def test_preprocessor_type_error():
    with pytest.raises(TypeError):
        preprocess_data(train_df, test_df, "age", categorical_features, drop_features, target)
    with pytest.raises(TypeError):
        preprocess_data(train_df, test_df, numerical_features, "education", drop_features, target)
    with pytest.raises(TypeError):
        preprocess_data(train_df, test_df, numerical_features, categorical_features, "null", target)
    with pytest.raises(TypeError):
        preprocess_data(train_df, test_df, numerical_features, categorical_features, drop_features, 3)

    


