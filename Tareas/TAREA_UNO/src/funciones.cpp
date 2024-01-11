/**
 * @file funciones.cpp
 * @author J. Antonio Franchi 
 * @brief Las funciones del juego
 * Contiene las distintas funciones requeridas para el funcionamiento del juego.
 * 
 * @copyright Copyleft
 * 
 */
#include "funciones.hpp"
#include <string>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;

/**
 * 
 * @brief Funcion para generar el numero aleatorio 
 * Esta funcion toma los datos dentro del struct Juego, y genera el numero aleatorio dentro del intervalo dado.
 * 
 * @param datos 
 * @return int numRandom numero aleatorio dentro del intervalo
 */
int generarNumeroRandom(Juego datos){
    int numRandom;
    srand((unsigned) time(NULL)); // Inicializa seed de la funcion srand
    
    numRandom = datos.numMin + rand() % ((datos.numMax - datos.numMin) + 1); // Calcula el numero aleatorio usando la fn rand dentro del rango
    datos.numAdivinar = numRandom;

    // Codigo para impresion del numero aleatorio en la terminal
    // para motivos de debuggeo
    // std::cout << "Num es: "<< datos.numAdivinar << '\n';

    return numRandom;
}


/** 
 * @brief Funcion para recibir un numero ingresado por el usuario.
 * Solicita al usuario que ingrese un numero por medio de la terminal y lo retorna.
 * Esta funcion se utiliza para obtener los numeros pnesados del usuario durante el juego.
 *
 * @return int El numero ingresado por el usuario.
 */
int getNumeroUsuario(){
    int numeroDigitado;

    std::cout << "Ingrese su numero: ";
    std::cin >> numeroDigitado;

    return numeroDigitado;
}



/**
 * @brief Funcion para calcular el numero de intentos en el juego
 * Esta funcion toma la estructura Juego como parametro y calcula el numero maximo de
 * intentos que tiene el usuario para adivinar el numero correcto. 
 * El numero de intentos se basa en un tercio del rango del intervalo de numeros.
 * 
 * @param datos El struct Juego que contiene los limites del intervalo de numeros.
 * @return int El numero maximo de intentos calculado.
 */
int calcularNumIntentos(Juego datos){
    int numIntentos;

    numIntentos = std::ceil((datos.numMax - datos.numMin) / 3.0);

    return numIntentos;
}


/**
 * @brief Funcion que muestra el menu principal del juego en la terminal.
 *
 * Esta funcion imprime las opciones disponibles en el menu principal del juego.
 * Las opciones incluyen establecer el intervalo de valores, seleccionar el nivel
 * de dificultad, iniciar el juego, o salir del programa.
 */
void mostrarMenu(){
    std::cout << "\n--- Menu Principal ---\n";
    std::cout << "1. Intervalo de valores deseados\n";
    std::cout << "2. Nivel de dificultad\n";
     std::cout << "3. Iniciar juego\n";
    std::cout << "4. Salir del programa\n";
}


/**
 * @brief Funcion que procesa la eleccion del usuario en el menu principal.
 *
 * Esta funcion solicita y lee la opcion del usuario e implementa la logica correspondiente
 * basada en la seleccion realizada. Las opciones incluyen establecer el intervalo de valores,
 * seleccionar el nivel de dificultad, iniciar el juego, o salir del programa.
 *
 * @param datos El struct Juego que contiene el estado actual del juego.
 *              Se actualiza segun las elecciones del usuario.
 */
void procesarOpcion(Juego datos){
    int opcion;
    int dificultad;
    // int min;
    // int max;
    int numRand;
    std::cout << "Ingrese una opcion: ";
    std::cin >> opcion;

    // Casos
    switch(opcion){
        case 1: // Intervalo de valores deseados
            std::cout << "Ingrese el limite inferior del intervalo: \n"; 
            std::cin >> datos.numMin;
            std::cout << "Ingrese el limite superior del intervalo: \n"; 
            std::cin >> datos.numMax;
            std::cout << "Volviendo al Menu Principal..." << endl;
            break;

        case 2: // Nivel de dificultad
            std::cout << "Ingrese modo dificultad: \n";
            std::cout << "1. Modo Estandar\n";
            std::cout << "2. Modo dificil\n";
            std::cin >> datos.modo;
            std::cout << "Volviendo al Menu Principal..." << endl;
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


/**
 * @brief Funcion para ejecutar el juego en el modo estandar.
 *
 * En este modo, el usuario intenta adivinar un numero desconocido generado aleatoriamente.
 * La funcion informa al usuario si su intento es mayor o menor que el numero desconocido.
 * El juego sigue hasta que el usuario adivina correctamente o se agotan los intentos.
 *
 * @param datos El struct Juego que contiene el estado actual del juego, incluyendo
 *              el numero desconocido a adivinar y los limites del intervalo de numeros.
 */
void jugarModoEstandar(Juego datos){
        int intentos = 0; // Contador del numero de intentos
        int maximosIntentos = calcularNumIntentos(datos);
        int numGanador = generarNumeroRandom(datos);

        // ciclo de juego mientras intentos sean menores que los maximos intentos
        while (intentos < maximosIntentos)
        {
            int numDigitado =  getNumeroUsuario();
            intentos++;
            if (numDigitado == numGanador) {
                std::cout << "Correcto!!! Has adivinado el numero correcto." << std::endl;
                return;
            } else if (numDigitado < numGanador) {
                std::cout << "El numero secreto es mayor al ingresado." << std::endl;
            } else {
                std::cout << "El numero secreto es menor al ingresado." << std::endl;
            }
        }
        // Mensaje mostrado cuando se agotan los intentos y se pierde el juego
        std::cout << "Has perdido. El numero era: " << numGanador << std::endl;
        
    }



/**
 * @brief Funcion para ejecutar el juego en el modo dificil.
 *
 * En este modo, el usuario intenta adivinar un numero desconcido generado aleatoriamente.
 * La funcion proporciona pistas basadas en que tan cerca esta el intento del numero desconocido,
 * utilizando terminos como "Hirviendo", "Caliente", "Frio" o "Congelado".
 * El juego continua hasta que el usuario adivina correctamente o se agotan los intentos.
 *
 * @param datos El struct Juego que contiene el estado actual del juego, incluyendo
 *              el numero desconocido a adivinar y los limites del intervalo de numeros.
 */
void jugarModoDificil(Juego datos){
        int intentos = 0;
        int maximosIntentos = calcularNumIntentos(datos);
        int numGanador = generarNumeroRandom(datos);
        
        int largoIntervalo = ((datos.numMax - datos.numMin) + 1);
        /**< Para los niveles de proximidad
         * hirviendo < 10 % del largo del intervalo
         * caliente entre 10 % y 30 %
         * frio entre 30 % y 60 %
         * congelado > 60 %
        */
        //int congelado =  std::ceil((largoIntervalo) * 0.8); 
        int frio =  std::ceil((largoIntervalo) * 0.6); 
        int caliente =  std::ceil((largoIntervalo) * 0.3); 
        int hirviendo =  std::ceil((largoIntervalo) * 0.1); 


       // Ciclo de juego mientras intentos sean menores que los maximos intentos
        while (intentos < maximosIntentos)
        {
            int numDigitado =  getNumeroUsuario();
            intentos++;
            // Declarando una variable de distancia para saber que tan cerca se esta del numero ganador
            int distancia = std::abs(numGanador - numDigitado);
            if (distancia == 0) {
                std::cout << "Correcto!!! Has adivinado el numero correcto." << std::endl;
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
        }
        // Mensaje mostrado cuando se agotan los intentos y se pierde el juego
        std::cout << "Has perdido. El numero era: " << numGanador << std::endl;

    }



/**
 * @brief Funcion para iniciar el juego en el modo de dificultad elegido.
 *
 * Dependiendo del modo de dificultad almacenado en la estructura Juego,
 * esta funcion inicia el juego en el modo estandar o en el modo dificil.
 *
 * @param datos El struct Juego que contiene el estado actual del juego,
 *              incluyendo el modo de dificultad seleccionado.
 */
void iniciarJuego(Juego datos){
    int modoDificultad = datos.modo;
    // Usando el Operador ternario para selecion de modos de juego
    modoDificultad == 1 ? jugarModoEstandar(datos) : jugarModoDificil(datos);
    }





