#include "OperacionesBasicas.hpp"

template <typename T>
OperacionesBasicas<T>::OperacionesBasicas(int filas, int columnas) : Matriz<T>(filas, columnas) {}

template <typename T>
void OperacionesBasicas<T>::esSumaORestaValida(const Matriz<T>& otra) const {
    // Implementacion de la validacion
    // return ( (this->filas == otra.filas) && (this->columnas == otra.columnas));
    if (this->filas != otra.filas || this->columnas != otra.columnas) {
        throw std::invalid_argument("Las dimensiones de las matrices deben ser iguales para la suma o resta");
    }    
}

template <typename T>
void OperacionesBasicas<T>::esMultiplicacionValida(const Matriz<T>& otra) const {
    // Implementacion de la validacion
    // return (this->columnas == otra.filas);
    if (this->columnas == otra.filas) {
        throw std::invalid_argument("Las dimension de las columnas (n x m) de la matriz 1 debe ser igual a la dim de las filas (m x k) de la matriz 2. ");
    }

}

template <typename T>
Matriz<T> OperacionesBasicas<T>::operator+(const Matriz<T>& otra) const {
    // Implementacion de la suma
    esSumaORestaValida(otra); // Tira la excepcion si no se cumplen las dimensiones apropiadas para la operacion
    
    // Declarando una variable para guardar el resultado
    Matriz<T> resultado(this->filas, this->columnas);
    for (int i = 0; i < (this->filas); ++i)
    {
        for (int j = 0; j < (this->columnas); ++j)
        {
            resultado.data[i][j] = this->data[i][j] + otra.data[i][j];
        }
        
    }
    
    return resultado;

}

template <typename T>
Matriz<T> OperacionesBasicas<T>::operator-(const Matriz<T>& otra) const {
    // Implementacion de la resta
    esSumaORestaValida(otra); // Tira la excepcion si no se cumplen las dimensiones apropiadas para la operacion

    // Declarando una variable para guardar el resultado
    Matriz<T> resultado(this->filas, this->columnas);
    for (int i = 0; i < (this->filas); ++i)
    {
        for (int j = 0; j < (this->columnas); ++j)
        {
            resultado.data[i][j] = this->data[i][j] - otra.data[i][j];
        }
        
    }
    
    return resultado;

}

template <typename T>
Matriz<T> OperacionesBasicas<T>::operator*(const Matriz<T>& otra) const {
    // Implementacion de la multiplicacion
    esMultiplicacionValida(otra); // Tira la excepcion si no se cumplen las dimensiones apropiadas para la operacion

    Matriz<T> resultado(this->filas, otra.columnas);
    for (int i = 0; i < this->filas; ++i) {
        for (int j = 0; j < otra.columnas; ++j) {
            T sumaDeElementos = T();
            for (int k = 0; k < this->columnas; ++k) {
                sumaDeElementos += this->data[i][k] * otra.data[k][j];
            }
            resultado.data[i][j] = sumaDeElementos;
        }
    }
    return resultado;


}


