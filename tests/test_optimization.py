import sys
import os 
import pytest 
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline 
from sklearn.svm import SVC 
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler 
import random

# import the optimization function from the src folder 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.optimization import optimization 

# create test data 
test_data = pd.DataFrame({
        "age": np.random.randint(18, 65, size=100),
        "balance": np.random.randint(0, 10000, size=100),
        "education": np.random.choice(["High School", "Bachelor's", "Master's"], size=100),
        "default": np.random.choice([0, 1], size=100),
        "target": np.random.choice([0, 1], size=100)
    })

X_train = test_data.drop(columns=["target"])
y_train = test_data["target"]

numerical_features = ["age", "balance"]
sample_preprocessor = make_column_transformer(
    (StandardScaler(), numerical_features),
    remainder="passthrough"
)

svc_ppl_sample = make_pipeline(StandardScaler(), SVC(random_state=123, class_weight="balanced"))

y_false = pd.Series([random.randint(1, 100) for _ in range(99)]) 

# test for input types 
def test_input_type(): 
    with pytest.raises(TypeError) as custom_string: 
        random_search1, best_model_random1 = optimization(svc_ppl_sample, 0, y_train)
    assert str(custom_string.value), "X_train must be a pandas DataFrame and y_train must be a pandas series"

def test_model_type(): 
    with pytest.raises(ValueError) as custom_string: 
        random_search1, best_model_random1 = optimization(0, X_train, y_train)
    assert str(custom_string.value), "svc_pipeline must be a pipeline with a SVC model"
   
# test if the length matches  
def test_Xy_len(): 
    with pytest.raises(ValueError) as custom_string: 
        random_search1, best_model_random1 = optimization(svc_ppl_sample, X_train, y_false)
    assert str(custom_string.value), "X_train and y_train must contain same amount of rows"
