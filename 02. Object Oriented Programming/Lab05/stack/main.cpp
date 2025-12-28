#include <iostream>
#include <string>
#include <cctype>
#include <cmath>

using namespace std;

#define SIZE 200

class Stack
{
    int tos;
    float arr[SIZE];
public:
    Stack()
    {
        tos = -1;
    }

    void push(float v)
    {
        arr[++tos] = v;
    }
    float pop()
    {
        return arr[tos--];
    }
    float top()
    {
        return arr[tos];
    }
    bool empty()
    {
        return tos == -1;
    }
};

int prec(char op)
{
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

bool apply(float a, float b, char op, float &res)
{
    switch (op)
    {
    case '+':
        res = a + b;
        break;
    case '-':
        res = a - b;
        break;
    case '*':
        res = a * b;
        break;
    case '/':
        if (b == 0)
        {
            cout << "Error: Division by zero!" << endl;
            return false;
        }
        res = a / b;
        break;
    default:
        return false;
    }
    return true;
}

float eval(string exp)
{
    Stack values, ops;
    bool valid = true;

    for (int i = 0; i < exp.size(); i++)
    {
        char c = exp[i];
        if (isspace(c))
            continue;

        if (isdigit(c))
        {
            float val = 0;
            while (i < exp.size() && isdigit(exp[i]))
            {
                val = val * 10 + (exp[i] - '0');
                i++;
            }
            i--;
            values.push(val);
        }

        else if (c == '(')
            ops.push(c);

        else if (c == ')')
        {
            while (!ops.empty() && ops.top() != '(')
            {
                float b = values.pop();
                float a = values.pop();
                char op = (char)ops.pop();
                float res;
                if (!apply(a, b, op, res)) return NAN;
                values.push(res);
            }
            ops.pop();
        }

        else
        {
            while (!ops.empty() && prec((char)ops.top()) >= prec(c))
            {
                float b = values.pop();
                float a = values.pop();
                char op = (char)ops.pop();
                float res;
                if (!apply(a, b, op, res)) return NAN;
                values.push(res);
            }
            ops.push(c);
        }
    }

    while (!ops.empty())
    {
        float b = values.pop();
        float a = values.pop();
        char op = (char)ops.pop();
        float res;
        if (!apply(a, b, op, res)) return NAN;
        values.push(res);
    }

    return values.pop();
}

int main()
{
    string exp;
    exp = "4 * 5 + (2 * 6) - (1 + 2) / 5"; // 31.4
    float result = eval(exp);
    if (!isnan(result))
        cout << "Result = " << result << endl;
    return 0;
}
