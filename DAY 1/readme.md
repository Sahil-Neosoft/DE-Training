# Overview

This repository is focused on several key programming concepts and tasks, including Object-Oriented Programming (OOP), working with dates and times, file handling, API integration, data storage, and aggregation queries.

---

## Object-Oriented Programming (OOP)

- Defined and used classes to model data and behavior.
- Understood and implemented the `__init__` method, along with instance and class variables.
- Created methods inside classes and used `self` for accessing instance data.
- Instantiated objects and worked with them in various simple class-based programs.
- Learned and applied inheritance and method overriding to extend and customize class behavior.

---

## Date and Time Manipulation

- Created date objects and retrieved today’s date.
- Accessed individual components such as year, month, and day.
- Created and worked with time and datetime objects.
- Performed date arithmetic using `timedelta` to add or subtract time intervals.

---

## File Handling

- Wrote data to text files and read from them.
- Handled CSV files by writing cleaned data to CSV and reading from CSV files.

---

## API Integration

- Selected a public API of REST Countries.
- Used the `requests` module to send GET requests to the API.
- Parsed and cleaned JSON responses.
- Extracted relevant fields such as country names, population, region, area, capital etc.

---

## Data Storage

### Saving Data to CSV

- Used the `pandas` module to create and write cleaned data to CSV files.
- Included appropriate column headers.

### Storing Data in MySQL

- Set up a MySQL database (local).
- Created tables matching the structure of the data.
- Used `pymysql` to connect to the database.
- Inserted API data into MySQL tables using parameterized queries to prevent SQL injection.
- Managed correct data types during insertion.

---

## Aggregation and Queries

- Performed basic aggregation queries such as:
  - `COUNT(*)` to get the total number of records inserted.
  - `SUM()` for totals like population or sales.
  - `AVG()` for averages like temperature or income.
  - `GROUP BY` to summarize data by categories like country or sales category.
- Printed these summaries in a readable format using `tabulate`.

---