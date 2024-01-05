#include <iostream>
using namespace std;

int main(){

    // Bucle for
    for (int i = 1; i <= 5; i++)
    {
        cout << i << " ";
    }
    
    // Bucle for 2
    int num_array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    for (int n : num_array)
    {
        cout << n << " ";
    }

    // Bucle while
    int i = 1;

    // while de 1 a 5
    while (i <= 5)
    {
        cout << i << " ";
        ++i;
    }
    

    // Bucle do-while
    int i = 1;

    // do...while de 1 a 5
    do
    {
        cout << i << " ";
        ++i;
    } 
    while (i <= 5);
    


    return 0;
}