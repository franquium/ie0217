#include <iostream>
using namespace std;

class ClassB;

class ClassA {
public:
    // inicializando el constructor numA a 12
    ClassA() : numA(12) {}

private:
    int numA;

    // declarancion de func amiga
    friend int add(ClassA, ClassB);
};

class ClassB {
public:
    // inicializando el constructor numB a 1
    ClassB() : numB(1) {}

private:
    int numB;

    // declarancion de func amiga
    friend int add(ClassA, ClassB);
};

// accesando miembros de ambas clases
int add(ClassA objectA, ClassB objectB) {
    return (objectA.numA + objectB.numB);
}

int main() {
    ClassA objectA;
    ClassB objectB;
    cout << "Sum: " << add(objectA, objectB);
    return 0;
}
