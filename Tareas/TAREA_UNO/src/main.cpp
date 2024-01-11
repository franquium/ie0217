/**
 * @file main.cpp
 * @author J. Antonio Franchi 
 * @brief Funcion principal del juego
 * Configura el programa del juego adivinar un numero en un rango definido, 
 * inicializando los valores predeterminados y ejecuta el loop principal del juego. 
 * Dentro del loop, muestra el menu y procesa las opciones seleccionadas por el usuario.
 * 
 * @return int Retorna 0 si el programa finaliza correctamente.
 *
 * @copyright Copyleft
 * 
 */

#include <iostream>
#include "funciones.hpp"

int main(){

    Juego datos; // Instancia del struct Juego para mantener el estado del juego
    bool enJuego = true; // Para controlar el loop principal

    /**< Configuración inicial del juego
    * a pesar de que se indico asumir que el usuario va a hacer buen uso
    * se pone como respaldo */
    datos.numMin = 1; // Valor minimo del intervalo por defecto
    datos.numMax = 20; // Valor maximo del intervalo por defecto
    datos.modo = 1; // Modo de juego por defecto, Modo Estandar

    while (enJuego) {
        
        mostrarMenu(); // Muestra el menu de opciones
        procesarOpcion(datos); // Procesa la opcion del usuario
        
    }


    return 0;
}