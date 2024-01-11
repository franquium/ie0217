#include <iostream>
using namespace std;

// funcion para swap la posicion de dos elementos
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// funcion para imprimir un array
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

// funcion del algoritmo selection sort
void selectionSort(int array[], int size) {
    for (int step = 0; step < size - 1; step++) {
        int min_idx = step;
        for (int i = step + 1; i < size; i++) {
            // Para ordenar en orden descendente, cambiar > a < en esta linea
            // Selecciona el elemento minimo o menor en cada loop.
            if (array[i] < array[min_idx])
                min_idx = i;
        }
        // pone min en la posicion correcta
        swap(&array[min_idx], &array[step]);
    }
}

// driver code
int main() {
    int data[] = {20, 12, 10, 15, 2};
    int size = sizeof(data) / sizeof(data[0]);
    selectionSort(data, size);
    cout << "Array ordenado en Orden Ascendente:\n";
    printArray(data, size);

    return 0;
}


