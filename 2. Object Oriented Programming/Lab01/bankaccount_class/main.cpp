#include <iostream>
#include <string.h>
#include <conio.h>
using namespace std;

class BanckAccount
{
private :
    int id;
    char name[20];
    float balance;
public :
    void setId(int _id)
    {
        if (_id < 0)
        {
            cout << "In Valid Id" << endl;
        }
        else
        {
            id = _id;
        }
    }

    void setName(char* _name)
    {
        strcpy(name, _name);
    }
    void setBalance(float _balance){
        if (_balance < 0)
        {
            cout << "In Valid Balance" << endl;
        }
        else
        {
            balance = _balance;
        }
    }

    float getBalance(){
        return balance;
    }
    int getId()
    {
        return id;
    }
    char* getName()
    {
        return name;
    }

    void deposite(float _balance){
        if (_balance < 0){
            cout << "Can't Deposite" << endl;
        }
        else {
            balance += _balance;
        }
    }

    void withdraw(float amount){
        if (amount > balance){
            cout << "Can't Withdraw This Amount:Your Account have't this amount" << endl;
        }
        else {
            balance -= amount;
        }
    }


};

int main()
{
    BanckAccount account;
    int id;
    float amount;
    char name[20];

    cout << "Enter Account Data : " << endl;
    cout << "Enter Id : " ;
    cin >> id;
    account.setId(id);
    cout << "Enter Name : ";
    fflush(stdin);
    gets(name);
    account.setName(name);
    cout << "Enter Balance : ";
    cin >> amount;
    account.setBalance(amount);

    int choice;
    do {
        cout << endl;
        cout << "\t\t 1. Current Balance\n\t\t 2. Withdraw\n\t\t 3. Deposite\n\t\t 4.Exit\n";
        cout << "\t\t Enter Your Choice (1-4) : ";
        cin >> choice;
        system("cls");
        switch(choice){
        case 1:
            cout << "\t\t Current Balance : " << account.getBalance() << endl;
            getch();
            break;
        case 2:
            cout << "\t\t Enter Amount : " ;
            cin >> amount;
            account.withdraw(amount);
            cout << "\t\t Success " << endl;
            getch();
            break;
        case 3:
            cout << "\t\t Enter Amount : " ;
            cin >> amount;
            account.deposite(amount);
            cout << "\t\t Success " << endl;
            getch();
            break;
        case 4:
            cout << "Good Bye !";
            getch();
            break;
        }
        system("cls");
    }while(choice != 4);



    return 0;
}
