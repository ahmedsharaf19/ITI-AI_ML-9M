#include <iostream>
#include <string.h>
using namespace std;

#define LENGTH_STR 20

void string_concatenate(char destination[],char str1[], char str2[]);

int main()
{
    char fname[LENGTH_STR] = "\0";
    char lname[LENGTH_STR] = "\0";
    char fullName[LENGTH_STR + LENGTH_STR] = "";
    cout << "Enter Your First Name : ";
    cin >> fname;
    cout << "Enter Your Second Name : ";
    cin >> lname;
    string_concatenate(fullName, fname, lname);
    cout << "You Name is : " << fullName;
    return 0;
}

void string_concatenate(char destination[],char str1[], char str2[]){
    strcat(destination, str1);
    strcat(destination, " ");
    strcat(destination, str2);
}

