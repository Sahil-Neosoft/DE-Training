from fastapi import FastAPI,HTTPException, Query
from pydantic import BaseModel,EmailStr
from typing import Optional

app=FastAPI()

@app.get("/")
def about():
    return {"message":"Welcome to FastAPI"}

class User(BaseModel):
    name:str
    age:int
    email:str

@app.post("/user/")
def create_user(user:User):
    return {
        "message":f"{user.name} added",
        "age":{user.age},
        "email":{user.email}
    }

@app.get("/employee/{emp_id}")
def get_employee(emp_id:int,department: str="General"):
    return {
        "emp_id":emp_id,
        "department":department
    }

# PROJECT

# Employee Onboarding FastAPI 
class Employee(BaseModel):
    name:str
    age:int
    email:EmailStr
    department:str

class EmployeeResponse(Employee):
    id:int

employees={}
employee_id_counter=1

def add_employee(data:Employee) ->int:
    global employee_id_counter
    employees[employee_id_counter]=data
    employee_id_counter+=1
    return employee_id_counter-1

def get_all_employees():
    return employees

def get_employee(emp_id:int) ->Optional[Employee]: # Returns None if no employee found 
    return employees.get(emp_id)

def get_employees_by_department(department: str):
    return {eid: emp for eid, emp in employees.items() if emp.department.lower() == department.lower()}

@app.post("/employees",response_model=EmployeeResponse) #response_model ensures the response conforms to the model (also auto-documents Swagger UI).
def Register_employee(employee:Employee):
    new_id=add_employee(employee)
    return EmployeeResponse(id=new_id,**employee.dict())

@app.get("/employees",response_model=dict[int,Employee])
def list_employees(department: Optional[str] =Query(None, description="Filter by department")):
    if department:
        return get_employees_by_department(department)
    return get_all_employees()

@app.get("/employee/{emp_id}",response_model=Employee)
def get_employee_by_id(emp_id:int):
    employee=get_employee(emp_id)
    if not employee:
        raise HTTPException(status_code=404,detail="Employee not Found")
    return employee