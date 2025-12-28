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
        cin >> arrayNumbers[i];
    }

    cout << endl;

    cout << "Pointer Add\t:Array Add\t:Pointer Element\t:Array Element  \n";
    for (int i = 0; i < numElement; i++)
        cout << pointerArray+i << "\t:" << &arrayNumbers[i] << "\t:" << *(pointerArray+i) << "\t\t\t:" << arrayNumbers[i] << endl;

    cout<<endl;

    cout << endl;

    return 0;
}
