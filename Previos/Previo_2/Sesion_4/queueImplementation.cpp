/* Archivo de implementacion del Queue en C++ */
#include <iostream>
#define SIZE 5

using namespace std;

class Queue {
private:
    int items[SIZE], front, rear;

public:
    Queue() {
        front = -1;
        rear = -1;
    }

    bool isFull() {
        if (front == 0 && rear == SIZE - 1) {
            return true;
        }
        return false;
    }

    bool isEmpty() {
        if (front == -1)
            return true;
        else
            return false;
    }

    void enQueue(int element) {
        if (isFull()) {
            cout << "Queue is full";
        } else {
            if (front == -1) front = 0;
            rear++;
            items[rear] = element;
            cout << endl
                 << "Inserted " << element << endl;
        }
    }

    int deQueue() {
        int element;
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return (-1);
        } else {
            element = items[front];
            if (front >= rear) {
                // Q posee un solo elemento,
                // hay que resetear queue despues de borrarlo.
                front = -1;
                rear = -1;
            } else {
                front++;
            }
            cout << endl
                 << "Deleted -> " << element << endl;
            return (element);
        }
    }
};

void display() {
    /* Func para mostrar elementos de Queue */
    int i;
    if (isEmpty()) {
        cout << endl
             << "Empty Queue" << endl;
    } else {
        cout << endl
             << "Front index-> " << front;
        cout << endl
             << "Items -> ";
        for (i = front; i <= rear; i++)
            cout << items[i] << " ";
        cout << endl
             << "Rear index-> " << rear << endl;
    }
};

int main() {
    Queue q;

    //dequeue no es posible en queue vacio
    q.deQueue();

    //enqueue 5 elementos
    q.enQueue(1);
    q.enQueue(2);
    q.enQueue(3);
    q.enQueue(4);
    q.enQueue(5);

    // 6to elemento no se puede agregar por el queue esta lleno
    q.enQueue(6);

    q.display();

    //dequeue remueve elemento ingresado primeramente i.e. 1
    q.deQueue();

    //Ahora solo hay 4 elementos
    q.display();

    return 0;
}

