import pymysql
from faker import Faker
import random
from datetime import datetime

# Set up Faker and DB connection
fake = Faker()
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='testdb'
)
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
)
""")

cursor.execute("""
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100),
    start_date DATE,
    end_date DATE
)
""")

cursor.execute("""
CREATE TABLE project_assignments (
    emp_id INT,
    project_id INT,
    assigned_date DATE,
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
)
""")

conn.commit()

# Insert fake departments
departments = ['Engineering', 'Marketing', 'HR', 'Finance', 'Product', 'Support']
for dept in departments:
    cursor.execute("INSERT INTO departments (dept_name) VALUES (%s)", (dept,))
conn.commit()

# Fetch dept_ids
cursor.execute("SELECT dept_id FROM departments")
dept_ids = [row[0] for row in cursor.fetchall()]

# Insert fake employees
num_employees = 500
for _ in range(num_employees):
    fname = fake.first_name()
    lname = fake.last_name()
    email = fake.unique.email()
    hire_date = fake.date_between(start_date='-10y', end_date='today')
    dept_id = random.choice(dept_ids)
    salary = round(random.uniform(40000, 120000), 2)

    cursor.execute("""
        INSERT INTO employees (first_name, last_name, email, hire_date, salary, dept_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (fname, lname, email, hire_date, salary, dept_id))

# Insert fake projects
num_projects = 50
for _ in range(num_projects):
    pname = fake.bs().capitalize()
    start = fake.date_between(start_date='-3y', end_date='-1y')
    end = fake.date_between(start_date=start, end_date='today')
    cursor.execute("""
        INSERT INTO projects (project_name, start_date, end_date)
        VALUES (%s, %s, %s)
    """, (pname, start, end))
conn.commit()

# Fetch all employee and project IDs
cursor.execute("SELECT emp_id FROM employees")
emp_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT project_id FROM projects")
project_ids = [row[0] for row in cursor.fetchall()]

# Assign employees to random projects
for emp_id in random.sample(emp_ids, int(num_employees * 0.8)):  # 80% assigned
    assigned_projects = random.sample(project_ids, random.randint(1, 5))
    for pid in assigned_projects:
        assign_date = fake.date_between(start_date='-2y', end_date='today')
        cursor.execute("""
            INSERT IGNORE INTO project_assignments (emp_id, project_id, assigned_date)
            VALUES (%s, %s, %s)
        """, (emp_id, pid, assign_date))
conn.commit()

print("Database created and populated with fake data!")

# Close connection
cursor.close()
conn.close()