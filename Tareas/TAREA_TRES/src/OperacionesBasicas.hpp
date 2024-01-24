#ifndef OPERACIONESBASICAS_HPP
#define OPERACIONESBASICAS_HPP

#include "Matriz.hpp"

template <typename T>
class OperacionesBasicas : public Matriz<T> {
public:
    OperacionesBasicas(int filas, int columnas);

    // Validar si es posible realizar operaciones
    void esSumaORestaValida(const Matriz<T>& otra) const;
    void esMultiplicacionValida(const Matriz<T>& otra) const;

    // Sobrecarga de operadores para operaciones matriciales
    Matriz<T> operator+(const Matriz<T>& otra) const;
    Matriz<T> operator-(const Matriz<T>& otra) const;
    Matriz<T> operator*(const Matriz<T>& otra) const;
};

#endif 
