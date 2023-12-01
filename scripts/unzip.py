# unzip.py
# author: Rachel Li
# date: 2023-11-29

import click
import os
import sys
import zipfile
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--path_to_zip_file', type=str)
@click.option('--directory_to_extract_to', type=str)

def main(path_to_zip_file, directory_to_extract_to):
    """Unzip the file and extract them into specific directory"""
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

if __name__ == '__main__':
    main()