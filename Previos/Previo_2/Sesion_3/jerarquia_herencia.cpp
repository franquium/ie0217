#include <iostream>
using namespace std;

class Animal {
public:
    void info() { cout << "I am an animal." << endl; }
};

class Dog : public Animal {
public:
    void bark() { cout << "I am a Dog. Woof woof." << endl; }
};

class Cat : public Animal {
public:
    void meow() { cout << "I am a Cat. Meow." << endl; }
};

int main() {
    // Crear objecto de Clase Dog 
    Dog dog1;
    cout << "Dog Class:" << endl;
    dog1.info(); // Parent Class func
    dog1.bark();

    // Crear objecto de Clase Cat
    Cat cat1;
    cout << "\nCat Class:" << endl;
    cat1.info(); // Parent Class func
    cat1.meow();

    return 0;
}
