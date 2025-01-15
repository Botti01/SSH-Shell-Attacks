# Scripts Directory

This directory contains Python scripts for implementing the project's functionality.

## Structure

- `README.md`: This file explains the purpose and contents of the `scripts/` directory.
- `install_dependencies.py`: Script to install dependencies required for different sections of the project.
- `data_storage_utils.py`: Utility script for saving plots.
- `data_processing.py`: Script for data sampling and splitting.
- `plotting_utils.py`: Script for generating various plots and visualizations.
- `__init__.py`: Initialization file for the scripts module.

## Script Categories

### Install Dependencies

- **Purpose**: Install dependencies required for different sections of the project.
- **Example**: `install_dependencies.py` to install packages listed in `requirements.txt`.

### Data Storage Utilities

- **Purpose**: Save Matplotlib figures with custom settings.
- **Example**: `data_storage_utils.py` to save plots in a specified directory.

### Data Processing

- **Purpose**: Perform data sampling and split data into train and test sets.
- **Example**: `data_processing.py` to sample data based on label combinations and split data for training and testing.

### Plotting Utilities

- **Purpose**: Generate various plots and visualizations for model evaluation and data analysis.
- **Example**: `plotting_utils.py` to plot ROC curves, precision-recall curves, loss curves, and more.

## Usage

Run scripts directly using Python. Example:
```bash
python scripts/install_dependencies.py section3
```
