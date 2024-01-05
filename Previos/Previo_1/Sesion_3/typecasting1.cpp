// Working of implicit type-conversion
#include <iostream>
using namespace std;

int main() {
    // asignando un valor tipo int a num_int
    int num_int = 9;

    // declarando una var de tipo double
    double num_double;

    // Conversion implicita
    // asignando un valor tipo int a var tipo double
    num_double = num_int;

    cout << "num_int = " << num_int << endl;
    cout << "num_double = " << num_double << endl;

    return 0;
}
