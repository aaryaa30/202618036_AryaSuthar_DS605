## LAB04 End-to-End Machine Learning Project: Airbnb Price Prediction
### THis project is used for predicting the price Airbnb listings in NY city.
It uses the dataset: Kaggle New York City Airbnb Open Data (AB_NYC_2019.csv)\
In this different regression models were trained and compared to find a suitable model for price prediction\
From the project a streamlit application is made where user can enter Airbnb listings and can know the estimated price for the same.

### Objectives:
-Analyze the Airbnb dataset and understand the factors affecting price.\
-Clean and prepare the data for machine learning.\
-Handle missing values and extreme values.\
-Perform feature engineering.\
-Apply preprocessing to numerical and categorical features.\
-Train and compare different regression models.\
-Tune the selected model using hyperparameter tuning.\
-Evaluate the final model using regression metrics.\
-Save the trained preprocessing and model pipeline.\
-Build a Streamlit application for price prediction.

### The dataset contains information about Airbnb listings such as:
Neighbourhood group\
Neighbourhood\
Latitude and longitude\
Room type\
Minimum nights\
Number of reviews\
Reviews per month\
Host listing count\
Availability\
Price\
The original dataset contains 48,895 rows and 16 columns.\
The dataset was first analyzed to understand its structure, missing values, duplicate records, distributions, and extreme values.

### Models Used
Three regression models were compared:\
Linear Regression\
Random Forest Regressor\
Gradient Boosting Regressor

The models were evaluated using:\
MAE (Mean Absolute Error)\
RMSE (Root Mean Squared Error)\
R² Score
