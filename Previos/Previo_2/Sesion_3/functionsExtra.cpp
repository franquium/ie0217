/* Archivo para el ejercicio de la Sesion 4 sobre una implementacion con headers para funciones y clases*/
#include "functionsExtra.hpp"
#include <iostream>
using namespace std;

// Implementacion de la funcion
void calculateAverage(Student s1, Student s2) {
    double average = (s1.marks + s2.marks) / 2;
    cout << "Average Marks = " << average << endl;
}
