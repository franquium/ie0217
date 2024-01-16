#include "MaterialLectura.hpp"

#include <iostream>
using namespace std;




// Constructor de la clase inicializacion
    MaterialLectura::MaterialLectura( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
                     string genero, string estado, int cantidadHojas, double precio)
                         {
                            this->titulo = titulo;
                            this->grupo = grupo;
                            this->tipoMaterial = tipoMaterial;
                            this->autor = autor;
                            this->editorial =editorial;
                            this->genero = genero;
                            this->estado = estado;
                            this->cantidadHojas = cantidadHojas;
                            this->precio = precio;
                         }
                          

// Forma Alternativa: Constructor de la clase con su lista de inicializacion
        // MaterialLectura( string titulo, string grupo, string tipoMaterial, string autor,string editorial,
        //                  string genero, string estado, int cantidadHojas, double precio)
        //                  : titulo(titulo), grupo(grupo), tipoMaterial(tipoMaterial), autor(autor),
        //                    editorial(editorial), genero(genero), estado(estado), cantidadHojas(cantidadHojas),
        //                    precio(precio) {}




// void Vehiculo::acelerar(){
//     cout << "Acelerando el vehiculo hasta " << velocidad << "km/h" << endl;
// }

// void Vehiculo::frenar(){
//     cout << "Frenando el vehiculo " << endl;
// }
