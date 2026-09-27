## Lab Assignment - 5 ##
Id - 202618036
### Machine Learning with Scikit-learn and From Scratch ###

Dataset : UCI Productivity Prediction of Garment Employees
This file contains lab 05 implementation of regression and classification using both Scikit-learn Implementation and From Scratch Implementation

PART A Scikit-learn Implementation:
- used Linear Regression and Logistic Regression
- Regression evaluated using - MAE, MSE, R^2
- Classification evaluated using - Accuracy , Precision, Recall, F1 Score

PART B From-Scratch Implementation:
- It was implemented using Pandas and Numpy without using Scikit-learn model

Part C: Optimization and Comparison
- The manual implementations were compared with the Scikit-learn implementations.
- The Linear Regression implementation was improved using L2 regularization.
- The Logistic Regression implementation was improved by tuning the learning rate and number of epochs

Observations:

For scratch Implementaion:
- The improved Linear regression produced a small improvement in R².
- The improved Logistic regression increased accuracy from 0.708333 to 0.733333.
- Even the F1 score for logistic improved from 0.824121 to 0.835897.
- The from scratch implementation had comparatively small prediction time.
- The improved Logistic Regression required more training time because multiple learning-rate and epoch settings were tested.
