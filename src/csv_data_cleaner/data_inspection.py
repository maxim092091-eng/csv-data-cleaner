import pandas as pd


def inspect(df: pd.DataFrame) -> None:
    """Display an overview of the input data."""
    print("\nData inspectiom")

    print(f"Shape: {df.shape}")

    print(f"\nFirst rows:\n{df.head()}")

    print(f"\nData types:\n{df.dtypes}")

    print(f"\nMissing values:\n{df.isna().sum()}")

    print(f"\nDuplicate rows:\n{df.duplicated().sum()}")
    
    print(f"\nUnique rows:\n{df.nunique()}")


def audit_data(
    original_df: pd.DataFrame,
    cleaned_df: pd.DataFrame,
) -> None:
    """Display cleaning changes."""
    print("\nAudit")

    print(f"Original shape: {original_df.shape}")
    print(f"Cleaned shape: {cleaned_df.shape}")

    print(f"\nData types before:\n{original_df.dtypes}")
    print(f"\nData types after:\n{cleaned_df.dtypes}")

    print(f"\nColumn names before:\n{original_df.columns.tolist()}")
    print(f"\nColumn names after:\n{cleaned_df.columns.tolist()}")

    print(f"\nMissing values before:\n{original_df.isna().sum()}")
    print(f"\nMissing values after:\n{cleaned_df.isna().sum()}")
