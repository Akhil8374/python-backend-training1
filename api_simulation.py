import json
import os

FILE_NAME = "employees.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# GET /employees
def get_employees():
    employees = load_data()
    return {
        "status": 200,
        "message": "Employees fetched successfully",
        "data": employees
    }


# GET /employees/{id}
def get_employee_by_id(emp_id):
    employees = load_data()

    for employee in employees:
        if employee["id"] == emp_id:
            return {
                "status": 200,
                "message": "Employee found",
                "data": employee
            }

    return {
        "status": 404,
        "message": "Employee not found"
    }


# POST /employees
def create_employee(employee):
    employees = load_data()
    employees.append(employee)
    save_data(employees)

    return {
        "status": 201,
        "message": "Employee created successfully",
        "data": employee
    }


# PUT /employees/{id}
def update_employee(emp_id, updated_data):
    employees = load_data()

    for employee in employees:
        if employee["id"] == emp_id:
            employee.update(updated_data)
            save_data(employees)

            return {
                "status": 200,
                "message": "Employee updated successfully",
                "data": employee
            }

    return {
        "status": 404,
        "message": "Employee not found"
    }


# DELETE /employees/{id}
def delete_employee(emp_id):
    employees = load_data()

    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)
            save_data(employees)

            return {
                "status": 200,
                "message": "Employee deleted successfully"
            }

    return {
        "status": 404,
        "message": "Employee not found"
    }


print("===== API SIMULATION TEST =====")

print("\nGET ALL EMPLOYEES")
print(get_employees())

print("\nGET EMPLOYEE BY ID")
print(get_employee_by_id(1))

new_employee = {
    "id": 999,
    "name": "Test User",
    "email": "test@example.com",
    "department": "IT",
    "salary": 50000,
    "experience": 2
}

print("\nCREATE EMPLOYEE")
print(create_employee(new_employee))

print("\nUPDATE EMPLOYEE")
print(update_employee(999, {"salary": 60000}))

print("\nDELETE EMPLOYEE")
print(delete_employee(999))