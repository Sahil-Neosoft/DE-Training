# Apache Spark Concepts – Summary

This document outlined foundational Apache Spark concepts and execution principles. It was intended to provide a concise and clear understanding of how Spark operated under the hood, enabling effective development and optimization of distributed data applications.

---

## 1. Spark Architecture

Apache Spark followed a **master-slave architecture**. The **driver program** served as the central coordinator, translating user code into a logical execution plan and scheduling it on **executors** running across worker nodes. Executors performed the actual data processing tasks and reported the results back to the driver. The architecture supported in-memory computation, making Spark significantly faster than traditional MapReduce-based systems.

---

## 2. Transformations and Actions

Spark distinguished operations into two categories:

- **Transformations** (e.g., `map`, `filter`, `flatMap`) were **lazy** and created a new RDD from an existing one without immediate computation.
- **Actions** (e.g., `collect`, `count`, `saveAsTextFile`) **triggered execution** of the DAG and returned results to the driver or persisted them.

This model allowed Spark to optimize the entire computation before running it.

---

## 3. DAG and Lazy Evaluation

Spark constructed a **Directed Acyclic Graph (DAG)** of stages and tasks based on transformations. This DAG represented the logical execution plan. Due to **lazy evaluation**, transformations were not computed immediately but recorded as lineage. Execution occurred only when an action was invoked, enabling Spark to optimize the processing pipeline.

---

## 4. Spark SQL Engine

Spark SQL provided support for processing **structured data** using SQL queries, the **DataFrame API**, and **Dataset API**. It leveraged the **Catalyst optimizer** for logical and physical query plan optimization, and **Tungsten** for memory management and code generation. This engine allowed efficient execution of complex queries and tight integration with Spark's core features.

---

## 5. RDD (Resilient Distributed Dataset)

The **RDD** was Spark's original abstraction for distributed data. It represented an immutable, partitioned collection of elements that could be processed in parallel. RDDs supported **fault tolerance** through lineage tracking and allowed developers to apply transformations and actions with fine-grained control over partitioning and execution.

---

## 6. SparkSession vs SparkContext

- **SparkContext** was the primary entry point in early versions of Spark, used to interact with the cluster and manage resources.
- **SparkSession** was introduced in Spark 2.0 as a unified entry point, replacing SparkContext and SQLContext. It allowed access to both core and SQL functionality from a single object, simplifying application development.

---

## 7. Spark Job, Stages, and Tasks

- A **Job** was launched when an action was invoked.
- Each job was divided into **Stages**, which were sets of tasks separated by shuffle boundaries.
- A **Task** was the smallest unit of work, executed on a single data partition. Tasks within a stage were distributed to executors for parallel execution.

---

## 8. Repartition vs Coalesce

- `**repartition(n)**` created a new RDD or DataFrame with `n` partitions by **shuffling data**, useful when increasing partitions.
- `**coalesce(n)**` reduced the number of partitions **without a full shuffle**, making it more efficient for operations that narrowed the dataset or required fewer partitions.

---

## 9. Spark Joins – Shuffle Sort Merge Join & Shuffle Hash Join

### Shuffle Sort Merge Join
This join strategy was used when both sides of the join were **large and sorted** by the join key. Spark **shuffled and sorted** both datasets before performing a **merge join**. It was **efficient** for large, sorted inputs but required both sides to be large enough and suitable for sorting.

### Shuffle Hash Join
In a **shuffle hash join**, Spark **shuffled both datasets** based on the join key, then built a **hash table** on one side (usually the smaller of the two) and probed it with the other. This strategy worked well when one side was **small enough to fit in memory**, but could fall back to sort-merge if memory was insufficient.

---
