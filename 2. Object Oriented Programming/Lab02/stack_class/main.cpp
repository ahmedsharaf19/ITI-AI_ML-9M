#include <iostream>
using namespace std;

#define SIZE 5

class Stack
{
private:
    int tos;
    int size;
    int* stackContent;

public:
    Stack(int _size = SIZE)
    {
        tos = -1;
        size = _size;
        stackContent = new int[size];
    }

    bool push(int value)
    {
        if (tos == size - 1)
        {
            cout << "Stack is Full" << endl;
            return false;
        }
        tos++;
        stackContent[tos] = value;
        return true;
    }

    bool pop(int* value)
    {
        if (tos == -1)
        {
            cout << "Stack is Empty" << endl;
            return false;
        }
        *value = stackContent[tos];
        tos--;
        return true;
    }

    friend void clear(Stack& s);

    void print()
    {
        if (tos == -1)
        {
            cout << "Stack is Empty" << endl;
        }
        else
        {
            cout << "Stack Elements: ";
            for (int i = 0; i <= tos; i++)
            {
                cout << stackContent[i] << " ";
            }
            cout << endl;
        }
    }

    ~Stack()
    {
        delete[] stackContent;
    }
};

void clear(Stack& s)
{
    s.tos = -1;
    cout << "Stack Cleared" << endl;
}

int main()
{
    Stack s(5);
    s.push(10);
    s.push(20);
    s.push(30);

    s.print();

    int val;
    s.pop(&val);
    cout << "Popped: " << val << endl;

    s.print();

    clear(s);
    s.print();

    return 0;
}
