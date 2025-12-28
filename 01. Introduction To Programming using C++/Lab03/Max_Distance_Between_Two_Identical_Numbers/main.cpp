#include <iostream>

using namespace std;

int main()
{
    int numElement = 0;
    cout << "Enter Number Element You Need : ";
    cin >> numElement;

    // Read Elements From User
    int arrayNumbers[numElement] = {0};
    for(int i = 0; i < numElement; i++)
    {
        cout << "Enter Element Number (" << i + 1 << ") : ";
        cin >> arrayNumbers[i];
    }

    cout << endl;

    // Get Maximum Element
    int maximum = arrayNumbers[0];
    for(int i = 1; i < numElement; i++)
        if (arrayNumbers[i] > maximum)
            maximum = arrayNumbers[i];


    // Max Distance Between Two Identical Elements
    int occurence[maximum+1] = {-1};

    int maxDistance = 0;
    for(int i = 0; i < numElement; i++)
    {
        if(occurence[arrayNumbers[i]] == -1)
        {
            occurence[arrayNumbers[i]] = i;
        }
        else
        {
            maxDistance = max(maxDistance, i - occurence[arrayNumbers[i]]);
        }
    }
    cout << "Max Distance = " << maxDistance  << endl;
    return 0;
}
