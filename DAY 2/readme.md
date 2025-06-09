# SQL Joins Practice with Python and MySQL

## 📘 Project Overview

- Use of multiple JOIN types (INNER, LEFT, RIGHT, SELF, CROSS, UNION, ANTI)
- Automatically generate a sample relational database
- Execute a wide variety of SQL queries

---

## 🗂️ Schema Overview

The following tables are created and populated:

| Table                | Columns |
|----------------------|---------|
| **employees**         | emp_id, first_name, last_name, email, hire_date, salary, dept_id |
| **departments**       | dept_id, dept_name |
| **projects**          | project_id, project_name, start_date, end_date |
| **project_assignments** | emp_id, project_id, assigned_date |

---

## 🔍 SQL JOIN Types Practiced

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- CROSS JOIN
- SELF JOIN
- UNION
- LEFT & RIGHT ANTI JOIN

---

## 🧪 Sample Query Outputs

### INNER JOIN 1: Employees with Their Department Names ---
('Diana', 'Jones', 'Engineering')
('Stephen', 'Stevens', 'Engineering')
('Amy', 'Davis', 'Engineering')
('Autumn', 'Fox', 'Engineering')
('Debbie', 'Pena', 'Engineering')
('Stephanie', 'Carrillo', 'Engineering')
('Vicki', 'Nelson', 'Engineering')
('Karen', 'Wagner', 'Engineering')
('Kimberly', 'Shaffer', 'Engineering')
('Julie', 'Lane', 'Engineering')

### INNER JOIN 2: Employees Assigned to Projects with Project Details ---      
('James', 'Anderson', 'Morph best-of-breed users', datetime.date(2023, 12, 22))
('Rose', 'Warner', 'Morph best-of-breed users', datetime.date(2024, 11, 26))   
('Joshua', 'Morgan', 'Morph best-of-breed users', datetime.date(2023, 8, 8))   
('Lisa', 'Schultz', 'Morph best-of-breed users', datetime.date(2024, 3, 1))    
('Anthony', 'Williams', 'Morph best-of-breed users', datetime.date(2023, 7, 14))
('Thomas', 'Peterson', 'Morph best-of-breed users', datetime.date(2024, 1, 25))
('Mary', 'Sparks', 'Morph best-of-breed users', datetime.date(2024, 7, 23))
('Rita', 'Cross', 'Morph best-of-breed users', datetime.date(2025, 1, 22))
('Jon', 'Jordan', 'Morph best-of-breed users', datetime.date(2023, 9, 30))
('Daniel', 'Clark', 'Morph best-of-breed users', datetime.date(2024, 6, 14))

### LEFT JOIN 1: All Employees and Their Departments (Include employees with no department) ---
('Erin', 'Stokes', 'HR')
('Andrea', 'Sloan', 'Support')
('Cynthia', 'Lang', 'Product')
('Diana', 'Jones', 'Engineering')
('Christian', 'Moore', 'Product')
('James', 'Carlson', 'Finance')
('Jennifer', 'Farrell', 'Marketing')
('Robert', 'Hines', 'Product')
('Brittany', 'Walker', 'Support')
('Mark', 'Gomez', 'Finance')

### RIGHT JOIN 1: All Departments and Their Employees (Include employees with no department) ---
('Erin', 'Stokes', 'HR')
('Andrea', 'Sloan', 'Support')
('Cynthia', 'Lang', 'Product')
('Diana', 'Jones', 'Engineering')
('Christian', 'Moore', 'Product')
('James', 'Carlson', 'Finance')
('Jennifer', 'Farrell', 'Marketing')
('Robert', 'Hines', 'Product')
('Brittany', 'Walker', 'Support')
('Mark', 'Gomez', 'Finance')

### RIGHT JOIN 2: All Projects and Their Assigned Employees (Include projects with no employees) ---
('Erin', 'Stokes', datetime.date(2024, 10, 19), 'Scale vertical architectures')
('Andrea', 'Sloan', datetime.date(2023, 11, 25), 'Synergize b2c platforms')
('Andrea', 'Sloan', datetime.date(2024, 2, 28), 'Optimize plug-and-play info-mediaries')
('Cynthia', 'Lang', datetime.date(2024, 1, 8), 'Target revolutionary communities')
('Cynthia', 'Lang', datetime.date(2024, 9, 18), 'Engineer killer technologies')
('Cynthia', 'Lang', datetime.date(2024, 11, 5), 'Innovate distributed synergies')
('Diana', 'Jones', None, None)
('Christian', 'Moore', datetime.date(2024, 1, 12), 'Engineer mission-critical e-markets')
('James', 'Carlson', datetime.date(2024, 6, 17), 'Unleash killer users')
('James', 'Carlson', datetime.date(2023, 12, 18), 'Productize customized platforms')

### CROSS JOIN 1: Pair every employee with every department ---
(1, 'Erin', 'Stokes', 'williamsjerry@example.net', datetime.date(2024, 7, 17), Decimal('74451.07'), 3, 6, 'Support')
(1, 'Erin', 'Stokes', 'williamsjerry@example.net', datetime.date(2024, 7, 17), Decimal('74451.07'), 3, 5, 'Product')
(1, 'Erin', 'Stokes', 'williamsjerry@example.net', datetime.date(2024, 7, 17), Decimal('74451.07'), 3, 4, 'Finance')
(1, 'Erin', 'Stokes', 'williamsjerry@example.net', datetime.date(2024, 7, 17), Decimal('74451.07'), 3, 3, 'HR')
(1, 'Erin', 'Stokes', 'williamsjerry@example.net', datetime.date(2024, 7, 17), Decimal('74451.07'), 3, 2, 'Marketing')


### SELF JOIN 1: Find employees hired on the same day ---
('Andrea', 'Brittany', datetime.date(2022, 6, 10))
('Mark', 'Karen', datetime.date(2022, 11, 27))
('Kimberly', 'Erica', datetime.date(2018, 10, 18))
('Michael', 'Linda', datetime.date(2025, 5, 5))
('Stephen', 'Jimmy', datetime.date(2017, 4, 28))
('Amy', 'Kathryn', datetime.date(2017, 3, 23))
('Autumn', 'William', datetime.date(2017, 12, 18))
('Kimberly', 'Cindy', datetime.date(2018, 7, 3))
('Michael', 'Harold', datetime.date(2015, 8, 6))
('Elizabeth', 'Jane', datetime.date(2015, 8, 8))

### SELF JOIN 2: Employees in the same department (but not the same person) ---
('Erin', 'Kimberly', 3)
('Erin', 'Curtis', 3)
('Erin', 'James', 3)
('Erin', 'Logan', 3)
('Erin', 'Latoya', 3)
('Erin', 'Daniel', 3)
('Erin', 'Alan', 3)
('Erin', 'Jimmy', 3)
('Erin', 'Rebecca', 3)
('Erin', 'Rodney', 3)

### UNION 1: Combine first names of employees and project names as one list ---
('Erin',)
('Andrea',)
('Cynthia',)
('Diana',)
('Christian',)
('James',)
('Jennifer',)
('Robert',)
('Brittany',)
('Mark',)

### UNION 2: Employees hired before 2015 and those with salary above 100k ---
(3, 'Cynthia')
(4, 'Diana')
(8, 'Robert')
(9, 'Brittany')
(14, 'Mia')
(15, 'Michael')
(17, 'Ashley')
(18, 'Stephen')
(21, 'Autumn')
(22, 'Curtis')