#include <iostream>

using namespace std;

int main()
{
    int number;
    cout << "Enter Number : ";
    cin >> number;
    if (number == 0)
        cout << number << " is Zero\n";
    else if (number % 2 == 0)
        cout << number << " is even" << endl;
    else
        cout << number << " is odd " << endl;
    return 0;
}
