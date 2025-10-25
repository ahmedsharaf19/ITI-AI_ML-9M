#include <iostream>

using namespace std;

class Complex{
private:
    float real;
    float img;
public :
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
};

void print(Complex number){
        if (number.getImg() > 0)
            cout << number.getReal() << '+' << number.getImg() << 'j' << endl;
        else
            cout << number.getReal() << number.getImg() << 'j' << endl;
    }


Complex sub(Complex numberOne, Complex numberTwo){
        Complex temp;
        temp.setReal(numberOne.getReal() - numberTwo.getReal());
        temp.setImg(numberOne.getImg() - numberTwo.getImg());
        return temp;
    }

int main()
{
    Complex c1;
    float real, img;
    cout << "Enter Complex Number One : \n";
    cout << "Enter Real Part : ";
    cin >> real;
    c1.setReal(real);
    cout << "Enter Img Part : ";
    cin >> img;
    c1.setImg(img);

    cout << endl;
    Complex c2;
    cout << "Enter Complex Number Two : \n";
    cout << "Enter Real Part : ";
    cin >> real;
    c2.setReal(real);
    cout << "Enter Img Part : ";
    cin >> img;
    c2.setImg(img);

    cout << "------------------------------------------------------------------\n";
    cout << "Complex Number One : ";
    print(c1);
    cout << "Complex Number Two : ";
    print(c2);
    Complex result = c1.add(c2);
    cout << "Addition Two Number : ";
    print(result);
    result = sub(c1, c2);
    cout << "Subtract Two Number : ";
    print(result);
    return 0;
}
