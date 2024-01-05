
#include "funciones.hpp"
#include <string>
#include <iostream>

void mostrarMenu(){
    std::cout << "\n--- Menú ---\n";
    std::cout << "1. Agregar empleados\n";
    std::cout << "2. Listar empleados\n";
    std::cout << "3. Eliminar empleado\n";
    std::cout << "4. Salir\n";
}

void procesarOpcion(){
    int opcion;
    std::cout << "Ingrese una opcion: "
    std::cin >> opcion;

    // Casos
    switch(opcion){
        case 1: // Agregar empleado
            agregarEmpleado(Empleado empleados[], int& numEmpleados);
            break;
        case 2: // Lista empleadoss
            listarEmpleados();
            break;
        case 3: // Eliminar empleado
            eliminarEmpleados();
            break;
        case 4: // Salir
            std::cout << "Saliendo del programa...\n";
            exit(0);
        default:
            std::cout << "Opcion no es valida. Intente de nuevo...\n";
    }
}