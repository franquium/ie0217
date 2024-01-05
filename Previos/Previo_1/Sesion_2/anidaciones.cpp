#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter an integer: ";
    cin >> num;

    // condicion if de afuera
    if (num != 0) {
        // condicion if de adentro
        if (num > 0) {
            cout << "The number is positive." << endl;
        }
        // condicion else de adentro
        else {
            cout << "The number is negative." << endl;
        }
    }
    // condicion else de afuera
    else {
        cout << "The number is 0 and it is neither positive nor negative." << endl;
    }

    cout << "This line is always printed." << endl;

    return 0;
}
