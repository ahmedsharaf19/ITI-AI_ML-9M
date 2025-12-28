#include <iostream>

using namespace std;

int main()
{
    int numRows, numCols;
    cout << "Enter Number Of Rows and Cols : ";
    cin >> numRows >> numCols;

    int twoDArray[numRows][numCols] = {{0}};

    // Read 2D Array From user
    for (int i = 0; i < numRows; i++){
        for (int j = 0; j < numCols; j++){
            cout << "Enter Values Of array[" << i << "," << j << "] : ";
            cin >> twoDArray[i][j];
        }
    }
    cout << endl;

    // Sum Of Each Row
    int sumRows[numRows] = {0};
    for (int i = 0; i < numRows; i++){
        for (int j = 0; j < numCols; j++){
            sumRows[i] += twoDArray[i][j];
        }
    }

    cout << "Summition of Each Rows : \n";
    for(int i = 0; i < numRows; i++){
        cout << "Sum Of Row Number [" << i << "] = " << sumRows[i] << endl;
    }

    cout << endl;

    // Avg Of Each Columns
    int sum;
    float avgCols[numCols] = {0};
    for (int i = 0; i < numCols; i++){
            sum = 0;
        for (int j = 0; j < numRows; j++){
            sum += twoDArray[j][i];
        }
        avgCols[i] = sum / float(numRows);
    }

    cout << "Average of Each Columns : \n";
    for(int i = 0; i < numCols; i++){
        cout << "Avg Of Col Number [" << i << "] = " << avgCols[i] << endl;
    }
    cout << endl;
    return 0;
}
