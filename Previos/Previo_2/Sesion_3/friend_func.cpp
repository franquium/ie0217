#include <iostream>
using namespace std;

class Distance {
private:
    int meter;

    // friend func o func amiga
    friend int addFive(Distance);

public:
    Distance() : meter(0) {}
};

int addFive(Distance d) {
    // accesando miembros privados members de la func friend
    d.meter += 5;
    return d.meter;
}

int main() {
    Distance D;
    cout << "Distance: " << addFive(D);
    return 0;
}
