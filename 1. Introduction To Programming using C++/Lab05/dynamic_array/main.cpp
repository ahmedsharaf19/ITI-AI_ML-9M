#include <iostream>

using namespace std;

int main()
{
    int numElement = 0;
    cout << "Enter Number Element You Need : ";
    cin >> numElement;

    int* pointerArray = new int[numElement];

    // Read Array
    for(int i = 0; i < numElement; i++){
        cout << "Enter Element Number (" << i + 1 << ") : ";
        cin >> pointerArray[i];
    }

    cout << endl;

    // Print Array
    for (int i = 0; i < numElement; i++)
        cout << *(pointerArray+i) << "\t";
    cout<<endl;


    cout << endl;

    // Summition OF Array
    int sum = 0;
    for(int i = 0; i < numElement; i++)
        sum += pointerArray[i];
    cout << "Sum of Array = " << sum << endl;
    cout << endl;

    // Max Element in Array
    int maximum = pointerArray[0];
    for(int i = 1; i < numElement; i++)
        if (pointerArray[i] > maximum)
            maximum = pointerArray[i];
    cout << "Max Number in Array = " << maximum << endl;
    cout << endl;

    // Min Element in Array
    int minmum = pointerArray[0];
    for(int i = 1; i < numElement; i++)
        if (pointerArray[i] < minmum)
            minmum = pointerArray[i];
    cout << "Min Number in Array = " << minmum << endl;
    cout << endl;

    delete[] pointerArray;
    return 0;
}
