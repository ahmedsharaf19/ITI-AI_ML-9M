#include <iostream>

using namespace std;

int main()
{
    int numElement = 0;
    cout << "Enter Number Element You Need : ";
    cin >> numElement;

    // Read Elements From User
    int arrayNumbers[numElement] = {0};
    for(int i = 0; i < numElement; i++){
        cout << "Enter Element Number (" << i + 1 << ") : ";
        cin >> arrayNumbers[i];
    }

    cout << endl;

    // Print Element To User
    for (int i = 0; i < numElement; i++)
        cout << arrayNumbers[i] << "\t";
    cout<<endl;

    cout << endl;

    // Summition OF Array
    int sum = 0;
    for(int i = 0; i < numElement; i++)
        sum += arrayNumbers[i];
    cout << "Sum of Array = " << sum << endl;
    cout << endl;

    // Max Element in Array
    int maximum = arrayNumbers[0];
    for(int i = 1; i < numElement; i++)
        if (arrayNumbers[i] > maximum)
            maximum = arrayNumbers[i];
    cout << "Max Number in Array = " << maximum << endl;
    cout << endl;

    // Min Element in Array
    int minmum = arrayNumbers[0];
    for(int i = 1; i < numElement; i++)
        if (arrayNumbers[i] < minmum)
            minmum = arrayNumbers[i];
    cout << "Min Number in Array = " << minmum << endl;
    cout << endl;

    // Search In Array
    int element;
    bool flag = 0; // Not Found
    cout << "Enter Element You Need To Search It : ";
    cin >> element;
    for(int i = 0; i < numElement; i++){
        if (arrayNumbers[i] == element){
            flag = 1;
            break;
        }
    }
    cout << "Result Of Search -> ";
    if(flag) cout << "Found" << endl;
    else cout << "Not Found" << endl;
    cout << endl;
    return 0;
}
