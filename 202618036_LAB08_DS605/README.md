## Lab 08 Decision Trees and Support Vector Machines ##

Name- Arya Suthar\
Id - 202618036

Dataset : UCI Banknote Authentication (1,372 samples, 4 features, 2 classes)

This lab implements Decision Tree and Support Vector Machine both manually and with Scikit-learn and evaluating their performance.

### Results and Observations

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Manual Decision Tree | 0.9709 | 0.9453 | 0.9918 | 0.9680 |
| Scikit-learn Decision Tree | 0.9927 | 0.9839 | 1.0000 | 0.9919 |
| Manual Linear SVM | 0.9745 | 0.9457 | 1.0000 | 0.9721 |
| Scikit-learn Linear SVM | 0.9745 | 0.9457 | 1.0000 | 0.9721 |
| Scikit-learn RBF SVM | 1.0000 | 1.0000 | 1.0000 | 1.0000 |


Compared five models using all four Banknote Authentication features:
-Manual Decision Tree
-Scikit-learn Decision Tree
-Manual Linear SVM
-Scikit-learn Linear SVM
-Scikit-learn RBF SVM\

The Scikit-learn RBF SVM achieved the best performance, with 100% accuracy, precision, recall and F1-score on the test set.\
The Scikit-learn Decision Tree achieved 99.27% accuracy, while the manual Decision Tree achieved 97.09%.\
The manual Linear SVM achieved 97.45% accuracy and matched the reported performance of the Scikit-learn Linear SVM.\
The Scikit-learn implementations takes comparatively less time and gets trained faster than the manual implementations.
