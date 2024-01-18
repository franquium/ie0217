#include <iostream>
#include <vector>
using namespace std;

int main() {
    // inicializando un vector de tipo int 
    vector<int> numbers = {1, 100, 10, 70, 100};

    // imprimir el vector
    cout << "Numbers are: ";
    for(auto &num: numbers) {
        cout << num << " ";
    }

    return 0;
}
