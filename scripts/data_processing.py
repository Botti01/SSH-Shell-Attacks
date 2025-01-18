
import pandas as pd
from sklearn.model_selection import train_test_split

# Function to perform sampling on a DataFrame
def sampling(df, min_label_count=2, sampling_ratio=0.05):
    """
    Perform sampling on a DataFrame based on the 'Set_Fingerprint' column.

    Parameters:
        df (pd.DataFrame): Input DataFrame with a column 'Set_Fingerprint'.
        min_label_count (int): Minimum number of occurrences of a label combination to keep.
        sampling_ratio (float): Proportion of rows to sample for each label combination.

    Returns:
        pd.DataFrame: DataFrame with sampled rows.
    """
    # Count occurrences of each label combination
    label_counts = df["Set_Fingerprint"].apply(lambda labels: frozenset(labels)).value_counts()

    # Remove combinations that occur less than the minimum count
    label_combinations_to_remove = label_counts[label_counts < min_label_count].index
    df = df[~df['Set_Fingerprint'].apply(lambda x: frozenset(x)).isin(label_combinations_to_remove)]

    # Recalculate label counts
    label_counts = df["Set_Fingerprint"].apply(lambda labels: frozenset(labels)).value_counts()
    label_counts_to_sample = label_counts[label_counts >= min_label_count]

    # Sample rows for each label combination
    selected_rows = pd.DataFrame()
    for label in label_counts_to_sample.index:
        rows_with_labels = df[df["Set_Fingerprint"].apply(lambda labels: frozenset(labels)).isin([label])]
        num_rows_to_select = max(2, int(len(rows_with_labels) * sampling_ratio))
        selected_rows = pd.concat([selected_rows, rows_with_labels.sample(n=num_rows_to_select)])

    return selected_rows

# Function to split data into train and test sets
def split_train_test(X, y, train_size=0.7, random_state=None):
    """
    Split data into train and test sets with stratification.

    Parameters:
        X (pd.DataFrame): Features DataFrame.
        y (pd.Series): Target column containing labels.
        train_size (float): Proportion of the dataset to include in the train split.
        random_state (int): Random seed for reproducibility.

    Returns:
        Tuple: (X_train, X_test, y_train, y_test)
    """
    # Convert labels to strings for stratification
    y_str = y.apply(lambda x: ', '.join(sorted(x)))
    X_train, X_test, y_train_str, y_test_str = train_test_split(
        X, y_str, train_size=train_size, stratify=y_str, random_state=random_state
    )

    # Convert back to list format
    y_train = y_train_str.apply(lambda x: x.split(', '))
    y_test = y_test_str.apply(lambda x: x.split(', '))

    return X_train, X_test, y_train, y_test
