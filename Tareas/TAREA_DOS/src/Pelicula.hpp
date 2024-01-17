#ifndef PELICULA_HPP
#define PELICULA_HPP

#include <iostream>
#include <string>
#include "MaterialAudiovisual.hpp"
using namespace std;

class Pelicula: public MaterialAudiovisual {
    
    protected:
        // atributos
        string resumenContenido;
        string materialRelacionado;

    public: 

        // Constructor de la clase con su lista de inicializacion
        Pelicula ( string titulo, string grupo, string tipoMaterial, string autor,
                string genero, string estado, int duracion, double precio,
                string resumenContenido, string materialRelacionado);

        // Metodos o funciones                 
        string calcularLongitud() const ; 
        void imprimirInfo() const ;

        // Destructor de la clase
        //~Pelicula();
      
};

#endif