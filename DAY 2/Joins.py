import pymysql

conn = pymysql.connect(
        host="localhost",
        user= "root",
        password= "root",
        database= "testdb"
)   

cursor=conn.cursor()

queries=[
    {
        "desc":"INNER JOIN 1: Employees with Their Department Names",
        "sql":"""
            select e.first_name,e.last_name,d.dept_name from employees e
            join departments d
            on e.dept_id=d.dept_id limit 10;
        """
    },
    {
        "desc": "INNER JOIN 2: Employees Assigned to Projects with Project Details",
        "sql":"""
            select e.first_name,e.last_name,p.project_name,pa.assigned_date from employees e
            join project_assignments pa
            on e.emp_id=pa.emp_id
            join projects p
            on pa.project_id=p.project_id
            limit 10;
        """
    },
    {
        "desc": "LEFT JOIN 1: All Employees and Their Departments (Include employees with no department)",
        "sql":"""
            select e.first_name,e.last_name,d.dept_name from employees e
            left join departments d
            on e.dept_id=d.dept_id
            limit 10;
        """
    },
    {
        "desc": "RIGHT JOIN 1: All Departments and Their Employees (Include employees with no department)",
        "sql":"""
            select e.first_name,e.last_name,d.dept_name from departments d
            right join employees e
            on e.dept_id=d.dept_id
            limit 10;
        """
    },
    {
        "desc": "RIGHT JOIN 2: All Projects and Their Assigned Employees (Include projects with no employees)",
        "sql":"""
            select e.first_name,e.last_name,pa.assigned_date,p.project_name 
            from projects p
            right join project_assignments pa on p.project_id=pa.project_id
            right join employees e on e.emp_id=pa.emp_id
            limit 10;
        """
    },
    {
        "desc":"CROSS JOIN 1: Pair every employee with every department",
        "sql":"""
            select * from employees e
            cross join 
            departments d
            limit 10;
        """
    },
    {
        "desc":"SELF JOIN 1: Find employees hired on the same day",
        "sql":"""
            select e1.first_name emp1,e2.first_name emp2,e1.hire_date
            from employees e1
            join employees e2
            on e1.hire_date=e2.hire_date AND e1.emp_id < e2.emp_id
            limit 10;
        """
    },
    {
        "desc":"SELF JOIN 2: Employees in the same department (but not the same person)",
        "sql":"""
            select e1.first_name emp1,e2.first_name emp2,e1.dept_id
            from employees e1
            join employees e2
            on e1.dept_id=e2.dept_id AND e1.emp_id<e2.emp_id
            limit 10;
        """
    },
    {
        "desc":"UNION 1: Combine first names of employees and project names as one list",
        "sql":"""
            select first_name from employees 
            UNION
            select project_name from projects
            limit 10;
        """
    },
    {
        "desc":"UNION 2: Employees hired before 2015 and those with salary above 100k",
        "sql":"""
            select emp_id,first_name from employees
            where hire_date<'2015-01-01'
            UNION
            select emp_id,first_name from employees
            where salary > 100000
            limit 10;
        """
    }
]

# | Feature        | LEFT JOIN                  | LEFT ANTI JOIN                    |
# | -------------- | -------------------------- | --------------------------------- |
# | Purpose        | Include all left + matches | Only unmatched from left          |
# | Matching rows  | Included                   | Excluded                          |
# | NULLs in right | Possible                   | No NULLs – right table not joined |
# | Use case       | Merging related data       | Finding orphan/missing entries    |

# LEFT ANTI JOIN

# Employees not assigned to any projects
"""
select * from employees e
left anti join
project_assignments pa
on e.emp_id=pa.emp_id;
"""

# Departments without any employees
"""
select dept_name from departments d
left anti join
employees e
on d.dept_id=e.dept_id;
"""

# RIGHT ANTI JOIN

# Projects with no assigned employees
"""
select * from project_assignments pa
right anti join
projects p
on pa.project_id=p.project_id; 
"""

# Employees not belonging to any department
"""
select * from departments d
right anti join
employees e
on e.dept_id=d.dept_id;
"""

for q in queries:
    print(f"\n--- {q['desc']} ---")
    cursor.execute(q['sql'])
    for row in cursor.fetchall():
        print(row)

cursor.close()
conn.close()