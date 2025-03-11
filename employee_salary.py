# Parent class (Base class)
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id  
        self.name = name  
        self._salary = salary  # Encapsulated (protected) attribute

    def calculate_salary(self):  
        pass  # Placeholder (will be overridden in subclasses)

# Subclass for hourly employees
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, 0)  # Using super() to call the parent class constructor  
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        self._salary = self.hourly_rate * self.hours_worked
        return self._salary  

# Subclass for salaried employees
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, monthly_salary)  # Using super() to avoid repeating code

    def calculate_salary(self):
        return self._salary  # Monthly salary is already set

# Asks the user for details instead of using fixed values
emp_type = input("Enter employee type (hourly/salaried): ").strip().lower()  
# .strip() removes extra spaces, .lower() makes input case-insensitive

if emp_type == "hourly":
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    hourly_rate = float(input("Enter Hourly Rate: "))
    hours_worked = float(input("Enter Hours Worked: "))
    employee = HourlyEmployee(emp_id, name, hourly_rate, hours_worked)

elif emp_type == "salaried":
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    monthly_salary = float(input("Enter Monthly Salary: "))
    employee = SalariedEmployee(emp_id, name, monthly_salary)

else:
    print("Invalid employee type entered.")
    exit()

# Output the salary
print(f"{employee.name}'s Salary: ${employee.calculate_salary():,.2f}")
