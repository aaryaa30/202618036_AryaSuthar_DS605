Lab 03 — Scikit-learn: Data Preprocessing and Model Performance Evaluation
* **Name:** Arya Suthar
* **Student ID:** 202618036
* 
## Dataset:
**Hotel Booking Dataset**

## Objective
The objective of this lab is to perform data cleaning and preprocessing, handle missing values and outliers, prevent data leakage, and compare Logistic Regression and Decision Tree classification models using two different preprocessing pipelines.

## Data Preprocessing

* Missing-value were counted and percentages were calculated for all columns.
* Columns with very high missingness were examined and `company` was removed because of its high percentage of missing values.
* `reservation_status` and `reservation_status_date` were removed to prevent data leakage because they directly reveal the final booking outcome.
* Numerical features were checked for outliers using boxplots and the IQR method.
* Clear/extreme outliers were removed where appropriate.
* The final cleaned dataset contained **115,596 rows**."`

The train-test split was used for all experiments:

* Test size: 20%
* Stratification: `y`
* Random state: 42

## Models

Two classification models were trained using both preprocessing pipelines:

1. Logistic Regression with `max_iter=1000`
2. Decision Tree Classifier with `random_state=42`



## Observations

1. Decision Tree with Pipeline A achieved the best overall result, with a testing accuracy of 86.75% and an F1-score of 0.8212.
2. StandardScaler performed slightly better than MinMaxScaler for Logistic Regression, although the difference was small.
3. Scaling had almost no effect on the Decision Tree because its results with StandardScaler and MinMaxScaler were nearly identical.
4. Logistic Regression showed very little overfitting because the difference between training and testing accuracy was small.
5. The Decision Tree showed noticeable overfitting, with training accuracy around 99.6% compared with testing accuracy around 86.7%.
