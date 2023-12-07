# Define the main targets and phony targets
.PHONY: all clean

all: results/metrics/optimization_results results/metrics/scoring_results results/models/model_pipeline.pickle

# Download and unzip data
data/raw/bank.zip:
	python scripts/download_data.py --url='https://archive.ics.uci.edu/static/public/222/bank+marketing.zip' --write_to='data/raw'

data/raw/bank/bank-full.csv: data/raw/bank.zip
	python scripts/unzip.py --path_to_zip_file='data/raw/bank.zip' --directory_to_extract_to='data/raw/bank'

# Split data into train and test sets
data/split/train_df.csv data/split/test_df.csv: data/raw/bank/bank-full.csv
	python scripts/train_test_split.py --raw-data='data/raw/bank/bank-full.csv' --data-to='data/split' --seed=522

# Perform exploratory data analysis (EDA)
results/figures/eda_output: data/raw/bank/bank-full.csv
	python scripts/EDA.py --data-frame="data/raw/bank/bank-full.csv" --plot-to="results/figures"

# Preprocess train and test data
data/processed/X_train.csv data/processed/y_train.csv data/processed/X_test.csv data/processed/y_test.csv results/models/preprocessor.pickle: data/split/train_df.csv data/split/test_df.csv
	python scripts/preprocessor.py --raw_train=data/split/train_df.csv --raw_test=data/split/test_df.csv --data_to=data/processed --preprocessor_to=results/models

# Model selection
results/models/model_pipeline.pickle: data/processed/X_train.csv data/processed/y_train.csv
	python scripts/model_selection.py --x_train=data/processed/X_train.csv --y_train=data/processed/y_train.csv --preprocessor=results/models/preprocessor.pickle --pipeline-to=results/models --results_to=results/metrics --seed=522

# Scoring metric for svc balanced model
results/metrics/scoring_results: data/processed/X_train.csv data/processed/y_train.csv data/processed/X_test.csv data/processed/y_test.csv results/models/model_pipeline.pickle
	python scripts/scoring_metric.py --x_train=data/processed/X_train.csv --y_train=data/processed/y_train.csv --x_test=data/processed/X_test.csv --y_test=data/processed/y_test.csv --model_type=results/models/model_pipeline.pickle --results_to=results/metrics --seed=522

# Optimization and Accuracy/Recall Scores
results/metrics/optimization_results: data/raw/bank/bank-full.csv data/processed/X_test.csv data/processed/y_test.csv results/models/model_pipeline.pickle
	python scripts/optimization.py --df=data/raw/bank/bank-full.csv --x_test=data/processed/X_test.csv --y_test=data/processed/y_test.csv --model_type=results/models/model_pipeline.pickle --results_to=results/metrics --results_to_1=results/metrics

# Clean up
clean:
	rm -rf data/raw/
	rm -f data/split/*.csv
	rm -rf data/processed/
	rm -rf results/figures/*
	rm -f results/models/*.pickle
	rm -f results/metrics/*
