/**
 * @file main.cpp
 * @author J. Antonio Franchi 
 * @brief Funcion principal del programa.
 * 
 * @return int Retorna 0 si el programa finaliza correctamente.
 *
 * @copyright Copyleft
 */

#include "Matriz.hpp"
#include "Matriz.cpp"
#include "OperacionesBasicas.hpp"
#include "OperacionesBasicas.cpp"
#include "ImpresionMatriz.hpp"
#include "ImpresionMatriz.cpp"
#include <iostream>
#include <string>
#include <vector>
#include <complex>
#include <type_traits>
#include <stdexcept>
#include <limits>
using namespace std;


int main() {
   
    try {

        // Solicitar al usuario el tipo de datos de la matriz
        // Por simplicidad, aqui usamos int, pero podrías modificarlo para otros tipos
        std::cout << ".....Creando una matriz de tipo int ...." << std::endl;

        // Crear instancias de matrices de dimensiones iniciales, se cambiaran despues
        Matriz<int> miMatriz(1, 1); // Tipo Int
        // Matriz<float> miMatriz(1, 1); // Tipo Float
        // Matriz<complex<float>> miMatriz3(1, 1, std::complex<float> (0.0f, 0.0f)); //Tipo complex

        // Solicitar al usuario que ingrese los datos de la matriz
        miMatriz.getTamannoYDatos();

        // Solicitar al usuario que elija una operación matematica
        char operacion = miMatriz.pedirTipoOperacion();
        std::cout << "Operacion elegida: " << operacion << std::endl;

        // Instanciando segundo matriz de tipo int
        std::cout << ".....Creando una segunda matriz de tipo int ...." << std::endl;

        // Crear instancias de matrices de dimensiones iniciales, se cambiaran despues
        Matriz<int> miMatriz2(1, 1); // Tipo Int
        // Matriz<float> miMatriz(1, 1); // Tipo Float
        // Matriz<complex<float>> miMatriz3(1, 1, std::complex<float> (0.0f, 0.0f)); //Tipo complex

        // Solicitar al usuario que ingrese los datos de la matriz
        miMatriz2.getTamannoYDatos();

        // Solicitar al usuario que elija una operación matematica
        char operacion2 = miMatriz2.pedirTipoOperacion();
        std::cout << "Operacion elegida: " << operacion2 << std::endl;

        // Asignar las matrices creadas para la Operacion Basicas
        int filasA, columnasA;
        filasA = miMatriz.filas;
        columnasA = miMatriz.columnas;
        int filasB, columnasB;
        filasB= miMatriz2.filas;
        columnasB = miMatriz2.columnas;
        OperacionesBasicas<int> matrizA(filasA, columnasA);
        OperacionesBasicas<int> matrizB(filasB, columnasB);


        //Realizar y mostrar la suma de las matrices

        //OperacionesBasicas<int> sumaMatrices = matrizA + matrizB;



        // // Matriz tipo float
        // std::cout << ".....Creando una matriz de tipo float ...." << std::endl;

        // // Crear instancias de matrices de dimensiones iniciales, se cambiaran despues
        // Matriz<float> miMatriz3(1, 1); // Tipo Float
        
       
        
        // // Solicitar al usuario que ingrese los datos de la matriz
        // miMatriz2.getTamannoYDatos();

        // // Solicitar al usuario que elija una operación matematica
        // char operacion3 = miMatriz3.pedirTipoOperacion();
        // std::cout << "Operacion elegida: " << operacion3 << std::endl;
    



    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    } catch (const std::out_of_range& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    } catch (...) {
        std::cerr << "Error desconocido." << std::endl;
        return 1;
    }

    return 0;
}

