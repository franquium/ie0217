#include "Libro.hpp"
#include <string>
using namespace std;
//#include <iostream>
//using namespace std;

// Constructor de la clase y la lista de  inicializacion
    Libro::Libro( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
                     string genero, string estado, int cantidadHojas, double precio,
                     string resumenContenido, string materialRelacionado)
                     : MaterialLectura(titulo, "Lectura", "Libro", autor, editorial, genero, estado, cantidadHojas,precio),
                       resumenContenido(resumenContenido),
                       materialRelacionado(materialRelacionado)
                       {}

    string Libro::calcularLongitud()  {
        //Falta codigo
    }

    void Libro::imprimirInfo() {
        cout << "Titulo: " << titulo << endl;
        cout << "Autor: " << autor << endl;
        cout << "Editorial: " << editorial << endl;
        cout<< "Genero: " << genero << endl;
        cout << "Estado: " << estado << endl;
        cout << "Cantidad de Hojas: " << cantidadHojas << endl;
        cout << "Precio: " << precio << endl;
        cout << "Resumen: " << resumenContenido << endl;
        cout << "Material Relacionado: " << materialRelacionado << endl;
    }
    

