import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_data(train_df, test_df, numerical_features, categorical_features, drop_features, target):
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
    """

    # Create the column transformer
    preprocessor = make_column_transformer(    
        (StandardScaler(), numerical_features),  # scaling on numeric features   
        (OneHotEncoder(drop="if_binary"), categorical_features),  # OHE on categorical features
        ("drop", drop_features),  # drop the drop features
    )

    # Seperate X and y
    X_train = train_df.drop(columns=[target])
    X_test = test_df.drop(columns=[target])
    y_train = train_df[target]
    y_test = test_df[target]

    # This line nicely formats the feature names from `preprocessor.get_feature_names_out()` so that we can more easily use them below
    preprocessor.verbose_feature_names_out = False

    # Create a dataframe with the transformed features and column names
    ct = preprocessor.fit(X_train)

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
    
    return  X_train_enc, X_train, y_train, X_test, y_test
