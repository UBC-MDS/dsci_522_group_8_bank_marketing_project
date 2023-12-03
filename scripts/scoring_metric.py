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
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.scoringmetrics import scoring_metrics

@click.command()
@click.option('--x_train', type=str, help="Path to training data")
@click.option('--y_train', type=str, help="Path to training data")
@click.option('--x_test', type=str, help="Path to training data")
@click.option('--y_test', type=str, help="Path to training data")
@click.option('--model_type', type=str, help="Path to model object")
@click.option('--results_to', type=str, help="Path to directory where the results will be written to")
@click.option('--seed', type=int, help="Random seed", default=522)

def main (x_train, y_train, x_test, y_test, model_type, results_to, seed):
    """
    Use SVC balanced classifier to get scoring metric.
    """
    np.random.seed(seed)

    # read in data
    x_train_svc = pd.read_csv(x_train)
    y_train_r = pd.read_csv(y_train)
    y_train_column = y_train_r["target"]
    y_train_svc = y_train_column.values.ravel()

    x_test_svc = pd.read_csv(x_test)
    y_test_r= pd.read_csv(y_test)
    y_test_column = y_test_r["target"]
    y_test_svc = y_test_column.values.ravel()
    
    if isinstance(model_type, str):
        with open(model_type, "rb") as file:
            model_sel = pickle.load(file)

    if isinstance(model_sel, str):
        with open(model_sel, "wb") as file:
            pickle.dump(model_sel, file)

    result=scoring_metrics(model_sel, x_train_svc, y_train_svc, x_test_svc, y_test_svc, pos_label="yes")
    result.to_csv(os.path.join(results_to, "scoring_metrics.csv"), index= False)

    return

if __name__ == '__main__':
    main()
