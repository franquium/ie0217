// Class template o plantilla de clase
#include <iostream>
using namespace std;

template <class T>

class Number {
    private:
    // Variable de tipo T
    T num;

    public:
        Number(T n) : num(n) {}  // constructor

        T getNum() {
            return num;
        }
};

int main() {
    
    // creando objecto con tipo int 
    Number<int> numberInt(7);

    // creando objecto con tipo double
    Number<double> numberDouble(7.7);

    cout << "int Number = " << numberInt.getNum() << endl;
    cout << "double Number = " << numberDouble.getNum() << endl;

    return 0;
}
