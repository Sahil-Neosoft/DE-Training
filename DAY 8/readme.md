# Data Processing and Transformation

This repository involved working with structured data using advanced data manipulation techniques. The objective was to read data from multiple sources, perform transformations, handle missing values, and execute analytical operations using a data processing framework such as PySpark or similar tools.

---

## Data Ingestion

- Read JSON files and CSV files successfully.
- Created and applied schema definitions to enforce data structure and types.
- Selected relevant columns from datasets to prepare for transformation and analysis.

---

## Data Selection and Filtering

- Applied **aliasing** to rename columns for improved readability.
- Used **filtering** operations to extract subsets of data based on specific conditions.

### Scenarios Implemented:
1. Filtered the dataset where `fat_content = 'Regular'`.
2. Sliced the data for records where `item_type = 'Soft Drinks'` and `weight < 10`.
3. Retrieved data where `Tier` was in ('Tier 1', 'Tier 2') and `Outlet_Size` was NULL.

---

## Column Transformations

- Renamed columns using `withColumnRenamed`.
- Added and modified columns using `withColumn`.
- Cleaned data using `regexp_replace` to standardize values.
- Cast data types appropriately using type casting.

---

## Sorting and Dropping

- Sorted data in ascending and descending order.
- Sorted data by multiple columns simultaneously.
- Dropped single and multiple unnecessary columns to optimize data.
- Removed duplicate records using `dropDuplicates`.
- Dropped duplicates based on specific columns using the `subset` parameter.

---

## Combining Datasets

- Merged datasets using `union` and `unionByName` methods to ensure schema consistency.

---

## String Operations

- Applied string transformations including:
  - `initcap()` – capitalized the first letter of each word.
  - `lower()` – converted strings to lowercase.
  - `upper()` – converted strings to uppercase.

---

## Date Functions

- Utilized built-in date functions including:
  - `current_date()`
  - `date_add()`
  - `date_sub()`
  - `datediff()`
  - `date_format()`  
- Performed calculations and formatting on date fields.

---

## Null Handling

- Dropped null records using `dropna()` with both `how='all'` and `how='any'` strategies.
- Dropped and filled null values in selected columns using the `subset` parameter.
- Replaced missing values using appropriate default values.

---

## Advanced Data Transformations

- Split string columns and accessed indexed values from resulting arrays.
- Used `explode()` to flatten nested array structures.
- Checked for presence of elements in arrays using `array_contains()`.

---

## Grouping and Aggregation

- Performed grouping and aggregations using:
  - `groupBy()` with aggregations like `sum`, `avg`, `count`, etc.
  - Grouping by multiple columns for multi-dimensional analysis.
  - Used `collect_list()` to aggregate values into lists.
  - Applied `pivot()` for wide-format aggregations.

---

## Conditional Logic

- Implemented complex conditional logic using `when().otherwise()` on multiple conditions.

---

## Joins

- Executed various types of joins including:
  - `inner`
  - `left`
  - `right`
  - `anti`  
- Combined datasets based on key columns to enrich the data.

---