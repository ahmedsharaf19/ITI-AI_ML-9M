#include <iostream>

using namespace std;

void swap(int* numOne, int* numTwo);

int main()
{
    int numberOne, numberTwo;
    cout << "Enter First Number : ";
    cin >> numberOne;
    cout << "Enter Second Number : ";
    cin >> numberTwo;

    cout << "\n\t\t\t------- Before Swap -------\n";
    cout << "\t\t\tnumberOneAdd = " << &numberOne << endl;
    cout << "\t\t\tnumberTwoAdd = " << &numberTwo << endl;
    cout << "\t\t\tnumberOne = " << numberOne << " : numberTwo = " << numberTwo << endl;
    swap(&numberOne, &numberTwo);
    cout << "\n\n\t\t\t------- After Swap -------\n";
    cout << "\t\t\tnumberOneAdd = " << &numberOne << endl;
    cout << "\t\t\tnumberTwoAdd = " << &numberTwo << endl;
    cout << "\t\t\tnumberOne = " << numberOne << " : numberTwo = " << numberTwo << endl;

    return 0;
}

void swap(int* numOne, int* numTwo){
    int temp = *numOne;
    *numOne = *numTwo;
    *numTwo = temp;
}
