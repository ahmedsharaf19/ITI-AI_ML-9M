#include <iostream>

using namespace std;

long long fibonacci(int x);

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;

    cout << "Fibonacci(" << n << ") = " << fibonacci(n) << endl;

    cout << "Series to " << n << " : ";
    for (int i = 0; i <= n; i++)
    {
        cout << fibonacci(i) << " ";
    }
    cout << endl;
    return 0;
}


long long fibonacci(int x){
    if (x == 0)
        return 0;
    if (x == 1)
        return 1;

    return fibonacci(x-1) + fibonacci(x-2);
}


