#ifndef LIBRO_HPP
#define LIBRO_HPP

#include <iostream>
#include <string>
#include "MaterialLectura.hpp"
using namespace std;

class Libro: public MaterialLectura {
    // Ver cuales cosas van aca
    /* Hereda de: MaterialLectura.
    * -> Informacion adicional: resumen de contenido, material relacionado que podrıa gustar.
    * -> Funciones:
    * 1. Metodo que indique si el libro es corto, mediano o largo dependiendo de la cantidad
    * de hojas (0 a 100 hojas es corto , 100 a 200 hojas es mediano y 200 o mas hojas es
    * largo).
    * 2. Metodo que imprima toda la informacion del libro..
    */
    
    protected:
        // atributos
        std::string resumenContenido;
        std::string materialRelacionado;

    public: 

        // Constructor de la clase con su lista de inicializacion
        Libro ( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
                string genero, string estado, int cantidadHojas, double precio,
                string resumenContenido, string materialRelacionado);

        // Metodos o funciones                 
        std::string calcularLongitud() ;
        void imprimirInfo() ;

        // Destructor de ;a clase
        //~Libro()
      
};

#endif