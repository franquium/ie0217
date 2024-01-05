// Programa para computar valor absoluto
// Funciona para ambos int y float

#include <iostream>
using namespace std;

// func con  parametro tipo float
float absolute(float var) {
    if (var < 0.0) {
        var = -var;
    }
    return var;
}

// func con  parametro tipo int 
int absolute(int var) {
    if (var < 0) {
        var = -var;
    }
    return var;
}

int main() {
    // Llamado func con  parametro tipo int 
    cout << "Absolute value of -5 = " << absolute(-5) << endl;

    // Llamado func con  parametro tipo float
    cout << "Absolute value of 5.5 = " << absolute(5.5f) << endl;
    return 0;
}
