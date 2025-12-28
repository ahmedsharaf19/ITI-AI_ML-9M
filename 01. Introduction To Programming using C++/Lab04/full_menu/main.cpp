/* ######################## Include Library ######################### */

#include <iostream>
#include <conio.h>
#include <windows.h>
/* ################################################################## */

using namespace std;

/* ###################### Define Preprcessors ####################### */

#define NEW 0
#define DISPLAY 1
#define EXIT 2
#define MENU_SIZE 3
#define MAX_EMPLOYEES 2

#define EXTENDED_KEY -32
#define UP 72
#define DOWN 80
#define ENTER 13
#define ESC 27

#define RED_COLOR 0x04
#define WHITE_COLOR 0x07

#define COLUMN_POSITION 15

#define NAME_LENGTH 20
/* ################################################################## */

/* ####################### Global Variables ######################### */
int highlightIndex = NEW;
char menu[MENU_SIZE][10] = {"New", "Display", "Exit"};

struct Employee {
    int id;
    char name[NAME_LENGTH];
    int age;
};
/* ################################################################## */

/* ##################### Function Declarations ###################### */

void viewMenu(int highlightIndex);
Employee newEmployee(Employee Employees[], int numValidEmp);
void displayEmployees(Employee employees[], int numberEmployee);
bool checkId(Employee allEmployees[], int id, int numOfEmployee);
/* ################################################################## */

/* ####################### Helper Functions ######################### */

void textattr(int i) {
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), i);
}

void gotoxy(int column, int line) {
    COORD coord;
    coord.X = column;
    coord.Y = line;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}
/* ################################################################## */

int main() {
    Employee Employees[MAX_EMPLOYEES];
    int numValidEmp = 0;

    char input;

    do {
        viewMenu(highlightIndex);
        input = getch();

        switch (input) {
        case EXTENDED_KEY:
            input = getch();
            if (input == DOWN) {
                highlightIndex++;
                if (highlightIndex > EXIT)
                    highlightIndex = NEW;
            } else if (input == UP) {
                highlightIndex--;
                if (highlightIndex < NEW)
                    highlightIndex = EXIT;
            }
            break;

        case ENTER:
            system("cls");
            gotoxy(COLUMN_POSITION, highlightIndex + 2);

            if (highlightIndex == NEW) {
                if (numValidEmp < MAX_EMPLOYEES) {
                    Employees[numValidEmp] = newEmployee(Employees, numValidEmp);
                    numValidEmp++;
                } else {
                    cout << "Can't Add New Employee! List is full.\n";
                }
            } else if (highlightIndex == DISPLAY) {
                if (numValidEmp > 0)
                    displayEmployees(Employees, numValidEmp);
                else
                    cout << "No employees to display!\n";
            } else if (highlightIndex == EXIT) {
                break;
            }

            cout << "\nPress any key to continue...";
            getch();
            break;

        case ESC:
            highlightIndex = EXIT;
            system("cls");
            gotoxy(COLUMN_POSITION, highlightIndex + 2);
            break;
        }

    } while (!((input == ENTER && highlightIndex == EXIT) || input == ESC));

    return 0;
}

void viewMenu(int highlightIndex) {
    system("cls");
    for (int i = 0; i < MENU_SIZE; i++) {
        if (highlightIndex == i)
            textattr(RED_COLOR);
        gotoxy(COLUMN_POSITION, i + 2);
        cout << menu[i];
        textattr(WHITE_COLOR);
    }
}

Employee newEmployee(Employee Employees[], int numValidEmp) {
    Employee newEmp;
    gotoxy(COLUMN_POSITION, highlightIndex + 2);
    cout << "Enter Data Of Your Employee:\n";
    bool flag = 1;
    do{
        cout << "\tNew ID: ";
        cin >> newEmp.id;
        flag = checkId(Employees, newEmp.id, MAX_EMPLOYEES - numValidEmp);
        if(!flag){
            cout << "\tThis Employee Id Already Existed !" << endl;
        }
    }while(!flag);
    fflush(stdin);
    cout << "\tName: ";
    //cin >> newEmp.name;
    gets(newEmp.name);
    cout << "\tAge: ";
    cin >> newEmp.age;
    return newEmp;
}

void displayEmployees(Employee employees[], int numberEmployee) {
    cout << "\t\t----------------- Employees Data ------------------\n\n";
    cout << "\t\t\t\tID\t\tName\t\tAge\n";
    cout << "\t\t\t---------------------------------------------------\n";
    for (int i = 0; i < numberEmployee; i++) {
        cout << "\t\t\t\t" << employees[i].id
             << "\t    " << employees[i].name
             << "\t" << employees[i].age << endl;
    }
}

bool checkId(Employee allEmployees[], int id, int numOfEmployee){
    for (int i = 0; i < numOfEmployee; i++){
        if (allEmployees[i].id == id){
            return 0;
        }
    }
    return 1;
}
