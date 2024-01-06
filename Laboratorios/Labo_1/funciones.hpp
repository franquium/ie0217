#ifndef FUNCIONES_HPP
#define FUNCIONES_HPP
#include <string>

#include <iostream>

// Maximo 10 empleados
const int MAX_EMPLEADOS = 10;

struct Empleado {
    int id;
    std::string nombre;
    double salario;

};

void mostrarMenu();
void procesarOpcion(Empleado empleados[], int &numEmpleados);
void agregarEmpleado(Empleado empleados[], int &numEmpleados);
void listarEmpleados(const Empleado empleados[], int &numEmpleados);
void eliminarEmpleados(Empleado empleados[], int &numEmpleados);

#endif