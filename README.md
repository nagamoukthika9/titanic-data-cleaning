Titanic Dataset Cleaning and Preprocessing

Project Overview

This project focuses on cleaning and preprocessing the Titanic dataset using Python and Pandas. The objective is to improve data quality and prepare the dataset for analysis.

Tools Used

- Python
- Pandas
- NumPy
- Excel

Dataset

The project uses the Titanic dataset containing passenger information, including passenger class, survival status, age, fare, cabin, and embarkation details.

Data Quality Issues Identified

- Missing values in several columns
- Incomplete passenger information
- Potential duplicate records
- Inconsistent data formats and data types

Cleaning and Preprocessing

- Inspected missing values and data types
- Removed duplicate rows
- Filled missing age and fare values using the median
- Handled missing categorical and other values according to the cleaning script
- Exported the cleaned dataset to CSV and Excel formats
- Recorded cleaning actions in a change log

Project Files

- "clean_data.py" — Python cleaning script
- "requirements.txt" — Required Python libraries
- "titanic_cleaned.csv" — Cleaned dataset in CSV format
- "titanic_cleaned.xlsx" — Cleaned dataset in Excel format
- "change_log.txt" — Record of cleaning actions

How to Run

1. Install Python.

2. Install dependencies:
   
   "python -m pip install -r requirements.txt"

3. Run the script:
   
   "python clean_data.py"

Validation

The script checks missing values and duplicate rows after cleaning. The final run reported zero missing values in the displayed columns and zero duplicate rows.

Conclusion

The project demonstrates basic data cleaning and preprocessing using Python and Pandas. The cleaned dataset is prepared for further analysis.
