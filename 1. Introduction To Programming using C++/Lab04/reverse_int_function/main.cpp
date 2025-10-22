#include <iostream>

using namespace std;
int reverseInt(int number);
int main()
{
    int number;
    cout << "Enter Number : ";
    cin >> number;
    cout << "Original Number : " << number << endl;
    cout << "Reversed Number : " << reverseInt(number) << endl;
    return 0;
}

int reverseInt(int number){
    int reversed = 0;
    int digit, temp;
    temp = number;
    while (temp){
       digit = temp % 10;
       reversed = (reversed * 10) + digit;
       temp /= 10;
    }
    return reversed;
}
