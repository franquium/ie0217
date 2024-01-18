#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector <string> languages = {"Python", "C++", "Java"};

    // creando un iterador a un vector string 
    vector<string>::iterator itr;

    // iterando sobre todos los elementos
    for (itr = languages.begin(); itr != languages.end(); itr++) {
        cout << *itr << " ";
    }

    return 0;
}
