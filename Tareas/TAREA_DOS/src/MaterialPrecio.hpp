#ifndef MATERIALPRECIO_HPP
#define MATERIALPRECIO_HPP

#include "MaterialLectura.hpp"
#include "MaterialAudiovisual.hpp"
#include "Libro.hpp"
#include "Noticia.hpp"
#include "Pelicula.hpp"
#include "Podcast.hpp"
#include <iostream>
#include <string>
#include <vector>
using namespace std;



class MaterialPrecio: public Libro, public Noticia, public Pelicula, public Podcast {
    
    protected:
        

    public:
         // Constructor de la clase 
        MaterialPrecio();
        // Desstructor de la clase
        ~MaterialPrecio();

        // Funciones
        void ordenarAscendeteMaterial();
        void ordenarDescendeteMaterial();
        void imprimirMaterial();


};

#endif