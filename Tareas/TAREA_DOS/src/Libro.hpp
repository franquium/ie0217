#ifndef LIBRO_HPP
#define LIBRO_HPP

#include <iostream>
#include <string>
#include "MaterialLectura.hpp"
using namespace std;

class Libro: public MaterialLectura {
    
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
        std::string calcularLongitud() const ; // sobre lo const
        void imprimirInfo() const ;

        // Destructor de ;a clase
        //~Libro()
      
};

#endif