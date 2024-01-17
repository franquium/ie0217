#ifndef MATERIALLECTURA_HPP
#define MATERIALLECTURA_HPP

#include <iostream>
#include <string>
using namespace std;

class MaterialLectura {
    
    protected:
        // atributos
        string titulo;
        string grupo;
        string tipoMaterial;
        string autor;
        string editorial;
        string genero;
        string estado;
        int cantidadHojas;
        double precio;

    public:
        // Constructor de la clase 
        MaterialLectura( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
                         string genero, string estado, int cantidadHojas, double precio) ;

        // Destructor de la clase
        // ~MaterialLectura()
};

#endif