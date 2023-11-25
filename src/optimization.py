from sklearn.model_selection import RandomizedSearchCV 
from scipy.stats import uniform
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

def optimization(svc_pipeline, X_train, y_train): 
    """
    Hyperparameter optimization for pipeline that contains a SVC model. 

    Parameters:
        svc_pipeline (sklearn.pipeline.Pipeline): The optimizing pipeline. 
        X_train (pandas.core.frame.DataFrame): The features used to train the model. 
        y_train (pandas.core.series.Series): The target used to train the model. 

    Raises:
        TypeError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
         (sklearn.model_selection._search.RandomizedSearchCV, sklearn.pipeline.Pipeline): A tuple of a object containing details about random search, and a pipeline with an optimized SVC model. 
    """

    if not isinstance(X_train, pd.DataFrame) or not isinstance(y_train, pd.Series):
        raise TypeError("X_train and y_train must be pandas DataFrames")
    if not isinstance(svc_pipeline, Pipeline) or not isinstance(svc_pipeline.named_steps.get('svc'), SVC):
        raise ValueError("svc_pipeline must be a pipeline with A SVC model")
    if len(X_train) != len(y_train): 
        raise ValueError("X_train and y_train must contain same amount of rows")
    
    param_dist = {
        'svc__C': uniform(0.1, 10),
        'svc__gamma': uniform(0.001, 0.1),
        'svc__kernel': ['rbf', 'sigmoid', 'linear']
    }

    random_search = RandomizedSearchCV(svc_pipeline, param_distributions=param_dist, n_iter=25, cv=5, n_jobs=-1, random_state=123)
    random_search.fit(X_train, y_train)
    
    best_model_random = random_search.best_estimator_
    return random_search, best_model_random


