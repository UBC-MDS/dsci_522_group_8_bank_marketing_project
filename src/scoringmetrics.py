import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from time import time

def scoring_metrics(model, X_train, y_train,X_test,y_test):
    """
    Calculate various classification metrics and timing for a Support Vector Classifier (SVC) model.

    Parameters:
    model :   The Support Vector Classifier model to evaluate.
    X_train : Training data
    y_train : Training target values
    X_test :  Test data
    y_test :  Test target values

    Returns:
    result_metrics : pandas.DataFrame
        DataFrame containing the following metrics:
        - 'train_accuracy': Accuracy on the training set
        - 'test_accuracy': Accuracy on the test set
        - 'train_precision': Precision on the training set
        - 'test_precision': Precision on the test set
        - 'train_recall': Recall on the training set
        - 'test_recall': Recall on the test set
        - 'train_f1': F1-score on the training set
        - 'test_f1': F1-score on the test set
        - 'fit_time': Time taken for model fitting
        - 'score_time': Time taken for prediction scoring

    This function fits the provided SVC model on the training data and evaluates its performance on the test set, computing various classification metrics including accuracy, precision, recall, and F1-score. It also measures the time taken for model fitting and prediction scoring.
    """
    # Training time
    start_fit = time()
    model.fit(X_train, y_train)
    end_fit = time()
    fit_time = end_fit - start_fit

    # Prediction time
    start_score = time()
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    end_score = time()
    score_time = end_score - start_score

    train_accuracy = accuracy_score(y_train, y_pred_train)
    test_accuracy = accuracy_score(y_test, y_pred_test)

    train_precision = precision_score(y_train, y_pred_train)
    test_precision = precision_score(y_test, y_pred_test)

    train_recall = recall_score(y_train, y_pred_train)
    test_recall = recall_score(y_test, y_pred_test)

    train_f1 = f1_score(y_train, y_pred_train)
    test_f1 = f1_score(y_test, y_pred_test)

    metrics = {
        'train_accuracy': train_accuracy,
        'test_accuracy': test_accuracy,
        'train_precision': train_precision,
        'test_precision': test_precision,
        'train_recall': train_recall,
        'test_recall': test_recall,
        'train_f1': train_f1,
        'test_f1': test_f1,
        'fit_time': fit_time,
        'score_time': score_time
    }

    result_metrics = pd.DataFrame(metrics, index=[0])

    return result_metrics