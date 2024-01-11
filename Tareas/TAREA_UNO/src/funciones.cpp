#include "funciones.hpp"
#include <string>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;


/*  Funcion para mostrar el Menu */
void mostrarMenu(){
    std::cout << "\n--- Menu ---\n";
    std::cout << "1. Intervalo de valores deseados\n";
    std::cout << "2. Nivel de dificultad\n";
     std::cout << "3. Iniciar juego\n";
    std::cout << "4. Salir del programa\n";
}


/*  Funcion generar el numero aleatorio dentro del intervalo */
void generarNumeroRandom(Juego datos){
    int numRandom;
    std::srand(std::time(NULL)); // Inicializa seed de la funcion srand
    
    numRandom = datos.numMin + std::rand() % ((datos.numMax - datos.numMax) + 1);
    datos.numAdivinar = numRandom;

    return numRandom;
}


/*  Funcion para recibir el numero  ingresado por usuario*/
int getNumeroUsuario(){
    int numeroDigitado;

    std::cout << "Ingrese su numero: ";
    std::cin >> numeroDigitado;

    return numeroDigitado;
};


/*  Funcion para calcular el numero de intentos */
int calcularNumIntentos(Juego datos){
    int numIntentos;

    numIntentos = ceil((datos.numMax - datos.numMin) / 3.0)

    return numIntentos;
};


/*  Funcion para procesar las opciones ingresadas */
void procesarOpcion(Juego datos){
    int opcion;
    int dificultad;
    int min;
    int max;
    int numRand;
    std::cout << "Ingrese una opcion: ";
    std::cin >> opcion;

    // Casos
    switch(opcion){
        case 1: // Intervalo de valores deseados
            // code 
            break;
        case 2: // Nivel de dificultad
            std::cout << "Ingrese modo dificultad: \n";
            std::cout << "1. Modo Estandar\n";
            std::cout << "2. Modo dificil\n";
            std::cin >> dificultad;
            datos.modo = dificultad;
            break;
        case 3: // Iniciar juego
            iniciarJuego();
            break;
        case 4: // Salir del programa
            std::cout << "Saliendo del programa...\n";
            exit(0);
        default:
            std::cout << "Opcion no es valida. Intente de nuevo...\n";
    }
}


/*  Funcion para el modo de juego estadar */
    void jugarModoEstandar(Juego datos){
        int intentos = 0; // Contador del numero de intentos
        int maximosIntentos = calcularNumIntentos(datos);
        int numGanador = generarNumeroRandom(datos);

        // ciclo de juego mientras intentos < maximosIntentos
        while (intentos < maximosIntentos)
        {
            int numDigitado =  getNumeroUsuario();
        intentos++;
        if (numDigitado == numGanador) {
            std::cout << "¡Correcto! Has adivinado el número correcto." << std::endl;
            return;
        } else if (numDigitado < numGanador) {
            std::cout << "El número secreto es mayor al ingresado." << std::endl;
        } else {
            std::cout << "El número secreto es menor al ingresado." << std::endl;
        }
        }


        std::cout << "Has perdido. El número era: " << datos.numAdivinar << std::endl;
        
        
    }

/*  Funcion para el modo de juego dificil */
    void jugarModoDificil(){
        int intentos;
         int maximosIntentos = calcularNumIntentos(datos);
        int numGanador = generarNumeroRandom(datos);
        
        int distancia;
        /**
         * Congelado > 0.80 del Intervalo
         * Frio > 0.50 del Intervalo
         *  Caliente = 0.20 del Intervalo
         *  Hirviendo = 0.10 del intervalor
         * 
        */

    }





