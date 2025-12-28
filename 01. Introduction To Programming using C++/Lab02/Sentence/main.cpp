#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    char prevChar = ' ';
    char ch;
    int numberWord = 0, numberChar = 0,  sentenceLength = 0;
    cout << "Enter Sentence : ";
    do
    {
        ch = getche();
        if((prevChar != ' ' && (ch == ' ' || ch == '.') ))
            numberWord++;

        if(ch != ' ' && ch != '.')
            numberChar++;

        prevChar = ch;
        sentenceLength++;
    }while(ch != '.');
    cout << "\nNumber Of All Characters : " << sentenceLength << endl;
    cout << "Number Of Actual Characters : " << numberChar << endl;
    cout << "Number Of Word : " << numberWord << endl;

    return 0;
}
