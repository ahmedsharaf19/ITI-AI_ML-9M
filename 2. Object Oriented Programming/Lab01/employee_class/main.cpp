#include <iostream>
#include <string.h>

using namespace std;


class Employee{
private :
    int id;
    char name[20];
    int age;
    float salary;
public:
    void setId(int _id){
        if (_id < 0){
            cout << "In Valid Id" << endl;
        }
        else {
            id = _id;
        }
    }
    void setAge(int _age){
        if (_age < 0){
            cout << "In Valid Age" << endl;
        }
        else {
            age = _age;
        }
    }

    void setName(char* _name){
        strcpy(name, _name);
    }

    void setSalary(float _salary){
        if (salary < 0) {
            cout << "In Valid Salary" << endl;
        }
        else {
            salary = _salary;
        }
    }


    int getId(){return id;}
    int getAge() {return age;}
    char* getName(){return name;}
    float getSalary(){return salary;}

    void printEmployee(){
        cout << "Id : " << id << "\t Name : " << name << "\t Age : " << age << " \t Salary : " << salary << endl;
    }
};

void printEmployee(Employee emp);


int main()
{
    Employee emp;
    int id, age;
    char name[20];
    float salary;
    cout << "Enter Employee Data : " << endl;
    cout << "Enter Id : " ;
    cin >> id;
    emp.setId(id);
    cout << "Enter Name : ";
    fflush(stdin);
    gets(name);
    emp.setName(name);
    cout << "Enter Age : ";
    cin >> age;
    emp.setAge(age);
    cout << "Enter Salary : ";
    cin >> salary;
    emp.setSalary(salary);

    cout << "\n\t\tPrinted Data By Memebr Function : \n";
    emp.printEmployee();

    cout << "--------------------------------------------------------------------------------------------------------\n";
    cout << "\n\t\tPrinted Data By Stand Alone Function : \n";
    printEmployee(emp);
    return 0;
}

void printEmployee(Employee emp){
     cout << "Id : " << emp.getId() << "\t Name : " << emp.getName() << "\t Age : " << emp.getAge() << " \t Salary : " << emp.getSalary() << endl;
}
