# SQL Practice with Python (Window Functions, Stored Procedures & Views)

## Overview

This repository contains examples and practice scripts demonstrating advanced SQL concepts including **Window Functions**, **Stored Procedures**, and **Views** using a MySQL database. It also shows how to interact with the database using Python and `pymysql`.

---

## Contents

### 1. Database Setup for Window Functions

- Created a sample database with the following table:
  - `employee_sales`: stores sales transactions by employees.
  
| Column       | Description                  |
|--------------|------------------------------|
| `sale_id`    | Primary key, unique sale ID  |
| `employee_id`| Employee who made the sale   |
| `sale_date`  | Date of sale                 |
| `sale_amount`| Amount of sale               |
| `region`     | Region of sale               |

---

### 2. Window Function Practice Queries

Examples of SQL queries using window functions:

- `ROW_NUMBER()` — Assigned unique row numbers per employee based on sale date.
- `RANK()` / `DENSE_RANK()` — Ranked employees by their total sales.
- `LAG()` / `LEAD()` — Compared sales amounts between current and previous/following rows.
- `FIRST_VALUE()` / `LAST_VALUE()` — Retrieved first and last sale amounts per employee.
- `NTILE()` — Distributed sales records into equal groups.
- `SUM() OVER (PARTITION BY ...)` — Calculated running totals per employee.
- `AVG()`, `MIN()`, `MAX()` window aggregates.

---

### 3. Stored Procedures

- Created stored procedures on `employee_sales` table for reusable logic.
- Examples include:
  - Retrieve total sales for a specific employee.
  - Calculated total sales by region.
  - Count sales within a date range.
  - Calculated monthly sales summary.
  - Insert a new sale record.
  
- Both parameterized and non-parameterized queries are included.

---

### 4. Views

- Created SQL Views for summarizing sales data:
  - `total_sales_by_employee` — total sales grouped by employee.
  - `sales_count_by_region` — count of sales per region.
- Python scripts to create and query views dynamically.
- Logging is implemented to track execution.

---

### 5. Python Integration

- Used `pymysql` to connect Python scripts to the MySQL database.
- Utilized environment variables for secure credential management (`dotenv`).
- Incorporated `pandas` for nicely formatted output of query results.
- Implemented error handling and logging for robustness.
- Scripts can run multiple SQL queries (CREATE, SELECT) sequentially.

---