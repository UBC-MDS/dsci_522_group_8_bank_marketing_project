# unzip.py
# author: Rachel Li
# date: 2023-11-29

import click
import os
import sys
import numpy as np
import pandas as pd
from sklearn import set_config
from sklearn.model_selection import train_test_split
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--raw-data', type=str, help="Path to raw data")
@click.option('--data-to', type=str, help="Path to directory where split data will be written to")
@click.option('--seed', type=int, help="Random seed", default=123)

def main(raw_data, data_to, seed):
    """Rename the target and split train/test set"""
    np.random.seed(seed)
    set_config(transform_output="pandas")
    
    df = pd.read_csv(raw_data, delimiter=";")
    df.rename(columns={"y": "target"}, inplace=True)
    train_df, test_df = train_test_split(df, test_size=0.8, random_state=123)
    train_df.to_csv(os.path.join(data_to, "train_df.csv"), index=False)
    test_df.to_csv(os.path.join(data_to, "test_df.csv"), index=False)

if __name__ == '__main__':
    main()

