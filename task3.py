import re

class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
    
    def validate_email(self):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, self.email):
            return True
        return False
    
    def save_to_file(self):
        try:
            with open("employees.txt", "a") as file:
                file.write(f"Name: {self.name}, Email: {self.email}, Salary: {self.salary}")
            print(f"Employee {self.name} details saved to file.")
        except IOError:
            print("Error: Could not write to file.")

# Function to get employee details from user input
def get_employee_details():
    name = input("Enter employee name: ")
    email = input("Enter employee email: ")
    salary = input("Enter employee salary: ")
    
    # Check if salary is a valid number
    try:
        salary = float(salary)
    except ValueError:
        print("Invalid salary. Please enter a numeric value.")
        return None
    
    employee = Employee(name, email, salary)
    
    # Validate email
    if not employee.validate_email():
        print("Error: Invalid email format.")
        return None
    
    return employee

def main():
    while True:
        print("\nEnter details for a new employee.")
        employee = get_employee_details()
        if employee:
            employee.save_to_file()

        # Ask the user if they want to add another employee
        another = input("Would you like to add another employee? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
