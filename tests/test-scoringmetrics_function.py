from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import sys
import os

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.scoringmetrics import scoring_metrics

# Test Data for Classification
X, y = make_classification(n_samples=100, n_features=10, n_classes=2, random_state=123)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
pos_label_value=1

# Create an SVC model with balanced class weights
model_svc = SVC(kernel='rbf', class_weight='balanced', random_state=123)
model_svc.fit(X_train, y_train)

# Test for correct return type
def test_scoring_metrics_returns_dataframe():
    result = scoring_metrics(model_svc, X_train, y_train, X_test, y_test, pos_label = pos_label_value)
    assert isinstance(result, pd.DataFrame), "scoring_metrics should return a pandas DataFrame"

# Test for non-negative scores and times
def test_scoring_metric_non_negative():
    result = scoring_metrics(model_svc, X_train, y_train, X_test, y_test, pos_label = pos_label_value)
    assert all(result[col][0] >= 0 for col in result.columns if col not in ['fit_time', 'score_time']), "All scores should be non-negative"
    assert all(result[col][0] >= 0 for col in ['fit_time', 'score_time']), "fit_time and score_time should be non-negative"

# Test for checking the metric columns
def test_scoring_metric_columns():
    result = scoring_metrics(model_svc, X_train, y_train, X_test, y_test, pos_label = pos_label_value)
    expected_columns = {'train_accuracy', 'test_accuracy', 'train_precision', 'test_precision', 'train_recall', 'test_recall', 'train_f1', 'test_f1', 'fit_time', 'score_time'}
    assert set(result.columns) == expected_columns, "Columns should match expected classification metrics"
