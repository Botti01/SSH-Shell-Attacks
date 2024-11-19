# Data Directory

## Overview
This directory contains the dataset and its processed versions used in the SSH Shell Attack Session project.

## Structure
- `README.md`: This file explains the structure and usage of the data.
- `raw/`: Contains the original dataset files.
- `processed/`: Contains preprocessed and feature-engineered data.

## Details
### Raw Data
- File: `ssh_attacks.parquet`
  - Format: Parquet
  - Description: Original dataset containing 230,000 SSH shell attack sessions.

### Processed Data
- Purpose: Cleaned and feature-engineered datasets used in model training.
- Contents: Placeholder files or processed data for feature extraction.

## How to Add New Data
1. Place raw files in the `raw/` directory.
2. Run preprocessing scripts in the `scripts/preprocessing/` folder to generate processed data.
3. Save processed files in the `processed/` directory.
