#include <iostream>
using namespace std;

struct temp{
    int i;
    float f;
};

struct Distance
{
    int feet;
    float inch;
};


int main(){

    temp *pointer;


    Distance *ptr, d;

    ptr = &d;

    cout << "Ingrese feet: ";
    cin >> (*ptr).feet;
    cout << "Ingrese inch: ";
    cin >> (*ptr).inch;

    cout << "Mostrando la info: " << endl;
    cout << "Distance = " << (*ptr).feet << " feet "<< (*ptr).feet << " inches ";


    return 0;
}