"""
Titanic Dataset Cleaning Project
MCA Python / Data Analytics Practical

Input:
    Titanic.csv (place it in this folder)
Output:
    Titanic_cleaned.csv

If Titanic.csv is not found, the program downloads the commonly used
Kaggle Titanic training dataset from a public GitHub mirror.
Internet access is required only for this fallback.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "Titanic.csv"
OUTPUT_FILE = BASE_DIR / "Titanic_cleaned.csv"
FALLBACK_URL = (
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)


def load_dataset():
    """Load local Titanic.csv, or use a public dataset fallback."""
    if INPUT_FILE.exists():
        print(f"Loading dataset: {INPUT_FILE.name}")
        return pd.read_csv(INPUT_FILE)

    print("Titanic.csv was not found in this folder.")
    print("Trying to download a public Titanic dataset...")
    try:
        df = pd.read_csv(FALLBACK_URL)
        df.to_csv(INPUT_FILE, index=False)
        print("Dataset downloaded and saved as Titanic.csv")
        return df
    except Exception as exc:
        raise FileNotFoundError(
            "Could not find Titanic.csv or download the fallback dataset. "
            "Place your Titanic CSV in this folder and run again."
        ) from exc


def clean_dataset(df):
    """Clean missing values, encode Sex, and drop selected columns."""
    df = df.copy()

    print("\nMissing values before cleaning:")
    print(df.isnull().sum().to_string())

    # Impute Age with the median, which is less affected by outliers than the mean.
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].median())

    # Fill missing Embarked values with the most frequent category.
    if "Embarked" in df.columns and df["Embarked"].isnull().any():
        modes = df["Embarked"].mode()
        if not modes.empty:
            df["Embarked"] = df["Embarked"].fillna(modes.iloc[0])

    # One-hot encode Sex if present.
    if "Sex" in df.columns:
        df = pd.get_dummies(df, columns=["Sex"], dtype=int)

    # Drop columns selected as irrelevant for this basic exercise.
    # Cabin is often highly incomplete; Name and Ticket are not used here.
    columns_to_drop = ["PassengerId", "Name", "Ticket", "Cabin"]
    df = df.drop(
        columns=[col for col in columns_to_drop if col in df.columns],
        errors="ignore",
    )

    return df


def main():
    try:
        original_df = load_dataset()
        print(f"\nOriginal dataset shape: {original_df.shape}")

        cleaned_df = clean_dataset(original_df)
        cleaned_df.to_csv(OUTPUT_FILE, index=False)

        print(f"\nCleaned dataset shape: {cleaned_df.shape}")
        print("\nFirst 5 cleaned rows:")
        print(cleaned_df.head().to_string(index=False))
        print("\nMissing values after cleaning:")
        print(cleaned_df.isnull().sum().to_string())
        print(f"\nSUCCESS: Cleaned CSV saved to:\n{OUTPUT_FILE}")
    except Exception as exc:
        print(f"\nERROR: {exc}")


if __name__ == "__main__":
    main()
