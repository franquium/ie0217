// Bubble sort optimizado en C++
#include <iostream>
using namespace std;

// Rerforma bubble sort
void bubbleSort(int array[], int size) {
    // loop para acceder a cada elemento del array
    for (int step = 0; step < (size-1); ++step) {
        // revisa si ocurre un swapping
        int swapped = 0;

        // loop para comparar dos elementos
        for (int i = 0; i < (size-step-1); ++i) {
            // comparara dos elementos del array
            // cambia > a < para ordenar en orden descendente
            if (array[i] > array[i + 1]) {
                // swapping ocurre si elementos
                // no estan en orden deseado
                int temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;

                swapped = 1;
            }
        }

        // no swapping implica que el array ya esta ordenado
        // ergo no hay necesidad de seguir la comparacion
        if (swapped == 0) {
            break;
        }
    }
}

// imprimir un array
void printArray(int array[], int size) {
    for (int i = 0; i < size; ++i) {
        cout << " " << array[i];
    }
    cout << "\n";
}

int main() {
    int data[] = {-2, 45, 0, 11, -9};

    // busca el largo del array
    int size = sizeof(data) / sizeof(data[0]);

    bubbleSort(data, size);

    cout << "Array ordenado en Orden Ascendente:\n";
    printArray(data, size);

    return 0;
}
