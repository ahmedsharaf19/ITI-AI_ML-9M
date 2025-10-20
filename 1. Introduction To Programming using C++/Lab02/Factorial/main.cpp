#include <iostream>

using namespace std;

int main()
{
    int number;
    long int fact = 1;

    cout << "Enter Number : ";
    cin >> number;
    if (number < 0)
        cout << "No Factorial Of Negative Value !" << endl;
    else {
        for(int counter = 2; counter <= number; counter++)
            fact *= counter;
        cout << "Factorial Of " << number << " = " << fact << endl;
    }

    return 0;
}
