# Time Series Functions & SQL Triggers

## 📦 Dataset & Setup
- Loaded a Hourly energy consumption dataset .
- Ensured the dataset included at least one date or datetime column.

## 🗓️ Datetime Formatting
- Converted string representations of dates into datetime format.
- Extracted individual date components such as year, month, day, hour, and the day name.

## 📆 Basic Date Operations
- Identified the minimum and maximum dates within the dataset.
- Filtered the dataset based on specific years or date ranges.

## 🔢 Set Index & Head
- Set the datetime column as the index to facilitate time-based operations.
- Viewed the first few rows of the dataset for verification.

## 📊 Resampling Time Series Data
- Aggregated data using different time intervals: daily, weekly, monthly, quarterly, and yearly.
- Applied aggregation functions like sum, mean, and count to resampled data.

## 📉 Aggregation Functions to Apply
- Performed operations such as sum, min/max, mean, count, standard deviation, first and last values within groups.

## 🌍 Timezone Handling
- Converted naive datetime values to specific timezones.
- Localized timestamps and adjusted them to different timezone regions.

## ⏱️ Time Series Functions
- Applied rolling windows to compute moving averages.
- Shifted values to analyze previous observations.

## 📦 Employee Sales Database For Triggers

### 🛠️ Table Setup
- Created the `employee_sales` table to store employee transactions with the following structure:

| Column        | Description |
|--------------|-------------|
| sale_id      | Primary key, unique sale ID |
| employee_id  | Employee who made the sale |
| sale_date    | Date of sale |
| sale_amount  | Amount of sale |
| region       | Region of sale |

###  Trigger Implementations
Implemented triggers to automate and enforce data validation rules:

1. **Set Default Sale Date**  
   - Automatically assigned `NOW()` to `sale_date` if no value was provided.

2. **Validate Region Input**  
   - Restricted `region` values to 'North', 'South', 'East', or 'West'.
   - Raised an error for invalid entries.

3. **Round Sale Amount**  
   - Ensured `sale_amount` was rounded to two decimal places before insertion.

---