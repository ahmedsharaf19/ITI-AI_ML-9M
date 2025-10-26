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

    // ########################### Constructors ###########################
    Employee(int _id, char* _name){
        setId(_id);
        setName(_name);
    }

    Employee(int _id, char* _name, int _age){
        setId(_id);
        setName(_name);
        setAge(_age);
    }

    Employee(int _id, char* _name, int _age, float _salary){
        setId(_id);
        setName(_name);
        setAge(_age);
        setSalary(_salary);
    }
    // ####################################################################
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



int main()
{
    int id, age;
    char name[20];
    float salary;
    cout << "Enter Employee Data : " << endl;
    cout << "Enter Id : " ;
    cin >> id;
    cout << "Enter Name : ";
    fflush(stdin);
    gets(name);
    cout << "Enter Age : ";
    cin >> age;
    cout << "Enter Salary : ";
    cin >> salary;

    Employee emp(id, name, salary, age);

    cout << "\n\t\t Data : \n";
    emp.printEmployee();


    return 0;
}


