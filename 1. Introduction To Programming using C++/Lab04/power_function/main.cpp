#include <iostream>

using namespace std;
float power(int x, int y);

int main()
{
    int x, y;
    cout << "This Program Calculate X Power Of Y (X^Y)\n";
    cout << "Enter X and Y : ";
    cin >> x >> y;
    float result = power(x, y);
    cout << x << " Power " << y << " = " << result << endl;

    return 0;
}





float power(int x, int y){
    int temp = y;
    float result = 1;
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
    return result;
}
