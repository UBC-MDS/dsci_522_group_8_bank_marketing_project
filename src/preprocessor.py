# preprocessor.py
# author: Rachel Li
# date: 2023-11-29

import click
import os
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.preprocessing import StandardScaler, OneHotEncoder

@click.command()
@click.option('--raw_train', type=str, help="Path to train_df")
@click.option('--raw_test', type=str, help="Path to test_df")
@click.option('--numerical features', type=list)
@click.option('--categorical_features', type=list)
@click.option('--categorical_features', type=list)
@click.option('--target', type=str, help="column name the target")
@click.option('--data-to', type=str, help="Path to directory where data will be written to")
@click.option('--preprocessor-to', type=str, help="Path to directory where the preprocessor object will be written to")

def preprocess_data(raw_train, raw_test, numerical_features, categorical_features, drop_features, target, data_to, preprocessor_to):
    """
    Preprocesses the data by applying scaling and one-hot encoding to the specified features.

    Parameters:
    - train_df (pd.DataFrame): The training DataFrame.
    - test_df (pd.DataFrame): The testing DataFrame.
    - numerical_features (list): List of numerical feature names.
    - categorical_features (list): List of categorical feature names.
    - drop_features (list): List of features to be dropped.
    - target (str): The name of the target column.

    Returns:
    - X_train_enc (pd.DataFrame): Preprocessed training data.
    - X_train (pd.DataFrame): Training set after spliting. 
    - y_train (pd.Series): Training labels.
    - X_test (pd.DataFrame): Testing set after spliting.
    - y_test (pd.Series): Testing labels.
    - preprocessor (ColumnTransformer): The fitted column transformer for future transformations.
    """
    
    # Data type validation
    if not isinstance(train_df, pd.DataFrame) or not isinstance(test_df, pd.DataFrame):
        raise TypeError("train_df and test_df must be pandas DataFrames")
    if not isinstance(numerical_features, list):
        raise TypeError("numerical_features must be a list of strings")
    if not isinstance(categorical_features, list):
        raise TypeError("categorical_features must be a list of strings")
    if not isinstance(drop_features, list):
        raise TypeError("drop_features must be a list of strings")
    if not isinstance(target, str):
        raise TypeError("target must be a string")

    # Create the column transformer
    preprocessor = make_column_transformer(    
        (StandardScaler(), numerical_features),  # scaling on numeric features   
        (OneHotEncoder(drop="if_binary"), categorical_features),  # OHE on categorical features
        ("drop", drop_features),# drop the drop features
        verbose_feature_names_out=False
    )

    pickle.dump(preprocessor, open(os.path.join(preprocessor_to, "preprocessor.pickle"), "wb"))
    
    preprocessor.fit(X_train)
    
    # Seperate X and y
    train_df = pd.read_csv(raw_train)
    test_df = pd.read_csv(raw_test)
    X_train = train_df.drop(columns=[target])
    X_test = test_df.drop(columns=[target])
    y_train = train_df[target]
    y_test = test_df[target]

    # Columns names after one hot encoding
    ohe_columns = list(
        preprocessor.named_transformers_["onehotencoder"]
        .get_feature_names_out(categorical_features)
    )

    # Columns after transformation
    new_columns = (
        numerical_features + ohe_columns
    )

    # Now create the DataFrame with the dense data
    X_train_enc = pd.DataFrame(preprocessor.transform(X_train), index=X_train.index, columns=new_columns)

    X_train.to_csv(os.path.join(data_to, "X_train.csv"), index=False)
    y_train.to_csv(os.path.join(data_to, "y_train.csv"), index=False)
    X_test.to_csv(os.path.join(data_to, "X_test.csv"), index=False)
    y_test.to_csv(os.path.join(data_to, "y_test.csv"), index=False)
    X_train_enc.to_csv(os.path.join(data_to, "X_train_enc.csv"), index=False)
    

    if __name__ == '__main__':
        main()