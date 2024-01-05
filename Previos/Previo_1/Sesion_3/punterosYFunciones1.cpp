#include <iostream>
using namespace std;

// func que toma el valor como parametro
void func1 (int numVal){
    // Codigo
}

// func que toma la referencia como parametro
// notar el & antes del parametro
void func2 (int &numRef){
    // Codigo
}

int main() {

    int num = 5;
    // Pasando por valor
    func1(num);

    // Pasando por referencia
    func2(num);

    return 0;
}