#include <iostream>
using namespace std;

/*@note: se hace un solo archivo para la seccion de Variables y su scope */

// Variable Global:
int g;


int main () {

// Variable Local:
int a, b;
int c;

// Inicializacion
a = 10;
b = 20;

c = a + b;
g = a + b;

cout << c;
cout << g;

return 0;
}