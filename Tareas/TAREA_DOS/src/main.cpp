/**
 * @file main.cpp
 * @author J. Antonio Franchi 
 * @brief Funcion principal de 
 * 
 * 
 * @return int Retorna 0 si el programa finaliza correctamente.
 *
 * @copyright Copyleft
 * 
 */

#include "Libro.hpp"
#include <iostream>


int main(){

    /* Creando una instancia de la Clase Libro*/
    Libro miLibro(
        "El Principito", 
        "Lectura", 
        "Libro", 
        "Antoine de Saint-Exupery",
        "Editorial C'est la Vie",
        "Ficcion",
        "Disponible",
        97,
        5000.0,
        "Un piloto encuentra un amigo en el lugar menos esperado",
        "Libros de filosofia sobre la vida"
    );
    
    // Imprimir info del libro
    miLibro.imprimirInfo();

    // Calcular y mostrar la longitud del libro
    std::string longitud = miLibro.calcularLongitud();
    std::cout << "Longitud del libro: " << longitud << std::endl;


    return 0;
}