class Employee:
    # Class variable shared by all employees
    company_name="Neosoft"

    def __init__(self,emp_id,name,dept):
        self.emp_id=emp_id   #Instance variable
        self.name=name
        self.dept=dept

    def display_details(self):
        print(f"Employee id : {self.emp_id}")
        print(f"Employee name : {self.name}")
        print(f"Employee Department : {self.dept}")


class Manager(Employee): #Inheritance
    def __init__(self,emp_id,name,dept,team_size):
        super().__init__(emp_id,name,dept)
        self.team_size=team_size

    # Method overriding
    def display_details(self):
        super().display_details()
        print(f"Manages team of size {self.team_size} people")

emp = Employee(14051,"Sahil Patel","Data Science")

mgr = Manager(14052,"Vipin Yadav","Data Science",20)

emp.display_details()
print("\n")
mgr.display_details()