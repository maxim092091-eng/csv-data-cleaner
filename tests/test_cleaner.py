import pandas as pd
from csv_data_cleaner.cleaner import clean_data

df = pd.DataFrame(
    {
        "Employee_ID": ["EMP1000", "EMP1001"],
        " Age": [25, pd.NA],
        "Department_Region    ": ["DevOps-California    ", "Finance-Texas        "],
        " Salary   ": ["59767.65 ", "59767.65 "],
        " Join_Date ": ["4/2/2021  ", "7/10/2020 "],
        " First_Name": ["  Bob       ", " Anna  "],
    }
)


def test_clean():
    expected_df = pd.DataFrame(
        {
            "age": [25, 25],
            "department": ["DevOps", "Finance"],
            "region": ["California", "Texas"],
            "salary": [59767.65, 59767.65],
            "join_date": pd.to_datetime(["2021-04-02", "2020-07-10"]),
            "first_name": ["Bob", "Anna"],
        },
        index=pd.Index(["EMP1000", "EMP1001"], name="employee_id"),
    )

    cleaned_df = clean_data(df)
    pd.testing.assert_frame_equal(cleaned_df, expected_df)
