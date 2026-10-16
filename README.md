# Titanic Dataset Cleaning Project

## Project Overview
This project cleans the Titanic dataset using Python and Pandas. It handles missing ages, encodes gender, removes unnecessary columns, and saves the cleaned data as a CSV file.

## Objectives
- Load the Titanic dataset.
- Identify and handle missing values.
- Fill missing Age values using the median.
- Encode the Sex column using one-hot encoding.
- Remove selected irrelevant columns.
- Save the cleaned dataset to a CSV file.

## Tools Used
- Python
- Pandas
- Visual Studio Code
- GitHub

## Data Cleaning Steps
1. Load the Titanic CSV dataset.
2. Check missing values.
3. Fill missing Age values using the median.
4. Fill missing Embarked values using the most frequent value.
5. Remove the Cabin column.
6. Encode Sex into Sex_female and Sex_male.
7. Remove PassengerId, Name, and Ticket.
8. Save the cleaned dataset as Titanic_cleaned.csv.
9. Verify that no missing values remain.

## Project Files
- `titanic_cleaning.py` — Python cleaning script.
- `Titanic_cleaned.csv` — Cleaned dataset.

## How to Run
Install Pandas:

```bash
python -m pip install pandas
```

Run the script:

```bash
python titanic_cleaning.py
```

## Output
The program generates a cleaned CSV file named Titanic_cleaned.csv.

## Author
Gayatri Khode
