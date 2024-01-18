#include <iostream>
using namespace std;

int main() {
    double numerator, denominator, divide;

    cout << "Ingrese numerador: ";
    cin >> numerator;

    cout << "Ingrese denominador: ";
    cin >> denominator;

    try {
        // lanza una excepcion si denominador es 0
        if (denominator == 0)
            throw 0;

        // no se ejecuta si denominador es 0
        divide = numerator / denominator;
        cout << numerator << " / " << denominator << " = " << divide << endl;
    }
    catch (int num_exception) {
        cout << "Error: No se puede dividir por " << num_exception << endl;
    }

    return 0;
}

