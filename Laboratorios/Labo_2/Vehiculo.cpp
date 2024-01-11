#include "Vehiculo.hpp"

#include <iostream>
using namespace std;

// Dos formas de hacerlo:
// Tomamos el segundo
// Vehiculo::Vehiculo(int velocidad) : velocidad(velocidad){} // Este ultimo despues del dos puntos: velocidad() es algo

Vehiculo::Vehiculo(int velocidad){
    this->velocidad = velocidad;
}

void Vehiculo::acelerar(){
    cout << "Acelerando el vehiculo hasta " << velocidad << "km/h" << endl;
}

void Vehiculo::frenar(){
    cout << "Frenando el vehiculo " << endl;
}