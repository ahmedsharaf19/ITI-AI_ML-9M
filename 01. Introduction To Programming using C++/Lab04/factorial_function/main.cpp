#include <iostream>

using namespace std;

long long factorial(int number);
int main()
{
    int number;
    cout << "Enter Number : ";
    cin >> number;

    if (number < 0)
        cout << "No Factorial Of Negative Value !" << endl;
    else {
        cout << "Factorial Of " << number << " = " << factorial(number) << endl;
    }

    return 0;
}

long long factorial(int number)
{
    long long fact = 1;
    for(int counter = 2; counter <= number; counter++)
            fact *= counter;
    return fact;
}
