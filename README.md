# Habit Tracker App

This is a simple command-line app, built with Python 3. 
This app helps you to create, manage and analyze your good habits.

## Features

- Create and manage daily or weekly habits
- Track your progress with check-ins
- View current and longest streaks
- Analyze skipped or most consistent habits
- Automatically saves and loads your data using SQLite
- Fully tested and documented

## Installation

Install the required packages:
```shell
pip install -r requirements.txt
```

## Environment setup

Make sure that the source folder (src/) is included in your PYTHONPATH.
If you're using PyCharm or VS Code, this is automatically handled via the included .env file.
Otherwise, you can set it manually in PowerShell :
```shell
$env:PYTHONPATH = "src"
```

## Running the app

Start the interactive command-line interface:
```shell
python main.py
```

## Running the tests

Run all tests using pytest code coverage:
```shell
pytest --cov=src tests/
```
You can generate an HTML coverage report:
```shell
pytest --cov=src --cov-report=html tests/
```
You will find the coverage report in the htmlcov/ folder.
Open htmlcov/index.html in your browser to view it.

## Project structure

habit_tracker/
├── src/
│   ├── __init__.py          # Makes src a package
│   ├── habit.py             # Habit class
│   ├── habit_manager.py     # HabitManager class
│   ├── analyze.py           # Tools for analytics
│   ├── db.py                # SQLite database handling
│   └── fixtures.py          # Predefined habit data for testing/demo
├── tests/                   # Test modules
│   ├── __init__.py          # Makes tests a package
│   ├── test_habit.py
│   ├── test_habit_manager.py
│   ├── test_analyze.py
│   └── test_db.py
├── main.py                  # Entry point for CLI with questionary-powered menu
├── .env                     # PYTHONPATH configuration
├── .gitignore               # Files and folders to exclude from GitHub
├── README.md
└── requirements.txt         # Required packages

## Author

Created by Zehra Cebi for the IU course "Object Oriented and Functional Programming with Python".