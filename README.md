# Bank Term Deposit Subscription Predictor

**Authors:** Anu Banga, Rafe Chang, Runtian Li, Sid Grover Contributors: N/A

This repository contains the data, code, and analysis for the project "Uncovering Key Predictors of and Making Predictions about Term Deposit Subscriptions". The classification goal is to predict if the client will subscribe a term deposit (variable y).

![Python](https://img.shields.io/badge/lanaguge-Python-red.svg)
![codesize](https://img.shields.io/github/languages/code-size/UBC-MDS/dsci_522_group_8_bank_marketing_project)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/UBC-MDS/dsci_522_group_8_bank_marketing_project?include_prereleases)
![GitHub](https://img.shields.io/github/license/UBC-MDS/dsci_522_group_8_bank_marketing_project)
![contributors](https://img.shields.io/github/contributors/UBC-MDS/dsci_522_group_8_bank_marketing_project)

### About

The data set [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) was created by Sérgio Moro and Paulo Rita at the University Institute of Lisbon, and Paulo Cortez at the University of Minhom. It is sourced from the UCI Machine Learning Repository. Each row in this data set is an observation related to direct marketing campaigns (phone calls) of a Portuguese banking institution.

In this report, we delve into an analysis of the determinants that determine client subscriptions of term deposits within a Portuguese banking institution. Our investigation revolves around a dataset with 45,211 client interactions, consisting of 17 distinct input features. By employing dummy classifier (dc), unbalanced/balanced logistic regression (LR), and unbalanced/balanced support vector machines (SVM), the analysis predicts term deposity subscription.

The exploratory data analysis (EDA) employs visualizations to unravel the intricacies of feature distributions and inter-feature correlations. Model evaluation places a deliberate emphasis on precision and recall, a decision driven by the inherent class imbalance within the data set. Rigorous data preprocessing, involving handling missing entries, categorical variable encoding, and numerical variable normalization and imputation, is performed and column transformers are to prepare the data set for the aforementioned ML models. The five models are tested for their precision, recall, F-1 score, fit time, and score time during cross-validation, and important features are identified.

The report's discoveries are important for banks to grasp and forecast how customers make decisions about term deposits. Understanding this helps fine-tune marketing strategies for future campaigns. We view these insights as a starting point for further research, potentially employing advanced models and more data to explore patterns and other factors that influence customer choices.


### Report

The report can be found at [`bank_analysis.pdf`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/blob/main/notebooks/bank_analysis.pdf)

### Suggested Improvements

-   Use of Ensemble Models: Ensemble models, through aggregation of predictions from diverse models, enhance accuracy, mitigate overfitting, and effectively capture non-linear relationships - making them well-suited for predicting term deposit subscriptions. Their robustness to outliers, versatility across data types, and feature importance make them a perfrct fit in this context.
-   Addressing Class Imbalance differently: A combination of techniques, such as Random Undersampling for the majority class and Synthetic Minority Over-sampling Technique (SMOTE) for the minority class, can be employed to address imbalances and enhance predictive performance.
-   Determining Casual Relationships: ML techniques like Random Forests and SHAP values can unveil key features influencing term deposit subscriptions and offer insights into causal relationships. Causal inference algorithms, including causal forests, handle observational data complexities, estimating treatment effects on outcomes by maximing differences between treatments. ML-driven counterfactual predictions can be used to assess how altering specific features impacts the likelihood of term deposit subscriptions. However, some of these may be beyond the scope of our current curriculum.

### Usage

To replicate this analysis: Clone this repository:

```         
git clone https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project
```

Pull the image by running this command from the root od the repository:
```
docker pull cchang5/dsci_522_group_8_bank_marketing:ee13699
```

After building the image successfully, run this command to run the container:
```
docker compose up
```

To run the analysis, run the following from the root of this repository:

```         
conda activate bank_marketing_analyis
jupyter lab 
```

Open `notebooks/bank_analysis.ipynb` in Jupyter Lab and under the "Kernel" menu click "Restart Kernel and Run All Cells...".

### Dependencies

-   `conda` (version 23.9.0 or higher)
-   `nb_conda_kernels` (version 2.3.1 or higher)
-   Python and packages listed in [`environment.yml`](environment.yml)

### License

This project is licensed under the MIT License - see LICENSE.md for details.

### References

1.  Moro,S., Rita,P., and Cortez,P., 2012. Bank Marketing. UCI Machine Learning Repository. <https://doi.org/10.24432/C5K306>"
2.  Timbers,T. , Ostblom,J., and Lee,M., 2023. Breast Cancer Predictor Report. GitHub repository, <https://github.com/ttimbers/breast_cancer_predictor_py/blob/0.0.1/src/breast_cancer_predictor_report.ipynb>",
3.  Moro, S., Cortez, P., & Rita, P. (2014). A data-driven approach to predict the success of bank telemarketing. Decis. Support Syst., 62, 22-31.
4.  Alsolami, F.J., Saleem, F., & Al-Ghamdi, A.S. (2020). Predicting the Accuracy for Telemarketing Process in Banks Using Data Mining.
5.  Vajiramedhin, C., & Suebsing, A. (2014). Feature Selection with Data Balancing for Prediction of Bank Telemarketing. Applied mathematical sciences, 8, 5667-5672.
6.  Moura, A.F., Pinho, C.M., Napolitano, D.M., Martins, F.S., & Fornari Junior, J.C. (2020). Optimization of operational costs of Call centers employing classification techniques. Research, Society and Development, 9.
