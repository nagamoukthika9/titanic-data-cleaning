Titanic Dataset Cleaning and Preprocessing

Project Overview

This project focuses on cleaning and preprocessing the Titanic dataset using Python and Pandas. The objective is to improve data quality and prepare the dataset for analysis.

Tools Used

- Python
- Pandas
- NumPy
- VS Code

Dataset

The Titanic dataset contains passenger information, including passenger class, survival status, age, sex, fare, and embarkation port.

Data Quality Issues Identified

- Missing values in several columns
- Missing age and fare values
- Missing embarkation information
- Duplicate row verification
- Inconsistent text formatting and data types

Cleaning Steps Performed

- Checked missing values before and after cleaning
- Removed duplicate rows, if present
- Filled missing numerical values using the median
- Handled missing categorical values
- Standardized text values and data types
- Exported the cleaned dataset to CSV and Excel files

Project Files

- "data/raw/titanic3.xls" — Original dataset
- "data/cleaned/titanic_cleaned.csv" — Cleaned CSV dataset
- "data/cleaned/titanic_cleaned.xlsx" — Cleaned Excel dataset
- "reports/change_log.txt" — Record of cleaning changes
- "clean_data.py" — Python cleaning script

Results

The original dataset contained 1,309 rows and 14 columns. After cleaning, the script reported zero missing values and zero duplicate rows.

How to Run

1. Install Python.
2. Install the required libraries:
   "python -m pip install pandas numpy xlrd openpyxl"
3. Run the script:
   "python clean_data.py"

Conclusion

The project demonstrates basic data cleaning and preprocessing using Python and Pandas. The cleaned dataset is ready for further exploratory data analysis.