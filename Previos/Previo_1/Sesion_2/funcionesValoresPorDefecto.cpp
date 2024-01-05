#include <iostream>
using namespace std;

// Invalido
void add(int a, int b = 3, int c,  int d);

// Invalido
void add(int a, int b = 3, int c,  int d = 4);

// Valido
void add(int a, int c,, int b = 3  int d = 4);

void display(char c = '*', int count = 5){
    // Codigo
}

int main(){
    // Llamado de func
    display();

    return 0;
}