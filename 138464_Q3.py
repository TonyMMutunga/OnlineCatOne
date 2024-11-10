class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary for {self.name} has been updated to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} (ID: {employee.employee_id}) has been added to the department '{self.department_name}'.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for the department '{self.department_name}' is: {total_salary}")
        return total_salary

    def display_all_employees(self):
        if not self.employees:
            print(f"No employees in the department '{self.department_name}'.")
        else:
            print(f"Employees in the department '{self.department_name}':")
            for employee in self.employees:
                employee.display_details()


# Interactive code to add employees to a department and display total expenditure
def main():
    # Create a department
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    # Interact with the department management system
    while True:
        print("\nDepartment Management System Menu:")
        print("1. Add an employee")
        print("2. Update an employee's salary")
        print("3. Display all employees in the department")
        print("4. Display total salary expenditure for the department")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new employee
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            try:
                salary = float(input("Enter employee salary: "))
                employee = Employee(name, employee_id, salary)
                department.add_employee(employee)
            except ValueError:
                print("Invalid input for salary. Please enter a numeric value.")

        elif choice == "2":
            # Update an employee's salary
            emp_id = input("Enter the employee ID to update salary: ")
            employee = next((emp for emp in department.employees if emp.employee_id == emp_id), None)
            if employee:
                try:
                    new_salary = float(input("Enter the new salary: "))
                    employee.update_salary(new_salary)
                except ValueError:
                    print("Invalid input for salary. Please enter a numeric value.")
            else:
                print(f"No employee found with ID {emp_id}.")

        elif choice == "3":
            # Display all employees in the department
            department.display_all_employees()

        elif choice == "4":
            # Display total salary expenditure for the department
            department.calculate_total_salary_expenditure()

        elif choice == "5":
            print("Exiting the Department Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the interactive department management system
main()
