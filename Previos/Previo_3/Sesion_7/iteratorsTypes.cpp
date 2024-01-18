#include <iostream>
#include <forward_list>
using namespace std;

int main() {
    forward_list<int> nums{1, 2, 3, 4};

    // inicializando un iterador que apuente
    // al inicio de una forward list
    forward_list<int>::iterator itr = nums.begin();

    while (itr != nums.end()) {
        // accede valor de interador usando indirection operator
        int original_value = *itr;

        // asignar valor nuevo usando indirection operator
        *itr = original_value * 2;

        // pasa adelante el iterador a la sig posicion
        itr++;
    }

    // muestra los contenidos de nums
    for (int num : nums) {
        cout << num << " ";
    }

    return 0;
}
