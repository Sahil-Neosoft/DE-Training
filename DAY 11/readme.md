# PySpark and Spark SQL Concepts

This repository documented and demonstrated key concepts related to Spark SQL and PySpark, focusing on various data processing techniques using window functions, aggregate functions, user-defined functions, and data writing operations.

## Topics Covered

### 1. Window Functions

Window functions were used to perform calculations across a set of table rows that were somehow related to the current row. These operations did not require a GROUP BY and included:

- **ROW_NUMBER()**  
  This function was used to assign a unique sequential number to rows within a partition of a dataset.

- **RANK vs DENSE_RANK**  
  - `RANK()` assigned the same rank to duplicate values but skipped subsequent ranks.
  - `DENSE_RANK()` also assigned the same rank to duplicates but did not skip any ranks afterward.

### 2. Aggregate Functions

Aggregate functions were applied to compute a single result from a set of input values. Examples included `SUM()`, `AVG()`, `MIN()`, and `MAX()`.

#### Cumulative Sum
The cumulative sum was implemented using window specifications, allowing us to compute running totals over partitions of data.

### 3. User Defined Functions (UDF)

Custom transformations were implemented using UDFs when built-in functions did not meet the requirements. These functions were registered and applied to DataFrames to extend Spark SQL's capabilities.

### 4. Data Writing Operations

Various modes of writing data to external storage were demonstrated using PySpark's DataFrameWriter API:

- **Append:** Added new data to existing data.
- **Overwrite:** Replaced the existing data.
- **Error (or ErrorIfExists):** Raised an error if data already existed.
- **Ignore:** Skipped writing if data already existed.

Different formats were also used, such as:

- **Parquet:** A columnar storage file format that supported efficient data compression and encoding.
- **Table:** Data was saved as a table in the Hive metastore or catalog.

### 5. Spark SQL

Spark SQL was used to run SQL queries on DataFrames. Temporary views were created from DataFrames to enable SQL-style querying using the `spark.sql()` method.

---