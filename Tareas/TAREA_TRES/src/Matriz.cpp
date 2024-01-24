/**
 * @file Matriz.cpp
 * @brief Implementaciones para  la plantilla de clase para representar una matriz bidimensional.
 * 
 * La clase Matriz es una plantilla que permite crear matrices de diferentes tipos de datos:
 * Soporta int, float y std::complex<float>.
 */

#include "Matriz.hpp"
#include <iostream>
#include <limits>
using namespace std;


template <typename T>
Matriz<T>::Matriz(int filas, int columnas) : filas(filas), columnas(columnas){
    if (filas <= 0 || columnas <= 0) {
        throw std::invalid_argument("Dimensiones de la matriz deben ser positivas");
    }
    data.resize(filas, std::vector<T>(columnas));
}


template <typename T>
void Matriz<T>::getTamannoYDatos(){
    // Solicita al usuario las dimensiones de la matriz
    std::cout << "Ingrese el numero de filas: ";
    std::cin >> filas;
    std::cout << "Ingrese el numero de columnas: ";
    std::cin >> columnas;

    // Valida las dimensiones ingresadas
    if (filas <= 0 || columnas <= 0) {
        throw std::invalid_argument("Dimensiones ingresadas no son validas");
    }

    // Redimensiona la matriz segun las dimensiones ingresadas
    data.resize(filas, std::vector<T>(columnas));

    // Solicita al usuario ingresar los elementos de la matriz
    T valor;
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            constexpr bool esInt = std::is_same<T, int>::value;
            constexpr bool esFloat = std::is_same<T, float>::value;
            // Caso num complejo
            // Verifica si T es std::complex<float>
            //constexpr bool esComplejo = std::is_same<T, std::complex<float>>::value;
           //cout << "esComplejo es:"  << esComplejo << endl;
            if (esInt || esFloat){
                std::cout << "Ingrese el elemento [" << i << "][" << j << "]: ";
                std::cin >> valor;
                if (std::cin.fail()) {
                    std::cin.clear(); // Limpia el valor erroneo de cin
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Descarta la entrada incorrecta
                    throw std::invalid_argument("Tipo de dato ingresado no es valido");
                }
                // Se guarda el resultado en data
                data[i][j] = valor;
            }

            else{
                /** @note Se comenta esta parte ya que no se logro implementar de forma exitosa el agregar elementos 
                 * de numeros complejos y que tambien aceptara ints e floats en el main, la version funcional solo funcionaba si solo se
                 * instanciaban en el main.cpp.
                 *  
                 * 
                 * Debido al error: 
                 * error: cannot convert 'std::complex<float>' to '__gnu_cxx::__alloc_traits<std::allocator<int> >::value_type {aka int}' 
                 * in assignment
                 *                  data[i][j] =  numComp;
                 * 
                 * Que tiene que ver con la forma que se asignan los valores de data, no se pudo resolver a tiempo :'(
                 * 
                 * Si se desea probar la parte de asignar valores complejos, asegurarse que solo haya instancias de tipo complex<float> en el main.cpp
                 * y descomentar el codigo del else que sigue despues de este largo comentario.
                 * */

                // Solicitar la parte real e imaginaria para numeros complejos
                // std::complex<float> numComp;
                // float real, imag;
                // std::cout << "Ingrese la parte real del elemento [" << i << "][" << j << "]: ";
                // std::cin >> real;
                // // Limpia el flujo de entrada
                // std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
                // if (std::cin.fail()) {
                //     std::cin.clear(); // Limpia el valor erroneo de cin
                //     std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Descarta la entrada incorrecta
                //     throw std::invalid_argument("Tipo de dato ingresado no es valido");
                // }
                // std::cout << "Ingrese la parte imag del elemento [" << i << "][" << j << "]: ";
                // std::cin >> imag;
                // // Limpia el flujo de entrada
                // std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
                // if (std::cin.fail()) {
                //     std::cin.clear(); // Limpia el valor erroneo de cin
                //     std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Descarta la entrada incorrecta
                //     throw std::invalid_argument("Tipo de dato ingresado no es valido");
                // }
                // // Se guarda el resultado en data de tipo complex
                // numComp = std::complex<float>(real, imag);
                // data[i][j] =  numComp;
                
                return ;           
                
            } 
            
        }
        
    }

    // IGNOREME: codigo para verificar funcionamiento
    // Para imprimir la matriz
    for (int i = 0; i < filas; i++) {
                    for (int j = 0; j < columnas; j++) {
                        cout << data[i][j] << "  ";
                    }
                    cout << endl;
    }

}

template <typename T>
char Matriz<T>::pedirTipoOperacion(){
    char operacion;
    std::cout << "Ingrese el tipo de operacion (+: suma, -: resta, *: multiplicacion): ";
    std::cin >> operacion;

    if (operacion != '+' && operacion != '-' && operacion != '*') {
        throw std::invalid_argument("El Tipo de Operacion no es valida");
    }

    return operacion;

}




























