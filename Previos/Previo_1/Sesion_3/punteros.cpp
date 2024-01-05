#include <iostream>
using namespace std;

int main() {
    int var = 5;

    // declarando variable puntero 
    int* pointVar;

    // guarda direccion de var
    pointVar = &var;

    // imprimir el valor de var
    cout << "var = " << var << endl;

    // imprimir direccion de var
    cout << "Address of var (&var) = " << &var 
         << endl;

    // imprimir puntero pointVar
    cout << "pointVar = " << pointVar << endl;

    // imprimir el contenido de la direccion a la cual apunta pointVar
    cout << "Content of the address pointed to by pointVar (*pointVar) = " << *pointVar << endl;

    return 0;
}
