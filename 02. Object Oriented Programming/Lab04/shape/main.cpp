#include <iostream>

using namespace std;

#define PI 3.14

class Shape{
private:
    float dim1, dim2;
public :
    Shape(){
    }

    Shape(float _dim1 = 0, float _dim2 = 0){
        dim1 = _dim1;
        dim2 = _dim2;
    }


    // Setters
    void setDimOne(float _dim1){dim1 = _dim1;}
    void setDimTwo(float _dim2){dim2 = _dim2;}
    void setDim(float _dim1, float _dim2){
        dim1 = _dim1;
        dim2 - _dim2;
    }

    // Getters
    float getDimOne(){return dim1;}
    float getDimTwo(){return dim2;}

    // Print Function
    void print(){
        cout << "Dim1 = " << dim1 << " , Dim2 = " << dim2;
    }

    float getArea(){
        return 0;
    }

};

class Recrangle : public Shape{
public :
    Recrangle(float _dim1 = 0, float _dim2 = 0) : Shape(_dim1, _dim2){

    }

    // Area
    float getArea(){
        return getDimOne() * getDimTwo();
    }
};

class Circle : public Shape{
public :
    Circle(float radoius) : Shape(radoius, radoius){

    }

    // Setters
    void setRadius(float radius){
         setDim(radius, radius);
    }

    // Area
    float getArea(){
        return getDimOne() * getDimTwo() * PI;
    }
};

class Triangle : public Shape{

public :
    Triangle(float height, float width) : Shape(height, width){
    }
    // Area
    float getArea(){
        return 0.5 * getDimOne() * getDimTwo();
    }
};

int main()
{
    Recrangle rect(4, 5);     // 4 * 5                  = 20
    Circle circle(5);         // 5 * 5 * 3.14           = 78.5
    Triangle triangle(6, 10); // 0.5 * 6 * 10           = 30
    cout << "\n=================== Area Of Rectangle ======================\n";
    cout << "Area = " << rect.getArea() << endl;

    cout << "\n=================== Area Of Circle ======================\n";
    cout << "Area = " << circle.getArea() << endl;

    cout << "\n=================== Area Of Triangle ======================\n";
    cout << "Area = " << triangle.getArea() << endl;
    return 0;
}
