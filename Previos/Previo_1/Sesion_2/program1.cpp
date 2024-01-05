// Program 1
#include <iostream>

int count;
extern void write_extern();

main () {
    count = 5;
    write_extern();
}