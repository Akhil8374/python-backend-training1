import json
import os

FILE_NAME = "employees.json"


# Load data from JSON file
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save data to JSON file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Add Employee
def add_employee():
    employees = load_data()

    employee = {
        "id": int(input("Enter ID: ")),
        "name": input("Enter Name: "),
        "email": input("Enter Email: "),
        "department": input("Enter Department: "),
        "salary": int(input("Enter Salary: ")),
        "experience": int(input("Enter Experience: "))
    }

    employees.append(employee)
    save_data(employees)
    print("Employee added successfully!\n")


# View Employees
def view_employees():
    employees = load_data()

    if not employees:
        print("No employees found!\n")
        return

    for emp in employees:
        print(emp)
    print()


# Update Employee
def update_employee():
    employees = load_data()
    emp_id = int(input("Enter Employee ID to update: "))

    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = input("Enter new Name: ")
            emp["email"] = input("Enter new Email: ")
            emp["department"] = input("Enter new Department: ")
            emp["salary"] = int(input("Enter new Salary: "))
            emp["experience"] = int(input("Enter new Experience: "))

            save_data(employees)
            print("Employee updated successfully!\n")
            return

    print("Employee not found!\n")


# Delete Employee
def delete_employee():
    employees = load_data()
    emp_id = int(input("Enter Employee ID to delete: "))

    new_employees = [emp for emp in employees if emp["id"] != emp_id]

    if len(new_employees) == len(employees):
        print("Employee not found!\n")
    else:
        save_data(new_employees)
        print("Employee deleted successfully!\n")


# Menu
def menu():
    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    menu()