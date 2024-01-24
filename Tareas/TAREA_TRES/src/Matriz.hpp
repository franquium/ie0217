/**
 * @file Matriz.hpp
 * @brief Plantilla de clase para representar una matriz bidimensional.
 * 
 * La clase Matriz es una plantilla que permite crear matrices de diferentes tipos de datos:
 * Soporta int, float y std::complex<float>.
 */
#ifndef MATRIZ_HPP
#define MATRIZ_HPP

#include <iostream>
#include <string>
#include <vector>
#include <complex>
#include <type_traits>
#include <stdexcept>
#include <limits>
using namespace std;

/**
 * La plantilla para una clase que representa una matriz bidimensional
 * 
 */
template <typename T>
class Matriz {
    static_assert(std::is_same<T, int>::value || std::is_same<T, float>::value ||
                  std::is_same<T, std::complex<float>>::value, 
                  "Tipo de Matriz no es valida!"
                );



       
        
        

    public:
         // atributos de la clase Matriz
        std::vector<std::vector<T>> data; // Almacena los elementos de la matriz.
        int filas;                        // Numero de filas de la matriz.
        int columnas;                     // Numero de columnas de la matriz.

        /**
         * @brief Constructor para crear una matriz con dimensiones especificas.
         * @param filas Numero de filas de la matriz.
         * @param columnas Numero de columnas de la matriz.
         */ 
        Matriz( int filas, int columnas);

        // // No dio tiempo de porbar con esta version y modificando el codigo
        // Matriz( int filas, int columnas, T data);


        // // Metodos de la clase Matriz

        // /**
        //  * @brief Metodo para solicitar al usuario  los datos de la matriz compleja
        //  * 
        //  */ 
        // void agregarElementosComplejos(std::complex<float>& data[i][j]);
        

        /**
         * @brief Metodo para solicitar al usuario el tamanno y los datos de la matriz.
         * Pide al usuario que ingrese el numero de filas y columnas, y luego los elementos de la matriz.
         * Valida que las dimensiones sean positivas y que los elementos ingresados sean del tipo correcto.
         */
        void getTamannoYDatos();


        /**
         * @brief Metodo estatico para pedir al usuario el tipo de operacion matematica.
         * Pide al usuario que ingrese un caracter que represente la operacion matematica deseada.
         * Valida que la entrada sea una operación valida (+, -, *).
         * 
         * @return char Caracter que representa la operacion matematica elegida.
         */
        static char pedirTipoOperacion();
        


        

        
};

#endif