#include <iostream>

using namespace std;

void swapByAddress(int*, int*);
void swapByRef(int&, int& );

int main()
{
    int numOne, numTwo;
    cout << "Enter Two Number : ";
    cin >> numOne >> numTwo; // 4 5

    cout << "---------------------------------------------------\n";
    cout << "Before Swapping : ";
    cout << "numOne = " << numOne << " : numtwo = " << numTwo << endl;
    cout << "---------------------------------------------------\n";

    cout << "After Swapping By Address: ";

    swapByAddress(&numOne, &numTwo); // 5 4
    cout << "numOne = " << numOne << " : numtwo = " << numTwo << endl;
    cout << "---------------------------------------------------\n";

    cout << "After Swapping By Reference: ";

    swapByRef(numOne, numTwo); // 4 5
    cout << "numOne = " << numOne << " : numtwo = " << numTwo << endl;
    return 0;
}


void swapByAddress(int *ptrOne, int *ptrTwo)
{
    int temp = *ptrOne;
    *ptrOne = *ptrTwo;
    *ptrTwo = temp;
}

void swapByRef(int& refOne, int& refTwo)
{
    int temp = refOne;
    refOne = refTwo;
    refTwo = temp;
}
