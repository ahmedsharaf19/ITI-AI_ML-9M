# Day 05 Lab Tasks

## ✅ Problem 1 — Employee Salary System  
### Create an abstract class Employee with:
- attributes: name, base_salary
- abstract method: calculate_total_salary()
- override the __str__() method to return a readable description of the employee: "Employee(name=..., base_salary=...)"

### Subclasses:
- Developer
  - attribute: num_bugs_fixed
  - bonus = num_bugs_fixed * 40
- Manager
  - attribute: num_projects
  - bonus = num_projects * 1200

### Requirements:
- Implement __str__() in each subclass so that:
  - Developer prints: "Developer: name, total_salary = X"
  - Manager prints: "Manager: name, total_salary = X"
- Implement the comparison magic method __lt__(self, other) → compare employees based on their total salary.
- Create at least 3 mixed employees.
- Sort them using Python’s sorted() and print the results using __str__().

## ✅ Problem 2 — Shape Hierarchy

### Create an abstract class Shape with:
- abstract methods:
  - area()
  - perimeter()
- implement __str__() to return the shape type (e.g., "Shape(type=Rectangle)")

### Subclasses:
- Rectangle(width, height)
- Circle(radius)
- Triangle(a, b, c)

### Requirements:
- Each subclass must override __str__() to return:
  - Shape name
  - Area
  - Perimeter
  - Example: "Rectangle: area=12.0, perimeter=14.0"
- Implement the equality magic method __eq__(self, other) → Two shapes are equal if their area is the same.
- Implement the addition magic method __add__(self, other) → Return a new object of a class CombinedShape with total area = sum of both shapes.
- Create a list of mixed shapes.

### Test:
- Equality between two shapes
- Adding two shapes
- Printing all shapes using __str__()