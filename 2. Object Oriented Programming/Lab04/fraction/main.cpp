#include <iostream>
#include <cstdlib>

using namespace std;


class Fraction{
private :
    int num;
    int denum;
public :
    Fraction(int _num = 0, int _denum = 1){
     setFraction(_num, _denum);
    }


    // Setters
    void setNum(int _num){
        if (_num != 0){
            num = _num;
        }
        else {
            num = 0;
            denum = 1;
        }
    }

    void setDenum(int _denum){
        if (_denum == 0){
            cout << "Invalid Zero In Denum!" << endl;
            return;
        }

        if (denum < 0) {
            denum *= -1;
            num *= -1;
        }else
            denum = _denum;

    }

    void setFraction(int _num, int _denum){
        setNum(_num);
        setDenum(_denum);
    }

    // getters
    int getNum(){
        return num;
    }

    int getDenum(){
        return denum;
    }

    // print
    void print(){
        if (num == 0){
            cout << num << endl;
        }
        else
            cout << num << " / " << denum << endl;
    }

    // Add Two Fraction
    Fraction add(Fraction& frc){
        Fraction result;
        int _num = (num * frc.getDenum()) + (denum * frc.getNum());
        result.setFraction(_num, denum * frc.getDenum());
        result.simplifiy();
        return result;
    }

    // Get GCD
    int GCD(){
        int a = abs(num);
        int b = abs(denum);
        if (a == 0) return -1;
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
     // Simplifiy Fraction
     void simplifiy(){
        int common_divisor = GCD();
        if (common_divisor == -1){
            return;
        }
        num = num / common_divisor;
        denum = denum / common_divisor;

        if (denum < 0) {
            denum *= -1;
            num *= -1;
        }
     }
};
int main()
{

    Fraction fractionOne(-5, 4);
    Fraction fractionTwo(6, -12);

//    Fraction fractionOne(5, 4);
//    Fraction fractionTwo(6, 12);

    cout << "\n ================= Fraction One ====================\n";
    fractionOne.print();
    fractionOne.simplifiy();
    cout << "Simplified Version : ";
    fractionOne.print();

    cout << "\n ================= Fraction Two ====================\n";
    fractionTwo.print();
    fractionTwo.simplifiy();
    cout << "Simplified Version : ";
    fractionTwo.print();

    cout << "\n ================= Addition ====================\n";
    Fraction result = fractionOne.add(fractionTwo);
    cout << "Result = ";
    result.print();

    return 0;
}
