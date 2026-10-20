import pandas as pd
from pathlib import Path

# Project folder paths
BASE_DIR = Path(__file__).resolve().parent
RAW_FILE = BASE_DIR / "data" / "raw" / "titanic3.xls"
OUTPUT_DIR = BASE_DIR / "data" / "cleaned"
REPORT_DIR = BASE_DIR / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load the Titanic dataset
df = pd.read_excel(RAW_FILE)

print("Original dataset shape:", df.shape)
print("\nMissing values before cleaning:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Keep a record of changes
change_log = []

# Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
change_log.append("Standardized column names.")

# Remove duplicate rows
duplicate_count = int(df.duplicated().sum())
df = df.drop_duplicates()
change_log.append(f"Removed {duplicate_count} duplicate rows.")

# Remove extra spaces from text
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].apply(
        lambda value: value.strip()
        if isinstance(value, str) else value
    )

change_log.append("Removed extra spaces from text values.")

# Handle missing values
for column in df.columns:
    missing = int(df[column].isnull().sum())

    if missing > 0:
        if column in ["age", "fare"]:
            df[column] = df[column].fillna(df[column].median())
            change_log.append(
                f"Filled missing {column} values with the median."
            )
        elif column in [
    "name", "ticket", "cabin", "boat",
    "body", "home.dest", "embarked"
]:
            df[column] = df[column].fillna("Unknown")
            change_log.append(
                f"Filled missing {column} values with 'Unknown'."
            )
        else:
            change_log.append(
                f"Missing values remain in {column} for review."
            )

# Save the cleaned dataset
df.to_csv(OUTPUT_DIR / "titanic_cleaned.csv", index=False)
df.to_excel(OUTPUT_DIR / "titanic_cleaned.xlsx", index=False)

# Save the change log and final quality checks
with open(REPORT_DIR / "change_log.txt", "w", encoding="utf-8") as file:
    file.write("TITANIC DATA CLEANING REPORT\n")
    file.write("============================\n")
    for change in change_log:
        file.write("- " + change + "\n")

    file.write("\nFinal dataset shape: " + str(df.shape) + "\n")
    file.write("\nMissing values after cleaning:\n")
    file.write(df.isnull().sum().to_string() + "\n")
    file.write(
        "\nDuplicate rows remaining: "
        + str(df.duplicated().sum()) + "\n"
    )

print("\nCleaning completed!")
print("Cleaned files saved in:", OUTPUT_DIR)
print("Change log saved in:", REPORT_DIR)
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nDuplicate rows remaining:", df.duplicated().sum())