/* Archivo de implementacion del Stack en C++ */
#include <stdlib.h>
#include <iostream>

using namespace std;

#define MAX 10
int size = 0;

// Creando un stack
struct stack {
    int items[MAX];
    int top;
};

typedef struct stack st;

void createEmptyStack(st *s) {
    s->top = -1;
}

// Revisa si el stack esta lleno
int isfull(st *s) {
    if (s->top == MAX - 1)
        return 1;
    else
        return 0;
}

// Revisa si el stack esta vacio
int isempty(st *s) {
    if (s->top == -1)
        return 1;
    else
        return 0;
}

// Agrega elementos al stack
void push(st *s, int newitem) {
    if (isfull(s)) {
        cout << "STACK LLENO";
    } else {
        s->top++;
        s->items[s->top] = newitem;
    }
    size++;
}

// Remueve elementos del stack
void pop(st *s) {
    if (isempty(s)) {
        cout << "\nSTACK VACIO\n";
    } else {
        cout << "Item popped= " << s->items[s->top];
        s->top--;
        size--;
        cout << endl;
    }
}

// Imprime elementos del stack
void printStack(st *s) {
    printf("Stack: ");
    for (int i = 0; i < size; i++) {
        cout << s->items[i] << " ";
    }
    cout << endl;
}

// Driver code
int main() {
    int ch;
    st *s = (st *)malloc(sizeof(st));

    createEmptyStack(s);

    push(s, 1);
    push(s, 2);
    push(s, 3);
    push(s, 4);

    printStack(s);

    pop(s);

    cout << "\nAfter popping out\n";
    printStack(s);

    return 0;
}
