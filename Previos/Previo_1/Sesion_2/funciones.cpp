#include <iostream>
using namespace std;

// Funcion greet
void greet(){
    cout << "Hello World";
}

// Argumentos en una funcion
void displayNumber(int n1, float n2){
    cout << "The int Number is: " << n1;
    cout << "The double Number is: " << n2;
}

// Return en un funcion
int add(int a, int b){
    return (a + b);
} 

int main(){


    // Llamado de func greet
    greet();

    // Llamado func displayNumber
    int num1 = 5;
    double num2 = 0.5;

    displayNumber(num1, num2);

    //Llamado de la funcion add y guardando su valor
    int sum;
    sum = add(100, 78);
    cout << "100 + 78 = " << sum << endl;


    return 0;
}