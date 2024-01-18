#include <iostream>
using namespace std;

// Plantilla de clase con Parametros multiples y Parametros  por default
template <class T, class U, class V = char>
class ClassTemplate {
    private:
        T var1;
        U var2;
        V var3;

    public:
        ClassTemplate(T v1, U v2, V v3) : var1(v1), var2(v2), var3(v3) {}

        void printVar() {
            cout << "var1 = " << var1 << endl;
            cout << "var2 = " << var2 << endl;
            cout << "var3 = " << var3 << endl;
        }
};

int main() {

    // creando objecto con tipos int, double y char
    ClassTemplate<int, double, char> obj1(7, 7.7, 'c');
    cout << "obj1 valores: " << endl;
    obj1.printVar();

    // creando objecto con tipos int, double y bool
    ClassTemplate<double, char, bool> obj2(8.8, 'a', false);
    cout << "obj2 valorees: " << endl;
    obj2.printVar();

    return 0;
}

