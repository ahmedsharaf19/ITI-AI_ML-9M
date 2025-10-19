#include <iostream>

using namespace std;

int main()
{
    char character;
    cout << "Enter Character : ";
    cin >> character;

    if (character >= 'A' && character <= 'Z'){
        character += 32;
        cout << character ;
    }
    else if (character >= 'a' && character <= 'z'){
        character -= 32;
        cout << character;
    }
    else
        cout << "Invalid Character";
    return 0;
}
