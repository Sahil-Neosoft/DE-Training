from dotenv import load_dotenv
import os
import pymysql
import logging
import pandas as pd

logging.basicConfig(
    filename='views_logs',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
 
load_dotenv()
 
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT",3306))
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

views=[
    {
        "desc": "Create view: total sales by employee",
        "sql":"""
            create or replace view total_sales_by_employee as
            select emp_id,sum(sale_amount)
            from employee_sales
            group by emp_id;
        """
    },
    {
        "desc": "Query view: total sales by employee",
        "sql":"""
            select * from total_sales_by_employee;
        """
    },
    {
        "desc": "Create view: sales count by region",
        "sql":"""
            create or replace view sales_count_by_region as
            select emp_id,count(*) sales_count
            from employee_sales
            group by region;
        """
    }
]

def run_views():
    conn=pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    try:
        with conn.cursor() as cursor:
            for v in views:
                 print(f"\n--- {v['desc']} ---")
                 cursor.execute(v['sql'])
                
                 if v["sql"].strip().lower().startswith("select"):
                     rows=cursor.fetchall()
                     print(pd.DataFrame(rows))
                 else:
                     conn.commit()
                     print("Query executed successfully")
    except Exception as e:
            logging.error(f"Error executing query: {e}")
    finally:
        conn.close()
        logging.info("Database connection closed")

if __name__=="__main__":
    run_views()