#include <iostream>
using namespace std;

class Student {
private:
    int age;

public:
    // inicializando constructor age a 12
    Student() : age(12) {}

    void getAge() {
        cout << "Age = " << age << endl;
    }
};

int main() {
    // declarando dinamicamente objeto Student
    Student* ptr = new Student();

    // llamado func getAge()
    ptr->getAge();

    // ptr memory es liberado
    delete ptr;

    return 0;
}
