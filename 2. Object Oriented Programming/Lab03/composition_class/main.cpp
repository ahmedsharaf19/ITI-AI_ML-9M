#include <iostream>
using namespace std;

/* ######################## Point ######################### */
class Point {
private:
    int x;
    int y;

public:
    Point(int _x = 0, int _y = 0) {
        x = _x;
        y = _y;
        cout << "Point Constructor ";
        print();
        cout << endl;
    }

    void setX(int _x) { x = _x; }
    void setY(int _y) { y = _y; }
    void setXY(int _x, int _y) {
        x = _x;
        y = _y;
    }

    int getX() { return x; }
    int getY() { return y; }

    void print() {
        cout << "(" << x << "," << y << ")";
    }

    ~Point() {
        cout << "Point Destruction (" << x << ", " << y << ")" << endl;
    }
};
/* ################################################################## */


/* ######################## Rectangle ######################### */
class Rectangle {
private:
    Point ul;
    Point lr;

public:
    Rectangle(int x1, int y1, int x2, int y2) : ul(x1, y1), lr(x2, y2) {
        cout << "Rectangle Constructor" << endl;
    }

    void setUl(int x, int y) { ul.setXY(x, y); }
    void setLr(int x, int y) { lr.setXY(x, y); }

    Point getUl() { return ul; }
    Point getLr() { return lr; }

    void print() {
        cout << "Rectangle: UL=";
        ul.print();
        cout << ", LR=";
        lr.print();
        cout << endl;
    }

    ~Rectangle() {
        cout << "Rectangle Destruction (Point Deletion)" << endl;
    }
};
/* ################################################################## */


/* ######################## Triangle ######################### */
class Triangle {
private:
    Point p1, p2, p3;

public:
    Triangle(int x1, int y1, int x2, int y2, int x3, int y3)
        : p1(x1, y1), p2(x2, y2), p3(x3, y3) {
        cout << "Triangle Constructor" << endl;
    }

    void print() {
        cout << "Triangle Points: ";
        p1.print();
        cout << " , ";
        p2.print();
        cout << " , ";
        p3.print();
        cout << endl;
    }

    ~Triangle() {
        cout << "Triangle Destruction (Point Deletion)" << endl;
    }
};
/* ################################################################## */


/* ######################## Circle ######################### */
class Circle {
private:
    Point center;
    int radius;

public:
    Circle(int x, int y, int r) : center(x, y) {
        radius = r;
        cout << "Circle Constructor" << endl;
    }

    void print() {
        cout << "Circle Center=";
        center.print();
        cout << ", Radius=" << radius << endl;
    }

    ~Circle() {
        cout << "Circle Destruction (Point Deletion)" << endl;
    }
};
/* ################################################################## */

int main() {
    cout << "=== Create Rectangle ===" << endl;
    Rectangle rect(0, 0, 10, 5);
    rect.print();

    cout << "\n=== Create Triangle ===" << endl;
    Triangle tri(0, 0, 5, 5, 10, 0);
    tri.print();

    cout << "\n=== Create Circle ===" << endl;
    Circle c(5, 5, 10);
    c.print();

    cout << "\n====================================" << endl;
    return 0;
}
