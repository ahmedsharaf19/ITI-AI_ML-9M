#include <iostream>
#include <windows.h>
#include <conio.h>
using namespace std;
#define null -32

void textattr(int i)
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), i);

}

void gotoxy( int column, int line )
{
    COORD coord;
    coord.X = column;
    coord.Y = line;
    SetConsoleCursorPosition(
        GetStdHandle( STD_OUTPUT_HANDLE ),
        coord
    );
}


int main()
{
    char input;
    int higlightIndex = 0;
    char menu[3][10] = {"New", "Display", "Exit"};
    do
    {
        system("cls");
        for(int i = 0; i < 3; i++)
        {

            if (higlightIndex == i)
                textattr(0x04);

            gotoxy(15, i + 2);
            cout << menu[i];
            textattr(0x07);
        }

        input = getch();
        switch(input)
        {
        case -32:
            input = getch();
            if (input == 80)
            {
                higlightIndex++;
                if (higlightIndex > 2)
                    higlightIndex = 0;
            }
            else if(input == 72)
            {
                higlightIndex--;
                if (higlightIndex < 0)
                    higlightIndex = 2;
            }
            break;
        case 13:
            system("cls");
            gotoxy(15, higlightIndex + 2);
            cout << menu[higlightIndex] << " Selected";
            if(higlightIndex == 2)
                break;
            gotoxy(15, higlightIndex + 4);
            cout << "Enter Any Character To Continue : ";
            input = getch();
            break;
        case 27:
            higlightIndex = 2;
            system("cls");
            gotoxy(15, higlightIndex + 2);
            cout << menu[higlightIndex] << " Selected";
        }

    }while(!((input == 13) && (higlightIndex == 2) || input == 27));

    return 0;
}
