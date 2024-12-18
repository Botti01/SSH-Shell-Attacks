# Data Directory

## Overview
This directory contains the dataset and its processed versions used in the SSH Shell Attack Session project.

## Structure
- `README.md`: This file explains the structure and usage of the data.
- `features.txt`: List of features used in the dataset.
- `raw/`: Contains the original dataset files.
  - `ssh_attacks.parquet`: Original dataset containing 230,000 SSH shell attack sessions.
- `processed/`: Contains preprocessed and feature-engineered data.
  - `BOW_DATASETS/`: Bag-of-Words datasets.
    - `ssh_attacks_bow.parquet`: BOW representation of the dataset.
    - `ssh_attacks_bow_sampled.parquet`: Sampled BOW dataset.
  - `TFIDF_DATASETS/`: TF-IDF datasets.
    - `ssh_attacks_tfidf.parquet`: TF-IDF representation of the dataset.
    - `ssh_attacks_tfidf_sampled.parquet`: Sampled TF-IDF dataset.
  - `ssh_attacks_decoded.parquet`: Decoded dataset.
  - `ssh_attacks_sampled_decoded.parquet`: Sampled and decoded dataset.
  - `train_encodings.pkl`: Training encodings.
  - `val_encodings.pkl`: Validation encodings.

## Details
### Raw Data
- File: `ssh_attacks.parquet`
  - Format: Parquet
  - Description: Original dataset containing 230,000 SSH shell attack sessions.

### Processed Data
- Purpose: Cleaned and feature-engineered datasets used in model training.
- Contents:
  - `BOW_DATASETS/`: Bag-of-Words datasets.
  - `TFIDF_DATASETS/`: TF-IDF datasets.
  - `ssh_attacks_decoded.parquet`: Decoded dataset.
  - `ssh_attacks_sampled_decoded.parquet`: Sampled and decoded dataset.
  - `train_encodings.pkl`: Training encodings.
  - `val_encodings.pkl`: Validation encodings.

## How to Add New Data
1. Place raw files in the `raw/` directory.
2. Run preprocessing scripts in the `scripts/` folder to generate processed data.
3. Save processed files in the `processed/` directory.
