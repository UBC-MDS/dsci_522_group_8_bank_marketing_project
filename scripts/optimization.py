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
    return random_search, best_model_random

@click.command()
@click.option('--df', type=str, help="path to df")
@click.option('--x_test', type=str, help="path to x_test")
@click.option('--y_test', type=str, help="path to y_test")
@click.option('--results_to', type=str, help="path to direct where the result will be written to")
@click.option('--plot_to', type=str, help="path to direct where the plot will be written to")

def main(df, x_test, y_test, results_to, plot_to): 

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
    X_test_sampled = test_df_sampled.drop(columns=["target"])
    y_train_sampled = train_df_sampled["target"]
    y_test_sampled = test_df_sampled["target"]

    # Transformation on the sample training data
    sample_preprocessor = make_column_transformer(
        (StandardScaler(), numerical_features),
        (OneHotEncoder(drop="if_binary"), categorical_features),
        ("drop", drop_features),
    )

    svc_bal_sample = make_pipeline(sample_preprocessor, SVC(random_state=123, class_weight="balanced"))
    
    random_search, best_model_random = optimization(svc_bal_sample, X_train_sampled, y_train_sampled)

    # show accuracy 
    accuracy_random = best_model_random.score(x_test, y_test)

    # show recall 
    predictions = best_model_random.predict(x_test)
    recall = recall_score(y_test, predictions, pos_label='yes')

    model_scores = pd.DataFrame({'Accuracy': [accuracy_random], 'Recall': [recall]}) 
    model_scores.to_csv(os.path.join(results_to, "results/metrics/model_scores.csv")) 
    
    # visualize the c and gamma 
    results = pd.DataFrame(random_search.cv_results_)
    # scatter = 
    alt.Chart(results).mark_circle().encode(
        x='param_svc__C:Q',
        y='param_svc__gamma:Q',
        color=alt.Color('mean_test_score:Q', 
                        scale=alt.Scale(scheme='viridis', reverse=True)
                    )
    ).properties(
        width=400,
        height=300,
        title='C and gamma vs. Mean Test Score'
    )

    # show the visual 
    # scatter
    plt.gcf().savefig(os.path.join(plot_to, "results/figures/optimization_plot.png"))


if __name__ == '__main__':
    main()

