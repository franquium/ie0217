#ifndef NOTICIA_HPP
#define NOTICIA_HPP

#include <iostream>
#include <string>
#include "MaterialLectura.hpp"
using namespace std;

class Noticia: public MaterialLectura {
    // Ver cuales cosas van aca
    /* Hereda de MaterialLectura.
    * -> Informacion adicional: resumen de contenido, material relacionado que podrıa gustar.
    * -> Funciones:
    * 1. Metodo que indique si la noticia es corto, mediano o largo dependiendo de la cantidad
    * de hojas (0 a 5 hojas es corta , 5 a 10 hojas es mediana y 10 o mas hojas es larga).
    * 2. Metodo que imprima toda la informacion del libro..
    */
    
    protected:
        // atributos
        std::string resumenContenido;
        std::string materialRelacionado;

    public:
        

        // Constructor de la clase con su lista de inicializacion
        Noticia ( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
                         string genero, string estado, int cantidadHojas, double precio,
                         string resumenContenido, string materialRelacionado);

        // Metodos o funciones                 
        std::string calcularLongitud() const;
        void imprimirInfo() const;

        

        // Destructor de ;a clase
        //~Libro()

        
};


#endif