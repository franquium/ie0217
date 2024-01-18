#include <iostream>
#include <list>
using namespace std;

int main() {
    list<int> nums {1, 2, 3, 4, 5};

    // inicializa el iterador a apuntar al inicio de nums
    list<int>::iterator itr = nums.begin();

    cout << "Moving forward: " << endl;
    // muestra los elementos en orden hacia delante (forward)
    while (itr != nums.end()) {
        cout << *itr << ", ";
        // mueve iterador una posicion hacia delante
        itr++;
    }

    cout << endl << "Moving backward: " << endl;

    // muestra los elementos en orden hacia atras (backwards)
    while (itr != nums.begin()) {
        if (itr != nums.end()) {
            cout << *itr << ", ";
        }
        // mueve iterador una posicion hacia atras
        itr--;
    }

    cout << *itr << endl;

    return 0;
}

