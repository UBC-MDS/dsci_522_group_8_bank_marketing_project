# download_data.py
# author: Rachel Li
# date: 2023-11-29

import click
import os
import sys
import warnings
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.read_zip import read_zip

warnings.filterwarnings('ignore', category=FutureWarning)
@click.command()
@click.option('--url', type=str, help="URL of dataset to be downloaded")
@click.option('--write_to', stype=str, help="Path to directory where raw data will be written to")

def main(url, write_to):
    """Downloads data zip data from the web to a local filepath and extracts it."""
    try:
        read_zip(url, write_to)
    except:
        os.makedirs(write_to)
        read_zip(url, write_to)

if __name__ == '__main__':
    main()