#ifndef MATERIALORDENADO_HPP
#define MATERIALORDENADO_HPP

#include "MaterialLectura.hpp"
#include "MaterialAudiovisual.hpp"
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class MaterialOrdenado {
    
    protected:
        std::vector<MaterialLectura*> materialesLec; // Vector de punteros a MaterialLectura
        std::vector<MaterialAudiovisual*> materialesAud; // Vector de punteros a MaterialAudiovisual

    public:
        // Constructor de la clase 
        MaterialOrdenado();
        // Desstructor de la clase
        ~MaterialOrdenado();

        // Funciones
        void agregarMaterial();
        void eliminarMaterial();
        void buscarMaterial(); // Revisar tipo de fn
};

#endif