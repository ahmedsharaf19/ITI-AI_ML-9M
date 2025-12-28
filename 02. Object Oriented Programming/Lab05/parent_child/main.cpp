#include <iostream>

using namespace std;

class Parent{

private :
    int x;
    int y;

public:

    Parent(int _x = 0, int _y = 0){
        x = _x;
        y = _y;
    }

    // Setters
    void setX(int _x){
        x = _x;
    }

    void setY(int _y){
        y = _y;
    }

    // Getters
    int getX(){
        return x;
    }

    int getY(){
        return y;
    }

    int add(){
        return x + y;
    }
};

class Child : public Parent{
private :
    int z;
public :
    Child(){}

    Child(int _x = 0, int _y = 0, int _z = 0): Parent(_x, _y){
        z = _z;
    }

    // Setters
    void setZ(int _z){
        z = _z;
    }

    // Getters
    int getZ(){
        return z;
    }

    // Override Add
    int add(){
        return getX() + getY() + z;
    }
};


int main()
{
    Parent p1(5, 10);
    cout << "Parent Add = " << p1.add() << endl;
    Child c1(5, 10, 20);
    cout << "Child Add = " << c1.add() << endl;
    return 0;
}
