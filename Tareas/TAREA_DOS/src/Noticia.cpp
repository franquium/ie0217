#include "Noticia.hpp"
#include <iostream>
#include <string>
using namespace std;

// Constructor de la clase y lista de inicializacion
/**
 * @brief Construct a new Noticia:: Noticia object
 * 
 * @param titulo 
 * @param grupo 
 * @param tipoMaterial 
 * @param autor 
 * @param editorial 
 * @param genero 
 * @param estado 
 * @param cantidadHojas 
 * @param precio 
 * @param resumenContenido 
 * @param materialRelacionado 
 */
    Noticia::Noticia( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
                     string genero, string estado, int cantidadHojas, double precio,
                     string resumenContenido, string materialRelacionado)
                     : MaterialLectura(titulo, "Lectura", "Noticia", autor, editorial, genero, estado, cantidadHojas,precio),
                       resumenContenido(resumenContenido),
                       materialRelacionado(materialRelacionado)
                       {}

    // Metodos o funciones 
    string Noticia::calcularLongitud() const {
       
        if (cantidadHojas < 5) {
            return "Corta";
        } else if (cantidadHojas < 10) {
            return "Mediana";
        } else {
            return "Larga";
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
    

