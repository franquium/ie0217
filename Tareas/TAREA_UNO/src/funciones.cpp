#include "funciones.hpp"
#include <string>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;



/*  Funcion generar el numero aleatorio dentro del intervalo */
int generarNumeroRandom(Juego datos){
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
}


/*  Funcion para calcular el numero de intentos */
int calcularNumIntentos(Juego datos){
    int numIntentos;

    numIntentos = std::ceil((datos.numMax - datos.numMin) / 3.0);

    return numIntentos;
}

/*  Funcion para mostrar el Menu */
void mostrarMenu(){
    std::cout << "\n--- Menu ---\n";
    std::cout << "1. Intervalo de valores deseados\n";
    std::cout << "2. Nivel de dificultad\n";
     std::cout << "3. Iniciar juego\n";
    std::cout << "4. Salir del programa\n";
}


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
            std::cin >> datos.modo;
            //datos.modo = dificultad;
            break;
        case 3: // Iniciar juego
            iniciarJuego(datos);
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
void jugarModoDificil(Juego datos){
        int intentos;
        int maximosIntentos = calcularNumIntentos(datos);
        int numGanador = generarNumeroRandom(datos);
        
        int largoIntervalo = ((datos.numMax - datos.numMin) + 1);
        // Para los niveles de proximidad
        //int congelado =  std::ceil((largoIntervalo) * 0.8); // 80 % del largo del intervalo
        int frio =  std::ceil((largoIntervalo) * 0.6); // 60 % del largo del intervalo
        int caliente =  std::ceil((largoIntervalo) * 0.3); // 30 % del largo del intervalo
        int hirviendo =  std::ceil((largoIntervalo) * 0.1); // 10 % del largo del intervalo

        /**
         * Congelado > 0.80 del Intervalo
         * Frio > 0.50 del Intervalo
         *  Caliente = 0.30 del Intervalo
         *  Hirviendo = 0.10 del intervalor
         * 
        */

       // ciclo de juego mientras intentos < maximosIntentos
        while (intentos < maximosIntentos)
        {
            int numDigitado =  getNumeroUsuario();
            intentos++;
            // Declarando una variable de distancia para saber que tan cerca se esta del numero ganador
            int distancia = std::abs(numGanador - numDigitado);
            if (distancia == 0) {
                std::cout << "¡Correcto! Has adivinado el número correcto." << std::endl;
                return;
            } 
            else if (distancia <= hirviendo) {
                std::cout << "Hirviendo!!!" << std::endl;
            }
            else if (distancia > hirviendo && distancia <= caliente) {
                std::cout << "Caliente!!!" << std::endl; 
            } 
            else if (distancia > caliente && distancia <= frio) {
                std::cout << "Frio!!!" << std::endl; 
            } 
            else if (distancia > frio) {
                std::cout << "Congelado!!!." << std::endl;
            } 
            //else {
            //    std::cout << "El número secreto es menor al ingresado." << std::endl;
            //}

        }
        std::cout << "Has perdido. El número era: " << numGanador << std::endl;

    }


/*  Funcion para iniciar el juego*/
void iniciarJuego(Juego datos){
    int modoDificultad = datos.modo;
    
    modoDificultad == 1 ? jugarModoEstandar(datos) : jugarModoDificil(datos);

    }





