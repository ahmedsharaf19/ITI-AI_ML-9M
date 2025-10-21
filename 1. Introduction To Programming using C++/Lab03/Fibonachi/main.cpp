#include <iostream>

using namespace std;

int main()
{
    int term;

    long long prevPrev = 0, prev = 1;
    long long fibonachiValue = 0;
    cout << "Enter Number Of Term You Need From Fibonachi Series : ";
    cin >> term;

    if (term == 0 )
    {
        fibonachiValue = prevPrev;
    }
    else if (term == 1)
    {
        fibonachiValue = prev;
    }
    else
    {
        for (int i = 0; i < term-1; i++)
        {
            fibonachiValue = prevPrev + prev;
            prevPrev = prev;
            prev = fibonachiValue;
        }

    }
    cout << "Fibonachi of term {" << term << "} = " << fibonachiValue;
    return 0;
}
