class Employee:
    def __init__(self, name, age, salary):
        self.name = name         
        self._age = age  
        self.salary = salary

    
    @property # allow to read only using obj.salary
    def salary(self):
        print('=== Salary property is called')
        return self.__salary
    
    @salary.setter # must have property called setter
    def salary(self, salary):
        if salary < 0:
            print("Invalid salary")
        else:
            self.__salary = salary
    
emp = Employee("Alice", 30, 50000)
emp.salary = 500  # Invalid salary
print(emp.salary) # read
print(emp.__dict__)