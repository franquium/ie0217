#include <iostream>
using namespace std;


int main(){

/************
 *  De break y continue
 * *********/

for (init; condition; update) {
    // code
    if ("condition to break") {
        break;
    }
    // code
}

while (condition) {
    // code
    if ("condition to break") {
        break;
    }
    // code
}

for (init; condition; update) {
    // code
    if ("condition to continue") {
        continue;
    }
    // code
}

while (condition) {
    // code
    if ("condition to continue") {
        continue;
    }
    // code
}



/************
 *  De Arrays
 * *********/

// declarando e inicializando un array
int x [6] = {19, 10, 8, 17, 9, 15};

// Matriz
int x2 [3][4];

int test [2][3] = {2, 4, 5, 9, 0, 19};
int test2 [2][3] = {{2, 4, 5}, {9, 0, 19}};


return 0;
}



