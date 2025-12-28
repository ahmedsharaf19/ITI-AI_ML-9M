#include <iostream>
using namespace std;

#define PI 3.14

// ===================== Shape Class =====================
class Shape {
private:
    float dim1, dim2;

public:
    Shape() {}
    Shape(float _dim1, float _dim2) {
        dim1 = _dim1;
        dim2 = _dim2;
    }

    // Setters
    void setDimOne(float _dim1) { dim1 = _dim1; }
    void setDimTwo(float _dim2) { dim2 = _dim2; }
    void setDim(float _dim1, float _dim2) {
        dim1 = _dim1;
        dim2 = _dim2;
    }

    // Getters
    float getDimOne() const { return dim1; }
    float getDimTwo() const { return dim2; }

    void print(){
        cout << "Dim1 = " << dim1 << ", Dim2 = " << dim2;
    }

    virtual float getArea(){
        return 0;
    }
};

// ===================== Rectangle =====================
class Rectangle : public Shape {
public:
    Rectangle(float _dim1 = 0, float _dim2 = 0) : Shape(_dim1, _dim2) {}
    float getArea(){
        return getDimOne() * getDimTwo();
    }
};

// ===================== Square =====================
class Square : public Rectangle {
public:
    Square(float side = 0) : Rectangle(side, side) {}

    // Setters
    void setSide(float side) {
        setDim(side, side);
    }

    // Getters
    float getSide(){
        return getDimOne();
    }

    float getArea(){
        return getDimOne() * getDimTwo();
    }

    void print(){
        cout << "Square side = " << getSide();
    }
};

// ===================== Circle =====================
class Circle : public Shape {
public:
    Circle(float radius = 0) : Shape(radius, radius) {}
    void setRadius(float radius) { setDim(radius, radius); }

    float getArea(){
        return PI * getDimOne() * getDimTwo();
    }
};

// ===================== Triangle =====================
class Triangle : public Shape {
public:
    Triangle(float base = 0, float height = 0) : Shape(base, height) {}
    float getArea() {
        return 0.5 * getDimOne() * getDimTwo();
    }
};

float sumArea(Shape* s[], int size);
int main() {
    Rectangle rect(4, 5);
    Circle circle(5);
    Triangle tri(6, 10);
    Square sq(7);

    Shape* shapes[4] = {&rect, &circle, &tri, &sq};
    cout << "\n=================== Rectangle ======================\n";
    rect.print();
    cout << " , Area = " << rect.getArea() << endl;

    cout << "\n=================== Circle ======================\n";
    circle.print();
    cout << " , Area = " << circle.getArea() << endl;

    cout << "\n=================== Triangle ======================\n";
    tri.print();
    cout << " , Area = " << tri.getArea() << endl;

    cout << "\n=================== Square ======================\n";
    sq.print();
    cout << " , Area = " << sq.getArea() << endl;

    cout << "\n=================== Sum Of Area ======================\n";
    cout << "Sum Of Areas = " << sumArea(shapes, 4) << endl;
    return 0;
}

float sumArea(Shape* s[], int size) {
    float sum = 0;
    for (int i = 0; i < size; i++) {
        sum += s[i]->getArea();
    }
    return sum;
}
