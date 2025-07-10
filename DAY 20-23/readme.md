# Data Warehousing and ETL

This document summarized key concepts in data warehousing, data modeling, ETL processes, and fact table design. All descriptions were written in past tense.

## Data Warehouse

A data warehouse had served as a centralized repository for historical and integrated data. It was subject-oriented, integrated, time-variant, and nonvolatile.

## Database vs Data Warehouse

A database had supported real-time transactional operations with normalized structures. A data warehouse had supported analytical workloads with dimensional schemas and historical snapshots.

## ETL

ETL had stood for Extract, Transform, and Load. Data had been extracted from source systems, transformed to clean and unify it, and loaded into target tables for reporting.

## Data Mart

A data mart had represented a department-specific subset of the data warehouse. It had been optimized for focused analytics and faster query performance for a single business line.

## Key ETL Concepts

- Incremental Loading had processed only new or changed records.  
- Transient tables had held temporary data for intermediate steps.  
- Persistent tables had stored final, historical data.  
- Staging areas had isolated raw extracts before transformation.  
- Truncate operations had cleared tables quickly while preserving structure.

## Types of Incremental Loading

1. High-Watermark had used timestamps or numeric keys to identify new rows.  
2. Change Data Capture had read database logs to detect detailed changes.  
3. Trigger-Based had used database triggers to capture deltas.  
4. Log-Based Replication had streamed write-ahead or binlog events.  
5. Batch vs Micro-Batch had referred to scheduled loads at defined intervals or very short cycles.

## Load Strategies

- Append had inserted only new rows into fact tables.  
- In-Place Update had modified existing rows for updated attributes.  
- Complete Replacement had truncated tables before reloading all rows.  
- Rolling Append had appended fresh data and purged old rows to maintain a window.

## Transformations

- Data Value Unification had standardized variant representations into a single form.  
- Data Type and Size Unification had aligned field types and lengths to target schema requirements.  
- Deduplication had identified and removed duplicate records.  
- Dropping Columns had removed unused fields to simplify schemas.  
- Dropping Records had filtered out invalid or irrelevant rows.  
- Null Value Handling had replaced or flagged missing values to maintain data quality.

## Fact and Dimension Tables

Fact tables had contained quantitative measures and foreign keys to descriptive dimensions. Dimension tables had held descriptive attributes and hierarchies for slicing and dicing measures.

## Fact Table Design Steps

1. The business process had been selected to define the subject.  
2. The grain had been declared to specify the level of detail.  
3. The relevant dimensions had been identified to provide context.  
4. The facts had been identified to capture the numeric measures.

## Types of Facts

- Additive facts had been fully summable across all dimensions.  
- Semi-additive facts had been summable across some dimensions but not time.  
- Non-additive facts had required non-sum aggregations such as averages or distinct counts.

## Types of Fact Tables

- Transactional fact tables had recorded one row per event at a fine grain.  
- Periodic snapshot tables had captured the state of metrics at regular intervals.  
- Accumulating snapshot tables had tracked process milestones by updating rows.  
- Factless fact tables had recorded the occurrence of events or relationships without numeric measures.

## Factless Fact Table

A factless fact table had linked dimensions to answer "did it happen" questions. It had enabled counting events and tracking participation without storing measures.