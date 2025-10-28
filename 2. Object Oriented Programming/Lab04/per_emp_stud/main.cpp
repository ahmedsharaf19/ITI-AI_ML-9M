#include <iostream>

using namespace std;

class Person{
private :
    int id;
    int age;
    char* name;
public :
    Person(int _id, char* _name, int _age){
        id = _id;
        name = _name;
        age = _age;
    }

    // Setters
    void setId(int _id){
        id = _id;
    }
    void setAge(int _age){
        age = _age;
    }
    void setName(char* _name){
        name = _name;
    }

    // Getters
    int getId(){return id;}

    int getAge(){return age;}

    char* getName(){return name;}

    // Print Function
    void print(){
        cout << "Id = " << id << " : Name = " << name << " : Age = " << age;
    }
};

class Student :public Person{
private :
    int grade;
public :
    Student(int _id, char* _name, int _age, int _grade) : Person(_id, _name, _age) {
        grade = _grade;
    }

    // Setters
    void setGrade(int _grade){
        grade = _grade;
    }

    // Getters
    int getGrade(){return grade;}

    // Override Print
    void print(){
        Person::print();
        cout << " : Grade = " << grade << endl;
    }
};

class Employee :public Person{
private :
    float salary;
public :
    Employee(int _id, char* _name, int _age, float _salary)  : Person(_id, _name, _age) {
        salary = _salary;
    }

    // Setters
    void setSalary(int _salary){
        salary = _salary;
    }

    // Getters
    int getSalary(){return salary;}

    // Override Print
    void print(){
        Person::print();
        cout << " : Salary = " << salary << endl;
    }
};

int main()
{
    Person person(1, "ahmed sharaf", 23);
    Student student(1, "Khalid Ali", 21, 70);
    Employee employee(1, "Saleh Ahmed", 40, 10000);

    // Print Info Of Person
    cout << "\n=================== Person Class =================== \n";
    person.print();

    // Print Info Of Student
    cout << "\n\n=================== Student Class =================== \n";
    student.print();

    // Print Info Of Employee
    cout << "\n\n=================== Employee Class =================== \n";
    employee.print();
    return 0;
}
