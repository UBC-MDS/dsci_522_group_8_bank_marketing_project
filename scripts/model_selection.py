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

@click.command()
@click.option('--x_train', type=str, help="Path to training data")
@click.option('--y_train', type=str, help="Path to training data")
@click.option('--preprocessor', type=str, help="Path to preprocessor object")
@click.option('--pipeline-to', type=str, help="Path to directory where the pipeline object will be written to")
@click.option('--results_to', type=str, help="Path to directory where the results will be written to")
@click.option('--seed', type=int, help="Random seed", default=522)

def main (x_train, y_train, preprocessor, pipeline_to, results_to, seed):
    """
    Fits a bank analysis classifier to the training data 
    and saves the pipeline object.
    """
    np.random.seed(seed)

    # read in data & preprocessor
    bank_X_train = pd.read_csv(x_train)
    y_train_r = pd.read_csv(y_train)
    y_train_column = y_train_r["target"]
    bank_y_train = y_train_column.values.ravel()
    bank_preprocessor = pickle.load(open(preprocessor, "rb"))

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
        pipe = make_pipeline(bank_preprocessor, model)
        cross_val_results[name] = (
            pd.DataFrame(
                cross_validate(
                    pipe,
                    bank_X_train,
                    bank_y_train,
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
    cross_val_results_df.to_csv(os.path.join(results_to, "model_selection_scores.csv"), index =True)

    # Save the entire pipeline object using pickle
    with open(os.path.join(pipeline_to, "model_pipeline.pickle"), 'wb') as file:
        pickle.dump(pipe, file)

    return

if __name__ == '__main__':
    main()
