#include <iostream>
using namespace std;


int main(){
    char oper; 
    float num1, num2;
    cout << "Digite un operador (+, -, *, /):";
    cin >> oper;
    cout << "Ingrese 2 numeros: " << endl;
    cin >> num1 >> num2;

    switch (oper){
        case '+':
            cout << num1 << " + " << num2 << " = " << num1 + num2;
            break;
        case '-':
            cout << num1 << " - " << num2 << " = " << num1 - num2;
            break;
        case '*':
            cout << num1 << " * " << num2 << " = " << num1 * num2;
            break;
        case '/':
            cout << num1 << " / " << num2 << " = " << num1 / num2;    
            break;
        default:
            // El Operador no concuerda con ninguno de (+, -, *, /)
            cout << "Error! El Operador no es correcto";
            break;
    }

    return 0;
}