#include <iostream>

using namespace std;

int main()
{
    int grade;
    cout << "Enter Your Grade : ";
    cin >> grade;

    if (grade > 100 || grade < 0)
        cout << "Invalid Grade" << endl;
    else if(grade >= 85 && grade <= 100)
        cout << "Excellent" << endl;
    else if (grade >= 75 && grade < 85)
        cout << "Very Good" << endl;
    else if (grade >= 65 && grade < 75)
        cout << "Good" << endl;
    else if (grade >= 60 && grade < 65)
        cout << "Poor" << endl;
    else
        cout << "Failed" << endl;

    return 0;
}
