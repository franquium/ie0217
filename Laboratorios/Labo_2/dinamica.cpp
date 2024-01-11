#include <iostream>
using namespace std;

/* .data section.*/
int variableGlobal = 10;
// si fuera const int var ieria a la seccion .text : Cosas que es peligroso cambiar

/* .text section* las funciones siempre van a la seccion .text */
void funcionGlobal(){

    /* data section estatica solo se hace una vez o ejecuta una vez aunque se llame a la func varia veces*/
    static int variableLocalEstatica = 5;        

    /* stack section*/
    int variableLocal = 20;

    cout << "Variable  global: " << variableGlobal << endl;
    cout << "Variable local estatica: " << variableLocalEstatica << endl;
    cout << "Variable local: " << variableLocal << endl;

    /* Remember Remember
    * Stack almacena variables locales
    *
    *
    * */

}



int main(){

    /* stack section*/
    int variableLocalMain = 15;

    funcionGlobal();

    cout << "Variable local en main: " << variableLocalMain << endl;

    /* heap section: la seccion del monton*/
    int* variableDinamica = new int;
    *variableDinamica = 25;

    cout << "Variable dinamica: " << variableDinamica << endl ;

    delete variableDinamica;


    return 0;
}
