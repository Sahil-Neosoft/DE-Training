# | Function                                        | Typical Use Cases & Examples                                                                                                                                                                                                                                         |
# | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | **ROW\_NUMBER()**                               | - Assign unique rankings to rows within partitions.<br>- Pick *exactly one* top/bottom row per group.<br>**Example:** Find the highest-paid employee in each department.                                                                                             |
# | **RANK()**                                      | - Ranking with gaps if there are ties.<br>- When you want to know relative positions but keep gaps for ties.<br>**Example:** Leaderboard showing tied scores with same rank but skipping next rank.                                                                  |
# | **DENSE\_RANK()**                               | - Ranking without gaps for ties.<br>- Use when ranking ties but want continuous ranking numbers.<br>**Example:** Product sales ranking where no ranks are skipped despite ties.                                                                                      |
# | **NTILE(n)**                                    | - Divide data into roughly equal groups (quartiles, percentiles).<br>- Use for bucket analysis or grouping by ranges.<br>**Example:** Classify customers into top 25%, next 25%, etc., based on sales.                                                               |
# | **LAG() / LEAD()**                              | - Compare current row with previous/next row.<br>- Calculate differences over time.<br>- Identify trends or changes.<br>**Example:** Calculate month-over-month sales change.                                                                                        |
# | **FIRST\_VALUE() / LAST\_VALUE()**              | - Get the first/last value within a partition.<br>- Useful in time-series for baseline or latest value.<br>**Example:** Show employee’s first salary or latest promotion date in their department.                                                                   |
# | **SUM() / AVG() / COUNT() as Window Functions** | - Compute running totals, moving averages, or partition-wise aggregates.<br>- Useful in financial reports, cumulative statistics, or group comparisons.<br>**Example:** Calculate cumulative sales by date or average salary per department alongside each employee. |
# | **ROWS BETWEEN**                                | - Customize the window frame to define how many rows before/after to consider.<br>- Useful for moving averages, cumulative sums, or lagged comparisons.<br>**Example:** 7-day moving average of daily sales.                                                         |

import pymysql

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "window_functions_db"
}

queries=[
    # ROW NUMBER
    {
        "desc": "ROW_NUMBER 1: Row number per employee by date",
        "sql": """
            select emp_id,sale_date,sale_amount,
            row_number() over(partition by emp_id order by sale_date) as row_num
            from employee_sales
            limit 10;
        """
    },
    {
        "desc": "ROW_NUMBER 2: Latest 3 sales per employee",
        "sql":"""
            select * from(
            select *,
            row_number() over(partition by emp_id order by sale_date desc) as rn
            from employee_sales) as latest_sale
            where rn<=3 limit 10;
        """
    },

    # RANK and DENSE_RANK
    {
        "desc": "RANK 1: Rank employees by total sales per region",
        "sql":"""
            select emp_id,region,sum(sale_amount) Total_sales,
            rank() over(partition by region order by sum(sale_amount) desc) as rnk
            from employee_sales
            group by emp_id,region
            limit 10;
        """
    },
    {
        "desc": "DENSE_RANK 2: Top 3 sale amounts per department",
        "sql":"""
            select * from
            (select *,
            dense_rank() over(partition by dept order by sale_amount desc) rnk
            from employee_sales) sub
            where rnk <= 3;
        """
    },
    # LAG and LEAD
    {
        "desc": "LAG 1: Previous sale per employee",
        "sql":"""
            select *,
            lag(sale_amount) over(partition by emp_id order by sale_date) prev_sale  
            from employee_sales
            limit 10;
        """
    },
    {
        "desc": "LEAD 2: Next sale and date per employee",
        "sql":"""
            select emp_id,sale_amount,sale_date,
            lead(sale_date) over(partition by emp_id order by sale_date) next_date,
            lag(sale_amount) over(partition by emp_id order by sale_date) next_amount
            from employee_sales
            limit 10;
        """
    },
    # NTILE
    {
        "desc": "NTILE 1: Sales quartile per region",
        "sql":"""
            select emp_id,sale_amount,region,
            ntile(4) over(partition by region order by sale_amount desc) quartile
            from employee_sales;
        """
    },
    {
        "desc": "NTILE 2: Bucket all sales into 5 performance tiers",
        "sql":"""
            select emp_id,sale_amount,
            ntile(5) over(order by sale_amount desc) performance_tiers
            from employee_sales;
        """
    },
    # SUM, AVG, COUNT OVER
    {
        "desc": "SUM 1: Running total per employee",
        "sql":"""
            select emp_id,sale_date,sale_amount,
            sum(sale_amount) over(partition by emp_id order by sale_date) as Running_sum
            from employee_sales
            limit 10;
        """
    },
    {
        "desc": "COUNT 2: Sales count per department for each employee",
        "sql":"""
            select distinct emp_id,dept,
            count(*) over(partition by dept,emp_id) dept_sales_cnt
            from employee_sales
            limit 10;
        """
    },
    # FIRST_VALUE / LAST_VALUE
    {
        "desc": "FIRST_VALUE 1: First and last sale per employee",
        "sql":"""
            select emp_id,sale_date,sale_amount,
            first_value(sale_amount) over(partition by emp_id order by sale_date) first_sale,
            last_value(sale_amount) over(partition by emp_id order by sale_date) last_sale
            from employee_sales
            limit 10;
        """
    }
]

def run_windows_functions():
    conn=pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            for q in queries:
                print(f"\n--- {q['desc']} ---")
                cursor.execute(q['sql'])
                for row in cursor.fetchall():
                    print(row)
    finally:
        conn.close()

if __name__=="__main__":
    run_windows_functions()