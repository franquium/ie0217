#include <iostream>
using namespace std;

// definicion de func para swapear valores
void swap(int &n1, int &n2) {
    int temp;
    temp = n1;
    n1 = n2;
    n2 = temp;
}

int main() {
    // inicializando variables
    int a = 1, b = 2;

    cout << "Antes del swapeo" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    // llamdo func swap
    swap(a, b);

    cout << "\nDespues del swapeo" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    return 0;
}
