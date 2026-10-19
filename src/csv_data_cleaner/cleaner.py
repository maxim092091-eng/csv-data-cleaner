import pandas as pd
from pandas.api.types import is_string_dtype


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert columns to numeric and datetime types if they meet the conditions.
    Standardize categorical values.
    """
    # Standardize column names.
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    # Standardize categorical values.
    for column in df.columns:
        if is_string_dtype(df[column]):
            df[column] = df[column].str.strip()

    # Set index
    df = df.set_index("employee_id")

    # Fill missing 'age' with the median
    median_age = df["age"].median()
    df["age"] = df["age"].fillna(median_age).astype("int64")

    # Split the combined column into two new, clean columns
    position = df.columns.get_loc("department_region")
    split_columns = df["department_region"].str.split("-", expand=True)

    df = df.drop(columns=["department_region"])

    df.insert(position, "department", split_columns[0])
    df.insert(position + 1, "region", split_columns[1])

    # Convert Salary column to numeric after stripping whitespace from column names
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    # Convert to datetime after removing leading and trailing whitespace
    df["join_date"] = pd.to_datetime(
        df["join_date"],
        errors="coerce",
    )

    return df
