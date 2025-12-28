#include <iostream>
#include <string.h>
using namespace std;

struct Employee{
    int id;
    char name[20];
    int age;
};
int main()
{
    int numberEmployee;
    do {
    cout << "Enter Number Of Employees : ";
    cin >> numberEmployee;
    }while(numberEmployee <= 0);

    Employee employees[numberEmployee];

    // Read Employees Data From User
    for (int i = 0; i < numberEmployee; i++){
        cout << "Enter Data Of Your Employee{" << i+1 << "} : " << endl;
        cout << "\t\tEnter Id : ";
        cin >> employees[i].id;
        cout << "\t\tEnter Name: ";
        fflush(stdin);
        //cin >> employees[i].name;
        gets(employees[i].name);
        cout << "\t\tEnter Age : ";
        cin >> employees[i].age;
    }

    // Print Employees Data To User
    cout << "\t\t\t--------------------- Employees Data ----------------------" << endl;
    cout << "\t\t\tId\t\t\tName\t\t\t\tAge" << endl;
    for (int i = 0; i < numberEmployee; i++){
            cout << "\t\t\t" << employees[i].id << "\t\t\t" << employees[i].name << "\t\t\t" << employees[i].age << endl;
    }



    return 0;
}
