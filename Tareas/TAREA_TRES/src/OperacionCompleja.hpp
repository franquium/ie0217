#ifndef OPERACIONCOMPLEJA_HPP
#define OPERACIONCOMPLEJA_HPP

#include "OperacionesBasicas.hpp"
#include <complex>

template <typename T>
class OperacionCompleja : public OperacionesBasicas<T> {
public:
    OperacionCompleja(int filas, int columnas);

    // Implementación de operaciones específicas para números complejos
    // ...
};

#endif 
