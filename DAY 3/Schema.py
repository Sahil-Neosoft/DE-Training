import pymysql
import random
from datetime import datetime, timedelta

# Connect to MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    autocommit=True
)

try:
    with connection.cursor() as cursor:
        # Create DB and use it
        cursor.execute("CREATE DATABASE IF NOT EXISTS window_functions_db")
        cursor.execute("USE window_functions_db")

        # Drop if already exists
        cursor.execute("DROP TABLE IF EXISTS employee_sales")

        # Create the table
        cursor.execute("""
            CREATE TABLE employee_sales (
                id INT AUTO_INCREMENT PRIMARY KEY,
                emp_id INT,
                dept VARCHAR(50),
                sale_amount DECIMAL(10, 2),
                sale_date DATE,
                region VARCHAR(50)
            )
        """)

        # Generate sample data
        departments = ['Sales', 'Marketing', 'Finance', 'HR']
        regions = ['North', 'South', 'East', 'West']
        start_date = datetime(2023, 1, 1)

        values = []
        for i in range(1, 101):  # 100 rows
            emp_id = random.randint(1, 10)
            dept = random.choice(departments)
            region = random.choice(regions)
            amount = round(random.uniform(100, 2000), 2)
            date = start_date + timedelta(days=random.randint(0, 365))
            values.append((emp_id, dept, amount, date.date(), region))

        # Insert sample data
        insert_sql = """
            INSERT INTO employee_sales (emp_id, dept, sale_amount, sale_date, region)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.executemany(insert_sql, values)

        print("Table 'employee_sales' created and populated successfully.")

finally:
    connection.close()