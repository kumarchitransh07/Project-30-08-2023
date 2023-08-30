import os
import time
class Company:
    def __init__(self, name):
        self.c_name = name

class Employee(Company):
    def __init__(self):
        super().__init__('')
        self.e_name = ''
        self.e_rollno = 0
        self.e_dept = ''
        self.e_desg = ''
        self.e_sal = 0
        self.e = {}

    def Accept(self, name, cname, rollno, dept, desg, hrs):
        if name.isdigit():
            print("Validation Error: Employee name cannot be an integer.")
            return
        if not name.isalpha():
            print("Validation Error: Employee name must contain only alphabetic characters.")
            return

        if not cname.isalpha():
            print("Validation Error: Company name must contain only alphabetic characters.")
            return
        if not dept.isalpha():
            print("Validation Error: Department must contain only alphabetic characters.")
            return
        if not desg.isalpha():
            print("Validation Error: Designation must contain only alphabetic characters.")
            return

        if not isinstance(rollno, int):
            print("Validation Error: Roll number must be an integer.")
            return
        if not isinstance(hrs, int):
            print("Validation Error: Working hours must be an integer.")
            return

        self.e_name = name
        self.c_name = cname
        self.e_rollno = rollno
        self.e_dept = dept
        self.e_desg = desg
        self.e_hrs = hrs
        self.CalculateSal(hrs)
        self.e[self.e_name] = [self.e_rollno, self.c_name, self.e_dept, self.e_desg, self.e_sal, self.e_hrs]

    def Display(self):
        if not self.e:
            print("No employees in the database.")
        else:
            print("\nEmployee Details:")
            for name, data in self.e.items():
                print("Employee Name:", name)
                print("Roll No.:", data[0])
                print("Company:", data[1])
                print("Department:", data[2])
                print("Designation:", data[3])
                print("Salary:", data[4])
                print("Working Hours:", data[5])
                print()

    def Search(self, name):
        if name in self.e:
            data = self.e[name]
            print("Given Employee's Roll No. is", data[0])
            print("Given Employee works for Company named", data[1])
            print("Given Employee works in Department named", data[2])
            print("Given Employee's designation is", data[3])
            print("Given Employee's monthly salary is Rs", data[4])
            print("Given Employee's monthly working hours are", data[5])
        else:
            print("Given Employee does not exist as per Company's record")

    def CalculateSal(self, hrs):
        self.e_sal = 10000 * hrs
e = Employee()
while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Display All Employees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter Employee Name: ")
        if name.isdigit():
            print("Employee name cannot be an integer.")
            time.sleep(4)
            os.system('cls')
            continue

        cname = input("Enter Company Name: ")
        if not cname.isalpha():
            print(" Company name must contain only alphabetic characters.")
            time.sleep(4)
            os.system('cls')
            continue
        
        try:
            rollno = int(input("Enter Roll Number: "))
        except ValueError:
            print(" Roll number must be an integer.")
            time.sleep(4)
            os.system('cls')
            continue
        
        dept = input("Enter Department: ")
        if not dept.isalpha():
            print("Department must contain only alphabetic characters.")
            time.sleep(4)
            os.system('cls')
            continue
        
        desg = input("Enter Designation: ")
        if not desg.isalpha():
            print("Designation must contain only alphabetic characters.")
            time.sleep(4)
            os.system('cls')
            continue
        
        try:
            hrs = int(input("Enter Working Hours: "))
        except ValueError:
            print("Working hours must be an integer.")
            time.sleep(4)
            os.system('cls')
            continue
        
        e.Accept(name, cname, rollno, dept, desg, hrs)
        print("Employee added successfully!")
        time.sleep(4)
        os.system('cls')  # For Windows

    elif choice == '2':
        name = input("Enter Employee Name: ")
        e.Search(name)
        time.sleep(4)
        os.system('cls')  # For Windows

    elif choice == '3':
        e.Display()
        time.sleep(4)
        os.system('cls')  # For Windows

    elif choice == '4':
        print("Exiting the program.")
        time.sleep(4)
        os.system('cls')
        break

    else:
        print("Invalid choice! Please select a valid option.")
        time.sleep(4)
        os.system('cls')  # For Windows
