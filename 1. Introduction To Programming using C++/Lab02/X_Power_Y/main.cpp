#include <iostream>

using namespace std;

int main()
{
    int x, y;
    float result = 1;
    cout << "This Program Calculate X Power Of Y (X^Y)\n";
    cout << "Enter X and Y : ";
    cin >> x >> y;
    int temp = y;

    if (temp != 0)
    {
        if (temp > 0)
        {
            while (temp)
            {
                result *= x;
                temp--;
            }
        }
        else
        {
            while (temp)
            {
                result *= x;
                temp++;
            }
            result = 1 / result;
        }

    }
    cout << x << " Power " << y << " = " << result << endl;
    return 0;
}
