#include "Pelicula.hpp"
#include <iostream>
#include <string>
using namespace std;


// Constructor de la clase y la lista de  inicializacion
    Pelicula::Pelicula( string titulo, string grupo, string tipoMaterial, string autor,
                     string genero, string estado, int duracion, double precio,
                     string resumenContenido, string materialRelacionado)
                     : MaterialAudiovisual(titulo, "Audiovisual", "Pelicula", autor, genero, estado, duracion, precio),
                       resumenContenido(resumenContenido),
                       materialRelacionado(materialRelacionado)
                       {}

    // Metodos o funciones 

    string Pelicula::calcularLongitud() const {
        
        if (duracion < 90) {
            return "Corta";
        } else if (duracion < 150) {
            return "Mediana";
        } else {
            return "Larga";
        }
    }

    void Pelicula::imprimirInfo() const {
        cout << "  -------------------------------------  " << endl;
        cout << "Titulo: " << titulo << endl;
        cout << "Grupo: " << grupo << endl;
        cout << "Tipo de Material: " << tipoMaterial << endl;
        cout << "Autor: " << autor << endl;
        cout << "Genero: " << genero << endl;
        cout << "Estado: " << estado << endl;
        cout << "Duracion: " << duracion << endl;
        cout << "Precio: " << precio << endl;
        cout << "Resumen: " << resumenContenido << endl;
        cout << "Material Relacionado: " << materialRelacionado << endl;
        cout << "  -------------------------------------  " << endl;
        cout << "\n";
    }
    

