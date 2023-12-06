# Download the data from zip url
python scripts/download_data.py \
   --url='https://archive.ics.uci.edu/static/public/222/bank+marketing.zip' \
   --write_to='data/raw'

# Unzip the file and subtract the files into folder data/raw/bank
python scripts/unzip.py \
   --path_to_zip_file='data/raw/bank.zip' \
   --directory_to_extract_to='data/raw/bank'

# split data into train and test sets and save them to csv file
python scripts/train_test_split.py \
   --raw-data='data/raw/bank/bank-full.csv' \
   --data-to='data/processed' \
   --seed=522

# Perform exploratory data analysis (EDA) on the given df
python scripts/EDA.py \
   --data-frame = "data/raw/bank/bank-full.csv" \
   --plot-to = "results/figures"

# split train_df and test_df into features and target and create preprocessor
python scripts/preprocessor.py \
   --raw_train=data/split/train_df.csv \
   --raw_test=data/split/test_df.csv \
   --data_to=data/processed \
   --preprocessor_to=results/models

# examine 5 candidate models by calculating score metrics
python scripts/model_selection.py \
    --x_train=data/processed/X_train.csv \
    --y_train=data/processed/y_train.csv  \
    --preprocessor=results/models/preprocessor.pickle \
    --pipeline-to=results/models \
    --results_to=results/metrics \
    --seed=522

# Scoring metric for svc balanced model
python scripts/scoring_metric.py  \
   --x_train=data/processed/X_train.csv  \
   --y_train=data/processed/y_train.csv  \
   --x_test=data/processed/X_test.csv  \
   --y_test=data/processed/y_test.csv  \
   --model_type=results/models/model_pipeline.pickle \
   --results_to=results/metrics \
   --seed=522

# Optimization and Accuracy/Recall Scores
python scripts/optimization.py
    --df=data/bank-full.csv
    --x_test=data/processed/X_test.csv
    --y_test=data/processed/y_test.csv
    --results_to=results/metrics
    --results_to_1=results/metrics
    --plot_to=results/figures