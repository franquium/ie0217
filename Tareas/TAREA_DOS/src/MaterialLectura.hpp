#ifndef MATERIALLECTURA_HPP
#define MATERIALLECTURA_HPP

#include <iostream>
#include <string>
using namespace std;

class MaterialLectura {
    // Ver cuales cosas van aca
    /*Atributos: Tıtulo, grupo(lectura), tipo de material (libro o noticia), autor, editorial,
    * genero, estado (disponible, prestado, reservado), cantidad de hojas y precio.
    */
    
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
                    

        // Creo que esta parte de la inicilizacion va en el .hpp
        // Constructor de la clase con su lista de inicializacion
        // MaterialLectura( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
        //                  string genero, string estado, int cantidadHojas, double precio)
        //                  : titulo(titulo), grupo(grupo), tipoMaterial(tipoMaterial), autor(autor),
        //                    editorial(editorial), genero(genero), estado(estado), cantidadHojas(cantidadHojas),
        //                    precio(precio) {}

        // Destructor de la clase
        // ~MaterialLectura()
};


#endif