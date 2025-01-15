# Notebooks Directory

This directory contains Jupyter notebooks for data exploration, preprocessing, and machine learning tasks.

## Structure

- `README.md`: This file explains the purpose and contents of the notebooks.
- `section0_data_preprocessing_and_cleaning.ipynb`: Data decoding and sampling.
- `section1_data_exploration_and_preprocessing.ipynb`: Data exploration and preprocessing.
- `section2_supervised_learning_classification.ipynb`: Supervised learning for intent classification.
- `section3_unsupervised_learning_clustering.ipynb`: Clustering SSH attack sessions.
- `section4_language_model_exploration.ipynb`: Exploring advanced NLP techniques for the dataset.

## Notebook Descriptions

### Section 0: Data Preprocessing and Cleaning

- Decode Base64-encoded SSH sessions.
- Tokenize sessions based on a predefined vocabulary.
- Save the processed dataset for further use.

### Section 1: Data Exploration and Preprocessing

- Visualize dataset distributions.
- Clean and preprocess data for modeling.
- Perform temporal analysis and session analysis.

### Section 2: Supervised Learning

- Train classifiers for intent prediction.
- Evaluate performance using metrics like accuracy and F1-score.
- Perform hyperparameter tuning and feature experimentation.

### Section 3: Unsupervised Learning

- Cluster sessions to uncover hidden patterns.
- Use algorithms like k-means and Gaussian Mixture Models.
- Evaluate clusters using methods like the Elbow Method and Silhouette Analysis.

### Section 4: Language Models

- Experiment with models like BERT and Doc2Vec.
- Fine-tune pre-trained models for intent classification.
- Plot learning curves and evaluate model performance.

## How to Run

1. Install dependencies using `requirements.txt`.
2. Open the notebooks in Jupyter or JupyterLab.
3. Follow the instructions provided within each notebook.

## Detailed Steps in Each Section

### Section 0: Data Preprocessing and Cleaning

- **Install Dependencies**: Install necessary packages.
- **Helper Functions**: Functions to decode Base64 strings, clean and tokenize sessions.
- **Load and Process Data**: Load raw data, decode sessions, clean and tokenize, save processed data.

### Section 1: Data Exploration and Preprocessing

- **Install Dependencies**: Install necessary packages.
- **Dataset Preparation**: Load and inspect the dataset, check for missing values and duplicates.
- **Temporal Analysis**: Analyze attack frequencies over time (hourly, daily, monthly trends).
- **Session Analysis**: Analyze the content and structure of attack sessions.
- **Intent Distribution**: Visualize the distribution of different attack intents.
- **Text Representation**: Represent text data using techniques like TF-IDF.
- **Error Reporting**: Report any errors encountered during preprocessing.

### Section 2: Supervised Learning

- **Install Dependencies**: Install necessary packages.
- **Data Splitting**: Split the dataset into training and testing sets.
- **Baseline Model Implementation**: Implement baseline classifiers like Logistic Regression, Random Forest, and SVM.
- **Hyperparameter Tuning**: Tune hyperparameters using GridSearchCV.
- **Result Analysis**: Analyze the performance of the models.
- **Feature Experimentation**: Experiment with different feature representations and preprocessing techniques.

### Section 3: Unsupervised Learning

- **Install Dependencies**: Install necessary packages.
- **Determine the Number of Clusters**: Use Elbow Method and Silhouette Analysis to find the optimal number of clusters.
- **Tune Other Hyperparameters**: Tune hyperparameters for clustering algorithms.
- **Visualize the Clusters**: Visualize the resulting clusters.
- **Cluster Analysis**: Analyze the characteristics of each cluster.
- **Assess Homogeneity and Intent Reflection**: Assess how well the clusters reflect different attack intents.
- **Associate Clusters with Specific Attack Categories**: Link clusters to specific categories of attacks.

### Section 4: Language Models

- **Install Dependencies**: Install necessary packages.
- **Model Selection**: Choose between BERT and Doc2Vec for intent classification.
- **Add a Dense Layer**: Extend the model with a custom dense layer for classification.
- **Fine-Tuning**: Fine-tune the model on the training dataset.
- **Plot Learning Curves**: Visualize training and validation loss curves to identify the optimal stopping point.
