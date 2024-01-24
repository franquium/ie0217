#ifndef IMPRESIONMATRIZ_HPP
#define IMPRESIONMATRIZ_HPP


#include "Matriz.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <complex>
#include <type_traits>
#include <stdexcept>
using namespace std;





/**
 * La plantilla para una clase que representa una matriz bidimensional
 * 
 */
template <typename T>
class ImpresionMatriz {
public:
    // Método estático para imprimir una matriz
    static void imprimir(const Matriz<T>& matriz);
};

#endif // IMPRESIONMATRIZ_HPP
