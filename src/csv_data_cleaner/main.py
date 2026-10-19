from .cleaner import clean_data
from .data_inspection import audit_data, inspect
from .data_io import read_csv, write_csv


def main() -> None:
    """Handle the CSV cleaning workflow from import to export."""

    original_df = read_csv()

    inspect(original_df)

    cleaned_df = clean_data(original_df.copy())

    text = write_csv(cleaned_df)
    print(f"\nCleared CSV saved to: {text}")

    audit_data(original_df, cleaned_df)


if __name__ == "__main__":
    main()
