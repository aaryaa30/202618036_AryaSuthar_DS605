## Lab 06 Feature Extraction and Machine Learning with Image and Text Data ##

Name- Arya Suthar\
Id - 202618036

Dataset:
- Image Dataset: Asphalt Crack Dataset - 400 Images (Mendeley Data)
- Text Dataset: Email Spam Classification Dataset - 5,172 Emails (Kaggle)

This lab focuses on image feature extraction, image classification, text vectorization, spam classification, and improving the representation.

PART - A 
There are total of 2 classes in this data each containing 200 images.\
OpenCV was used to read and work with the images

PART - B
The dataset contains 5172 email records and a Prediction column representing the class - Spam and Not Spam.\
The email word-frequency data was converted into text representation by reconstructing the words according to their frequency.

For improving the representation,\
max_features=2000 was used to reduce the features.\
This reduced the number of generated features while keeping the classification performance almost unchanged.

Improved Results\
Accuracy: 97.20%\
Precision: 93.85%\
Recall: 96.67%
F1 Score: 95.24%
