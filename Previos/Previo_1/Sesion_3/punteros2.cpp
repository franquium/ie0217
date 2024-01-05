#include <iostream>
using namespace std;

int main() {
    int var = 5;
    int* pointVar;

    // guarda direccion de var
    pointVar = &var;

    // imprimir var
    cout << "var = " << var << endl;

    // imprimir *pointVar
    cout << "pointVar = " << pointVar << ", " << "*pointVar = " << *pointVar << endl;

    cout << "Cambiando valor de var a 7:" << endl;

    // cambiar valor de var a 7
    var = 7;

    // imprimir var
    cout << "var = " << var << endl;

    // imprimir *pointVar
    cout << "pointVar = " << pointVar << ", " << "*pointVar = " << *pointVar << endl;

    cout << "Cambiando valor de *pointVar a 16:" << endl;

    // cambiar valor de var a 16
    *pointVar = 16;

    // imprimir var
    cout << "var = " << var << endl;

    // imprimir *pointVar
    cout << "pointVar = " << pointVar << ", " << "*pointVar = " << *pointVar << endl;

    return 0;
}
