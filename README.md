# SSH Shell Attacks Project

![polito](resources/logo_polito.jpg)

<!-- TODO: decide what to keep in this README -->

<!-- TODO: add badges ? -->



<!-- ## Table of Contents -->

<!-- TODO: make prettier -->

<details closed>
<summary><b>Table of Contents</b></summary>
 
&nbsp;• [Overview](#overview) <br>
&nbsp;• [Dataset](#dataset) <br>
&nbsp;• [Project Structure](#project-structure) <br>
&nbsp;• [Tools and Technologies](#tools-and-technologies) <br>
&nbsp;• [How to Run the Project](#how-to-run-the-project) <br>
&nbsp;• [Detailed Documentation](#detailed-documentation) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• [Data Directory](data/README.md) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• [Notebooks Directory](notebooks/README.md) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• [Results Directory](results/README.md) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• [Scripts Directory](scripts/README.md) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• [Tests Directory](tests/README.md) <br>
&nbsp;• [Authors](#authors) <br>
&nbsp;• [License](#license) <br>
&nbsp;• [Acknowledgments](#acknowledgments) <br>

<div align="right">
<i>Last updated: November 2024</i>
</div>

</details>


## Overview

This project is part of the **Machine Learning for Networking (ML4N)** course at Politecnico di Torino. It focuses on analyzing SSH shell attack sessions recorded from honeypot deployments to classify attacker intents and explore underlying patterns.

> **Navigation Tip**: This `README` provides a general overview of the project. For detailed documentation, check the specific `README` files in each directory ([see Table of Contents above](#table-of-contents)). Each subdirectory contains in-depth information about its specific components.
 
> **Quick Links**:
> - For data structure and preprocessing: [Data Documentation](data/README.md)
> - For analysis notebooks: [Notebooks Documentation](notebooks/README.md)
> - For implementation details: [Scripts Documentation](scripts/README.md)

### Objectives

1. **Classification:** Automatically identify and assign attacker intents (e.g., `Persistence`, `Discovery`) to each SSH attack session.
2. **Clustering:** Group similar attack sessions to uncover attack patterns and fine-grained categories.
3. **Language Models:** Explore advanced NLP techniques like BERT and Doc2Vec for improved classification performance.

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

## Project Structure

```plaintext
SSH-Shell-Attacks/
├── data/                           # Dataset and related resources
│   ├── raw/                        # Original dataset files (e.g., ssh_attacks.parquet)
│   └── processed/                  # Pre-processed and feature-engineered files
│
├── notebooks/                      # Jupyter notebooks
│
├── scripts/                        # Python scripts for algorithms and utilities
│   ├── preprocessing/              # Data processing and preparation scripts
│   ├── supervised_learning/        # Supervised learning algorithms
│   ├── unsupervised_learning/      # Clustering algorithms
│   ├── language_models/            # Scripts for language model experimentation
│   └── utils/                      # General-purpose utilities
│
├── results/                        # Outputs from the models and analysis
│   ├── figures/                    # Plots and visualizations
│   ├── models/                     # Saved models (e.g., .pkl, .h5)
│   └── metrics/                    # Evaluation metrics and reports
│
├── tests/                          # Unit tests
│
├── README.md                       # High-level overview of the project
├── requirements.txt                # Python dependencies
├── .gitignore                      # Ignore unnecessary files for versioning
└── LICENSE                         # Licensing information (optional)
```

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:**
  - Data Processing: `pandas`, `numpy`, `pyarrow`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning: `scikit-learn`, `xgboost`
  - NLP: `nltk`, `gensim`, `transformers`
  - Clustering: `scipy`, `sklearn`

## How to Run the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ML4Net/SSH-Shell-Attacks.git
   cd SSH-Shell-Attacks
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

| Name              | GitHub                                                                                                               | LinkedIn                                                                                                                                  | Email                                                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Andrea Botticella | [![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?logo=github)](https://github.com/Botti01)       | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/andrea-botticella-353169293/) | [![Email](https://img.shields.io/badge/Email-Send-blue?logo=gmail)](mailto:andrea.botticella@studenti.polito.it) |
| Elia Innocenti    | [![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?logo=github)](https://github.com/eliainnocenti) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/eliainnocenti/)               | [![Email](https://img.shields.io/badge/Email-Send-blue?logo=gmail)](mailto:elia.innocenti@studenti.polito.it)    |
| Renato Mignone    | [![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?logo=github)](https://github.com/RenatoMignone) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/renato-mignone/)              | [![Email](https://img.shields.io/badge/Email-Send-blue?logo=gmail)](mailto:renato.mignone@studenti.polito.it)    |
| Simone Romano     | [![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?logo=github)](https://github.com/sroman0)       | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/simone-romano-383277307/)     | [![Email](https://img.shields.io/badge/Email-Send-blue?logo=gmail)](mailto:simone.romano2@studenti.polito.it)    |

## License

This project is licensed under the **[appropriate license, e.g., MIT License]**. Please see the `LICENSE` file for details.

## Acknowledgments

- **Luca Vassio** ([luca.vassio@polito.it](mailto:luca.vassio@polito.it)): the professor supervising our work and the primary point of reference for the project.
- **Matteo Boffa** ([matteo.boffa@polito.it](mailto:matteo.boffa@polito.it)): the creator and organizer of this project.

<div align="right">
<a href="#top">Back to top</a>
</div>
