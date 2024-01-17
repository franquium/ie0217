#include "Podcast.hpp"
#include <iostream>
#include <string>
using namespace std;


// Constructor de la clase y la lista de  inicializacion
    Podcast::Podcast( string titulo, string grupo, string tipoMaterial, string autor,
                     string genero, string estado, int duracion, double precio,
                     string resumenContenido, string materialRelacionado)
                     : MaterialAudiovisual(titulo, "Audiovisual", "Podcast", autor, genero, estado, duracion, precio),
                       resumenContenido(resumenContenido),
                       materialRelacionado(materialRelacionado)
                       {}

    // Metodos o funciones 

    string Podcast::calcularLongitud() const {
        
        if (duracion < 30) {
            return "Corto";
        } else if (duracion < 90) {
            return "Mediano";
        } else {
            return "Largo";
        }
    }

    void Podcast::imprimirInfo() const {
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
    

