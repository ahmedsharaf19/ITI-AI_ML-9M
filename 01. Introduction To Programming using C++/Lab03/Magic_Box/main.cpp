#include <iostream>
#include <windows.h>

#define SCALE 4

using namespace std;


void gotoxy(int x, int y)
{
    COORD c = { (short)x, (short)y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}

/* ######### Rules #########
if CurrentNumber == 1 => Set This in row = 1 & col = middle (n / 2 + 1)
if PrevNumber % n != 0 => row--, col-- => if row < 1 | col < 1 => row = n , col = n
if prevNumber % n == 0 => row++ => if row > n then row = 1
*/

int main()
{
    int n;
    do
    {
        cout << "Enter Magic Square Number (Odd Number): " ;
        cin >> n;
    }
    while(n % 2 == 0);
    system("cls");

    int row = 1, col = n / 2 + 1;
    for(int i = 1; i <= (n*n) ; i++){
        gotoxy(col * SCALE, row * SCALE);
        cout << i;

        if (i % n == 0){
            row++;
            if(row > n) row = 1;
        }
        else {
            row = row - 1 == 0 ?  n : row - 1;
            col = col - 1 == 0 ?  n : col - 1;
        }
    }
    gotoxy(0, n * SCALE+ 2);
    cout << endl;
    return 0;
}

