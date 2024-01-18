#include <iostream>
#include <map>
using namespace std;

int main() {
    map<int, string> student;

    // usar  operador [] para agregar elementos
    student[1] = "Jacqueline";
    student[2] = "Blake";

    // usar metodo insert() para agregar elementos
    student.insert(make_pair(3, "Denise"));
    student.insert(make_pair(4, "Blake"));

    // agregar elementos con keys duplicados
    student[5] = "Timothy";
    student[5] = "Aaron";

    for (int i = 1; i <= student.size(); ++i) {
        cout << "Student[" << i << "]: " << student[i] << endl;
    }

    return 0;
}


