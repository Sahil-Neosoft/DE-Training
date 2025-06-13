# Apache Spark – Concepts Learned

This README summarizes key concepts that were learned while studying Apache Spark, its architecture, and execution model.

---

## How Spark Worked  
Apache Spark was a distributed data processing engine. It used a **driver** to manage the application and coordinate distributed **executors** across **worker nodes**, enabling fast, in-memory data computation.

---

## DAG, Lazy Evaluation, and Query Optimizer  
- **DAG (Directed Acyclic Graph):** Spark created a DAG to represent the logical execution plan of transformations.  
- **Lazy Evaluation:** Transformations were not executed until an action was called, allowing Spark to optimize execution.  
- **Query Optimizer (Catalyst):** Optimized logical plans for better performance using techniques like predicate pushdown and plan pruning.

---

## Transformations and Actions  
- **Transformations:** Operations like `map`, `filter`, and `flatMap` that created new RDDs. These were lazily evaluated.  
- **Actions:** Operations like `collect`, `count`, and `saveAsTextFile` that triggered the actual execution of transformations.

---

## SparkSession  
The unified entry point to work with Spark. It replaced older contexts like `SQLContext` and `HiveContext`, making it easier to access Spark SQL and DataFrame APIs.

---

## RDD and Partitioning  
- **RDD (Resilient Distributed Dataset):** The core abstraction in Spark for distributed data.  
- **Partitioning:** RDDs were split into partitions, allowing parallel processing across executors. Efficient partitioning reduced data shuffling and improved performance.

---

## Spark Memory Between Master and Workers  
- The **driver (master)** handled job scheduling and task distribution.  
- **Executors (workers)** ran the tasks and stored intermediate data.  
- Memory was divided into execution memory, storage memory, and overhead. Proper tuning improved job efficiency.

---

## Core Spark Components  
- **SparkSession:** Main API for working with structured and unstructured data.  
- **SparkContext:** Managed the connection to the Spark cluster.  
- **Jobs:** Triggered by actions, jobs were made up of stages.  
- **Stages:** Divided jobs into smaller sets of tasks based on shuffle boundaries.  
- **Tasks:** Smallest unit of execution, each running on a partition.

---