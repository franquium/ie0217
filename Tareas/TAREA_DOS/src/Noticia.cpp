#include "Noticia.hpp"
#include <iostream>
#include <string>
using namespace std;


// Constructor de la clase y lista de inicializacion
    Noticia::Noticia( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
                     string genero, string estado, int cantidadHojas, double precio,
                     string resumenContenido, string materialRelacionado)
                     : MaterialLectura(titulo, "Lectura", "Noticia", autor, editorial, genero, estado, cantidadHojas,precio),
                       resumenContenido(resumenContenido),
                       materialRelacionado(materialRelacionado)
                       {}

    /* Forma alternativa sin usar lista de inicializacion con 
    * this-> atributo = atributo NO FUNKA y no se el proque :/
    */
    // Noticia::Noticia(string titulo, string grupo, string tipoMaterial, string autor, string editorial,
    //          string genero, string estado, int cantidadHojas, double precio,
    //          string resumenContenido, string materialRelacionado) 
    //          {
    //             // Asignacion a los atributos heredados de MaterialLectura
    //             this->titulo = titulo;
    //             this->grupo = grupo;
    //             this->tipoMaterial = tipoMaterial;
    //             this->autor = autor;
    //             this->editorial = editorial;
    //             this->genero = genero;
    //             this->estado = estado;
    //             this->cantidadHojas = cantidadHojas;
    //             this->precio = precio;

    //             // Asignacion directa a los atributos específicos de Libro
    //             this->resumenContenido = resumenContenido;
    //             this->materialRelacionado = materialRelacionado;
    //         }
    

    // Metodos o funciones 
    string Noticia::calcularLongitud() const {
        //Falta revisar este codigo para calcular la longitud
        if (cantidadHojas < 5) {
            return "Corto";
        } else if (cantidadHojas < 10) {
            return "Mediano";
        } else {
            return "Largo";
        }
    }

    void Noticia::imprimirInfo() const {
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
    

