#include <iostream>
#include "persona.hpp"

using namespace std;

int main(){
    Persona p("Joan", 25);

    cout << "Nombre: " << p.getNombre() << endl;
    cout << "Edad: " << p.getEdad() << endl;

    p.setEdad(26);

    cout << "Nueva edad: " << p.getEdad() << endl;

    return 0;
}