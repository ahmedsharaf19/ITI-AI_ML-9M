#include <iostream>
#include <conio.h>
using namespace std;

int main()
{
    char ch;
    int flag = 0;
    do
    {
        cout << "Menu List : " << endl;
        cout << "\t1.New\n\t2.Delete\n\t3.Exit\n";
        cout << "\tEnter Your Choise (N, D, E): ";
        ch = getche();
        cout<<endl;
        switch(ch)
        {
        case 'n':
        case 'N':
            cout << "You Are Selected New" << endl;
            break;
        case 'd':
        case 'D':
            cout << "You Are Selected Delete" << endl;
            break;
        case 'e':
        case 'E':
        case 27:
            cout << "You Are Selected Exites : Bye!" << endl;
            flag = 1;
            break;
        }
        getch();
        system("cls");
    }
    while (!flag);
    return 0;
}
