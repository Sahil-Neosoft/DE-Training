# Apache Airflow – Concepts

This repository provided a complete overview of Apache Airflow's core components and functionalities. It described how Airflow had been used for workflow orchestration and how its features supported the creation and management of data pipelines.

## What Was Apache Airflow and How Did It Work

Apache Airflow was an open-source platform used to programmatically author, schedule, and monitor workflows. It operated by using Directed Acyclic Graphs (DAGs) to represent workflows, where each task had defined dependencies. The scheduler evaluated DAGs and scheduled task execution, while the executor processed the tasks based on available resources.

## Understanding Cron Jobs and Cron Syntax Formats

Airflow used cron expressions to define the scheduling intervals for DAGs. Cron syntax consisted of five fields that represented minute, hour, day of month, month, and day of week. These expressions allowed users to schedule tasks to run periodically at specific times or intervals.

## What Was a DAG in Airflow and How Was It Created

A DAG, or Directed Acyclic Graph, defined a collection of tasks and their execution order. DAGs were created using Python, and each DAG included metadata such as schedule intervals, start dates, and task definitions. DAGs ensured that tasks were executed in the correct sequence without any circular dependencies.

## DAGs, Operators, Tasks, Providers and airflow.cfg

DAGs represented workflows. Operators defined what actions a task would perform, such as executing Python code or running shell commands. Tasks were specific instances of operators assigned within DAGs. Providers added integrations with third-party services like AWS, GCP, and databases. The `airflow.cfg` file held configuration values for the entire Airflow environment, including executor type, database settings, and logging options.

## Variables and Connections in Airflow

Variables were key-value pairs stored in Airflow to dynamically configure DAGs and tasks. Connections held credentials and parameters needed to connect to external systems, such as databases, APIs, and cloud services. Both were managed through the Airflow UI, CLI, or environment variables.

## Airflow Sensors with Examples

Sensors were special types of operators designed to wait for a certain condition to be met before proceeding. These conditions could include the existence of a file, the completion of a process, or the availability of data. Sensors helped ensure that tasks only executed when their dependencies were satisfied.

## Deferrable Operators and Triggers in Airflow

Deferrable operators allowed tasks to pause and free up worker resources while waiting for external conditions. Once the conditions were met, a trigger resumed the task. This approach reduced resource consumption and improved scalability in high-latency workflows.

## XCom (Passing Data Between Tasks)

XCom, short for cross-communication, allowed tasks to share small pieces of data with one another. This enabled workflows to be more dynamic and dependent on the results of previous tasks. Data was pushed and pulled using XCom mechanisms between task instances.

## Data Sets and Data-Aware Scheduling (Cross DAG Dependencies)

Airflow supported data-aware scheduling using datasets. A dataset represented a unit of data that, when updated, could trigger downstream DAGs. This enabled event-driven workflows and established dependencies between separate DAGs, enhancing orchestration flexibility.

## Trigger Rules, Conditional Branching, Setup/Teardown, Last Only, Depends on Past

Trigger rules defined how tasks reacted to the state of upstream tasks, such as running only if all prior tasks succeeded or if at least one failed. Conditional branching allowed workflows to take different paths based on logic. Setup and teardown tasks managed resources or services before and after workflow execution. The "last only" feature ensured a task ran only on the most recent DAG run, while "depends on past" made task execution conditional on its own previous run status.

## Airflow Hooks

Hooks were reusable interfaces used to connect to external systems, such as cloud platforms, databases, and APIs. They encapsulated the logic required to authenticate and interact with these services, and were often used inside custom operators or tasks.

## Airflow Python and CMD Operators

Airflow provided operators to run Python code and shell commands. The Python operator allowed execution of Python functions within tasks, while the CMD or Bash operators executed command-line instructions. These operators offered flexibility and simplicity in building workflows that integrated with existing scripts and processes.

## Summary

This document summarized the key concepts and components of Apache Airflow. It covered how workflows were built using DAGs, how scheduling was managed, and how Airflow integrated with external systems. Through its modular and extensible architecture, Airflow enabled the orchestration of complex, scalable, and maintainable data pipelines.