#include <iostream>
using namespace std;

class Molde {
    public: // Especificador de acceso
        double largo;
        double ancho;
        double altura;

        // Constructor de la clase
        Molde() {
            cout << "Esto se ejecuta en cada instanciacion" << endl;
            cout << "Iniciando un objeto de la clase Room" << endl;
        }

        // Metodos
        double calcularArea(){
            return largo * ancho;
        }

        double calcularVolumen(){
            return largo * ancho * altura;
        }
};

int main(){

    // Instanciando un Objeto llamado Pared basado en la clase Molde.
    Molde pared;

    // Asignando valores al Objeto pared
    pared.largo = 400.5;
    pared.ancho = 20.8;
    pared.altura = 315.2;

    // Calcular y desplegar el area y volumen
     cout << "Area =  " <<  pared.calcularArea() << endl;
     cout << "Volumen =  " <<  pared.calcularVolumen() << endl;

    return 0;
}