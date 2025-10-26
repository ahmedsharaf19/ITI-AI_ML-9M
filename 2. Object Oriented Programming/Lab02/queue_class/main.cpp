#include <iostream>
using namespace std;

#define SIZE 5

class Queue
{
private:
    int front;
    int rear;
    int size;
    int* queueContent;

public:
    Queue(int _size = SIZE)
    {
        size = _size;
        queueContent = new int[size];
        front = -1;
        rear = -1;
    }

    bool enqueue(int value)
    {
        if (rear == size - 1)
        {
            cout << "Queue is Full" << endl;
            return false;
        }

        if (front == -1)
            front = 0;

        rear++;
        queueContent[rear] = value;
        return true;
    }

    bool dequeue(int* value)
    {
        if (front == -1 || front > rear)
        {
            cout << "Queue is Empty" << endl;
            return false;
        }

        *value = queueContent[front];
        front++;
        if (front > rear)
        {
            front = rear = -1;
        }
        return true;
    }

    friend void clear(Queue& q);

    void print()
    {
        if (front == -1 || front > rear)
        {
            cout << "Queue is Empty" << endl;
        }
        else
        {
            cout << "Queue Elements: ";
            for (int i = front; i <= rear; i++)
            {
                cout << queueContent[i] << " ";
            }
            cout << endl;
        }
    }
    ~Queue()
    {
        delete[] queueContent;
    }
};

void clear(Queue& q)
{
    q.front = q.rear = -1;
    cout << "Queue Cleared" << endl;
}

int main()
{
    Queue q(5);

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.print();

    int val;
    q.dequeue(&val);
    cout << "Dequeued: " << val << endl;

    q.print();

    clear(q);
    q.print();

    return 0;
}
