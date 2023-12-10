# :bank: Bank Term Deposit Subscription Predictor

### Authors: Anu Banga, Rafe Chang, Runtian Li, Sid Grover 
*GitHub Page: https://ubc-mds.github.io/dsci_522_group_8_bank_marketing_project/bank_analysis.html*


This repository contains the data, code, and analysis for the project "Uncovering Key Predictors of and Making Predictions about Term Deposit Subscriptions". The classification goal is to predict if the client will subscribe a term deposit (variable y).


![Python](https://img.shields.io/badge/lanaguge-Python-red.svg)
![codesize](https://img.shields.io/github/languages/code-size/UBC-MDS/dsci_522_group_8_bank_marketing_project)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/UBC-MDS/dsci_522_group_8_bank_marketing_project?include_prereleases)
![contributors](https://img.shields.io/github/contributors/UBC-MDS/dsci_522_group_8_bank_marketing_project)
[![MIT License](https://img.shields.io/badge/License-MIT-informational?style=flat-square)](LICENSE-MIT)
[![CC License](https://img.shields.io/badge/CCC-informational?style=flat-square)](LICENSE-CCC)


## About

The data set [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) was created by Sérgio Moro and Paulo Rita at the University Institute of Lisbon, and Paulo Cortez at the University of Minhom. It is sourced from the UCI Machine Learning Repository. Each row in this data set is an observation related to direct marketing campaigns (phone calls) of a Portuguese banking institution.

In this report, we delve into an analysis of the determinants that determine client subscriptions of term deposits within a Portuguese banking institution. Our investigation revolves around a dataset with 45,211 client interactions, consisting of 17 distinct input features. By employing dummy classifier (dc), unbalanced/balanced logistic regression (LR), and unbalanced/balanced support vector machines (SVM), the analysis predicts term deposity subscription.

The exploratory data analysis (EDA) employs visualizations to unravel the intricacies of feature distributions and inter-feature correlations. Model evaluation places a deliberate emphasis on precision and recall, a decision driven by the inherent class imbalance within the data set. Rigorous data preprocessing, involving handling missing entries, categorical variable encoding, and numerical variable normalization and imputation, is performed and column transformers are to prepare the data set for the aforementioned ML models. The five models are tested for their precision, recall, F-1 score, fit time, and score time during cross-validation, and important features are identified.

For model selection and evaluation, we employed five classification models, including a Dummy Classifier as a baseline, Logistic Regression, and Support Vector Classifier (SVC). Emphasizing recall as a critical metric, balanced models such as Balanced Logistic Regression and Balanced Support Vector Classifier (svc_bal) proved superior in identifying potential clients subscribing to term deposits. Hyperparameter optimization was conducted on the Support Vector Classifier (SVC) with a reduced dataset, resulting in a model with an 86% accuracy on the test set and a notable recall of 87%

The report's discoveries are important for banks to grasp and forecast how customers make decisions about term deposits. Understanding this helps fine-tune marketing strategies for future campaigns. We view these insights as a starting point for further research, potentially employing advanced models and more data to explore patterns and other factors that influence customer choices. Some suggested improvements are discussed below. 


## :ledger: Report

The report can be found at [`bank_analysis.html`](https://ubc-mds.github.io/dsci_522_group_8_bank_marketing_project/bank_analysis.html)

## Suggested Improvements

-   **Use of Ensemble Models:** Ensemble models, through aggregation of predictions from diverse models, enhance accuracy, mitigate overfitting, and effectively capture non-linear relationships - making them well-suited for predicting term deposit subscriptions. Their robustness to outliers, versatility across data types, and feature importance make them a perfrct fit in this context.
-   **Addressing Class Imbalance differently:** A combination of techniques, such as Random Undersampling for the majority class and Synthetic Minority Over-sampling Technique (SMOTE) for the minority class, can be employed to address imbalances and enhance predictive performance.
-   **Determining Casual Relationships:** ML techniques like Random Forests and SHAP values can unveil key features influencing term deposit subscriptions and offer insights into causal relationships. Causal inference algorithms, including causal forests, handle observational data complexities, estimating treatment effects on outcomes by maximing differences between treatments. ML-driven counterfactual predictions can be used to assess how altering specific features impacts the likelihood of term deposit subscriptions. However, some of these may be beyond the scope of our current curriculum.
-   **Temporal Adaptability with Statsmodels and Prophet:** Assess the model's adaptability to evolving trends over time is key. Utilizing tools such as Statsmodels for statistical analysis and Facebook Prophet for time-series forecasting ensures the model remains relevant in dynamic market conditions and adapts accordingly to new information.
-   **Cost-Sensitive Learning and Hinge Loss:** Cost-sensitive learning enables the model to explicitly weigh the costs associated with false positives and false negatives. This optimization aligns marketing investments more closely with potential benefits, ensuring that resources are allocated judiciously to maximize return on investment. For SVMs, a cost-sensitive version of the hinge loss can be employed to penalize misclassifications based on their associated costs, encouraging the model to minimize the overall economic costs.

## Usage

Follow the instructions below to reproduce the analysis.

### Setup

1. [Install](https://www.docker.com/get-started/) 
and launch Docker on your computer.

2. Clone this GitHub repository.
```         
git clone https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project
```

### Running the analysis

1. Pull the image by running this command from the root of the repository:
```
docker pull cchang5/dsci_522_group_8_bank_marketing:0aacd5b
```
2. After building the image successfully, open VS code, navigate to the root of this project and run this command to run the container:
```
docker-compose run --rm analysis-env bash
```
3. Navigate to the root of this project on your computer using the command line 
and enter the following command to reset the project to a clean state 
(i.e., remove all files generated by previous runs of the analysis):
Sometimes your root folder inside the container is work/. So make sure you have navigated to root folder by running `cd work/`!!!!!!! ⚠️⚠️⚠️⚠️
```
make clean
```
4. To run the analysis in its entirety, 
enter the following command in the terminal in the project root:
```
make all
```
⚠️⚠️⚠️ The whole process might take more than one hour to run. You might want to grab a cup of coffee while doing this.

## Developer notes

### Working with the project in the container using Jupyter lab

1. Navigate to the root of this project on your computer using the command line and enter the following command:

```
docker compose up
```

2. In the terminal, look for a URL that starts with
`http://127.0.0.1:8888/lab?token=` 
Copy and paste that URL into your browser and change '8888' to '8889'

3. You should now see the Jupyter lab IDE in your browser, 
with all the project files visible in the file browser pane 
on the left side of the screen.

## Clean up

1. To shut down the container and clean up the resources, 
type `Cntrl` + `C` in the terminal
where you launched the container, and then type `docker compose rm`

## Dependencies
-    Docker: software used to build the container (compuational environment) [`Dockerfile`](Dockerfile)
-   `conda` (version 23.9.0 or higher)
-   `nb_conda_kernels` (version 2.3.1 or higher)
-   Python and packages listed in [`environment.yml`](environment.yml)

## Contributing
We welcome all contributions! Check out [`CONTRIBUTING.md`](CONTRIBUTING.md)

## License

This project is licensed under the MIT License and Creative Commons License 4.0 (NonCommerical Attribution) - see LICENSE.md for details.

## References

1.  Moro,S., Rita,P., and Cortez,P., 2012. Bank Marketing. UCI Machine Learning Repository. <https://doi.org/10.24432/C5K306>"
2.  Timbers,T. , Ostblom,J., and Lee,M., 2023. Breast Cancer Predictor Report. GitHub repository, <https://github.com/ttimbers/breast_cancer_predictor_py/blob/0.0.1/src/breast_cancer_predictor_report.ipynb>",
3.  Moro, S., Cortez, P., & Rita, P. (2014). A data-driven approach to predict the success of bank telemarketing. Decis. Support Syst., 62, 22-31.
4.  Alsolami, F.J., Saleem, F., & Al-Ghamdi, A.S. (2020). Predicting the Accuracy for Telemarketing Process in Banks Using Data Mining.
5.  Vajiramedhin, C., & Suebsing, A. (2014). Feature Selection with Data Balancing for Prediction of Bank Telemarketing. Applied mathematical sciences, 8, 5667-5672.
6.  Moura, A.F., Pinho, C.M., Napolitano, D.M., Martins, F.S., & Fornari Junior, J.C. (2020). Optimization of operational costs of Call centers employing classification techniques. Research, Society and Development, 9.
