#include <iostream>

using namespace std;

int main()
{
    int number, sum = 0;
    for (int i = 0; i < 5; i++)
    {
        cout << "Enter Number {"<< i + 1<< "} : ";
        cin >> number;
        sum += number;
    }
    cout << "Sum Your Five Numbers = " << sum << endl;

    return 0;
}
