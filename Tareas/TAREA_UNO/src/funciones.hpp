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
void procesarOpcion();
void iniciarJuego();
void generarNumeroRandom();
void jugarModoEstandar();
void jugarModoDificil();
int getNumeroUsuario();

#endif