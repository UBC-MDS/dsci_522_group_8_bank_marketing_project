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

To replicate this analysis: Clone this repository:

```         
git clone https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project
```

Pull the image by running this command from the root of the repository:
```
docker pull cchang5/dsci_522_group_8_bank_marketing:58fe205
```

After building the image successfully, run this command to run the container:
```
docker compose up
```
Copy the URL starting with `http://127.0.0.1:8888/lab?token=`, then paste and replace the last "8" with a "9" so the URL looks like `http://127.0.0.1:8889/lab?token=` to your browser to open Jupyter Lab. 

To run the analysis, enter the following commands in the terminal in the project root:

```         
# Download the data from zip url
python scripts/download_data.py \
   --url='https://archive.ics.uci.edu/static/public/222/bank+marketing.zip' \
   --write_to='data/raw'

# Unzip the file and subtract the files into folder data/raw/bank
python scripts/unzip.py \
   --path_to_zip_file='data/raw/bank.zip' \
   --directory_to_extract_to='data/raw/bank'

# split data into train and test sets and save them to csv file
python scripts/train_test_split.py \
   --raw-data='data/raw/bank/bank-full.csv' \
   --data-to='data/processed' \
   --seed=522

# Perform exploratory data analysis (EDA) on the given df
python scripts/EDA.py \
   --data-frame = "data/raw/bank/bank-full.csv" \
   --plot-to = "results/figures"

# split train_df and test_df into features and target and create preprocessor
python scripts/preprocessor.py \
   --raw_train=data/split/train_df.csv \
   --raw_test=data/split/test_df.csv \
   --data_to=data/processed \
   --preprocessor_to=results/models

# examine 5 candidate models by calculating score metrics
python scripts/model_selection.py \
    --x_train=data/processed/X_train.csv \
    --y_train=data/processed/y_train.csv  \
    --preprocessor=results/models/preprocessor.pickle \
    --pipeline-to=results/models \
    --results_to=results/metrics \
    --seed=522

# Scoring metric for svc balanced model
python scripts/scoring_metric.py  \
   --x_train=data/processed/X_train.csv  \
   --y_train=data/processed/y_train.csv  \
   --x_test=data/processed/X_test.csv  \
   --y_test=data/processed/y_test.csv  \
   --model_type=results/models/model_pipeline.pickle \
   --results_to=results/metrics \
   --seed=522

# Optimization and Accuracy/Recall Scores

python scripts/optimization.py \
  --df=data/bank-full.csv \
  --x_test=data/processed/X_test.csv \
  --y_test=data/processed/y_test.csv \
  --results_to=results/metrics \
  --results_to_1=results/metrics \
  --plot_to=results/figures
```

After you've run the above command line (this might take a while cuz we are optimizing the svc_bal here), you can run the command in the root folder to render the jupyter book:
```
jupyter-book build notebooks
```
Then, you can navigate to `notebooks/_build/html` and click the `index.html` in the folder to see the rendered report.

## Running Tests
Navigate to the project root directory and use the following command in terminal to test the functions used in this project. 
```
pytest test/*
```

## Clean up

To shut down the container and clean up the resources, 
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
