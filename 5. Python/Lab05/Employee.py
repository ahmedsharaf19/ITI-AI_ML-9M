from abc import ABC, abstractmethod
from typing import override

# Employee 
#   attributes: name, base_salary
#   methods: calculate_salary() -> abstract method
#   override __str__ to return "Employee: {name}, Base Salary: {base_salary}"

class Employee(ABC):
    def __init__(self, name: str, base_salary: float) -> bool:
        """
        Initialize an Employee with a name and base salary.
        paremeters :
            name, base_salary

        """
        self.name = name
        self.base_salary = base_salary

    @abstractmethod
    def calculate_salary(self):
        """
        Calculate the total salary of the employee.
        """
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the Employee.
        return :
            str > message
        """
        return f"Employee: {self.name}, Base Salary: {self.base_salary}"
    
    @override
    def __lt__(self, other: 'Employee') -> bool:
        """
        Compare two employees based on their total salary.
        parameters :
            Employee
        return :
            bool
        """
        return self.calculate_salary() < other.calculate_salary()

# Developer class inheriting from Employee
# attributes: num_bugs_fixed, (@property)bouns = num_bugs_fixed * 40
 
 # Manager Class inheriting from Employee
 # attributes: num_projects, (property) bonus = num_projects * 1200

# override __str__ to print "Delveloper/manager: name, total_salary = X"


class Developer(Employee):
    def __init__(self, name: str, base_salary: float, num_bugs_fixed: int) -> None:
        """
        Initialize a Developer with a name, base salary, and number of bugs fixed.
        parameters :
            name, base_salary, num_bugs_fixed
        
        """
        super().__init__(name, base_salary)
        self.num_bugs_fixed = num_bugs_fixed

    @property
    def bonus(self) -> float:
        """
        Calculate the bonus based on the number of bugs fixed.
        return :
            bonus
        """
        return self.num_bugs_fixed * 40
    
    def calculate_salary(self) -> float:
        """
        Calculate the total salary of the developer.
        return :
            total_salary
        """
        return self.base_salary + self.bonus
    
    @override
    def __str__(self) -> str:
        """
        Return a string representation of the Developer.
        return :
            str > message
        """
        return f"Developer: {self.name}, Total Salary: {self.calculate_salary()}"



class Manager(Employee):
    def __init__(self, name: str, base_salary: float, num_projects: int) -> None:
        """
        Initialize a Manager with a name, base salary, and number of projects.
        parameters :
            name, base_salary, num_projects
        
        """
        super().__init__(name, base_salary)
        self.num_projects = num_projects

    @property
    def bonus(self) -> float:
        """
        Calculate the bonus based on the number of projects.
        return :
            bonus
        """
        return self.num_projects * 1200

    def calculate_salary(self) -> float:
        """
        Calculate the total salary of the manager.
        """
        return self.base_salary + self.bonus

    @override
    def __str__(self) -> str:
        """
        Return a string representation of the Manager.
        """
        return f"Manager: {self.name}, Total Salary: {self.calculate_salary()}"


if __name__ == "__main__":
    employees = [
        Developer("ahmed", 50000, 50),
        Manager("hossam", 60000, 5),
        Developer("khalid", 55000, 70),
    ]
    sorted_employees = sorted(employees)
    for emp in sorted_employees:
        print(emp)  