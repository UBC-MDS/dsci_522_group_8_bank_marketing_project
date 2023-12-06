import click
import os
import pickle 
import pandas as pd 
import altair as alt 
import matplotlib.pyplot as plt 

from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.svm import SVC
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import recall_score 
from scipy.stats import uniform


def optimization(svc_pipeline, X_train, y_train): 
    """
    Hyperparameter optimization for pipeline that contains a SVC model. 
   
    """
    if not isinstance(X_train, pd.DataFrame) or not isinstance(y_train, pd.Series):
        raise TypeError("X_train must be a pandas DataFrame and y_train must be a pandas series")
    if not isinstance(svc_pipeline, Pipeline) or not isinstance(svc_pipeline.named_steps.get('svc'), SVC):
        raise ValueError("svc_pipeline must be a pipeline with a SVC model")
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

    best_params_random = random_search.best_params_

    return random_search, best_model_random, best_params_random

@click.command()
@click.option('--df', type=str, help="path to df")
@click.option('--x_test', type=str, help="path to x_test")
@click.option('--y_test', type=str, help="path to y_test")
@click.option('--model_type', type=str, help="Path to model object")
@click.option('--results_to', type=str, help="path to direct where the result will be written to")
@click.option('--results_to_1', type=str, help="path to direct where the result will be written to")
# @click.option('--plot_to', type=str, help="path to direct where the plot will be written to")

def main(df, x_test, y_test, model_type, results_to, results_to_1): 

    numerical_features=["age", "balance", "duration", "campaign", "pdays", "previous"] 
    categorical_features=["job", "marital", "education", "default", "housing", "loan", "poutcome"] 
    drop_features=["contact", "day", "month"] 

    df = pd.read_csv(df, delimiter=";")
    df.rename(columns={"y": "target"}, inplace=True)
    x_test = pd.read_csv(x_test)
    y_test = pd.read_csv(y_test)

    # Creating a sample of 10000 observations
    sample_data = df.sample(n=10000, random_state=123)
    train_df_sampled, test_df_sampled = train_test_split(sample_data, test_size=0.2, random_state=123)

    X_train_sampled = train_df_sampled.drop(columns=["target"])
    y_train_sampled = train_df_sampled["target"]

    # Transformation on the sample training data
    sample_preprocessor = make_column_transformer(
        (StandardScaler(), numerical_features),
        (OneHotEncoder(drop="if_binary"), categorical_features),
        ("drop", drop_features),
    )
    
    if isinstance(model_type, str):
        with open(model_type, "rb") as file:
            model_sel = pickle.load(file)

    if isinstance(model_sel, str):
        with open(model_sel, "wb") as file:
            pickle.dump(model_sel, file) 
    
    random_search, best_model_random, best_params_random = optimization(model_sel, X_train_sampled, y_train_sampled)

    accuracy_random = best_model_random.score(x_test, y_test)

    predictions = best_model_random.predict(x_test)
    recall = recall_score(y_test, predictions, pos_label='yes')

    model_scores = pd.DataFrame({'Accuracy': [accuracy_random], 'Recall': [recall]}) 
    model_scores.to_csv(os.path.join(results_to, "model_scores.csv")) 

    best_param_df = pd.DataFrame([best_params_random]) 
    best_param_df.to_csv(os.path.join(results_to_1, "best_params.csv")) 

if __name__ == '__main__':
    main()

