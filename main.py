import os
import time

class Company:
    def __init__(self, name):
        self.company_name = name

class Employee(Company):
    def __init__(self):
        super().__init__('')
        self.employee_name = ''
        self.employee_rollno = 0
        self.employee_department = ''
        self.employee_designation = ''
        self.employee_salary = 0
        self.employee_data = {}

    def accept_employee(self, name, company_name, rollno, department, designation, hours):
        if name.isdigit():
            print("Validation Error: Employee name cannot be a number.")
            return
        if not name.isalpha():
            print("Validation Error: Employee name must consist of only letters.")
            return

        if not company_name.isalpha():
            print("Validation Error: Company name must consist of only letters.")
            return
        if not department.isalpha():
            print("Validation Error: Department name must consist of only letters.")
            return
        if not designation.isalpha():
            print("Validation Error: Designation must consist of only letters.")
            return

        if not isinstance(rollno, int):
            print("Validation Error: Roll number must be an integer.")
            return
        if not isinstance(hours, int):
            print("Validation Error: Working hours must be an integer.")
            return

        self.employee_name = name
        self.company_name = company_name
        self.employee_rollno = rollno
        self.employee_department = department
        self.employee_designation = designation
        self.employee_hours = hours
        self.calculate_salary(hours)
        self.employee_data[self.employee_name] = [self.employee_rollno, self.company_name, self.employee_department, self.employee_designation, self.employee_salary, self.employee_hours]

    def display_employee(self):
        if not self.employee_data:
            print("No employees found in the database.")
        else:
            print("\nEmployee Details:")
            for name, data in self.employee_data.items():
                print("Employee Name:", name)
                print("Employee ID:", data[0])
                print("Company:", data[1])
                print("Department:", data[2])
                print("Designation:", data[3])
                print("Salary:", data[4])
                print("Working Hours:", data[5])
                print()

    def search_employee(self, name):
        if name in self.employee_data:
            data = self.employee_data[name]
            print("Employee ID: ", data[0])
            print("Employee Organisation:", data[1])
            print("Employee Department:", data[2])
            print("Employee Job Title:", data[3])
            print("Employee Salary: $", data[4])
            print("Employee Shift Hours:", data[5])
        else:
            print("Employee not found in the company records")

    def calculate_salary(self, hours):
        self.employee_salary = 10000 * hours

employee_object = Employee()

while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Display All Employees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Employee Name: ")
        if name.isdigit():
            print("Employee name cannot be a number.")
            time.sleep(4)
            os.system('cls')
            continue

        company_name = input("Organisation: ")
        if not company_name.isalpha():
            print("Company name must consist of only letters.")
            time.sleep(4)
            os.system('cls')
            continue

        try:
            rollno = int(input("Employee ID: "))
        except ValueError:
            print("Roll number must be an integer.")
            time.sleep(4)
            os.system('cls')
            continue

        department = input("Department: ")
        if not department.isalpha():
            print("Department name must consist of only letters.")
            time.sleep(4)
            os.system('cls')
            continue

        designation = input("Job Title: ")
        if not designation.isalpha():
            print("Designation must consist of only letters.")
            time.sleep(4)
            os.system('cls')
            continue

        try:
            hours = int(input("Shift Hours: "))
        except ValueError:
            print("Working hours must be an integer.")
            time.sleep(4)
            os.system('cls')
            continue

        employee_object.accept_employee(name, company_name, rollno, department, designation, hours)
        print("Employee added successfully!")
        time.sleep(4)
        os.system('cls')

    elif choice == '2':
        name = input("Employee Name: ")
        employee_object.search_employee(name)
        time.sleep(4)
        os.system('cls')

    elif choice == '3':
        employee_object.display_employee()
        time.sleep(4)
        os.system('cls')

    elif choice == '4':
        print("Exiting the program.")
        time.sleep(4)
        os.system('cls')
        break

    else:
        print("Invalid choice! Please select a valid option.")
        time.sleep(4)
        os.system('cls')
