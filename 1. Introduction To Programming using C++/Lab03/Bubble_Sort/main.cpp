#include <iostream>

using namespace std;
#define SIZE 5

int main()
{
    int temp = 0;
    int numbers[SIZE] = {2, 1, 5, 4, 3};
    for (int i = 0; i < SIZE ; i++){
        for (int j = i + 1; j < SIZE; j++){
            if(numbers[i] > numbers[j]){
            temp = (numbers[i] ^ numbers[j]);
            numbers[i] ^= temp;
            numbers[j] ^= temp;
            }
         }
    }
    for(int i = 0; i < SIZE; i++)
        cout << numbers[i] << '\t';

    return 0;
}
