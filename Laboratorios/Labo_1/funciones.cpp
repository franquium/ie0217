
#include "funciones.hpp"
#include <string>
#include <iostream>

void mostrarMenu(){
    std::cout << "\n--- Menu ---\n";
    std::cout << "1. Agregar empleados\n";
    std::cout << "2. Listar empleados\n";
    std::cout << "3. Eliminar empleado\n";
    std::cout << "4. Salir\n";
}

void procesarOpcion(Empleado empleados[], int& numEmpleados){
    int opcion;
    std::cout << "Ingrese una opcion: ";
    std::cin >> opcion;

    // Casos
    switch(opcion){
        case 1: // Agregar empleado
            agregarEmpleado(empleados, numEmpleados);
            break;
        case 2: // Lista empleadoss
            listarEmpleados(empleados, numEmpleados);
            break;
        case 3: // Eliminar empleado
            eliminarEmpleados(empleados, numEmpleados);
            break;
        case 4: // Salir
            std::cout << "Saliendo del programa...\n";
            exit(0);
        default:
            std::cout << "Opcion no es valida. Intente de nuevo...\n";
    }
}

    void agregarEmpleado(Empleado empleados[], int& numEmpleados){
        /*  Hay un error con este
        *   Cuando se elimina un nuevo empleado, y despues al agregar un nuevo empleado
        *   se repite el id de numEmpleados +1, es decir si estaba hasta 4 y elimino 2, y agrgo uno van a salir dos 4
        *   Posibles Sols: 
        *           --Ver el id del ultimo empleado y subarle uno
        */
        if(numEmpleados < MAX_EMPLEADOS){
            Empleado nuevoEmpleado;
            nuevoEmpleado.id = numEmpleados + 1;


            std::cout << "Ingrese el nombre del empleado: ";
            std::cin >> nuevoEmpleado.nombre;

            std::cout << "Ingrese el salario del empleado: ";
            std::cin >> nuevoEmpleado.salario;

            empleados[numEmpleados++] = nuevoEmpleado;
            std::cout << "Empleado agregado con exito.\n";



        } else{
            std::cout << "No se puede agregar mas, limite alcanzado. \n";
        }
    }

    void listarEmpleados(const Empleado empleados[], int& numEmpleados){
        std::cout << "--- Lista de empleados --- \n";

        for (int i = 0; i < numEmpleados; ++i)
        {
           std::cout << "ID: "<< empleados[i].id << ", Nombre: " <<
           empleados[i].nombre << ", Salario: " << empleados[i].salario << "\n";
        }
    }

    void eliminarEmpleados(Empleado empleados[], int& numEmpleados){
        int idEliminar;

        std::cout << "Ingrese el ID a eliminar:  \n";
        std::cin >> idEliminar;

        for (int i = 0; i < numEmpleados; ++i)
        {
            if (empleados[i].id == idEliminar)
            {
                for (int j = i; j < numEmpleados - 1; ++j)
                {
                    empleados[j] = empleados[j+1];
                }
                --numEmpleados;
                std::cout << "Empleado eliminado con exito. \n";
                return; // para que no siga en el for-loop aunque como hay nada despues no efecta a lista
            }
            
        }
        
    }

