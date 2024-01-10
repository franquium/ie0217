#include <iostream>
using namespace std;

class ClassB;

class ClassA {
private:
    int numA;

    // declarancion de clase amiga
    friend class ClassB;

public:
    // inicializando el constructor numA a 12
    ClassA() : numA(12) {}
};

class ClassB {
private:
    int numB;

public:
    // inicializando el constructor numB a 1
    ClassB() : numB(1) {}

    // func miembra para sumar numA
    // de ClassA y numB des ClassB
    int add() {
        ClassA objectA;
        return objectA.numA + numB;
    }
};

int main() {
    ClassB objectB;
    cout << "Sum: " << objectB.add();
    return 0;
}
