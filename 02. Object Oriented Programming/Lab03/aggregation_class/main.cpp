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
    Point* ul;
    Point* lr;

public:
    Rectangle() {
        ul = NULL;
        lr = NULL;
        cout << "Rectangle Constructor" << endl;
    }

    Rectangle(Point* _ul, Point* _lr) {
        ul = _ul;
        lr = _lr;
        cout << "Rectangle Constructor Created Point" << endl;
    }


    void setPoints(Point* _ul, Point* _lr) {
        ul = _ul;
        lr = _lr;
    }

    void print() {
        if (ul != NULL && lr != NULL) {
            cout << "Rectangle: UL=";
            ul->print();
            cout << ", LR=";
            lr->print();
            cout << endl;
        } else {
            cout << "Rectangle has No points" << endl;
        }
    }

    ~Rectangle() {
        cout << "Rectangle Destruction (no Point Deletion)" << endl;
    }
};
/* ################################################################## */

/* ######################## Triangle ######################### */
class Triangle {
private:
    Point *p1, *p2, *p3;

public:
    Triangle() {
        p1 = p2 = p3 = NULL;
        cout << "Triangle Constructor" << endl;
    }

    Triangle(Point* _p1, Point* _p2, Point* _p3) {
        p1 = _p1;
        p2 = _p2;
        p3 = _p3;
        cout << "Triangle Constructor Created Point" << endl;
    }


    void print() {
        if (p1 != NULL && p2 != NULL && p3 != NULL) {
            cout << "Triangle Points: ";
            p1->print();
            cout << " , ";
            p2->print();
            cout << " , ";
            p3->print();
            cout << endl;
        } else {
            cout << "Triangle has No points" << endl;
        }
    }

    ~Triangle() {
        cout << "Triangle Destruction (no Point Deletion)" << endl;
    }
};
/* ################################################################## */


/* ######################## Circle ######################### */
class Circle {
private:
    Point* center;
    int radius;

public:
    Circle(int _r = 0) {
        radius = _r;
        center = NULL;
        cout << "Circle Constructor" << endl;
    }

    Circle(Point* _center, int _r = 0) {
        center = _center;
        radius = _r;
        cout << "Circle Constructor Created Point" << endl;
    }

    void print() {
        if (center != NULL) {
            cout << "Circle Center=";
            center->print();
            cout << ", Radius=" << radius << endl;
        } else {
            cout << "Circle has No center" << endl;
        }
    }

    ~Circle() {
        cout << "Circle Destruction (no Point Deletion)" << endl;
    }
};
/* ################################################################## */

int main() {
    Point p1(0, 0);
    Point p2(10, 0);
    Point p3(5, 10);
    Point p4(10, 5);
    Point center(6, 6);

    cout << "=== Create Rectangle ===" << endl;
    Rectangle rect(&p1, &p4);
    rect.print();
    cout << "\n=== Create Triangle ===" << endl;
    Triangle tri(&p1, &p2, &p3);
    tri.print();

    cout << "\n=== Create Circle ===" << endl;
    Circle c(&center, 8);
    c.print();

    cout << "\n====================================" << endl;
    return 0;
}
