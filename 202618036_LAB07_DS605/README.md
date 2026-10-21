## Lab 07 Image Representation, PCA, Eigenfaces and Face Recognition ##

Name- Arya Suthar\
Id - 202618036

Dataset: AT&T Database of Faces (ORL)

This lab focuses on representing images numerically, reducing their dimensionality using PCA/eigenfaces, performing face matchingin the reduced space, and comparing the result with traditional machine-learning classifiers.

Dataset
-The experiment uses the ORL (AT&T) Face Database.\
-Total images: 400\
-Number of subjects: 40\
-Images per subject: 10\
-Image dimensions: 112 × 92 pixels\
-Features per image: 10,304 grayscale pixel values

Images were converted into grayscale pixel matrices and flattened into feature vectors. PCA was implemented using NumPy covariance eigendecomposition and SVD. The principal components were used for dimensionality reduction, eigenface visualization, image reconstruction, and storage comparison. Face recognition was performed using Euclidean distance, KNN, and SVM.\

PCA reduced the image features from 10,304 to 99 components while retaining at least 90% variance. Raw-pixel nearest-neighbor accuracy was 1.25%, while PCA nearest-neighbor accuracy reached 98.75%. KNN achieved 82.50% accuracy and SVM achieved 93.75%. The PCA representation reduced the calculated storage requirement by approximately 67.79%, including the basis and mean face.
