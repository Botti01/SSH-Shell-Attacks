# Data Directory

This directory contains the dataset and its processed versions used in the SSH Shell Attack Session project.

## Structure

- `README.md`: This file explains the structure and usage of the data (1.6 KB)
- `features.txt`: List of features used in the dataset (352 B)
- `raw/`: Contains the original dataset files
  - `ssh_attacks.parquet`: Original dataset containing 230,000 SSH shell attack sessions (34.7 MB)
- `processed/`: Contains preprocessed and feature-engineered data
  - `BOW_DATASETS/`: Bag-of-Words datasets
    - `ssh_attacks_bow.parquet`: BOW representation of the dataset (2.2 MB)
  - `TFIDF_DATASETS/`: TF-IDF datasets
    - `ssh_attacks_tfidf.parquet`: TF-IDF representation of the dataset (4.6 MB)
  - `ssh_attacks_decoded.parquet`: Decoded dataset (21.9 MB)

## Details

### Raw Data

- File: `ssh_attacks.parquet`
  - Format: Parquet
  - Size: 34.7 MB
  - Description: Original dataset containing 230,000 SSH shell attack sessions

### Processed Data

- Purpose: Cleaned and feature-engineered datasets used in model training
- Contents:
  - `BOW_DATASETS/`: Bag-of-Words representation
    - `ssh_attacks_bow.parquet`: BOW features (2.2 MB)
  - `TFIDF_DATASETS/`: Term Frequency-Inverse Document Frequency representation
    - `ssh_attacks_tfidf.parquet`: TF-IDF features (4.6 MB)
  - `ssh_attacks_decoded.parquet`: Decoded dataset with processed features (21.9 MB)

### Total Size

- Raw data: 34.7 MB
- Processed data: 28.7 MB
- Total directory size: ~64 MB
