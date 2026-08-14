LAB 02-Vectorized Programming with NumPy and Data Wrangling with Pandas
 **Name:**Arya Suthar
**Student ID:**202618036

Dataset: Titanic Dataset  
Source:Kaggle Titanic Dataset  
File used:train.csv

The Titanic dataset contains information about passengers, including their age, sex, passenger class, fare, family members, port of embarkation, and survival status.
Part A - Vectorized Programming with NumPy:
tasks-
-Created arrays using random integers.
- Calculated minimum, maximum, mean, median, and standard deviation.
- Used `np.arange()`, `np.zeros()`, `np.ones()`, and `np.linspace()`.
- Compared `np.linspace()` and `np.arange()`.
- Demonstrated indexing, rows, columns, and slicing.
- Created and worked with 2D and 3D arrays.
- Used `reshape()` and `flatten()`.
- Performed vectorized arithmetic operations.
- Performed matrix multiplication using `@`.
- Calculated matrix transpose, determinant, and inverse.
- Verified the matrix inverse using `np.allclose()`.
- Generated normally distributed data and visualized it using a histogram.

Part-B Data Wrangling with Pandas: Titanic Dataset
- Loaded and inspected the dataset using `head()`, `tail()`, `shape`, `columns`, `info()`, and `describe()`.
- Used `loc` and `iloc` for selecting rows and columns.
- Filtered and queried passenger records using Boolean conditions.
- Used `groupby()` and aggregation to calculate survival rates, passenger counts, average age, and average fare.
- Identified and handled missing values.
- Filled missing Age values using mean imputation and demonstrated other imputation methods.
- Detected Fare outliers using the IQR method.
- Created `FamilySize` and `IsAlone` features.
- Created a pivot table showing mean survival rates by Sex and Pclass.
- Created visualizations to analyze the dataset

OBSERVATIONS:
-Here the first class passengers had a higher survival rate than second and third class passengers.
-The female passengers had a higher survival rate compared to the male passengers. This can be said from the Sex × Pclass pivot table.
-fare and pclass show a noticeable relationship.
-Passengers travelling with family had different survival pattern compared to the one travelling alone.
-from the Age vs Fare scatter plotit can be said that people with higher fare were less and most were with relatively lower fares.
-the age and cabin had missing values.

Files Included

- `202618036_LAB02_DS605.ipynb` 
- `train.csv` - 
- `cleaned_titanic.csv` 
- `missing_values.png` 
- `correlation_heatmap.png` 
- `survival_rate_by_sex.png` 
- `age_vs_fare.png` 
- `README.md` 