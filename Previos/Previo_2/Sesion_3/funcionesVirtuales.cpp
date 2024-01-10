/* Archivo sobre las funciones virtuales en C++ */
#include <iostream>
using namespace std;

class Base {
public:
    virtual void print() {
        cout << "Base Function" << endl;
    }
};

class Derived : public Base {
public:
    void print() {
        cout << "Derived Function" << endl;
    }
};

int main() {
    Derived derived1;

    // puntero de tipo Base que apunta a derived1
    Base* base1 = &derived1;

    // llama la func miembro de clase Derived
    base1->print();

    return 0;
}
