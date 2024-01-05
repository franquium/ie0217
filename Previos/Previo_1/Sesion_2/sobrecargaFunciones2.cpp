#include <iostream>
using namespace std;

// func con dos  parametros 
void display(int var1, double var2) {
    cout << "Integer number: " << var1;
    cout << " and double number: " << var2 << endl;
}

// func con un solo parametro tipo double
void display(double var) {
    cout << "Double number: " << var << endl;
}

// func con un solo parametro tipo int 
void display(int var) {
    cout << "Integer number: " << var << endl;
}

int main() {
    int a = 5;
    double b = 5.5;

    // Llamado func con  parametro tipo int 
    display(a);

    // Llamado func con  parametro tipo double
    display(b);

    // Llamado func con dos  parametros 
    display(a, b);

    return 0;
}
