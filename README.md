# csv-data-cleaner
A Python project for cleaning and standardizing an employee dataset using pandas.

## Features

- Clean messy CSV datasets by standardizing data types, dates, and categorical values.
- Display dataset inspection results before cleaning.
- Generate an audit report showing changes made during cleaning.
- Save the cleaned dataset in the same directory as the input file.

## Requirements

- Python 3.10+

## Technologies

- Python
- Pandas

## Installation

### Clone the repository

```bash
git clone https://github.com/maxim092091-eng/csv-data-cleaner.git
``` 

### Navigate to the project directory

```bash
cd csv-data-cleaner
``` 

### Create a virtual environment

#### On Windows

```bash
py -m venv .venv
```

#### On Linux/macOS

```bash
python3 -m venv .venv
```

### Activate the virtual environment

#### On Windows

```bash
.venv\Scripts\activate
```

#### On Linux/macOS

```bash
source .venv/bin/activate
```

### Install the project

```bash
python -m pip install .
```

## Usage

Run the application:

```bash
csv-cleaner
```

## Project Structure

```text
csv-data-cleaner/
├── src/
│   └── csv_data_cleaner/
|       ├── data/
|       |      └── Messy_Employee_dataset.csv
│       ├── cleaner.py
│       ├── data_inspection.py
|       ├── data_io.py
│       └── main.py
├── tests/
│   └── test_cleaner.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Tests

Run the tests with:

```bash
pytest
```

## Project

This project was built following the [Clean a CSV with Pandas](https://roadmap.sh/projects/clean-csv) project requirements from Roadmap.sh.

## License

This project is licensed under the MIT License.

## Author

Created by [Maxim](https://github.com/maxim092091-eng).
