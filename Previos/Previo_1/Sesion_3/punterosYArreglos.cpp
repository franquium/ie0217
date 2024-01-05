// C++ Program para mostrar dir de cada elemento de un arreglo
#include <iostream>
using namespace std;

int main() {
    float arr[3];

    // declarando pointer variable
    float *ptr;

    cout << "Mostrando direccion usando arrays: " << endl;

    // usando for loop para imprimir dirs de todos los elementos del array
    for (int i = 0; i < 3; ++i) {
        cout << "&arr[" << i << "] = " << &arr[i] << endl;
    }

    // ptr = &arr[0]
    ptr = arr;

    cout << "\nMostrando direccion usando  punteros: " << endl;

    // usando for loop para imprimir dirs de todos los elementos del array
    // usando notacion de  puntero
    for (int i = 0; i < 3; ++i) {
        cout << "ptr + " << i << " = " << ptr + i << endl;
    }

    return 0;
}
