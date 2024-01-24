/**
 * @file OperacionesBasicas.hpp
 * @brief Define la clase OperacionesBasicas para realizar operaciones básicas con matrices.
 *
 * La clase OperacionesBasicas extiende la funcionalidad de la clase Matriz para incluir
 * operaciones matematicas basicas como suma, resta y multiplicacion.
 */
#ifndef OPERACIONESBASICAS_HPP
#define OPERACIONESBASICAS_HPP

#include "Matriz.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <complex>
#include <type_traits>
#include <stdexcept>
#include <limits>
using namespace std;

template <typename T>
class OperacionesBasicas : public Matriz<T> {
public:
    /**
     * @brief Constructor para crear una matriz con operaciones basicas.
     * @param filas Numero de filas de la matriz.
     * @param columnas Numero de columnas de la matriz.
     */
    OperacionesBasicas(int filas, int columnas);


    // Validar si es posible realizar operaciones
    /**
     * @brief Verifica si es posible realizar la suma o resta con otra matriz.
     * @param otra La otra matriz con la que se realizara la operacion.
     * @throws std::invalid_argument si las dimensiones de las matrices no son compatibles.
     */
    void esSumaORestaValida(const Matriz<T>& otra) const;


    /**
     * @brief Verifica si es posible realizar la multiplicacion con otra matriz.
     * @param otra La otra matriz con la que se realizará la operacion.
     * @throws std::invalid_argument si las dimensiones de las matrices no son compatibles.
     */
    void esMultiplicacionValida(const Matriz<T>& otra) const;


    // Sobrecarga de operadores para operaciones matriciales
    /**
     * @brief Sobrecarga del operador + para sumar dos matrices.
     * @param otra La otra matriz a sumar.
     * @return Matriz<T> Resultado de la suma.
     */
    Matriz<T> operator+(const Matriz<T>& otra) const;


    /**
     * @brief Sobrecarga del operador - para restar dos matrices.
     * @param otra La otra matriz a restar.
     * @return Matriz<T> Resultado de la resta.
     */
    Matriz<T> operator-(const Matriz<T>& otra) const;


    /**
     * @brief Sobrecarga del operador * para multiplicar dos matrices.
     * @param otra La otra matriz a multiplicar.
     * @return Matriz<T> Resultado de la multiplicacion.
     */
    Matriz<T> operator*(const Matriz<T>& otra) const;
};

#endif 
