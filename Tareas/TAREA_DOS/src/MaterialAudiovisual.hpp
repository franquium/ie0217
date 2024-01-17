#ifndef MATERIALAUDIOVISUAL_HPP
#define MATERIALAUDIOVISUAL_HPP

#include <iostream>
#include <string>
using namespace std;

class MaterialAudiovisual {
    
    protected:
        // atributos
        string titulo;
        string grupo;
        string tipoMaterial;
        string autor;
        string genero;
        string estado;
        int duracion;
        double precio;

    public:
        // Constructor de la clase 
        MaterialAudiovisual( string titulo, string grupo, string tipoMaterial, string autor,
                         string genero, string estado, int duracion, double precio) ;

        // Destructor de la clase
        // ~MaterialAudiovisual()
};

#endif