#include <iostream>

using namespace std;

int main()
{
    int numElement = 0;
    cout << "Enter Number Element You Need : ";
    cin >> numElement;

    int arrayNumbers[numElement] = {0};
    int* pointerArray = arrayNumbers;
    for(int i = 0; i < numElement; i++){
        cout << "Enter Element Number (" << i + 1 << ") : ";
        cin >> *(pointerArray+i);
    }

    cout << endl;

    for (int i = 0; i < numElement; i++)
        cout << *(pointerArray+i) << "\t";
    cout<<endl;

    cout << endl;

    return 0;
}
