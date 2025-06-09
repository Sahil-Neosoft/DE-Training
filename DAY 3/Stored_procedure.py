from dotenv import load_dotenv
import os
import pymysql
import logging
import pandas as pd

logging.basicConfig(
    filename='stored_procedure_logs',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
 
load_dotenv()
 
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT",3306))
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

queries=[
    {
        "desc": "1. Total Sales by Region (Non-Parameterized)",
        "sql":"""
            select region,sum(sale_amount) Total_sales
            from employee_sales
            group by region;
        """,
        "params":None,
        "use_params":False
    },
    {
        "desc": "2. Sales by Employee ID (Parameterized)",
        "sql":"""
            select * from employee_sales
            where emp_id=%s
            order by sale_date;
        """,
        "params":(1,),
        "use_params":True  
    },
    {
        "desc": "3. Insert New Sale Record (Parameterized)",
        "sql":"""
            Insert into employee_sales(emp_id,dept,region,sale_amount,sale_date)
            values (%s, %s, %s, %s, %s);
        """,
        "params":(9,"HR","North",2000,"2025-06-08"),
        "use_params":True 
    },
    {
        "desc": "4. Monthly Sales Summary (Non-Parameterized)",
        "sql":"""
            select date_format(sale_date,'%Y-%m') month,
            sum(sale_amount) Total_sales
            from employee_sales
            group by month
            order by month;
        """,
        "params":None,
        "use_params":False
    },
    {
        "desc": "5. Sales in a Region (Parameterized)",
        "sql":"""
            select emp_id,sale_amount,region
            from employee_sales
            where region=%s;
        """,
        "params":("North",),
        "use_params":True         
    }
]

def run_queries():

    conn = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
    )
    
    try:
        with conn.cursor() as cursor:
            for q in queries:
                print(f"\n--- {q['desc']} ---")
                logging.info(f"Executing: {q['desc']}")

                if q["use_params"]:
                    cursor.execute(q["sql"],q["params"])
                else:
                    cursor.execute(q["sql"])
                
                if q["sql"].strip().lower().startswith("select"):
                    rows=cursor.fetchall()
                    if rows:
                        print(pd.DataFrame(rows))
                    else:
                        print("No data returned")
                else:
                    conn.commit()
                    print("Query executed successfully")
    except Exception as e:
            logging.error(f"Error executing query: {e}")
    finally:
        conn.close()
        logging.info("Database connection closed")

if __name__=="__main__":
    run_queries()