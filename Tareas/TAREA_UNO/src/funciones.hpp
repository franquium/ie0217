#ifndef FUNCIONES_HPP
#define FUNCIONES_HPP
#include <string>
#include <iostream>


struct Juego {
    int numMin; // Cota inferior del intervalo
    int numMax; // Cota superior del intervalo
    int modo;
    int numAdivinar;

};

void mostrarMenu();
void procesarOpcion(Juego datos);
void iniciarJuego(Juego datos);
void jugarModoEstandar(Juego datos);
void jugarModoDificil(Juego datos);
int generarNumeroRandom(Juego datos);
int getNumeroUsuario();
int calcularNumIntentos(Juego datos);

#endif