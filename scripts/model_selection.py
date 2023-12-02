# author: Rachel Li
# date: 2023-12-01
#Model Selection

import sys
import click
import os
import numpy as np
import pandas as pd
import pickle
from sklearn import set_config

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split, RandomizedSearchCV
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.metrics import make_scorer, f1_score, recall_score, precision_score, accuracy_score, ConfusionMatrixDisplay, classification_report, PrecisionRecallDisplay
from scipy.stats import uniform
#sys.path.append('..')
#from src.preprocessor import preprocess_data

@click.command()
@click.option('--train_df', type=str, help="Path to train df")
#@click.option('--test_df', type=str, help="Path to test df")
@click.option('--pipeline_to', type=str, help="Path to directory where the pipeline object will be written to")
@click.option('--results_to', type=str, help="Path to directory where the plot will be written to")
@click.option('--seed', type=int, help="Random seed", default=522)

def main (train_df, pipeline_to, results_to, seed):
    """
    Select and Train the preprocessor and estimator for co2 per capita prediction on the training data
    """
    np.random.seed(seed)

    # Load data
    train_data = pd.read_csv(train_df)
    X_train = train_data.drop(columns=["target"])
    y_train = train_data["target"]

    numerical_features = ["age", "balance", "duration", "campaign", "pdays", "previous"]
    categorical_features = ["job", "marital", "education", "default", "housing", "loan", "poutcome"]
    drop_features = ["contact", "day", "month"]

    #preprocessor = make_preprocessor(
    #    drop_feats=drop_features,
    #    categorical_feats=categorical_features,
    #    numerical_feats=numerical_features,
    #)
    preprocessor = make_column_transformer(
        (StandardScaler(), numerical_features),
        (OneHotEncoder(), categorical_features),
        ('drop', drop_features),
    )

        # Model Selection
    # List of models
    models = {
        "dummy": DummyClassifier(),
        "logreg": LogisticRegression(max_iter=1000, random_state=123),
        "svc": SVC(random_state=123),
        "logreg_bal": LogisticRegression(max_iter=1000, random_state=123, class_weight="balanced"),
        "svc_bal":SVC(random_state=123, class_weight="balanced"),
    }
    # List of metrics
    score_types = {
    "accuracy": 'accuracy',
    'precision': make_scorer(precision_score, pos_label="yes", zero_division=0),
    'recall': make_scorer(recall_score, pos_label="yes"),
    'f1': make_scorer(f1_score, pos_label="yes")
}

    # Evaluate models
    cross_val_results = dict()
    for name, model in models.items():
        pipe = make_pipeline(preprocessor, model)
        cross_val_results[name] = (
            pd.DataFrame(
                cross_validate(
                    pipe,
                    X_train,
                    y_train,
                    cv=10,
                    scoring=score_types,
                    return_train_score=True,
                )
            )
            .agg(["mean", "std"])
            .round(3)
            .T
        )

    cross_val_results_df = pd.concat(
        cross_val_results, axis="columns"
    )
    cross_val_results_df.to_csv(os.path.join(results_to, "model_selection_scores.csv"), index=False)

    return

if __name__ == '__main__':
    main()
