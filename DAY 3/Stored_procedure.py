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
port = int(os.getenv("DB_PORT", 3306))
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Procedure definitions
procedure_definitions = [
    """
    DROP PROCEDURE IF EXISTS sp_total_sales_by_region;
    """,
    """
    CREATE PROCEDURE sp_total_sales_by_region()
    BEGIN
        SELECT region, SUM(sale_amount) AS Total_sales
        FROM employee_sales
        GROUP BY region;
    END;
    """,
    """
    DROP PROCEDURE IF EXISTS sp_sales_by_emp_id;
    """,
    """
    CREATE PROCEDURE sp_sales_by_emp_id(IN emp INT)
    BEGIN
        SELECT * FROM employee_sales
        WHERE emp_id = emp
        ORDER BY sale_date;
    END;
    """,
    """
    DROP PROCEDURE IF EXISTS sp_insert_new_sale;
    """,
    """
    CREATE PROCEDURE sp_insert_new_sale(
        IN p_emp_id INT,
        IN p_dept VARCHAR(50),
        IN p_region VARCHAR(50),
        IN p_sale_amount DECIMAL(10,2),
        IN p_sale_date DATE
    )
    BEGIN
        INSERT INTO employee_sales(emp_id, dept, region, sale_amount, sale_date)
        VALUES (p_emp_id, p_dept, p_region, p_sale_amount, p_sale_date);
    END;
    """,
    """
    DROP PROCEDURE IF EXISTS sp_monthly_sales_summary;
    """,
    """
    CREATE PROCEDURE sp_monthly_sales_summary()
    BEGIN
        SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month,
               SUM(sale_amount) AS Total_sales
        FROM employee_sales
        GROUP BY month
        ORDER BY month;
    END;
    """,
    """
    DROP PROCEDURE IF EXISTS sp_sales_in_region;
    """,
    """
    CREATE PROCEDURE sp_sales_in_region(IN p_region VARCHAR(50))
    BEGIN
        SELECT emp_id, sale_amount, region
        FROM employee_sales
        WHERE region = p_region;
    END;
    """
]

queries = [
    {
        "desc": "1. Total Sales by Region (Stored Procedure, No Params)",
        "sql": "CALL sp_total_sales_by_region()",
        "params": None,
        "use_params": False
    },
    {
        "desc": "2. Sales by Employee ID (Stored Procedure, Parameterized)",
        "sql": "CALL sp_sales_by_emp_id(%s)",
        "params": (1,),
        "use_params": True  
    },
    {
        "desc": "3. Insert New Sale Record (Stored Procedure, Parameterized)",
        "sql": "CALL sp_insert_new_sale(%s, %s, %s, %s, %s)",
        "params": (9, "HR", "North", 2000, "2025-06-08"),
        "use_params": True 
    },
    {
        "desc": "4. Monthly Sales Summary (Stored Procedure, No Params)",
        "sql": "CALL sp_monthly_sales_summary()",
        "params": None,
        "use_params": False
    },
    {
        "desc": "5. Sales in a Region (Stored Procedure, Parameterized)",
        "sql": "CALL sp_sales_in_region(%s)",
        "params": ("North",),
        "use_params": True         
    }
]

def create_procedures(conn):
    with conn.cursor() as cursor:
        for proc_sql in procedure_definitions:
            cursor.execute(proc_sql)
        conn.commit()
    print("Stored procedures created or updated successfully.")

def run_queries():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    
    try:
        create_procedures(conn)
        
        with conn.cursor() as cursor:
            for q in queries:
                print(f"\n--- {q['desc']} ---")
                logging.info(f"Executing: {q['desc']}")

                if q["use_params"]:
                    cursor.execute(q["sql"], q["params"])
                else:
                    cursor.execute(q["sql"])
                
                # Try fetch results
                try:
                    rows = cursor.fetchall()
                except pymysql.err.ProgrammingError:
                    rows = None
                
                if rows:
                    print(pd.DataFrame(rows))
                else:
                    conn.commit()
                    print("Query executed successfully")
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        print(f"Error: {e}")
    finally:
        conn.close()
        logging.info("Database connection closed")

if __name__ == "__main__":
    run_queries()