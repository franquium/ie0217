#include "ImpresionMatriz.hpp"

template <typename T>
void ImpresionMatriz<T>::imprimir(const Matriz<T>& matriz) {
    for (int i = 0; i < matriz.filas; ++i) {
        for (int j = 0; j < matriz.columnas; ++j) {
            std::cout << matriz.data[i][j] << " ";
        }
        std::cout << std::endl;
    }
}



