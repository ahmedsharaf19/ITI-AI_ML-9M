#include <iostream>

using namespace std;

int main()
{
    int intFormat;
    cout << "Enter Number : ";
    cin >> intFormat;

    char charFormat = intFormat;
    cout << "Char Format Of Int Value \"" << intFormat << "\"" << " Is " << "\"" << charFormat << "\"\n";
    return 0;
}
