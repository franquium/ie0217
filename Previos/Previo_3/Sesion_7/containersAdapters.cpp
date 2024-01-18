#include <iostream>
#include <stack>
using namespace std;

int main() {
    // creando un stack de ints
    stack<int> numbers;

    // empujando o push en el stack
    numbers.push(1);
    numbers.push(100);
    numbers.push(10);

    cout << "Numbers are: ";

    // se puede acceder el elemento usando el top y popping
    // hasta que el stack este vacio
    while(!numbers.empty()) {
        // imprimir elemento top
        cout << numbers.top() << ", ";
        
        // pop elemento top del stack
        numbers.pop();
    }

    return 0;
}
