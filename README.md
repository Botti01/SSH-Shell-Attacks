# SSH Shell Attack Session Project

## Overview

This project is part of the **Machine Learning for Networking (ML4N)** course at Politecnico di Torino. It focuses on analyzing SSH shell attack sessions recorded from honeypot deployments to classify attacker intents and explore underlying patterns.

### Objectives

1. **Classification:** Automatically identify and assign attacker intents (e.g., `Persistence`, `Discovery`) to each SSH attack session.
2. **Clustering:** Group similar attack sessions to uncover attack patterns and fine-grained categories.
3. **Language Models:** Explore advanced NLP techniques like BERT and Doc2Vec for improved classification performance.

---

## Dataset

The dataset consists of approximately 230,000 Unix shell attack sessions recorded from honeypots. It includes:

- **Session Commands:** Malicious commands executed in an SSH session.
- **Timestamps:** The exact time each attack started.
- **Labels:** Pre-assigned intents based on the MITRE ATT&CK framework.

### Intents (Classes)

The dataset uses 7 main intent classes:

1. **Persistence**
2. **Discovery**
3. **Defense Evasion**
4. **Execution**
5. **Impact**
6. **Other** (Miscellaneous intents)
7. **Harmless** (Non-malicious commands)

---

## Project Structure

```plaintext
SSH_Shell_Attack_Project/
├── data/                            # Dataset and related resources
│   ├── raw/                         # Original dataset files
│   ├── processed/                   # Pre-processed data
│   └── README.md                    # Dataset details
├── notebooks/                       # Jupyter notebooks
│   ├── main.ipynb                   # Main execution notebook
│   ├── exploration.ipynb            # Data exploration and visualization
│   └── experiments.ipynb            # Experimental notebooks
├── scripts/                         # Python scripts for modular code
│   ├── preprocessing/               # Data preprocessing scripts
│   ├── supervised_learning/         # Supervised learning algorithms
│   ├── unsupervised_learning/       # Clustering scripts
│   ├── language_models/             # NLP-based models (BERT, Doc2Vec)
│   └── utils/                       # General-purpose utilities
├── results/                         # Outputs from models and analyses
│   ├── figures/                     # Visualizations
│   ├── models/                      # Trained model files
│   ├── metrics/                     # Performance metrics
├── tests/                           # Unit tests
│   ├── test_preprocessing.py        # Tests for preprocessing
│   ├── test_models.py               # Tests for ML pipelines
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore file
└── LICENSE                          # License file
```

---

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:**
  - Data Processing: `pandas`, `numpy`, `pyarrow`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning: `scikit-learn`, `xgboost`
  - NLP: `nltk`, `gensim`, `transformers`
  - Clustering: `scipy`, `sklearn`

---

## How to Run the Project

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd SSH_Shell_Attack_Project
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute the Main Notebook:**
   Open `notebooks/main.ipynb` and follow the instructions to:

   - Load the dataset.
   - Perform data exploration.
   - Train and evaluate machine learning models.

4. **Explore Scripts:**
   Run modular scripts in the `scripts/` directory for specific tasks like preprocessing or model training.

---

## Authors

| Name              | GitHub                                                                                                               | LinkedIn                                                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Andrea Botticella | [![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?logo=github)](https://github.com/botti001)      | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/andrea-botticella-353169293/) |
| Elia Innocenti    | [![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?logo=github)](https://github.com/eliainnocenti) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/eliainnocenti/)               |
| Renato Mignone    | [![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?logo=github)](https://github.com/RenatoMignone) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/renato-mignone/)              |
| Simone Romano     | [![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?logo=github)](https://github.com/sroman0)       | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/simone-romano-383277307/)     |

---

## License

This project is licensed under the **[appropriate license, e.g., MIT License]**. Please see the `LICENSE` file for details.

---

## Acknowledgments

Special thanks to **Luca Vassio** and **Matteo Boffa** for their guidance on this project.

---

Feel free to contribute or reach out for collaboration opportunities!
