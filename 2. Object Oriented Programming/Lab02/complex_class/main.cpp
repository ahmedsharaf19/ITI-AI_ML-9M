#include <iostream>

using namespace std;

class Complex{
private:
    float real;
    float img;
public :

    Complex(float _real = 0, float _img = 0){
        setReal(_real);
        setImg(_img);
    }

    void setReal(float _real){
        real = _real;
    }
    void setImg(float _img){
        img = _img;
    }

    float getReal(){return real;}
    float getImg(){return img;}

    Complex add(Complex number){
        Complex temp;
        temp.setReal(real + number.getReal());
        temp.setImg(img + number.getImg());
        return temp;
    }

    Complex sub(Complex number){
        Complex temp;
        temp.setReal(getReal() - number.getReal());
        temp.setImg(getImg() - number.getImg());
        return temp;
    }

    void print(){
        if (getImg() >= 0)
            cout << getReal() << '+' << getImg() << 'j' << endl;
        else
            cout << getReal() << getImg() << 'j' << endl;
    }
};






int main()
{
    Complex c1;
    Complex c2(10, 20);
    cout << "------------------------------------------------------------------\n";
    cout << "Complex Number One : ";
    c1.print();
    cout << "Complex Number Two : ";
    c2.print();
    Complex result = c1.add(c2);
    cout << "Addition Two Number : ";
    result.print();
    result = c1.sub(c2);
    cout << "Subtract Two Number : ";
    result.print();
    return 0;
}
