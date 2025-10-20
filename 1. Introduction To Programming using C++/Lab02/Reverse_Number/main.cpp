#include <iostream>

using namespace std;

int main()
{
    int number, temp;
    int reversed = 0;
    int digit;
    cout << "Enter Number : ";
    cin >> number;

    temp = number;
    while (temp){
       digit = temp % 10;
       reversed = (reversed * 10) + digit;
       temp /= 10;
    }
    cout << "Original Number : " << number << endl;
    cout << "Reversed Number : " << reversed << endl;
    return 0;
}
