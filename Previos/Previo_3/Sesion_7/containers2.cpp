#include <iostream>
#include <set>
using namespace std;

int main() {
    // inicializando un set o conjunto de tipo int 
    set<int> numbers = {1, 100, 10, 70, 100};

    // imprimir el set
    cout << "Numbers are: ";
    for(auto &num: numbers) {
        cout << num << " ";
    }

    return 0;
}
