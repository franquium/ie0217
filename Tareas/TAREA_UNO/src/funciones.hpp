/**
 * @file funciones.hpp
 * @author J. Antonio Franchi 
 * @brief Archivo de headers de funciones
 * Contiene los headers de las funciones del juego,
 * asi como la definicion del Struct Juego para los datos requeridos en el juego.
 * 

 * @copyright Copyleft
 * 
 */
#ifndef FUNCIONES_HPP
#define FUNCIONES_HPP
#include <string>
#include <iostream>

/**
 * @struct Juego
 * @brief Almacena los datos del estado del juego de adivinar.
 *
 * Esta estructura almacena los detalles del juego, como el rango de números para adivinar,
 * el modo de juego seleccionado y el número que el jugador debe adivinar.
 */
struct Juego {
    int numMin; // Cota inferior del intervalo
    int numMax; // Cota superior del intervalo
    int modo;   // Modo de juego
    int numAdivinar; // Numero aleatorio a adivinar

};

// Colocando los headers de las funciones del programa
void mostrarMenu();
void procesarOpcion(Juego datos);
void iniciarJuego(Juego datos);
void jugarModoEstandar(Juego datos);
void jugarModoDificil(Juego datos);
int generarNumeroRandom(Juego datos);
int getNumeroUsuario();
int calcularNumIntentos(Juego datos);

#endif