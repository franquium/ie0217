#include <iostream>
using namespace std;

// funcion para imprimir un array
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

void insertionSort(int array[], int size) {
    for (int step = 1; step < size; step++) {
        int key = array[step];
        int j = step - 1;

        // Comparara key con cada elemento a su izquierda hasta un elemento mas pequenno que
        // el es encontrado.
        // Para orden descendente, cambiar key[array[j]] por key>array[j].
        while (key < array[j] && j >= 0) {
            array[j + 1] = array[j];
            --j;
        }
        array[j + 1] = key;
    }
}

// Driver code
int main() {
    int data[] = {9, 5, 1, 4, 3};
    int size = sizeof(data) / sizeof(data[0]);
    insertionSort(data, size);
    cout << "Array ordenado en Orden Ascendente:\n";
    printArray(data, size);

    return 0;
}

