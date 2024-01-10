/* Archivo sobre la Herencia en C++ */
#include <iostream>
using namespace std;

class Animal {
public:
    void eat() { // Func monchar
        cout << "I can eat!" << endl; // Poder monchar
    }

    void sleep() { // Func mimir
        cout << "I can sleep!" << endl; // Poder mimir
    }
};

class Dog : public Animal {
public:
    void bark() { // Func Ladrar
        cout << "I can bark! Woof woof!" << endl; // Guauu Guauu!
    }
};

int main() {
    Dog dog1;

    // Calling members of the base class
    dog1.eat();
    dog1.sleep();

    // Calling member of the derived class
    dog1.bark();

    return 0;
}
