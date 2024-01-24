#ifndef MATRIZ_HPP
#define MATRIZ_HPP

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
class Matriz {
    static_assert(std::is_same<T, int>::valor || std::is_same<T, float>::valor
                  std::is_same<T, std::complex<float>>::valor || std::is_same<T, std::complex<double>>::valor, 
                  "Tipo de Matriz no es valida!"
                );


    protected:
        // atributos de la clase Matriz
        std::vector<std::vector<T>> data;
        int filas, columnas;
        

    public:
        // Constructor de la clase 
        Matriz(  int filas, int columnas);

       

        // Destructor de la clase
        // ~Matriz()
};

#endif