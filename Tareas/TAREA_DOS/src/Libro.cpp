#include "Libro.hpp"
#include <iostream>
#include <string>
using namespace std;


// Constructor de la clase y la lista de  inicializacion
    Libro::Libro( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
                     string genero, string estado, int cantidadHojas, double precio,
                     string resumenContenido, string materialRelacionado)
                     : MaterialLectura(titulo, "Lectura", "Libro", autor, editorial, genero, estado, cantidadHojas,precio),
                       resumenContenido(resumenContenido),
                       materialRelacionado(materialRelacionado)
                       {}

    // Metodos o funciones 

    string Libro::calcularLongitud() const {
        
        if (cantidadHojas < 100) {
            return "Corto";
        } else if (cantidadHojas < 200) {
            return "Mediano";
        } else {
            return "Largo";
        }
    }

    void Libro::imprimirInfo() const {
        cout << "  -------------------------------------  " << endl;
        cout << "Titulo: " << titulo << endl;
        cout << "Grupo: " << grupo << endl;
        cout << "Tipo de Material: " << tipoMaterial << endl;
        cout << "Autor: " << autor << endl;
        cout << "Editorial: " << editorial << endl;
        cout<< "Genero: " << genero << endl;
        cout << "Estado: " << estado << endl;
        cout << "Cantidad de Hojas: " << cantidadHojas << endl;
        cout << "Precio: " << precio << endl;
        cout << "Resumen: " << resumenContenido << endl;
        cout << "Material Relacionado: " << materialRelacionado << endl;
        cout << "  -------------------------------------  " << endl;
        cout << "\n";
    }
    

