from flask import Flask,render_template,jsonify,request
from employees import employees

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>About page</h1> <p>This is a simple Flask app.</p>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/api/user")
def user():
    return jsonify(name="Sahil",age=24) #jsonify() converts Python dict to JSON for APIs

@app.route("/greet")
def greet():
    return f"Hello, {request.args.get('name','Guest')}"

# Employee Management API 

# List all employees
@app.route("/employees",methods=['GET'])
def list_employees():
    return jsonify(employees)

# Get a specific employee by ID
@app.route("/employee/<int:emp_id>",methods=['GET'])
def get_employee(emp_id):
    emp=employees.get(emp_id)
    if emp:
        return jsonify(emp)
    return jsonify(error="Employee not Found"),404

# Add a new employee
@app.route("/employee",methods=['POST'])
def add_employee():
    data=request.get_json()

    try:
        emp_id=data['id']
        if emp_id in employees:
            return jsonify(error="Employee id already exist"), 400
        employees[emp_id]={
            "name":data['Sahil Patel'],
            "department":data['Data Science'],
            "salary":data[15000]
        }
        return jsonify(message="Employee added",employee=employees[emp_id]),201
    except (KeyError,ValueError,TypeError):
        return jsonify(error="Invalid data format"),400

# Search by department
@app.route("/search")
def search_by_department():
    dept=request.args.get('department')
    results={eid:emp for eid,emp in employees.items() if emp['department'].lower()==dept.lower()}
    return jsonify(results)

if __name__=="__main__":
    app.run(debug=True)