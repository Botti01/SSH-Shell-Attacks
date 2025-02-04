# SSH Shell Attacks

![polito](resources/logo_polito.jpg)

<!-- ## Table of Contents -->

<details closed>
<summary><b>Table of Contents</b></summary>
 
&nbsp;• [Overview](#overview) <br>
&nbsp;• [Dataset](#dataset) <br>
&nbsp;• [Project Report](#project-report) <br>
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
<i>Last updated: January 2025</i>
</div>

</details>

## Overview

This project is part of the [Machine Learning for Networking](https://didattica.polito.it/pls/portal30/gap.pkg_guide.viewGap?p_cod_ins=01DSMUV&p_a_acc=2025&p_header=S&p_lang=IT&multi=N) course at **Politecnico di Torino**. It focuses on analyzing SSH shell attack sessions recorded from honeypot deployments to classify attacker intents and explore underlying patterns.

- Original Project Repository: [ML4Net/SSH-Shell-Attacks](https://github.com/ML4Net/SSH-Shell-Attacks)
- Original Report Repository: [ML4Net/latex-report](https://github.com/ML4Net/latex-report)

> **Navigation Tip**: This `README` provides a general overview of the project. For detailed documentation, check the specific `README` files in each directory ([see Table of Contents above](#table-of-contents)). Each subdirectory contains in-depth information about its specific components.

> **Quick Links**:
>
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

## Project Report

The project report is a comprehensive document detailing the methodologies, experiments, and findings of the SSH Shell Attacks project.

- **Format:** PDF
- **Template:** ACM format single column (acmlarge)

The report is named [SSH-Shell-Attacks-report.pdf](SSH-Shell-Attacks-report.pdf) and can be found in the root directory of the repository.

There is also an appendix of the project that contains extra plots and additional information. The appendix is also in the root directory, in PDF format, and uses the same ACM format single column template. The appendix is named [SSH-Shell-Attacks-appendix.pdf](SSH-Shell-Attacks-appendix.pdf).

The original source code of the report can be found in the repo [latex-report](https://github.com/ML4Net/latex-report).

## Project Structure

```plaintext
SSH-Shell-Attacks/
│
├── data/                           # Dataset and related resources
│   ├── raw/                        # Original dataset files (e.g., ssh_attacks.parquet)
│   └── processed/                  # Pre-processed and feature-engineered files
│
├── notebooks/                      # Jupyter notebooks
│
├── scripts/                        # Python scripts for algorithms and utilities
│
├── results/                        # Outputs from the models and analysis
│   ├── figures/                    # Plots and visualizations
│   ├── models/                     # Saved models (e.g., .pkl, .h5)
│   └── metrics/                    # Evaluation metrics and reports
│
├── README.md                       # High-level overview of the project
├── SSH-Shell-Attacks-report.pdf    # Report of the project
├── SSH-Shell-Attacks-appendix.pdf  # Appendix of the report
├── requirements.txt                # Python dependencies
├── .gitignore                      # Ignore unnecessary files for versioning
└── LICENSE                         # Licensing information (optional)
```

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:**
  - Data Processing: `pandas`, `numpy`, `pyarrow`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning: `scikit-learn`
  - Clustering: `scikit-learn`, `wordcloud`
  - Language Models: `scikit-learn`, `transformers`, `torch`

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

3. **Execute the Notebooks:**
   Open the relevant notebook for each section and follow the instructions to:

   - Load the dataset.
   - Perform data exploration.
   - Train and evaluate machine learning models.

   Notebooks:

   - `section0_data_preprocessing_and_cleaning.ipynb`
   - `section1_data_exploration_and_preprocessing.ipynb`
   - `section2_supervised_learning_classification.ipynb`
   - `section3_unsupervised_learning_clustering.ipynb`
   - `section4_language_model_exploration.ipynb`

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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Luca Vassio** ([luca.vassio@polito.it](mailto:luca.vassio@polito.it)): the professor supervising our work and the primary point of reference for the project.
- **Matteo Boffa** ([matteo.boffa@polito.it](mailto:matteo.boffa@polito.it)): the creator and organizer of this project.
- **Team Members**: Andrea Botticella, Elia Innocenti, Renato Mignone, and Simone Romano.

Please cite us if this project is copied, used for inspiration, or if any material is taken from it.

<div align="right">
<a href="#top">Back to top</a>
</div>
