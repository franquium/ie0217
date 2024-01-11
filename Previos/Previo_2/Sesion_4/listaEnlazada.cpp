#include <bits/stdc++.h>
#include <iostream>
using namespace std;

// Creando un node
class Node {
public:
    int value;
    Node* next;
};

int main() {
    Node* head;
    Node* one = NULL;
    Node* two = NULL;
    Node* three = NULL;

    // allocando 3 nodes en el heap
    one = new Node();
    two = new Node();
    three = new Node();

    // Asignando valores  value
    one->value = 1;
    two->value = 2;
    three->value = 3;

    // Conectandos nodes
    one->next = two;
    two->next = three;
    three->next = NULL;

    // Imprimir el valor de la lista enlazada
    head = one;
    while (head != NULL) {
        cout << head->value;
        head = head->next;
    }
}
