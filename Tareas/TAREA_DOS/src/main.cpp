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
#include "Noticia.hpp"
#include "Pelicula.hpp"
#include "Podcast.hpp"
#include <iostream>

/**
 * @brief 
 * 
 * @return int 
 */
int main(){

    /**
     * @note Los datos suministrados en los siguientes ejemplos
     * contienen informacion de manera ilustrativa, mas no deben tomarse
     * como informacion veraz sobre libros, noticias y otros. 
     */


    /* Creando una instancia de la Clase Libro */
    Libro miLibro(
        "El Principito", 
        "--Lectura--", 
        "--Libro--", 
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
    std::string longitudLibro = miLibro.calcularLongitud();
    std::cout << "Longitud del libro: " << longitudLibro  << std::endl;
    std::cout << "\n"; // Para imprimir salto linea, por razones esteticas nada mas


    /* Creando una instancia de la clase Noticia */
    Noticia miNoticia(
        "Violacion de la Covarianza en las Leyes de la Fisica", 
        "--Lectura--", 
        "--Noticia--", 
        "Isaac Newton",
        "Editorial Patotito",
        "Ciencia",
        "Reservado",
        15,
        15000.0,
        "Un nuevo fenomeno es descubierto que viola la Covarianza...",
        "Noticias sobre ciencia y matematica"
    );
    
    // Imprimir info de la noticias
    miNoticia.imprimirInfo();

    // Calcular y mostrar la longitud de la noticia
    std::string longitudNoticia = miNoticia.calcularLongitud();
    std::cout << "Longitud de la noticia es: " << longitudNoticia  << std::endl;
    std::cout << "\n"; // Para imprimir salto linea, por razones esteticas nada mas


    /* Creando una instancia de la Clase Pelicula */   
    Pelicula miPeli(
        "Trainspotting", 
        "--Audiovisual--", 
        "--Peli--", 
        "Danny Boyle",
        "Comedia-Drama",
        "Prestado",
        93,
        2000.0,
        "La historia de Renton y sus colegas en el mundo de la heroina la Edimburgo de los 80s...Choose Life!  ",
        "Peliculas 'edgy' y de humor oscuro"
    );
    
    // Imprimir info de la pelicula
    miPeli.imprimirInfo();

    // Calcular y mostrar la longitud de la pelicula
    std::string longitudPeli = miPeli.calcularLongitud();
    std::cout << "Longitud de la pelicula: " << longitudPeli  << std::endl;
    std::cout << "\n"; // Para imprimir salto linea, por razones esteticas nada mas


    /* Creando una instancia de la Clase Podcast */   
    Podcast miPodcast(
        "JRE", 
        "--Audiovisual--", 
        "--Podcast--", 
        "Joe Rogan",
        "Comedia",
        "Disponible",
        120,
        0.0,
        "Entrevistas y conversaciones (Talk Show) sobre una basta variedad de temas",
        "Lex Fridman Podcast and so on"
    );
    
    // Imprimir info del Podcast
    miPodcast.imprimirInfo();

    // Calcular y mostrar la longitud del Podcast
    std::string longitudPodcast = miPodcast.calcularLongitud();
    std::cout << "Longitud del Podcast: " << longitudPodcast  << std::endl;
    std::cout << "\n"; // Para imprimir salto linea, por razones esteticas nada mas




    return 0;
}