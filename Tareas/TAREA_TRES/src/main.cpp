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

        //Matriz tipo float
        std::cout << ".....Creando una matriz de tipo float ...." << std::endl;

        // Crear instancias de matrices de dimensiones iniciales, se cambiaran despues
        Matriz<float> miMatriz2(1, 1); // Tipo Float
        
       
        
        // Solicitar al usuario que ingrese los datos de la matriz
        miMatriz2.getTamannoYDatos();

        // Solicitar al usuario que elija una operación matematica
        char operacion2 = miMatriz2.pedirTipoOperacion();
        std::cout << "Operacion elegida: " << operacion << std::endl;
    

        // // Imprimir matriz
        // // void imprimirMatriz() {
        //         for (int i = 0; i < miMatriz.filas; i++) {
        //             for (int j = 0; j < miMatriz.columnas; j++) {
        //                 cout << miMatriz.data[i][j] << " ";
        //             }
        //             cout << endl;
        //         }
        // // }


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

