from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"
INPUT_PATH = DATA_DIR / "Messy_Employee_dataset.csv"
OUTPUT_PATH = DATA_DIR / "cleared_employee_dataset.csv"


def read_csv(path: Path = INPUT_PATH) -> pd.DataFrame:
    """Read a CSV file with predefined column data types."""
    # Column names contain trailing spaces in the source CSV file.
    return pd.read_csv(
        path,
        sep=",",
        skipinitialspace=True,
        engine="python",
        encoding="utf-8",
        na_values=["N/A"],
        dtype={
            "Employee_ID": str,
            "First_Name": str,
            "Last_Name": str,
            "Age": "Int64",
            "Department_Region    ": str,
            "Status  ": str,
            "Join_Date ": str,
            "Salary   ": str,
            "Email                       ": str,
            "Phone      ": str,
            "Performance_Score": str,
            "Remote_Work": "boolean",
        },
    )


def write_csv(data: pd.DataFrame, path: Path = OUTPUT_PATH) -> str:
    """Write a DataFrame to a CSV file."""
    data.to_csv(path, index=True, mode="w")
    return str(path)
